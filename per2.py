angka1 = int(input('Masukan Angka Pertama : '))
angka2 = int(input('Masukan Angka Kedua : '))
print('Operator : \n1.Penjumlahan \n2.Pengurangan \n'
        '3.Perkalian \n4.Pembagian')
pilih = int(input('Masukan Operator : '))
if pilih == 1:
    tambah = angka1+angka2
    print('Hasilnya Adalah ', tambah)
elif pilih == 2:
    kurang = angka1-angka2
    print('Hasilnya Adalah ', kurang)
elif pilih == 3:
    kali = angka1*angka2
    print('Hasilnya Adalah ', kali)
elif pilih == 4:
    bagi = angka1/angka2
    print('Hasilnya Adalah ', bagi)
else:
    print('Operator yang anda masukan tidak ada')