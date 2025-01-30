# Fakta tentang durasi bermain game online
batas_durasi = 3  # Batas durasi bermain game online yang direkomendasikan dalam jam

# Aturan apakah durasi bermain melebihi batas
def perlu_kurangi_durasi(durasi_harian):
    if durasi_harian > batas_durasi:
        return True
    else:
        return False

# Pertanyaan berdasarkan fakta dan aturan
print("Pemeriksaan Durasi Bermain Game Online")
durasi_harian = float(input("Berapa jam Anda bermain game online setiap hari? "))

# Evaluasi aturan
if perlu_kurangi_durasi(durasi_harian):
    print("Anda perlu mengurangi durasi bermain game online.")
    print("Rekomendasi: Bermain tidak lebih dari 3 jam per hari untuk menjaga kesehatan.")
else:
    print("Durasi bermain game online Anda sudah dalam batas sehat.")
    print("Tetap pertahankan kebiasaan baik ini!")
