#1
def konversi_suhu(suhu, satuan: str):

 if satuan == 'C':
    return suhu *9 /5 + 32
 else:
    return (suhu - 32 ) *5/9

suhu_celcius = float(input("Masukkan suhu dalam Celcius: "))
suhu_fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))

#Mengkonversikan suhu ke Farenheit
suhu_fahrenheit_dari_celcius = konversi_suhu(suhu_celcius, 'C')
print(f"{suhu_celcius} Celcius sama dengan {suhu_fahrenheit_dari_celcius} Fahrenheit.")

# Mengkonversi suhu Fahrenheit ke Celcius
suhu_celcius_dari_fahrenheit = konversi_suhu(suhu_fahrenheit, 'F')
print(f"{suhu_fahrenheit} Fahrenheit sama dengan {suhu_celcius_dari_fahrenheit} Celcius.")

#2
sum = lambda S: S*S;
S = int(input("panjang sisi: "))
luas = sum(S)
print ("luas persegi : ",luas)