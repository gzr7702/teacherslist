from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys

class NewUserTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        #self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_user_can_create_a_list_and_retreive_it_later(self):
        self.browser.get('http://localhost:8000/lists')

        #we got to the main page and find the title "Teacher's List"
        assert "Teacher's List" in self.browser.title

        #we see the header that mentions creating a new list
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Welcome to Teacher\'s List', header_text)

        #we are invited to create a new list
        #inputbox = self.browser.find_element_by_id('id_new_list')
        #self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter the name of your new list')

        #we type in the name of the list 'classes'
        """
        div = self.browser.find_element_by_id('form_div')
        inputbox.send_keys('Classes')
        inputbox.send_keys(Keys.ENTER)
        rows = table.find_elements_by_tag_name('td')
        self.assertTrue(any(row.text == "Class\tStudent") for row in rows)
        """


if __name__ == "__main__":
    unittest.main()
