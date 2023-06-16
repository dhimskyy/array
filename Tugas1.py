#TUGAS 1 mencari data yang ada pada array
bilangan = int(input("Masukkan jumlah kata: "))
kata = []
for x in range(bilangan):
    kata.append(input("Masukkan kata: "))
print("")
cari = input("Masukkan kata yang ingin dicari: ")
found =  False
for h in kata:
    if(h == cari):
        print(cari, "ditemukan pada indeks ke- ", kata.index(h))
        found = True
        break
if not found:
    print("Data tidak ditemukan !")