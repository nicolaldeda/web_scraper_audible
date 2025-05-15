from selenium import webdriver
from selenium.webdriver.chrome.service import Service


web='https://www.audible.com/search'
service = Service(executable_path = 'D:\\\\Users\\\\dnicolalde\\\\Downloads\\\\chromedriver-win64\\\\chromedriver.exe')
# Set up the Chrome WebDriver
driver = webdriver.Chrome(service=service)
# Set the URL of the page you want to scrape
driver.get(web)
# Wait for the page to load
products = driver.find_elements(by='xpath', value ='//li[contains(@class, "productListItem")]')   

for product in products:
    # Extract the title, author, and runtime
    title = product.find_element(by='xpath', value ='.//h3[contains(@class, "bc-heading")]').text
    author = product.find_element(by='xpath', value ='.//li[contains(@class, "authorLabel")]').text
    runtime = product.find_element(by='xpath', value ='.//li[contains(@class, "runtimeLabel")]').text

    # Print the extracted information
    print(f'Title: {title}')
    print(f'Author: {author}')
    print(f'Runtime: {runtime}')
    print('---')

driver.quit()