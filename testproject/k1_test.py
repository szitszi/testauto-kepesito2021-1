from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_rect(1200, 400, 1300, 1000)

driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html")
time.sleep(1)

a_field = driver.find_element_by_id("a")
b_field = driver.find_element_by_id("b")
calc_button = driver.find_element_by_id("submit")
c_part = driver.find_element_by_xpath('//*[@id="results"]/p')


# TC01 - Applikáció betöltésekor a lokátorok ellenőrzése
def test_tc1_start_status():
    assert a_field.text == ""
    assert b_field.text == ""
    assert not c_part.is_displayed()


# TC02 - Helyes adtokkal való kitöltés
def test_tc2_right_fill():
    test_data_2 = ["2", "3", "10"]
    a_field.clear()
    a_field.send_keys(test_data_2[0])
    b_field.clear()
    b_field.send_keys(test_data_2[1])
    calc_button.click()
    c_field = driver.find_element_by_id("result")
    assert c_field.text == test_data_2[2]


# TC03 - Üres adatokkal való kitöltés
def test_empty_fill():
    test_data_3 = ["", "", "NaN"]
    a_field.clear()
    a_field.send_keys(test_data_3[0])
    b_field.clear()
    b_field.send_keys(test_data_3[1])
    calc_button.click()
    c_field = driver.find_element_by_id("result")
    assert c_field.text == test_data_3[2]

    driver.quit()
