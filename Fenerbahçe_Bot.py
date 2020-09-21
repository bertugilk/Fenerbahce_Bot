from selenium import webdriver
import time

class Main():
    def __init__(self):
        self.browser= webdriver.Chrome(r"C:\Users\bertug\Downloads\chromedriver85.exe")
        self.browser.get("https://www.google.com/")

    def Search(self):
        self.browser.fullscreen_window()
        time.sleep(3)
        google_searchbox= self.browser.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")
        google_searchbox.send_keys("Fenerbahçe")
        time.sleep(2)
        searchButton= self.browser.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]")
        searchButton.click()
        self.browser.fullscreen_window()
        time.sleep(5)

    def Haberler(self):
        haberler=self.browser.find_element_by_xpath("//*[@id='sports-app']/div/div[2]/div/div/div/ol/li[2]")
        haberler.click()
        self.browser.fullscreen_window()
        time.sleep(3)
        for i in range(1, 3):
            self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(3)

    def oyuncular(self):
        oyuncu = self.browser.find_element_by_xpath(
            "//*[@id='liveresults-sports-immersive__team-fullpage']/div/div[1]/div[2]/div/ol/li[4]")
        oyuncu.click()
        time.sleep(3)
        self.browser.fullscreen_window()
        for i in range(1, 3):
            self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(3)

    def puanDurumu(self):
        puan=self.browser.find_element_by_xpath("//*[@id='liveresults-sports-immersive__team-fullpage']/div/div[1]/div[2]/div/ol/li[3]")
        puan.click()
        time.sleep(3)
        self.browser.fullscreen_window()
        for i in range(1, 3):
            self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(3)

main=Main()
main.Search()
main.Haberler()
time.sleep(8)
main.oyuncular()
time.sleep(8)
main.puanDurumu()
