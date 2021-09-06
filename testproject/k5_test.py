from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_rect(1200, 400, 1300, 1000)

driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html")
time.sleep(1)


# tc01
def test_begin_status():
    table_fields = driver.find_elements_by_tag_name("td")
    assert len(table_fields) == 25
    number_list = driver.find_elements_by_xpath('//*[@id="numbers-list"]/li')
    assert len(number_list) == 75


# tc02
def test_guess_process():
    play_button = driver.find_element_by_id("spin")

    # addig nyomjuk a play-t, amíg az üzeneteknél nem jelenik meg a felirat
    while True:
        messages = driver.find_elements_by_xpath('//*[@id="messages"]/li')
        if len(messages) == 0:
            play_button.click()
        else:
            break
    # megkeressük a bingo számokat
    b_numbers = driver.find_elements_by_xpath('//td[@class="checked"]/div')

    bingo_numbers = []
    for num in b_numbers:
        bingo_numbers.append(num.text)
    print(bingo_numbers)

    # megkeressük a találgatott (bepipált) számokat
    c_numbers = driver.find_elements_by_xpath('//li[@class="checked"]/input')
    checked_numbers = []
    for num in c_numbers:
        checked_numbers.append(num.get_attribute("value"))
    print(checked_numbers)

    # megnézzük, hogy a bingo számokat tartalmazza-e a találgatott számok listája
    for num in bingo_numbers:
        assert num in checked_numbers
    time.sleep(3)


# tc03
def test_new_strat():
    init_button = driver.find_element_by_id("init")
    init_button.click()
    time.sleep(1)
    # új játék indításával a egyik bingo vagy találgatotott számnak sem szabad checked-nek lennie, ezzel ellenőrizzük, hogy új játék indul
    new_bingo_numbers = driver.find_elements_by_xpath('//td[@class="checked"]/div')
    assert len(new_bingo_numbers) == 0
    new_checked_numbers = driver.find_elements_by_xpath('//li[@class="checked"]/input')
    assert len(new_checked_numbers) == 0

    driver.quit()
