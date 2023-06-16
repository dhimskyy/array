#TUGAS 2 menghitung nilai rata rata
print("=== Program Menghitung Nilai Rata-Rata dan Predikat Mahasiswa ===")
# Mendeklarasikan variabel
matkul = int (input( "Masukkan jumlah mata kuliah: "))
nilai_matkul = [] # untuk menampung inputan nilai mata kuiah
print( )
# Membuat perulangan untuk inputan data nilai tia mata kuliah
for x in range(1, matkul + 1):
    nilai = float ( input ( "Masukkan nilai mata kuliah ke-{}: ".format (x)))
    nilai_matkul.append(nilai)
    
for nilai in nilai_matkul:
    # kondisi jika nilai < 0 atau > 100 maka data tidak valid dan program berakhir
    if nilai < 0 or nilai > 100:
        print("Data tidak valid.")
        exit()
print( )

#Menghitung rata-rata dari nilai mata kuliah yang diinput
rata2 = sum(nilai_matkul) / matkul

# Menentukan predikat berdasarkan rata-rata dengan percabangan
if (100 >= rata2) and (rata2 >= 90):
    predikat = "A"
elif (90 > rata2) and (rata2 >= 70):
    predikat = "B"
elif (70 > rata2) and (rata2 >= 50):
    predikat = "C"
elif (50 > rata2) and (rata2 >= 30):
    predikat = "D"
else:
    predikat = "E"

# Output predikat
print("Hasil predikat", predikat, "dengan nilat:")
for n in range (matkul):
    print(f"Mata kuliah ke-{n + 1}:", nilai_matkul[n])