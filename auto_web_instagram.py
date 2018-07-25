# selenium 3.12.0
# chromedriver 2.39 (http://chromedriver.storage.googleapis.com/index.html?path=2.39/)
#

import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

opts = webdriver.ChromeOptions()
# opts.add_argument('headless')
opts.add_argument('window-size=1920,1080')

driver = webdriver.Chrome('./resource/chromedriver', chrome_options=opts)

try:
    driver.get('https://www.instagram.com/')

    wait = WebDriverWait(driver, 3)

    cond = ec.element_to_be_clickable((By.LINK_TEXT, '로그인'))
    btn = wait.until(cond)
    btn.click()

    time.sleep(1)

    cond = ec.visibility_of_element_located((By.NAME, 'username'))
    elem = wait.until(cond)
    elem.send_keys('devfuner@gmail.com')

    cond = ec.visibility_of_element_located((By.NAME, 'password'))
    elem = wait.until(cond)
    elem.send_keys(open('password').read().strip())

    elem.send_keys(Keys.RETURN)

    cond = ec.visibility_of_element_located((By.LINK_TEXT, '나중에 하기'))
    btn = wait.until(cond)
    btn.click()

    cond = ec.visibility_of_element_located((By.CLASS_NAME, 'eyXLr'))
    elem = wait.until(cond)
    action = ActionChains(driver)
    action.move_to_element(elem)
    action.click()
    action.send_keys('#파이썬')
    action.perform()

    time.sleep(2)

    action.reset_actions()
    action.move_by_offset(0, 50)
    action.click()
    action.perform()

    cond = ec.visibility_of_element_located((By.CLASS_NAME, 'EZdmt'))
    elem = wait.until(cond)

    posts = elem.find_elements_by_class_name('KL4Bh')
    action = ActionChains(driver)

    for post in posts:
        action.reset_actions()
        action.move_to_element(post)
        action.click()
        action.perform()

        try:
            cond = ec.visibility_of_element_located((By.CLASS_NAME, 'fr66n'))
            elem = wait.until(cond)
            elem.click()
        except NoSuchElementException as e:
            print(type(e), e)
            pass
        except TimeoutException as e:
            print(type(e), e)
            pass

        action.reset_actions()
        action.send_keys(Keys.ESCAPE)
        action.perform()

        time.sleep(1)
except Exception as e:
    print(type(e), e)
finally:
    driver.quit()
