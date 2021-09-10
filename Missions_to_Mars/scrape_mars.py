from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd
from flask import Flask

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_collection = {}

    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    mars_collection["news_title"] = soup.find('div', class_="content_title").get_text()
    mars_collection["news_snip"] = soup.find('div', class_="rollover_description_inner").get_text()

    images_url = 'https://spaceimages-mars.com/image/featured/mars1.jpg'
    browser.visit(images_url)
    response = browser.html
    image_soup = BeautifulSoup(response, 'html.parser')
    xpath = images_soup.find_all('img')[0]["src"]
    featured_image_url = images_url + xpath
    featured_image_url
    pictures = []
    for image in images:
        picture = image[featured_image_url]
        pictures.append(picture)
    
    mars_collection["Feautred_image"] = "https://spaceimages-mars.com/image/featured/mars1.jpg" + pictures[2]


