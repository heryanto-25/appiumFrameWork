import time

from EdotAppiumFrameWork.base.BasePage import BasePage
import pytest
from EdotAppiumFrameWork.base.DriverClass import Driver

"""
file ini gak boleh di ubah namanya, kalau di ubah nanti method di file ini gak akan ke execute pas kita jalanin py.test
file name conftest ini template bawaan dari pytest, jadi misalkan kalau ada file name conftest di salah satu package
py.test, compilernya bakal jalanin file conftest dulu sebelum mereka jalanin file test_testcase sehingga nanti file test_testcaseName
bisa memakai method yang ada di dalam conftest ini (method beforeClass dan method afterClass)
"""


"""
ada logic cara makai base page didalam, jadi sebelum makai base page
script driver = driver1.getDriverMethod() harus diatas dlu baru kita parse
drivernya kedalam BasePage(driver) karna basepage itu butuh param driver
buat jalanin semua methodnya
"""
@pytest.fixture(scope='class')
def beforeClass(request):
    print('Before Class')
    driver1 = Driver()
    driver = driver1.getDriverMethod()
    bs = BasePage(driver)
    bs.takeScreenshot("testing1")
    print('Jalan screenshot')
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print('After Class')

@pytest.fixture()
def beforeMethod():
    print('Before Method')
    yield
    print('After Method')
    #BasePage.takeScreenshot("testing")
