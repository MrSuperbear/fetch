
# Fetch Coding Exercise - SDET

Coding and automation challenge to find the lightest gold bar from a group of nine bars. My implementation was coded in Python and I used Playwright as the automation tool. I followed a POM implementation. 


## Installation

Python 3.11 or higher is required

```bash
  pip install pytest-playwright
  pip install numpy 
  
  playwright install 
```
    
## Example 
 The test "test_lightest_gold_bar" in tests/test_scale.py runs the automation. The page layout and functions are in pages/scale.py.
```bash
============================= test session starts =============================
collecting ... collected 1 item

test_scale.py::test_lightest_gold_bar Random seed for test: 20
PASSED                             [100%]
Alert Message: Yay! You find it!
The fake gold bar is 1 
It was found in 2 measurements
Weighings:
[1,7,3] < [8,0,6]
[1] < [7]


============================= 1 passed in 11.15s ==============================
```