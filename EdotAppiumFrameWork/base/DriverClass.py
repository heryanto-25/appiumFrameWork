from appium import  webdriver


class Driver:

    def getDriverMethod(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        #desired_caps['platformVersion'] = '10'
        #desired_caps['deviceName'] = 'Pixel'
        desired_caps['app'] = ('/Users/heryanto/Downloads/Edot/APP Edot/app-release-staging(v0.99.0-stag).apk')
        desired_caps['noReset'] = True
        #desired_caps['appPackage'] = 'com.code2lead.kwad'
        #desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        return driver