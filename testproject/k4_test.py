from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_rect(1200, 400, 1300, 1000)

driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html")
time.sleep(1)


# test_data_1 = [!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~]


# tc01 - Szöveg ellenőrzés (ehhez listába vagy str-be kell a tesztadatot tenni)
def test_text():
    start_app_text = driver.find_element_by_xpath('//div[@class="flex-child"]/p[3]').text
    print(start_app_text)
    # assert test_data_1 == start_app_text


# tc02 - Műveleti tagok ellenőrzése (a chr esetében a lista/str alapján kell az assert)
def test_apperance():
    chr_field = driver.find_element_by_id("chr").text
    assert chr_field in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    op_field = driver.find_element_by_id("op").text
    assert op_field == "+" or "-"
    num_field = int(driver.find_element_by_id("num").text)
    print(num_field)


# tc03 -
def test_calculation():
    calc_button = driver.find_element_by_id("submit")
    calc_button.click()
    result_char = driver.find_element_by_id("result").text
    print(result_char)

    driver.quit()
