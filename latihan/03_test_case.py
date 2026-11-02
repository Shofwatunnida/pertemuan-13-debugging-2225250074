
def status_lulus(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


test_case = [
    (59, "Tidak lulus"),
    (60, "Lulus"),
    (80, "Lulus"),
]

for nilai, hasil_harapan in test_case:
    hasil_aktual = status_lulus(nilai)

    if hasil_aktual == hasil_harapan:
        status = "PASS"
    else:
        status = "FAIL"

    print(
        f"Nilai: {nilai} | "
        f"Harapan: {hasil_harapan} | "
        f"Aktual: {hasil_aktual} | "
        f"{status}"
    )
