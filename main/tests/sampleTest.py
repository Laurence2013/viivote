from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver

class SampleTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_00_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/main/'))
