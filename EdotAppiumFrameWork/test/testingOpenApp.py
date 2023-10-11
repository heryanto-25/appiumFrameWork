from EdotAppiumFrameWork.base.DriverClass import Driver
import EdotAppiumFrameWork.utilities.CustomLogger as cl
from EdotAppiumFrameWork.base.BasePage import BasePage

# buka app edot
driver1 = Driver()
log = cl.customLogger()

# setting launching app dan driver
driver = driver1.getDriverMethod()
bp = BasePage(driver)
log.info("Launching app")

# coba screenshot sebelum testcase dijalanin
bp.screenShot("screenshot1")
log.info("Screenshot taken")

# masukin testcase
element = bp.waitForElement("//android.widget.TextView[@text='Skip']" ,"xpath")
bp.clickElement("//android.widget.TextView[@text='Skip']")

