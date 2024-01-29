import scrapy
import requests
from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
import pandas as pd

data = []

class JaverSpider(scrapy.Spider):
    name = 'javer'
    start_urls = [
            'https://www.javer.com.mx/desarrollos/pilares-la-puerta/propiedad/%C3%A1guila',
            'https://www.javer.com.mx/desarrollos/pilares-la-puerta/propiedad/%C3%A1guila-real'
            ]
    #start_urls = [
            #'https://www.javer.com.mx/desarrollos/pilares-la-puerta/propiedad/%C3%A1guila',
            #'https://www.javer.com.mx/desarrollos/pilares-la-puerta/propiedad/%C3%A1guila-real',
            #'https://www.javer.com.mx/desarrollos/privada-belterra/propiedad/mil%C3%A1n',
            #'https://www.javer.com.mx/desarrollos/valle-condesa-sector-britania/propiedad/mil%C3%A1n',
            #'https://www.javer.com.mx/desarrollos/privada-cantabria/propiedad/mil%C3%1n',
            #'https://www.javer.com.mx/desarrollos/valle-condesa-sector-franc%C3%A9s/propiedad/aura-premium',
            #'https://www.javer.com.mx/desarrollos/valle-santa-isabel/propiedad/%C3%A1guila-elite',
            #'https://www.javer.com.mx/desarrollos/valle-santa-isabel/propiedad/albatros',
            #'https://www.javer.com.mx/desarrollos/valle-santa-isabel/propiedad/%C3%A1guila-tienda',
            #'https://www.javer.com.mx/desarrollos/valle-de-lincoln-sector-minas/propiedad/albatros',
            #'https://www.javer.com.mx/desarrollos/valle-de-lincoln-sector-minas/propiedad/albatros-plus',
            #'https://www.javer.com.mx/desarrollos/valle-de-lincoln-sector-minas/propiedad/albatros-piso',
            #'https://www.javer.com.mx/desarrollos/porto-sector-/propiedad/aura-elite-3n',
            #'https://www.javer.com.mx/desarrollos/muriel-residencial/propiedad/aura-elite',
            #'https://www.javer.com.mx/desarrollos/valle-de-santa-elena/propiedad/%C3%A1guila',
            #'https://www.javer.com.mx/desarrollos/mision-de-los-angeles-1er-sector-arcangeles/propiedad/aura-elite',
            #'https://www.javer.com.mx/desarrollos/residencial-privada-las-plazas/propiedad/aura-elite']

    def parse(self, response):
        driver = webdriver.Chrome()
        driver.maximize_window()

        try:
            driver.get(response.url)

            lista_precios = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, f"//p[text()='{"Lista de precios"}']"))
            )

            lista_precios.click()
            list_price = driver.find_elements(By.TAG_NAME, 'p')
            for price in list_price:
                data.append(price.text)

            
        finally:
            for a, d in enumerate(data):
                print(a, d)
            driver.quit()

