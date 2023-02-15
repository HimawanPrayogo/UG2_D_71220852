print("============ MAKANAN ============")
print("1. Telur Bakar\t\t: Rp 7.000")
print("2. Lele Terbang Mas Bhe\t: Rp 10.000")
print("3. Es Coklat Lempu\t: Rp 5.000")
print("4. Es Doger Langensari\t: Rp 13.000")
print()
print("=============== PESANAN ===============")

telur=int(input("Telur Bakar\t:"))
lele=int(input("Lele Terbang\t:"))
coklat=int(input("Es Coklat\t:"))
doger=int(input("Es Doger\t:"))

#rumus
hargatelur=telur*7000
hargalele=lele*10000
hargacoklat=coklat*5000
hargadoger=doger*13000
hargatotal=hargatelur+hargalele+hargacoklat+hargadoger

print("==================== TOTAL ====================")
print("TOTAL TELUR BAKAR x",telur,"\t",": Rp",hargatelur)
print("TOTAL LELE TERBANG x",lele,"\t",": Rp",hargalele)
print("TOTAL ES COKLAT x",coklat,"\t",": Rp",hargacoklat)
print("TOTAL ES DOGER x",doger,"\t",": Rp",hargadoger)
print("Jumlah total biaya yang harus dibayar adalah Rp",hargatotal)
