from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

class SampleTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    # Lozza has heard about this new sick app, called viivote.com. Out of curiosity
    # Lozza goes away and checked it out
    def test_00_client_goes_to_site_and_try_to_log_in(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/main/'))
        # Lozza noticed that title and header mention viivote
        self.assertIn('viiVote', self.selenium.title)

        # Lozza thinks that is a member, because he is confused, he decided to enter his username and password
        self.selenium.find_element_by_xpath('//input[@name="username"]').send_keys('lozza199')
        self.selenium.find_element_by_xpath('//input[@name="password"]').send_keys('qazwsxedcrfv')
        self.selenium.find_element_by_xpath('//button[@class]').click()
        self.fail('Finish the test!')

        




if __name__ == '__main__':
    unittest.main(warning = 'ignore')
