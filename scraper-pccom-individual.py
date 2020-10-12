from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import pandas as pd
import time

#Previously download the DRIVER depending on which BROWSER are you going to use
#in this case I am using chrome
#download chrome driver depending on your borwser VERSION
#download page https://chromedriver.chromium.org/downloads
driver = webdriver.Chrome('/Users/manutaberner/Downloads/chromedriver') #path to driver

product_list = []
price_list = []
brand_list = []
category_list = []

#getting the web page, SELECT WHICH ONE BY CHANGING THE VARIABLE "componentes"
#'placas-base
#'procesadores'
#'tarjetas-graficas'
#'capturadoras'
#'discos-duros'
#'memorias-ram'
#'grabadoras-dvd-blu-ray'
#'multilectores'
#'tarjetas-sonido'
#'ventiladores'
#'fuentes-alimentacion'
#'modding'
#'cables-internos-de-pc'
#'conectividad'
componentes = 'ventiladores'
webpage = 'https://www.pccomponentes.com/'+componentes                           
driver.get(webpage)                          
time.sleep(2)                            

#CLICKS on the button "Ver más" so all the content starts loading                            
driver.find_element_by_id("btnMore").send_keys(Keys.ENTER)                           

#SCROLL TO BOTTOM to load all the content                            
current_scroll_position, new_height= 0, 1 #start position and height of the scroll                           
scroll_speed = 50 #SPEED of the scroll, depends on YOUR INTERNET, if your time of page loading is slow DECREASE the number                           

#starts scrolling                            
while current_scroll_position <= new_height:                             
    current_scroll_position += scroll_speed                          
    driver.execute_script("window.scrollTo(0, {});".format(current_scroll_position))                             
    time.sleep(0.01) #time to let the page load                             
    new_height = driver.execute_script("return document.body.scrollHeight")                          

#GETTING THE PRODUCT INFORMATION                             
names = driver.find_elements_by_xpath("//a[@class='c-product-card__title-link cy-product-link']")                                        
prices = driver.find_elements_by_xpath("//a[@class='c-product-card__title-link cy-product-link']")                           
brands = driver.find_elements_by_xpath("//a[@class='c-product-card__title-link cy-product-link']")                               
categories = driver.find_elements_by_xpath("//a[@class='c-product-card__title-link cy-product-link']")                               


for p in range(len(names)):                          
    product_list.append(names[p].text)                           
    precio = prices[p].get_attribute("data-price")                           
    price_list.append(precio)                            
    marca = brands[p].get_attribute("data-brand")                            
    brand_list.append(marca)                             
    categoria = categories[p].get_attribute("data-category")                             
    category_list.append(categoria)                              

#CREATING THE DATAFRAME
data_tuples = list(zip(product_list[0:],price_list[0:],brand_list[0:],category_list[0:]))
df = pd.DataFrame(data_tuples, columns=['Product','Price','Brand','Category'])

print(df)

#Output to CSV format
now = datetime.now() # current date and time
date_time = now.strftime("%m/%d/%Y_%H:%M:%S")
df.to_csv('pccom-componentes_.csv',index = False, encoding='utf-8')

#close the driver
driver.close()