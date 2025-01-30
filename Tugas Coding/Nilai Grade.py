def hitung_grade(nilai_total):
    if 90 <= nilai_total <= 100:
        return 'A'
    
    elif 80 <= nilai_total <= 89:
        return 'B'
    
    elif 70 <= nilai_total <= 79:
        return 'C'
    
    elif nilai_total <= 69:
        return 'D'
    
    else:
        return 'nilai tidak valid'
    

Nama = input("Masukan nama:")
Npm = input("Masukan NPM :")
Kelas = input("Masukan Kelas:")
Mata_kuliah = input("Masukan Mata kuliah:")
Nilai_uts = float(input("Masukan Nilai UTS:"))
Nilai_ujian_utama= float(input("Masukan Nilai Ujian Utama:"))


Nilai_total = (0.5 * Nilai_uts) + (0.5 * Nilai_ujian_utama)


grade = hitung_grade(Nilai_total)


print(f"Nama           :{Nama}")
print(f"NPM            :{Npm}")
print(f"Kelas          :{Kelas}")
print(f"Mata Kuliah    :{Mata_kuliah}")
print(f"Nilai Total    :{Nilai_total:.2f}")
print(f"Grade          :{grade}")