"""
browser window methods
"""
"""
maximize_window():
    *it will maximize a window/browser.
minimize_window():
    *it will minimize a window/browser.
fullsecreen_window():
    *it will make a browser/window full screen.
get_window_position():
    *it will return dictionary of 'x' and 'y' axis/cordinates.
get_window_size():
    *it will return dictionary of 'height' and 'width'.
get_window_rect():
    *it will return dictionary of 'x', 'y', 'height' and 'width'.
set_window_position():
    *it will set a window/browser position based on 'x' and 'y' axis.
set_window_size():
    *it will set a window/browser position based on 'height' and 'width'.
set_window_rect():
    *it will set a window/browser position based on 'x','y','height','width'.
"""

from selenium.webdriver import Chrome
from time import sleep

#ws to maximize a window
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.fb.com")
driver.maximize_window()
"""

#ws to minimize, maximize and close browser
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.fb.com")
driver.maximize_window()
driver.minimize_window()
driver.maximize_window()
driver.close()
"""

#ws to full screen a window
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.fb.com")
driver.fullscreen_window()
driver.close()
"""

#ws to get x and y axis of window
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.meesho.com/")
pos = driver.get_window_position()
print(pos)          #{'x': 10, 'y': 10}
print(pos['x'])     #10
print(pos['y'])     #10
"""

#ws to get height and width of window
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.meesho.com/")
loc = driver.get_window_size()
print(loc)          #{'width': 1050, 'height': 708}
print(f"height: {loc['height']}")       #height: 708
print(f"width: {loc['width']}")         #width: 1050
"""

#ws to get x,y.width,height axis of window
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.meesho.com/")
rect = driver.get_window_rect()
print(rect)     #{'height': 708, 'width': 1050, 'x': 10, 'y': 10}
"""

#ws to set window based on x and y axis
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.amazon.com/")
driver.set_window_position(89, 7)
"""

# ws to set window based on height and width axis
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.amazon.com/")
driver.set_window_size(23, 897)
"""

# ws to set window based on x, y, height and width axis
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.amazon.com/")
driver.set_window_rect(87, 55, 273, 796)
"""
####################################################################################################
"""
verification of webapges:
=========================
*to verify if we navigate from one webpage to another webpage then we use below property.
1.title:
    *it will return current webpage title.
2.current_url:
    *it will return current webpage url.
3.page_source:
    *it will return current webpage source code.
"""
#ws to print the current title of a ajio webpage
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.ajio.com/")
t = driver.title
print(t)
#Online Shopping for Women, Men, Kids – Clothing, Footwear | AJIO
"""

#ws to verify home page is displayed or not
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.ajio.com/")
atitle = driver.title
if atitle=='Online Shopping for Women, Men, Kids – Clothing, Footwear | AJIO':
    print("Home page displayed and Testcase pass")
else:
    print("Testcase Fail, DEFECT")
"""

#ws to print current webpage url
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.myntra.com/men-tshirts")
url = driver.current_url
print(url)
#https://www.myntra.com/men-tshirts
"""

#ws to verify home page is displayed or not in mytra
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.myntra.com/men-tshirts")
aurl = driver.current_url
if aurl == 'https://www.myntra.com/men-tshirt':
    print("mens-tshirt page displayed and Testcase pass")
else:
    print("Testcase Fail, DEFECT")
"""

#ws to print current webpage page source code
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.myntra.com/men-tshirts")
src = driver.page_source
print(src)
"""

#ws to verify home page is displayed or not in mytntra
"""
driver = Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.myntra.com/men-tshirts")
src = driver.page_source
if "Buy Men's T-shirts Online at India's Best Fashion Store | Myntra" in src:
    print("title matches")
else:
    print("defect")
"""





















