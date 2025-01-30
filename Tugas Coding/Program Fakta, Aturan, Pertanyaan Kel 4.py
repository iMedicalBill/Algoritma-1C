# Fakta penggunaan kacamata minus
batas_mata_minus = -1  # Mata minus di bawah batas ini perlu kacamata

# Aturan perlu kacamata
def perlu_kacamata(mata_kiri, mata_kanan):
    if mata_kiri <= batas_mata_minus or mata_kanan <= batas_mata_minus:
        return True
    else:
        return False

# Pertanyaan berdasarkan fakta dan aturan
print("Pemeriksaan Kebutuhan Kacamata")
mata_kiri = float(input("Berapa minus mata kiri Anda? "))
mata_kanan = float(input("Berapa minus mata kanan Anda? "))

# Evaluasi aturan
if perlu_kacamata(mata_kiri, mata_kanan):
    print("Anda perlu menggunakan kacamata.")
else:
    print("Anda tidak perlu menggunakan kacamata.")
