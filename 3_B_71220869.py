print ("=========== CATATAN BELANJA ==========")
print ("=========== Daftar 1 ==========")
mylist = ['Sikat Gigi', 'odol', 'Shampoo', 'Sabun', 'Ciduk']
print ("Daftar Belanja 1 :", mylist)
print ("")
print ("=========== Daftar 2 ==========")
my_list = ['Teh', 'Gula', 'Garam', 'Micin', 'Kecap']
print ("Daftar belanja 2 :", my_list)
print ("")
print ("Jawab dengan angka [1/2]")
print ("1. Rubah Belanjaan")
print ("2. Keluar")
opsi = int(input("Masukkan Pilihan :"))
if opsi == 2:
    print
else:
    if opsi == 1:
        opsi2 = input("Masukkan nama item ke daftar 1 : ")
        opsi3 = int(input("Masukkan index yang ingin dirubah : "))
        mylist[opsi3]=opsi2
        opsi4 = input("Masukkan nama item ke daftar 2 : ")
        opsi5 = int(input("Masukkan index yang ingin dirubah : "))
        my_list[opsi5]=opsi4
        print("")
        print ("===== Daftar 1 =====")
        print ("Daftar Belanja 1: ", mylist)
        print ("")
        print ("===== Daftar 2 ======")
        print ("Daftar Belanja 2: ", my_list)
    else:
        print ("Errorrr")
        




