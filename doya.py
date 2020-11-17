def not_hesapla(satır):
    satır = satır[:-1]
    liste = satır.split(",")
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])

    son_not = not1*0.3 + not2*0.3 +not3*0.4


    if (son_not >= 95):
        harf = "AA"

    elif (son_not >= 90):
        harf = "BA"

    elif (son_not >= 80):
        harf = "BB"
    elif (son_not >= 70):
        harf = "CB"

    elif (son_not >= 60):
        harf = "CC"
    else:
        harf = "FF"

    return isim+ "------------------------>" +harf +"\n"





with open("dosya.txt" ,"r",encoding= "UTF -8") as file:
    eklenecekler = []
    for i in file:
        eklenecekler.append(not_hesapla(i))


with open("notlar.txt" ,"w", encoding="UTF-8") as file:

    for i in eklenecekler:
       file.write(i)











