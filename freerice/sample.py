from rice import FreeRice

freerice=FreeRice()
freerice.signIn()
freerice.content()
while True:
    sonuc=freerice.mathI()
    freerice.selectMath(sonuc)
    print(sonuc)
    


