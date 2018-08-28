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
from pathlib import Path
import zipfile

#release or development set r for release and d for dev
type = 'd'
# type = 'r'

ch_driver = Path("chromedriver")
if not ch_driver.exists():
    wget.download('https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip')
    zip_ref = zipfile.ZipFile("chromedriver", 'r')
    zip_ref.extractall()
    zip_ref.close()
output_path = "outputs/"
images_path = output_path + "images/"
labels_path = output_path + "labels/"
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
    page_no = 20 if (type == 'd') else 1
    driver.get(url + '?page='+str(page_no))
    print("[+]Moving to URL:{}".format(url + '?page='+str(page_no)))
    try:
        while("404 - There are no bras on this page" not in driver.find_element_by_tag_name('h1').text):
            driver.get(url1 + '?page='+str(page_no))
            time.sleep(3)
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
    print("[+]Start Scrapping...")
    try:
        output_json = {}
        for link in main_links:
            driver.get(link)
            time.sleep(3)
            image_src = ""
            image_details = ""
            image_index_size = ""
            image_brand = ""
            image_size = ""
            if(url == url1):
                pre = "n_"
            else:
                pre = "r_"


            json_save = labels_path +pre +(link.split("/")[len(link.split("/"))-2]) + ".json"



            image_des = driver.find_elements_by_xpath('.//blockquote')[0].text
            image_fit = driver.find_elements_by_xpath('.//div[@class="related-info fit-summary"]')[0].text


            print("Image Description:", image_des)
            print("Image Fit Center:", image_fit)
            images = []
            for image in driver.find_elements_by_xpath('.//a[@class="pic-box"]'):
                print("Attribute:",image.get_attribute("href"))
                images.append(image.get_attribute("href"))
            image_arr = []
            for image in images:
                driver.get(image)
                time.sleep(5)
                image_src = driver.find_elements_by_xpath('.//img')[0].get_attribute("src")
                image_details = driver.find_elements_by_xpath('.//figcaption')[0].text
                image_index_size = driver.find_elements_by_xpath('.//span[@class="index-size"]')[0].text
                image_brand = driver.find_elements_by_xpath('.//span[@class="brand-name"]')[0].text
                image_size = driver.find_elements_by_xpath('.//span[@class="size-str"]')[0].text
                print("Image src:", image_src)
                print("Details:", image_details)
                print("Index size:", image_index_size)
                print("Brand:", image_brand)
                print("Size:", image_size)
                image_save = images_path +pre +(link.split("/")[len(link.split("/"))-2]) +"/" +image_src.split("/")[len(image_src.split("/"))-1]
                if not os.path.exists(images_path +pre + (link.split("/")[len(link.split("/"))-2])):
                    os.makedirs(images_path +pre + (link.split("/")[len(link.split("/"))-2]))
                wget.download(image_src, image_save)
                print(" Image Saved:", image_save)

                print("Filepath:",image_save)
                image_arr.append({"location":str(image_save).replace("'", '"'),"description":str(image_details).replace("'", '"')})
                time.sleep(5)
            output_json['images'] = str(image_arr).replace("'", '"')
            output_json['brand'] = str(image_brand).replace("'", '"')
            output_json['size'] = str(image_size).replace("'", '"')
            output_json['index_size'] = str(image_index_size).replace("'", '"')
            output_json['description'] = str(image_des).replace("'", '"')
            output_json['fit_info'] = str(image_fit).replace("'", '"')
            with open(json_save, "wb") as f:
                f.write(json.dumps(output_json).encode("utf-8"))
            print("[+]File Saved:",json_save)
            print(output_json)
            output_json = {}
            if type == 'd':
                driver.quit()
                exit(0)
    except Exception as err:
        print("[-]Error:{0}".format(err))
    driver.quit()
