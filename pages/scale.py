from time import sleep


class ScalePage:
    def __init__(self, page):
        self.page = page
        self.left0 = page.locator("#left_0")
        self.left1 = page.locator("#left_1")
        self.left2 = page.locator("#left_2")
        self.right0 = page.locator("#right_0")
        self.right1 = page.locator("#right_1")
        self.right2 = page.locator("#right_2")
        self.zero = page.locator("#coin_0")
        self.one = page.locator("#coin_1")
        self.two = page.locator("#coin_2")
        self.three = page.locator("#coin_3")
        self.four = page.locator("#coin_4")
        self.five = page.locator("#coin_5")
        self.six = page.locator("#coin_6")
        self.seven = page.locator("#coin_7")
        self.eight = page.locator("#coin_8")
        self.left_scale = {0: self.left0, 1: self.left1, 2: self.left2}
        self.right_scale = {0: self.right0, 1: self.right1, 2: self.right2}
        self.reset_button = page.get_by_role("button", name="Reset")
        self.weigh_button = page.get_by_role("button", name="Weigh")

    def navigate(self):
        self.page.goto("https://sdetchallenge.fetch.com")

    def weigh(self, a, b):
        to_be_weighed = zip(a, b)
        for index, value in enumerate(to_be_weighed):
            self.left_scale[index].fill(str(value[0]))
            self.right_scale[index].fill(str(value[1]))
        self.weigh_button.click()
        sleep(3)
        result = self.page.locator("xpath=/html/body/div/div/div[1]/div[2]/button").text_content()
        self.reset_scale()
        return result

    def select_fake(self, fake: str):
        match fake:
            case "0":
                self.zero.click()
            case "1":
                self.one.click()
            case "2":
                self.two.click()
            case "3":
                self.three.click()
            case "4":
                self.four.click()
            case "5":
                self.five.click()
            case "6":
                self.six.click()
            case "7":
                self.seven.click()
            case "8":
                self.eight.click()
            case _:
                print("The fake bar  is not a vaild entry")

    def print_weighings(self):
        print("Weighings:")
        measurements = []
        for i in range(1, 3):
            weighing = self.page.locator(f"xpath=/html/body/div/div/div[1]/div[5]/ol/li[{i}]").text_content()
            measurements.append(weighing)
        for measurement in measurements:
            print(measurement)

    def reset_scale(self):
        self.reset_button.click()
