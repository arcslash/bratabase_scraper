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
import wget
import json

output_path = "outputs/"
images_path = output_path + "/images/"
labels_path = output_path + "/labels/"
url1 = "https://www.bratabase.com/troubleshoot/"
url2 = "https://www.bratabase.com/troubleshoot/closed/"
if not os.path.exists(images_path):
       print("[-]Path Do not Exist, Making Directories")
       os.makedirs(images_path)
       print("[+]Directory Made:"+images_path)
if not os.path.exists(labels_path):
       print("[-]Path Do not Exist, Making Directories")
       os.makedirs(labels_path)
       print("[+]Directory Made:"+labels_path)
# Adding options to chrome driver
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome('./chromedriver',chrome_options=chrome_options)
urls = [url1, url2]
for url in urls:
    main_links = []
    page_no = 20
    driver.get(url + '?page='+str(page_no))
    print("[+]Moving to URL:{}".format(url + '?page='+str(page_no)))
    try:
        while("404 - There are no bras on this page" not in driver.find_element_by_tag_name('h1').text):
            driver.get(url1 + '?page='+str(page_no))
            print("[+]Moving to URL:{}".format(url + '?page='+str(page_no)))
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
        output_json = {}
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
                image_src = driver.find_elements_by_xpath('.//img')[0].get_attribute("src")
                image_details = driver.find_elements_by_xpath('.//figcaption')[0].text
                image_index_size = driver.find_elements_by_xpath('.//span[@class="index-size"]')[0].text
                image_brand = driver.find_elements_by_xpath('.//span[@class="brand-name"]')[0].text
                image_size = driver.find_elements_by_xpath('.//span[@class="size-str"]')[0].text
                print("Image src:", image_src)
                wget.download(image_src, images_path)
                print("Details:", image_details)
                print("Index size:", image_index_size)
                print("Brand:", image_brand)
                print("Size:", image_size)


                #build json
                output_json['images'].append({'location':image_src, 'description':image_details})
                time.sleep(5)
            output_json['brand'] = image_brand
            output_json['size'] = image_size
            output_json['index_size'] = image_index_size
            output_json['description'] = "main description"
    except Exception as err:
        print("[-]Error:{0}".format(err))
    driver.quit()
