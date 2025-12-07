# deneme algosu
def toplama(a,b):
    return a + b
print(toplama(5,3))


# üçlüleri karşılaştırma problemi
def compareTiplets(a,b):
    person1_puan=0
    person2_puan=0
    
    for i in range (3):
        if a[i]>b[i]:
            person1_puan +=1
            
        elif a[i] < b[i]:
            person2_puan +=1
        #eşit ise değişiklik yok
    return [person1_puan,person2_puan]

a=[10,30,22]
b=[20,21,10]
sonuc=compareTiplets(a,b)  # [2, 1] dönecektir
print (f"Sonuc:{sonuc}")