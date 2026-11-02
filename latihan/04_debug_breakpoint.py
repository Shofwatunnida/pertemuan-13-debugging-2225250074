
def hitung_total(daftar_nilai):
    total = 0

    for nilai in daftar_nilai:
        total += nilai

    rata_rata = total / len(daftar_nilai)
    return total, rata_rata


nilai = [80, 75, 90, 85]

total, rata_rata = hitung_total(nilai)

print("Daftar nilai:", nilai)
print("Total nilai:", total)
print("Rata-rata:", rata_rata)
