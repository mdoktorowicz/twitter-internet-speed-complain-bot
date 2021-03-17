from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os
from time import *

class InternetSpeedTwitterBot():

    def __init__(self):
        chrome_driver_path = "C:/Users/Maciek/PycharmProjects/chromedriver_win32/chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.TWITTER_EMAIL = os.environ.get("email")
        self.TWITTER_PASSWORD = os.environ.get("password")

    def post_on_twitter(self, speed, down_limit, up_limit):
        self.driver.get("https://twitter.com/")
        self.download_speed = speed[0]
        self.upload_speed = speed[1]
        self.threshold_down = down_limit
        self.threshold_up = up_limit

        if self.download_speed < self.threshold_down or self.upload_speed < self.threshold_up:
            print("Need to post on twitter")
            sleep(4)
            login_button = self.driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]")
            login_button.click()

            sleep(2)
            email_input = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
            email_input.send_keys(self.TWITTER_EMAIL)

            sleep(1)
            password_input = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")
            password_input.send_keys(self.TWITTER_PASSWORD)

            sleep(0.5)
            final_login_button = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div")
            final_login_button.click()

            sleep(4)
            textbox = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div")
            textbox.send_keys(f"Hey Internet Provider, why is my internet speed {self.download_speed} MBps down & {self.upload_speed} MBps up when I pay for {self.threshold_down} down and {self.threshold_up} up?")

            sleep(1)
            send_button = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div/span/span")
            send_button.click()

            self.driver.quit()

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        sleep(2)
        consent_button = self.driver.find_element_by_css_selector("#_evidon-banner-acceptbutton")
        consent_button.click()

        sleep(2)
        test_speed_button = self.driver.find_element_by_css_selector(".start-text")
        test_speed_button.click()

        sleep(50)
        try:
            desktop_app_popup = self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/div[2]/a")
            desktop_app_popup.click()
        except NoSuchElementException:
            pass

        sleep(2)
        download_speed_span = self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
        download_speed = float(download_speed_span.text)

        upload_speed_span = self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span")
        upload_speed = float(upload_speed_span.text)

        speed_tuple = (download_speed, upload_speed)

        print(f"Download speed: {download_speed}")
        print(f"Upload speed: {upload_speed}")

        return speed_tuple