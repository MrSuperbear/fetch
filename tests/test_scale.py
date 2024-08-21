import random

from playwright.sync_api import sync_playwright
from pages.scale import ScalePage
from pytest import fixture
from random import shuffle
from numpy import array_split
from time import sleep


def handle_dialog(dialog):
    """When added to a listener it will print and dismiss an Alert dialog"""
    print(f"\nAlert Message: {dialog.message}")
    dialog.dismiss()


# test fixture for ScalePage (page object model)
@fixture
def scale_page():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # add listener for dialog (alert) event
        page.on("dialog", handle_dialog)
        scale_page = ScalePage(page)
        yield scale_page

        # clean up
        context.close()
        browser.close()

@fixture()
def generated_seed():
    gen_seed = random.randint(0, 99)
    print(f"Random seed for test: {gen_seed}")
    return gen_seed


def test_lightest_gold_bar(scale_page, generated_seed):
    # for reproducibility, I set a random seed but this does not control the randomness of the site.
    random.seed(generated_seed)
    remaining_bars = list((range(9)))
    shuffle(remaining_bars)
    scale_page.navigate()
    measurement_count = 0
    while len(remaining_bars) > 1:
        a, b, c = array_split(remaining_bars, 3)
        weight_result = scale_page.weigh(a, b)
        measurement_count += 1
        match weight_result:
            case "<":
                remaining_bars = a
            case ">":
                remaining_bars = b
            case "=":
                remaining_bars = c
    fake = str(remaining_bars[0])
    sleep(3)
    scale_page.select_fake(fake)
    print(f"The fake gold bar is {remaining_bars[0]} \nIt was found in {measurement_count} measurements")
    scale_page.print_weighings()


