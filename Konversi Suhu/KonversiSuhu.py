print("PROGRAM KONVERSI SUHU")
print("=============================")
print("Ketik Nomor Suhu Awal yang akan Dikonversi")
print("1.Celcius")
print("2.Farenheit")
print("3.Kelvin")
print("4.Reamur")
print("*contoh jika ingin konversi suhu celcius ke suhu lainnya, ketik: 1")
print("-----------------------------")
Pilih = int(input("Ketik Nomor Suhu = "))

# Celcius
if(Pilih == 1):
    Celcius = float(input("Input Suhu dalam Celcius = "))
    print("Celcius = ",Celcius)
    Farenheit = (Celcius*9)/5+32
    Kelvin = Celcius + 273
    Reamur = (Celcius*4)/5
    Farenheit = float(Farenheit)
    Kelvin = float(Kelvin)
    Reamur = float(Reamur)
    print("Konversi Suhu dalam:")
    print("1.Farenheit = ",Farenheit)
    print("2.Kelvin = ",Kelvin)
    print("3.Reamur = ",Reamur)
    print("=============================")
    print("PROGRAM SELESAI")
#Farenheit
elif(Pilih == 2):
    Farenheit = float(input("Input Suhu dalam Farenheit = "))
    print("Farenheit = ",Farenheit)
    Celcius = ((Farenheit-32)*5)/9
    Kelvin = Celcius + 273
    Reamur = ((Farenheit-32)*4)/9
    Celcius = float(Celcius)
    Kelvin = float(Kelvin)
    Reamur = float(Reamur)
    print("Konversi Suhu dalam:")
    print("1.Celcius = ",Celcius)
    print("2.Kelvin = ",Kelvin)
    print("3.Reamur = ",Reamur)
    print("=============================")
    print("PROGRAM SELESAI")

#Kelvin
elif(Pilih == 3):
    Kelvin = float(input("Input Suhu dalam Kelvin = "))
    print("Kelvin = ",Kelvin)
    Celcius = (Kelvin-273.0)
    Farenheit = ((Kelvin - 273)*9)/5 +32
    Reamur = ((Kelvin - 273)*4)/5
    Farenheit = float(Farenheit)
    Celcius = float(Celcius)
    Reamur = float(Reamur)
    print("Konversi Suhu dalam:")
    print("1.Celcius = ",Celcius)
    print("2.Farenheit = ",Farenheit)
    print("3.Reamur = ",Reamur)
    print("=============================")
    print("PROGRAM SELESAI")

#Reamur   
elif(Pilih == 4):
    Reamur = float(input("Input Suhu dalam Reamur = "))
    print("Reamur = ",Reamur)
    Celcius = (Reamur*5)/4
    Farenheit = ((Reamur*9)/4) +32
    Kelvin = (Reamur*5)/4 +273
    Farenheit = float(Farenheit)
    Celcius = float(Celcius)
    Kelvin = float(Kelvin)
    print("Konversi Suhu dalam:")
    print("1.Celcius = ",Celcius)
    print("2.Kelvin = ",Kelvin)
    print("3.Farenheit = ",Farenheit)
    print("=============================")
    print("PROGRAM SELESAI")
