from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_rect(1200, 400, 1300, 1000)

driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html")
time.sleep(1)

input_field = driver.find_element_by_id("title")
test_data = ["abcd1234", "teszt233@", "abcd"]


# tc01 - Helyes kitöltés
def test_right_fill():
    input_field.send_keys(test_data[0])
    message = driver.find_element_by_tag_name("span")
    assert message.text == ""


# tc02 - Speciális karakterrel kitöltés
def test_spec_character_fill():
    input_field.clear()
    input_field.send_keys(test_data[1])
    message = driver.find_element_by_tag_name("span")
    time.sleep(0.5)
    assert message.text == "Only a-z and 0-9 characters allewed"


# tc03 - Rövidebb kitöltés
def test_short_fill():
    input_field.clear()
    input_field.send_keys(test_data[2])
    message = driver.find_element_by_tag_name("span")
    time.sleep(0.5)
    assert message.text == "Title should be at least 8 characters; you entered 4."

    driver.quit()
