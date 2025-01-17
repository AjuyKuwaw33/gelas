# Program untuk menghitung jumlah gelas

def hitung_total_gelas(gelas):
    total = 0
    for jenis, jumlah in gelas.items():
        total += jumlah
    return total

# Contoh penggunaan
gelas = {
    'gelas_kaca': 10,
    'gelas_plastik': 15,
    'gelas_kertas': 20
}

total_gelas = hitung_total_gelas(gelas)
print(f"Total jumlah gelas: {total_gelas}")
