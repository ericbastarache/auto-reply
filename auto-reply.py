from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import threading
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

LINKEDIN_EMAIL = os.environ.get("LINKEDIN_EMAIL")
LINKEDIN_PASSWORD = os.environ.get("LINKEDIN_PASSWORD")
TEXT_TO_SEARCH = os.environ.get("TEXT_TO_SEARCH")

class AutoReply:
    def __init__(self):
        self.ChromeDriver = Chrome(executable_path="/opt/WebDriver/bin/chromedriver")

    def login(self):
        linkedin = self.ChromeDriver.get("https://www.linkedin.com/")
        email = self.ChromeDriver.find_element_by_name("session_key")
        password = self.ChromeDriver.find_element_by_name("session_password")
        login_button = self.ChromeDriver.find_element_by_class_name("sign-in-form__submit-button")

        email.send_keys(LINKEDIN_EMAIL)
        password.send_keys(LINKEDIN_PASSWORD)
        login_button.click()
        if "manage-account" in self.ChromeDriver.current_url:
            confirm_button = self.ChromeDriver.find_element_by_class_name("primary-action-new")
            confirm_button.click()
        WebDriverWait(self.ChromeDriver, 15)
        self.read_messages()
    def read_messages(self):
        messaging_link = self.ChromeDriver.find_element_by_css_selector("[data-control-name='nav.messaging']")
        if messaging_link is not None:
            messaging_link.click()
            time.sleep(10)
            self.send_message(self.ChromeDriver.find_elements_by_xpath("//*[contains(@class, 'msg-conversation-card__unread-count')]/parent::div/parent::div"))


    def send_message(self, messages):
        for message in messages:
            message.click()
            time.sleep(5)
            message_body = self.ChromeDriver.find_element_by_class_name("msg-s-event-listitem__body")
            if TEXT_TO_SEARCH in message_body.text:
                time.sleep(3)
                input_field = self.ChromeDriver.find_element_by_class_name("msg-form__contenteditable")
                sender_name = self.ChromeDriver.find_element_by_class_name("msg-s-message-group__name").text.split()[0]
                send_button = self.ChromeDriver.find_element_by_class_name("msg-form__send-button")
                message = f"Hi {sender_name},\n\nThank you for reaching out to me about this opportunity, however I'm not currently looking for a new position at this time.\n\nRegards,\n\nEric"
                input_field.click()
                input_field.send_keys(message)
                time.sleep(2)
                send_button.click()
            else:
                self.ChromeDriver.quit()


def create_auto_replier():
    reply_bot = AutoReply()
    reply_bot.login()
    reply_bot.read_messages()

if __name__ == "__main__":
    threading.Timer(1800, create_auto_replier).start()

