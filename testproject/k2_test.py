from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_rect(1200, 400, 1300, 1000)

driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html")
time.sleep(1)

random_color_name = driver.find_element_by_id("randomColorName").text


# tc01 - Applikáció helyes indulása
def test_start_of_app():
    print(random_color_name)
    test_color_name = driver.find_element_by_id("testColorName").text
    print(test_color_name)
    assert test_color_name == ""


# tc02 - start és stop gombok működésa
def test_start_and_stop():
    start_button = driver.find_element_by_id("start")
    start_button.click()
    test_color_name = driver.find_element_by_id("testColorName").text
    assert not test_color_name == ""
    stop_button = driver.find_element_by_id("stop")
    assert stop_button.is_enabled()
    stop_button.click()


# tc03 - szín ellenőrzése
def test_message_check():
    test_color_name = driver.find_element_by_id("testColorName").text
    result_message = driver.find_element_by_id("result").text
    print(result_message)
    if random_color_name == test_color_name:
        assert result_message == "Correct!"
    else:
        assert result_message == "Incorrect!"

    driver.quit()
