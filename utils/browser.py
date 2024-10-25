from selenium import webdriver

class Browser:
    @staticmethod
    def start_browser():
        options = webdriver.ChromeOptions()
        options.add.argument('--headless')
        options.add.argument('--no-sandbox')
        driver - webdriver.Chrome(options=options)
        return driver
