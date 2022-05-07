import random
import time
from selenium import webdriver



driver_path = 'C:/Users/es_lo/Desktop/msedgedriver.exe'

browser = webdriver.Edge(executable_path=driver_path)
# browser.get("https://eksisozluk.com/mustafa-kemal-ataturk--34712?p=")
entries = []
pageCount=1
while pageCount <= 10:
    randomPage = random.randint(1,1290)
    browser.get(f"https://eksisozluk.com/mustafa-kemal-ataturk--34712?p={randomPage}")
    content =  browser.find_elements_by_css_selector(".content")
    with open("entry.txt","w",encoding="utf-8") as file:
        for element in content:
            entries.append(element.text)
            file.write(element.text)
    time.sleep(2)
    pageCount += 1


 

# content =  browser.find_elements_by_css_selector(".content")
# for element in content:
#     print(element.text)
#     print("**************************************************")




# time.sleep(10)
browser.close()