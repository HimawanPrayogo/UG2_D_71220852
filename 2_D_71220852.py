nomor=input("Masukkan Nomor Telepon :")
tipe=nomor[0:3+1]
belakang=nomor[-1]
d=int(belakang)
c=len(nomor)
if c==12:
    if tipe=="0816":
        print("Anda menggunakan operator Indosat")

    elif tipe=="0814":
        print("Anda menggunakan operator Telkomsel")

    else:
        print("Operator Anda tidak diketaui")

    if d%2==0:
        print("Nomor anda berakhiran genap")

    else:
        print("Nomor anda berakhiran ganjil")
else:
    print("nomor anda belum 12 digit")

