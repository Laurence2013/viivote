from django.contrib.auth.models import User
from django.test.client import Client
from nose.tools import nottest
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from main.models import *

class UsersLoginTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
        
        # Setup Lozza's username and password
        my_pass = 'mysha25pass'
        lozza_admin = User.objects.create_superuser('lozza2000', 'lozza2000@gmail.com', my_pass)
        client = Client()
        client.login(username = lozza_admin.username, password = my_pass)


    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    # Lozza has heard about this new sick app, called viivote.com. Out of curiosity
    # Lozza goes away and checked it out
    @nottest
    def test_00_client_goes_to_site_and_try_to_log_in(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/main/'))
        # Lozza noticed that title and header mention viivote
        self.assertIn('viiVote', self.selenium.title)

        # Lozza thinks that he is a member, because he is confused, he decided to enter his username and password
        self.selenium.find_element_by_xpath('//input[@name="username"]').send_keys('lozza199')
        self.selenium.find_element_by_xpath('//input[@name="password"]').send_keys('qazwsxedcrfv')
        self.selenium.find_element_by_xpath('//button[@class]').click()
        # So it failed
        self.fail('Finish the test!')

    # Then Lozza has realises that he is not a member, therefore, he registers
    # He enters his details, clicks on submit
    # Voala! The site takes him back to the login page
    # Lozza this time login his username and password
    def test_01_client_wil_now_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/main/login'))
        # Lozza will now try his username and password
        self.selenium.find_element_by_xpath('//input[@name="username"]').send_keys('lozza2000')
        self.selenium.find_element_by_xpath('//input[@name="password"]').send_keys('mysha25pass')
        self.selenium.find_element_by_xpath('//button[@class]').click()

        main = self.selenium.current_url
        str_main = str(main)
        self.assertEqual('main', str_main[23:-1])

    # And there you go, Lozza was able to go to the main page

    
if __name__ == '__main__':
    unittest.main(warning = 'ignore')
