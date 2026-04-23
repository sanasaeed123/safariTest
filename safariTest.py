# To launch:
# python3 -m pip install -U selenium
# python3 -m pip install (-U) Appium-Python-Client
# python3 appiumTest.py

import time
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# SETUP our iPhone Simulator
options = AppiumOptions()
options.set_capability("platformName", "iOS")
options.set_capability("appium:deviceName", "iPhone 17")
options.set_capability("appium:platformVersion", "26.4")
options.set_capability("appium:automationName", "XCUITest")
options.set_capability("browserName", "Safari")

#Connect to Appium server
driver = webdriver.Remote("http://localhost:4723", options=options)

#TEST 1: Navigate to Bing
driver.get("https://bing.com")
time.sleep(3)

#TEST 2: Realize we would rather use Google
driver.get("https://google.com")
time.sleep(3)

#Switch context to work on web
webview = driver.contexts[1]
driver.switch_to.context(webview)

#TEST 3: Look up how people feel about different iPhone alarms
search_box = driver.find_element("name", "q")
search_box.send_keys("iPhone alarms ranked\n")
search_box.submit()
time.sleep(3)

#TEST 4: Scroll down a bit
driver.execute_script("""
window.scrollBy({
    top: 800,
    left: 0,
    behavior: 'smooth'
});
""")
time.sleep(5)

#TEST 5: Scroll back to the top
driver.execute_script("""
window.scrollBy({
    top: -800,
    left: 0,
    behavior: 'smooth'
});
""")
time.sleep(2)

# OH NO, IT STARTED RAINING OUTSIDE!! This is unexpected - it never rains ! We need an umbrella!

#TEST 6: Go to Amazon
driver.get("https://amazon.com")
time.sleep(2)

#TEST 7: Search for an Umbrella
wait = WebDriverWait(driver, 5)
search_box = wait.until(
    lambda d: d.find_element(By.CSS_SELECTOR, "input[type='text']")
)
search_box.send_keys("umbrella", Keys.RETURN)
driver.execute_script("window.scrollBy(0, 400)")
time.sleep(3)

#TEST 8: Get it ASAP - rain is in the forecast all week!
wait = WebDriverWait(driver, 5)
button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Get It Fast')]"))
)
button.click()
time.sleep(3)

#TEST 9: Scroll down
driver.execute_script("""
window.scrollBy({
    top: 600,
    left: 0,
    behavior: 'smooth'
});
""")

#TEST 10: Select listing
size = driver.get_window_size()

driver.execute_script("mobile: tap", {
    "x": size["width"] // 3,
    "y": size["height"] // 2
})
time.sleep(3)

#TEST 11: Scroll down and ddd to cart
driver.execute_script("""
window.scrollBy({
    top: 1300,
    left: 0,
    behavior: 'smooth'
});
""")
time.sleep(2)

wait = WebDriverWait(driver, 5)
add_to_cart = driver.find_element(By.ID, "add-to-cart-button")
add_to_cart.click()

input("Press Enter to quit...")
driver.quit()