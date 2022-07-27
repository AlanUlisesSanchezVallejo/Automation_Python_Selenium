# from businessHours import test_businessHours
from .imports import *
from .features import *


	
class Usando_unittest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")
	
	def test_flow(self):
		driver = self.driver
		driver.get("http://dev.omnitracslabs.com")

		file = open(r'C:\Users\Alan Sanchez\Desktop\Automation_\Flow1\readme.txt','w')

		file.write('--- Testing Login... ---' + os.linesep)
		test_login(driver)	
		file.write('Login pass the test Successfully :)' + os.linesep)
		
		file.write('--- Testing searchByLocation... ---' + os.linesep)
		test_searchByLocation(driver)
		file.write('searchByLocation pass the test Successfully :)' + os.linesep)

		file.write('--- Testing Searching Results... ---' + os.linesep)
		test_SearchResults(driver)
		file.write('Searching Results pass the test Successfully :)' + os.linesep)

		file.write('--- Testing Edit Details... ---' + os.linesep)
		test_editDetails(driver)
		file.write('Edit Details pass the test Successfully :)' + os.linesep)

		file.write('--- Edit Location Name.... ---' + os.linesep)
		test_locationNames(driver,file)
		file.write('Edit Location Name pass the test Successfully :)' + os.linesep)

		file.write('--- Edit Location TYPE.... ---' + os.linesep)
		test_locationTypes(driver,file)
		file.write('Edit Location TYPE pass the test Successfully :)' + os.linesep)
		
		file.write('--- Edit Contact.... ---' + os.linesep)
		test_contact(driver,file)
		file.write('Edit Contact pass the test Successfully :)' + os.linesep)

		file.write('--- BUSINESS HOURS.... ---' + os.linesep)
		test_businessHours(driver,file)
		file.write('BUSINESS HOURS pass the test Successfully :)' + os.linesep)

		test_submitButton(driver,file)
		file.write('--- CONGRATULATIONS! Automation Regression test was a success ---')

		file.close()

	def tearDown(self):
		self.driver.close()
	#driver.close()
