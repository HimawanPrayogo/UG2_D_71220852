while True:
 print("!! Selamat datang di H+ GYM !!")
 print("Silahkan pilih menu dibawah ini:")
 print("1. Menambah data \n2. Menampilkan data \n3. Keluar")

 pilihan=input("Silahkan masukan pilihan yang anda inginkan:")

 tnama=[""]
 tjenis=[""]
 if pilihan=="1":
     nama=input("Masukan nama pelanggan:")
     jenis=input("Masukan jenis member:")
     tnama.append(nama)
     tjenis.append(jenis)
     print("Data sudah berhasil ditambahkan!")

 elif pilihan=="2":
     print("-------------------")

     print("pelanggan","\n",tnama)
     print("member","\n",tjenis)

 else:
     print("Sistem Berhenti")
     break
    

    
