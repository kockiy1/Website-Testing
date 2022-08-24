import unittest
from selenium import webdriver
import page


class PythonOrgSearch(unittest.TestCase):
	
	def setUp(self):
		''' Setting up for the testing, driver and opening a page. Will run for every test case in the class. '''
		self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
		self.driver.get("http://www.pyhton.org")
		
	def test_search_python(self):
		mainPage = page.MainPage(self.driver)
		assert mainPage.is_title_matches()
		mainPage.search_text_element = "pycon"
		mainPage.click_go_button()
		search_result_page = page.SearchResultPage(self.driver)
		assert search_result_page.is_result_found()
		
	def tearDown(self):
		''' Run after test case, clean up the work. '''
		self.driver.close()
		

		
		
if __name__ == "__main__":
	unittest.main()
