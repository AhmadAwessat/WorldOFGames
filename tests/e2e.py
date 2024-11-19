from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def test_scores_service(url_test):
    # Provide the correct path to chromedriver.exe
    service = Service("C:\\Users\\Ahmad\\Desktop\\chromedriver-win64\\chromedriver.exe")
    my_driver_for_facebook = webdriver.Chrome(service=service)

    # Test the webpage
    my_driver_for_facebook.get(url_test)

    string = my_driver_for_facebook.find_element(By.XPATH, '//*[@id="score"]').text
    splited_str = string.split(' ')
    time.sleep(10)

    if int(splited_str[-1]) in range(1, 1000):
        return True
    else:
        return False

def main_function():
    flag = False
    if test_scores_service('http://localhost:8777/') == flag:
        return -1
    else:
        return 0

main_function()
