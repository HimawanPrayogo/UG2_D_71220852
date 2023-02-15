brand=input("Masukkan brand apa saja yang hendak dibeli (pisahkan dengan koma:").split(",")

harga1=input("Berapa harga barang",brand[0],"?:")
if harga1>=10000000:
    harga1s=harga1*10/100
    print("Harga",brand[0],"\t Rp.",harga1,"Diskon Rp.",harga1s)

elif harga1>=25000000:
    harga1ss=harga1*25/100
    print("Harga",brand[0],"\t Rp.",harga1,"Diskon Rp.",harga1ss)
else:
    print("Harga",brand[0],"\t Rp.",harga1,"Diskon Rp.",0)
    
harga2=input("Berapa harga barang",brand[1],"?:")
if harga2>=10000000:
    harga2s=harga1*10/100
    print("Harga",brand[1],"\t Rp.",harga2,"Diskon Rp.",harga2s)

elif harga2>=25000000:
    harga2ss=harga1*25/100
    print("Harga",brand[1],"\t Rp.",harga2,"Diskon Rp.",harga2ss)
else:
    print("Harga",brand[1],"\t Rp.",harga2,"Diskon Rp.",0)
    
harga3=input("Berapa harga barang",brand[2],"?:")
if harga3>=10000000:
    harga3s=harga1*10/100
    print("Harga",brand[2],"\t Rp.",harga3,"Diskon Rp.",harga3s)

elif harga3>=25000000:
    harga3ss=harga1*25/100
    print("Harga",brand[2],"\t Rp.",harga3,"Diskon Rp.",harga3ss)
else:
    print("Harga",brand[2],"\t Rp.",harga3,"Diskon Rp.",0)

harga4=input("Berapa harga barang",brand[3],"?:")
if harga4>=10000000:
    harga4s=harga1*10/100
    print("Harga",brand[3],"\t Rp.",harga4,"Diskon Rp.",harga4s)

elif harga4>=25000000:
    harga4ss=harga1*25/100
    print("Harga",brand[3],"\t Rp.",harga4,"Diskon Rp.",harga4ss)
else:
    print("Harga",brand[3],"\t Rp.",harga4,"Diskon Rp.",0)

totaldisc=harga1s+harga2s+harga3s+harga4s+harga1ss+harga2ss+harga3ss+harga4ss
print("Total diskon yang anda dapatkan adalah sebesar: Rp.",totaldisc)

