def hitung_diskon(harga, diskon):
	potongan = harga * diskon / 100
	total = harga - potongan
	return total


harga = 100000
diskon = 20

hasil = hitung_diskon(harga, diskon)
print("Harga awal:", harga)
print("Diskon:", diskon, "%")
print("Harga setelah diskon:", hasil)
