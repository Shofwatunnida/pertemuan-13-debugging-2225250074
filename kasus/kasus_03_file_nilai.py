
def baca_nilai(nama_file):
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                data = baris.strip().split(",")
                nama = data[0]
                nilai = float(data[1])
                print(f"{nama}: {nilai}")

    except FileNotFoundError:
        print("File tidak ditemukan.")
    except ValueError:
        print("Data nilai tidak valid.")


baca_nilai("data/nilai.txt")
