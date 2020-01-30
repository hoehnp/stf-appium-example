import os
from time import sleep

import unittest

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class SimpleAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps['platformName'] = 'Android'
        desired_caps['automationName'] = 'uiAutomator2'
        desired_caps['deviceName'] = 'MR7LIZDUQKHM6SY5'
        desired_caps['newCommandTimeout'] = 9999
        desired_caps['app'] = 'apks/android-debug-0.5.4.apk'
        desired_caps['udid'] = 'MR7LIZDUQKHM6SY5'
        self.driver = webdriver.Remote('http://10.0.0.178:4723/wd/hub', desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def test_find_elements(self):
        try:
            #if self.driver.is_locked():
            self.driver.unlock()
            video=self.driver.start_recording_screen()
            el = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("OK")')
            el.click()
        except Exception as e:
            pass
        try:
            el = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("Yes")')
            el.click()
        except Exception as e:
            pass
        try:
            el = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("OK")')
            el.click()
        except Exception as e:
            pass
        self.driver.press_keycode(82)
        try:
            el = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("Download")')
            el.click()
            el = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("Europe")')
            el.click()
            el = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("Azores")')
            el.click()
            self.driver.get_screenshot_as_file('/home/stf_user/shot.png')
            sleep(100)
            #video = self.driver.stop_recording_screen()
            #self.driver.stop_recording_screen()
            #self.driver.save_recording_screen('/home/stf_user/video.mp4')
            #newfile=open('/tmp/video.mp4','wb')
        except Exception as e:
            pass



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
