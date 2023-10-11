import time
import unittest
import pytest

from EdotAppiumFrameWork.base.DriverClass import Driver
import EdotAppiumFrameWork.utilities.CustomLogger as cl
from EdotAppiumFrameWork.base.BasePage import BasePage
from EdotAppiumFrameWork.pages.DemoAppEdoTestCasePage import DemoAppForm

"""
cara 1 

# buka app edot
driver1 = Driver()
log = cl.customLogger()

# setting launching app dan driver
driver = driver1.getDriverMethod()
df = DemoAppForm(driver)
log.info("Launching app")

# masukin testcase
time.sleep(2)
df.ClickAdd()
df.ClickPhoto()

time.sleep(2)
df.ClickGallery()

time.sleep(2)
df.ChooseImg()

df.ClickDone()

df.ClickContinue()
"""

@pytest.mark.usefixtures("beforeClass","beforeMethod")
class DemoAppTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.df = DemoAppForm(self.driver)

    @pytest.mark.run(order=1)
    def test_stepOne(self):
        cl.allureLogs("app launched")

        #self.df.clickHotButton()
        #self.df.clickFollowing()
        time.sleep(10)
        self.df.ClickAdd()
        self.df.ClickPhoto()

    @pytest.mark.run(order=2)
    def test_stepTwo(self):
        self.df.ClickGallery()
        self.df.ChooseImg()
        self.df.ClickDone()
        self.df.ClickContinue()
        self.df.WriteCaption()
        test1 = self.df.ScrollSave()
        self.df.clickSaveDraft()
        cl.allureLogs(test1)
        #self.df.check()




