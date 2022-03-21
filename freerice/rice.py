from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class FreeRice:

    def __init__(self):
        self.browser=webdriver.Firefox()
    
    def signIn(self):
        self.browser.get("https://freerice.com/")
        time.sleep(3)
        self.browser.find_element_by_xpath("/html/body/div/section/div/div[1]/div/div[2]/div/div[2]/button").click()
        time.sleep(3)

    def content(self):
        self.browser.find_element_by_xpath("//*[@id='Path_7605']").click()
        time.sleep(3)
        self.browser.find_element_by_xpath("/html/body/div/nav/div/nav/ul/li[2]/div/a").click()
        time.sleep(3)
        self.browser.get("https://freerice.com/categories")
        time.sleep(3)
        #self.browser.find_element_by_xpath("/html/body/div/div[3]/div[1]/div[2]").click()
        #time.sleep(3)
        self.browser.execute_script("window.scrollTo(0, 2800);")
        time.sleep(3)
        self.browser.find_element_by_xpath("/html/body/div/section/div/div[1]/div/div[2]/div/div/div[9]/div[3]/div/div[1]").click()
        time.sleep(3)

    def mathI(self):
        twoSum=self.browser.find_element_by_class_name("card-title").text
        list1=twoSum.rstrip("=").rstrip(" ").split(" ")
        sonuc=0
        if str(list1[1])=="+":
            sonuc=int(list1[0]) + int(list1[2])
        elif str(list1[1])=="-":
            sonuc=int(list1[0]) - int(list1[2])
        elif str(list1[1])=="x":
            sonuc=int(list1[0]) * int(list1[2])
        else:
            sonuc=int(list1[0]) / int(list1[2])
        return sonuc
        
        
    def selectMath(self,sonuc):

        for num in self.browser.find_elements_by_class_name("fade-appear-done.fade-enter-done"):
            if (num.find_elements_by_class_name("card-button")[0].text == str(int(sonuc))) :
                #num.find_elements_by_class_name("card-button")[0].click()
                num.click()
                break




freerice=FreeRice()
freerice.signIn()
freerice.content()
while True:
    sonuc=freerice.mathI()
    freerice.selectMath(sonuc)
    print(sonuc)
    time.sleep(4)