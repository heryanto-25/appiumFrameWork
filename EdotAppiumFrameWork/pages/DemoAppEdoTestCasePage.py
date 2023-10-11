from EdotAppiumFrameWork.base.BasePage import BasePage
import EdotAppiumFrameWork.utilities.CustomLogger as cl
class DemoAppForm(BasePage):

    """
    fungsi def init ini buat meng-nginitialize method yang dilempar pada
    saat kita pakai class ini jadi method method yang lainnya tidak perlu
    init driver dll lagi
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators yang ada di page
    _plusButton = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[6]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[1]/com.horcrux.svg.SvgView"
    _photoBottomSheetButton = "//*[@resource-id = 'botSheetAddPhoto']"
    _galleryButton = "(//*[@class = 'android.widget.ImageView'])[1]"
    _picButton = "(//*[@class = 'android.widget.ImageView'])[4]"
    _doneButton = "//android.widget.TextView[@text = 'Done']"
    _continueButton = "//android.widget.TextView[@text = 'Continue']"
    _saveDraft = "//android.widget.TextView[@text = 'Save as Draft']"
    _writeCaption = "//android.widget.EditText[@text='Write a caption']"
    _hotButton = "(//*[@class = 'com.horcrux.svg.RectView'])[1]"
    _followingButton = "//android.widget.EditText[@text='Following']"

    # method yang di pakai di page
    def isDisplay(self):
        self.isDisplayed(self._plusButton,"xpath")
        cl.allureLogs("element displayed")

    def ClickAdd(self):
        self.clickElement(self._plusButton,"xpath")
        cl.allureLogs("add button clicked")

    def ClickPhoto(self):
        self.clickElement(self._photoBottomSheetButton)
        cl.allureLogs("photo button clicked")

    def ClickGallery(self):
        self.clickElement(self._galleryButton)
        cl.allureLogs("gallery button clicked")

    def ChooseImg(self):
        self.clickElement(self._picButton)
        cl.allureLogs("chooseImg button clicked")

    def ClickDone(self):
        self.clickElement(self._doneButton)
        cl.allureLogs("done button clicked")

    def ClickContinue(self):
        self.clickElement(self._continueButton)
        cl.allureLogs("continue button clicked")

    def ScrollSave(self):
        self.scrollToElement(self._saveDraft)
        cl.allureLogs("berhasil ke scroll")

    def WriteCaption(self):
        self.sendText("testing draft", self._writeCaption)
        cl.allureLogs("berhasil send text")

    def clickSaveDraft(self):
        self.clickElement(self._saveDraft)

    def clickHotButton(self):
        self.clickElement(self._hotButton)

    def clickFollowing(self):
        self.clickElement(self._followingButton)
