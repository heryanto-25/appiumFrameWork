# 1. Import the files
import  unittest

from EdotAppiumFrameWork.test.DemoAppEdoTestCase import DemoAppTest


# 2. Create the object of the class using unitTest
dat = unittest.TestLoader().loadTestsFromTestCase(DemoAppTest)
#cf = unittest.TestLoader().loadTestsFromTestCase(ContactFormTest)
#gt = unittest.TestLoader().loadTestsFromTestCase(LoginTest)

# 3. Create TestSuite
#regressionTest = unittest.TestSuite([cf,gt])
regressionTest = unittest.TestSuite([dat])

# 4. Call the Test Runner method
unittest.TextTestRunner(verbosity=1).run(regressionTest)

