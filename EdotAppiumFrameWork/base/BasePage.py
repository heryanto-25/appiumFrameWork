import allure
from allure_commons.types import AttachmentType
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import EdotAppiumFrameWork.utilities.CustomLogger as cl
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest

class BasePage:
    log = cl.customLogger()
    """
    ini kalau mau pakai class ini harus ada param driver, tau dari mana
    harus ada param driver? nah di python itu cara kita kasih tau
    ke org kalau class ini butuh param itu dari method def __init__ gtu
    kalau def __init__(self, nama) berarti butuh dimasukin param nama saat
    kita mau pakai method ini, cthnya  bs = BasePage(nama) jadi nanti namanya
    bakal jadi parameternya buat method yang ada di class basepage sehingga
    nanti di base page bisa pakai variabel nama ini.
    """


    """
    logic try and expect
    try and expect itu fungsinya kek if else
    disini walaupun testcasenya gagal klik attributnya, dia gak akan fail langsung
    karena dia pakai konsep try and expect, jdi konsepnya itu jika kondisi di dalam try 
    itu failed, maka app tidak langsung error melainkan langsung lompat ke kondisi yang
    ada di expect, klu di expectnya kondisinya sukses maka kodingannya gak akan lempar
    error. itu sebabnya kalau misalkan di kodingan di bawah klu kita gagal ngeklick
    dia tidak error karna dia akan jalankan kodingan expect yaitu print log doang
    dan itu bukan kondisi gagal jdi gak failed karna log gagalnya berhasil
    ke print
    
    cth :
     def scrollToElement3(self, locatorValue, max_swipes=0, timeout=10, locatorType="xpath"):
            i = 10;
            try:
               assert i > 50
               self.log.info("testing 1")
            except:
                self.log.info("testing tanpa assert")
    """
    def __init__(self, driver):
        self.driver = driver

    def waitForElement(self, locatorvalue, locatorType):
        locatorType = locatorType.lower()
        element = None
        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])
        if locatorType == "id":
            element = wait.until(lambda x: x.find_element(AppiumBy.ID, locatorvalue))
            return element
        elif locatorType == "class":
            element = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME, locatorvalue))
            return element
        elif locatorType == "des":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'UiSelector().description("%s")' % (locatorvalue)))
            return element
        elif locatorType == "index":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(%d)" % int(locatorvalue)))
            return element
        elif locatorType == "text":
            element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("%s")' % locatorvalue))
            return element
        elif locatorType == "xpath":
            element = wait.until(lambda x: x.find_element(AppiumBy.XPATH, '%s' % (locatorvalue)))
            return element
        else:
            self.log.info("Locator value " + locatorvalue + "not found")
            ##assert False
            return element

    def getElement(self, locatorValue, locatorType="xpath"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            self.log.info("Element found with LocatorType: " + locatorType + " with the locatorValue :" + locatorValue)
        except:
            self.log.info(
                "Element not found with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
        return element

    def clickElement(self, locatorValue, locatorType="xpath"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            element.click()
            self.takeScreenshot(locatorType)
            self.log.info(
                "Clicked on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
        except:
            self.log.info(
                "Unable to click on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            raise Exception(f"Element {locatorValue} not found")

    def sendText(self, text, locatorValue, locatorType="xpath"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            element.send_keys(text)
            self.log.info(
                "Send text  on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
        except:
            self.log.info(
                "Unable to send text on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            raise Exception(f"Element {locatorValue} not found")

    def isDisplayed(self, locatorValue, locatorType="xpath"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            element.is_displayed()
            self.log.info(
                " Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + "is displayed ")
            return True
        except:
            self.log.info(
                " Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + " is not displayed")
            return False


    def screenShot(self, screenshotName):
        fileName = screenshotName + "_" + (time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshotDirectory = "../screenshots/"
        screenshotPath = screenshotDirectory + fileName
        try:
            self.driver.save_screenshot(screenshotPath)
            self.log.info("Screenshot save to Path : " + screenshotPath)

        except:
            self.log.info("Unable to save Screenshot to the Path : " + screenshotPath)

    def takeScreenshot(self, text):
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)

    def tapAndHold(self, locatorValue, locatorType="xpath"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            action = ActionChains(self.driver)
            action.click_and_hold(element).perform()
            self.log.info(
                " Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + "is displayed ")
        except:
            self.log.info(
                " Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + " is not displayed")
            raise Exception(f"Element {locatorValue} not found")

    def scrollToElement(self, locatorValue, max_swipes=0, timeout=10,locatorType="xpath"):
        while(max_swipes<5):
            try:
                locatorType = locatorType.lower()
                element = self.getElement(locatorValue, locatorType)
                if(element != None):
                    return True
                self.log.info("ini elementnya = " + element)
                self.log.info(
                    " Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + "is displayed ")
                max_swipes = 5
            except:
                # Scroll down using TouchAction
                size = self.driver.get_window_size()
                startx = 10
                starty = size['height'] * 0.8
                endy = size['height'] * 0.2
                endx = 10
                actions = TouchAction(self.driver)
                actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()
                time.sleep(2)
                self.log.info("Scroll element not found")
                max_swipes +=1
