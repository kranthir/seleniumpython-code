from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.alert import Alert
#class selenium.webdriver.common.action_chains.ActionChains(driver)

#driver = webdriver.Chrome()
driver = webdriver.Chrome("C:\chandhu\chromedriver.exe")
#driver.get("https://www.amazon.com/")
driver.get("http://toolsqa.wpengine.com/handling-alerts-using-selenium-webdriver/")
driver.find_element_by_xpath("//*[@id='content']/p[4]/button").click()

#driver.find_element_by_xpath(".//*[@id='content']/p[8]/button").click()
time.sleep(2)
#Alert(driver).accept()
print Alert(driver).text
#driver.find_element_by_id("pass").send_keys("chad")

#driver.implicitly_wait(50)
#driver.maximize_window()
time.sleep(5)

#myele = driver.find_element_by_xpath("//*[@id='nav-link-prime']/span[2]")
act = ActionChains(driver)






#act.click(Keys.CONTROL)
#m1=driver.find_element_by_xpath("//*[@id='a-autoid-0-announce']/span")
#m2=driver.find_element_by_xpath("//*[@id='twotabsearchtextbox']")
#s=ActionChains(driver).key_down(Keys.CONTROL).context_click(m1).perform()
#ActionChains(driver).key_down(Keys.CONTROL).click_and_hold(m1).perform()

time.sleep(2)
#ActionChains(driver).release().perform()
#ActionChains(driver).move_to_element(m2).release().perform()
#m33=driver.find_element_by_xpath("//*[@id='popular-departments-ns_41HN88B4VDM4P2E6GGTX_1906_']/h3")
#ActionChains(s).move_by_offset(122,252).perform()

#m=act.move_to_element(myele).perform()
#click((Keys.CONTROL))


#driver.find_element_by_xpath(".//*[@id='u_0_o']").click()
#driver.back()
#driver.forward()
#driver.get_screenshot_as_file("C:\Users\ChandrashekarChary\Desktop\hy\hai.png")

#Sel = Select(driver.find_element_by_xpath("//*[@id='day']"))
#Sel.select_by_index(4)
time.sleep(2)
#Sel.select_by_visible_text("25")
#select = Select(driver.find_element_by_name('name'))

#emailele=WebDriverWait(driver,5).until(lambda driver: driver.find_element_by_id("email"))
#emailele.send_keys("chdn")

#driver.close()
