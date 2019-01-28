from django.contrib.staticfiles.testing import StaticLiveServerTestCase
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
    

if __name__ == '__main__':
    unittest.main(warning = 'ignore')
