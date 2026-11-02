
def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return 0
    return sum(nilai) / len(nilai)


def status(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


def nilai_tertinggi(nilai):
    tertinggi = nilai[0]
    for x in nilai:
        if x > tertinggi:
            tertinggi = x
    return tertinggi


nilai = [80, 60, 90, 70]

print("Rata-rata:", hitung_rata_rata(nilai))
print("Status 60:", status(60))
print("Tertinggi:", nilai_tertinggi(nilai))

print("\n=== PENGUJIAN TEST CASE ===")

print("T1 - Rata-rata [80, 60, 90, 70]:",
      hitung_rata_rata([80, 60, 90, 70]),
      "| Expected: 75.0")

print("T2 - Rata-rata [100, 80]:",
      hitung_rata_rata([100, 80]),
      "| Expected: 90.0")

print("T3 - Status 60:",
      status(60),
      "| Expected: Lulus")

print("T4 - Status 59:",
      status(59),
      "| Expected: Tidak lulus")

print("T5 - Nilai tertinggi [80, 60, 90, 70]:",
      nilai_tertinggi([80, 60, 90, 70]),
      "| Expected: 90")
