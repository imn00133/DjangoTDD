from selenium import webdriver

browser = webdriver.Firefox(executable_path='C:/Users/Jaehyeong/AppData/Local/Programs/python/geckodriver.exe')
browser.get('http://localhost:8000')

assert 'Django' in browser.title
