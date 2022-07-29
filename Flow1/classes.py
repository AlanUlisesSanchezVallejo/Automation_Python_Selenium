# from businessHours import test_businessHours
from .imports import *
from .features.features import *


	
class Usando_unittest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")
	
	def test_flow(self):
		driver = self.driver
		driver.get("http://dev.omnitracslabs.com")

		# file = open(r'C:\Users\Alan Sanchez\Desktop\Automation_\Flow1\readme.txt','w')

		# file.write('--- Testing Login... ---' + os.linesep)
		test_login(driver)	
		# file.write('Login pass the test Successfully :)' + os.linesep)
		
		# file.write('--- Testing searchByAddress... ---' + os.linesep)
		test_searchByAddress(driver)
		# file.write('searchByAddress pass the test Successfully :)' + os.linesep)

		test_searchAddressResults(driver)
		# file.close()

		test_editDetails(driver)

		test_closures(driver)

		test_appointmentSch(driver)

		test_amenities(driver)

		test_services(driver)


	def tearDown(self):
		self.driver.close()
	#driver.close()
