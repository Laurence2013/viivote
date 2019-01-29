import requests
from nose.tools import nottest
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from main.tests.db_setup.db_setup import UserRegistrationInfo
from selenium.webdriver.common.keys import Keys 
from selenium import webdriver

class UserRegistrationTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    # Lozza really likes the idea of the website, so he clicks in the Register button
    # He ends up in the register page and input some wrong details, which he accidently typed in wrong
    @nottest
    def test_00_user_lands_on_registration_page_but_enter_the_wrong_email(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/main/register/'))
        # To make sure Lozza checks that the registration page has 'Join Today' text

        # Lozza enters proper username
        self.selenium.find_element_by_xpath('//input[@name="username"]').send_keys('lozza199')

        # In the username Lozza enters the wrong email address 
        self.selenium.find_element_by_xpath('//input[@name="email"]').send_keys('lozza199')

        # Lozza enter the correct password twice
        self.selenium.find_element_by_xpath('//input[@name="password1"]').send_keys('lozzdddddda199')
        self.selenium.find_element_by_xpath('//input[@name="password2"]').send_keys('lozzdddddda199')

        self.selenium.find_element_by_xpath('//button[@class]').click()
        # So it failed
        self.fail('Finish the test!')

    # Because Lozza realised he entered wrong credentials he now enters with care his credentials and he is successfull because he is sent to the login page and credentials is saved to db
    def test_01_user_credentials_is_correct_and_now_is_saved_to_db_and_sent_back_to_login_page(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/main/register/'))
        # To make sure Lozza checks that the registration page has 'Join Today' text

        # Lozza enters proper username
        self.selenium.find_element_by_xpath('//input[@name="username"]').send_keys('lozza1999')

        # In the username Lozza enters the wrong email address 
        self.selenium.find_element_by_xpath('//input[@name="email"]').send_keys('lozza1999@gmail.com')

        # Lozza enter the correct password twice
        self.selenium.find_element_by_xpath('//input[@name="password1"]').send_keys('lozzdddddda199')
        self.selenium.find_element_by_xpath('//input[@name="password2"]').send_keys('lozzdddddda199')

        self.selenium.find_element_by_xpath('//button[@class]').click()
        
        login = self.selenium.current_url
        str_login = str(login)

        # And there you go, Lozza was able to go to the login page
        self.assertEqual('main/login', str_login[23:-1])


if __name__ == '__main__':
    unittest.main(warning = 'ignore')
