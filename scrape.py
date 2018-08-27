'''
Auther: Ishara Abeykoon
email: isharaux@gmail.com
'''
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import wget
import os
import time

output_path = "outputs/"
url1 = "https://www.bratabase.com/troubleshoot/"
url2 = "https://www.bratabase.com/troubleshoot/closed/"
if not os.path.exists(output_path):
       print("[-]Path Do not Exist")
       os.makedirs(output_path)
# Adding options to chrome driver
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome('./chromedriver',chrome_options=chrome_options)

'''
Scraping Unsolved
'''
main_links = []
page_no = 20
driver.get(url1 + '?page='+str(page_no))
print("[+]Moving to URL:{}".format(url1 + '?page='+str(page_no)))
try:
    while("404 - There are no bras on this page" not in driver.find_element_by_tag_name('h1').text):
        driver.get(url1 + '?page='+str(page_no))
        print("[+]Moving to URL:{}".format(url1 + '?page='+str(page_no)))
        try:
             for link in driver.find_elements_by_class_name('fit-request-list-item'):
                 print("[+]Added Link:", link.get_attribute("href"))
                 main_links.append(link.get_attribute("href"))
        except NoSuchElementException as err:
            print("[-]Error:{0}".format(err))
        page_no = page_no + 1
except Exception as err:
    print("[-]Error:{0}".format(err))

##scrapping the main_links

try:
    for link in main_links:
        driver.get(link)
        time.sleep(3)
        #images = driver.find_elements_by_xpath("//img[@class='photo']")
        images = []
        for image in driver.find_elements_by_xpath('.//a[@class="pic-box"]'):
            print("Attribute:",image.get_attribute("href"))
            images.append(image.get_attribute("href"))
        for image in images:
            driver.get(image)
            print("Image src:",driver.find_elements_by_xpath('.//img')[0].get_attribute("src"))
            print("details:",driver.find_elements_by_xpath('.//figcaption')[0].text)
            print("index size:",driver.find_elements_by_xpath('.//span[@class="index-size"]')[0].text)
            print("brand:",driver.find_elements_by_xpath('.//span[@class="brand-name"]')[0].text)
            print("size:",driver.find_elements_by_xpath('.//span[@class="size-str"]')[0].text)
            time.sleep(5)






        exit(0)
except Exception as err:
    print("[-]Error:{0}".format(err))

driver.quit()
