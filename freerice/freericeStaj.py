from selenium import webdriver #webdriver’ı importluyoruz
import time #time modülünü importluyoruz
from selenium.webdriver.common.keys import Keys #tuşları kullanmak için importluyoruz
class FreeRice: #FreeRice isimli bir class tanımlıyoruz

    def __init__(self): #Constructor tanımlıyoruz
        self.browser=webdriver.Firefox()#browser olarak Firefox’u seçiyorum
    
    def signIn(self): #Giriş için fonksiyon tanımlıyorum
        self.browser.get("https://freerice.com/") #freerice sitesine giriyoruz
        time.sleep(3) # 3 saniye bekliyoruz
        self.browser.find_element_by_xpath("/html/body/div/section/div/div[1]/div/div[2]/div/div[2]/button").click()
        #save butonuna tıklıyoruz
        time.sleep(3) #3 saniye bekliyoruz

    def content(self): #content fonksiyonu tanımlıyoruz
        self.browser.find_element_by_xpath("//*[@id='Path_7605']").click()#sol üstteki içindekiler butonuna tıklıyorum
        time.sleep(3) #3 saniye bekliyoruz
        self.browser.find_element_by_xpath("/html/body/div/nav/div/nav/ul/li[2]/div/a").click() #listedeki categories butonuna tıklıyoruz
        time.sleep(3) #3 saniye bekliyoruz
        self.browser.get("https://freerice.com/categories") #kategori sekmesini yeni bir sayfada açıyoruz
        time.sleep(3) #3 saniye bekliyoruz
        #self.browser.find_element_by_xpath("/html/body/div/div[3]/div[1]/div[2]").click() #ekrana gelen reklamı kapatıyoruz
        #time.sleep(3) #3 saniye bekliyoruz
        self.browser.execute_script("window.scrollTo(0, 2800);") #scrollu aşağı indirip matematik kategorisine kadar indiriyoruz
        time.sleep(3) #3 saniye bekliyoruz
        #self.browser.find_element_by_xpath("/html/body/div/section/div/div[1]/div/div[2]/div/div/div[10]/div[3]").click()
        self.browser.find_element_by_xpath("/html/body/div/section/div/div[1]/div/div[2]/div/div/div[9]/div[3]/div/div[1]").click()
        #self.browser.find_element_by_xpath("/html/body/div/section/div/div[1]/div/div[2]/div/div/div[10]/div[2]/div/div[1]").click()
        #Basic Math’ı tıklıyoruz
        time.sleep(3) #3 saniye bekliyoruz

    def mathI(self): #mathI fonksiyonu tanımlıyoruz
        twoSum=self.browser.find_element_by_class_name("card-title").text
        #gelen sayfadaki sorunun text kısmını değişkenin içine atıyorum
        list1=twoSum.rstrip("=").rstrip(" ").split(" ")
        #eşittir ve boşluğu rstrip() metodu ile siliyorum, split() metodu ile boşluğa göre bölüyorum
        sonuc=0 #sonuç değerine sıfıra eşitliyorum
    # Üç parçaya böldüğüm bu sonucu listenin içine attım ve bu listenin 0. ve 2. İndisinde rakamlar, 1. İndisinde ise işlem bulunuyor,
    # buna göre aşağıda dört işlem algoritması kuracağız;
        if str(list1[1])=="+": #listenin 1. Elemanı artı ise
            sonuc=int(list1[0]) + int(list1[2]) #toplama işlemi yap
        elif str(list1[1])=="-": #listenin 1. Elemanı eksi ise
            sonuc=int(list1[0]) - int(list1[2]) #çıkarma işlemi yap
        elif str(list1[1])=="x": #listenin 1. Elemanı çarpma ise
            sonuc=int(list1[0]) * int(list1[2]) #çarpma işlemi yap
        else:
            sonuc=int(list1[0]) / int(list1[2]) #bölme işlemi yap
        return sonuc #sonucu bize döndür
        
        
    def selectMath(self,sonuc): #selectMath diye fonksiyon tanımladım(sorulardaki doğru şıkkı seçmek için)

        for num in self.browser.find_elements_by_class_name("fade-appear-done.fade-enter-done"): 
            #class name selektörüne göre for döngüsü yaptım
            if (num.find_elements_by_class_name("card-button")[0].text == str(int(sonuc))) : 
                #eğer class name’in sıfırıncı indisinin texti sonucumuza eşit ise
                #num.find_elements_by_class_name("card-button")[0].click() 
                num.click()#doğru şıkkı seç
                break #döngüden çık
    #Şimdide yazdığımız kodları çağıralım;
freerice=FreeRice() #yazdığımız sınıfın bir nesnesini oluşturduk
freerice.signIn() #giriş metodunu çağırdık
freerice.content() #içerik metodunu çağırdık
while True: #while döngüsü tanımladık
    sonuc=freerice.mathI() #sorunun doğru cevabını sonuç değişkenine attık
    freerice.selectMath(sonuc) #doğru sonucu tıklamak için metodumuza doğru sonucu parametre olarak yolladık ve seçme işlemi yaptık
    print(sonuc) #her sorunun doğru cevabını ekranımıza yazdık
    time.sleep(4)#4 saniye bekledik

