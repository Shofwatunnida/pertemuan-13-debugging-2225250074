 # Pertemuan 13 — Debugging dan Testing

**Nama:** Shofwatunnida  
**NIM:** 2225250074  
**Kelas:** 3A

## 1. Kasus

Pada pertemuan ini, dilakukan praktik debugging dan testing pada program Python yang memiliki tiga bug logika. Program digunakan untuk menghitung rata-rata nilai, menentukan status kelulusan, dan mencari nilai tertinggi.

Tujuan praktik ini adalah mengidentifikasi kesalahan, memperbaiki kode, dan memastikan program berjalan sesuai hasil yang diharapkan melalui pengujian test case.

## 2. Test Case

| ID | Input | Expected | Actual Awal | Status Awal |
|---|---|---:|---:|---|
| T1 | `[80, 60, 90, 70]` untuk rata-rata | 75.0 | 60.0 | Gagal |
| T2 | `[100, 80]` untuk rata-rata | 90.0 | 36.0 | Gagal |
| T3 | Nilai 60 untuk status | Lulus | Tidak lulus | Gagal |
| T4 | Nilai 59 untuk status | Tidak lulus | Lulus | Gagal |
| T5 | `[80, 60, 90, 70]` untuk nilai tertinggi | 90 | 0 | Gagal |

## 3. Bug Report

### Bug 1 — Perhitungan Rata-rata

**Gejala:** Hasil rata-rata tidak sesuai dengan data nilai.

**Lokasi:** Fungsi `hitung_rata_rata()`.

**Akar penyebab:** Jumlah nilai selalu dibagi dengan angka 5, padahal jumlah data dapat berbeda.

**Perbaikan:** Pembagi diganti dengan `len(nilai)` agar sesuai dengan jumlah data.

### Bug 2 — Status Kelulusan

**Gejala:** Nilai 60 dinyatakan tidak lulus.

**Lokasi:** Fungsi `status()`.

**Akar penyebab:** Kondisi menggunakan operator `>` sehingga nilai yang tepat 60 tidak memenuhi syarat.

**Perbaikan:** Operator diubah menjadi `>=` agar nilai 60 dinyatakan lulus.

### Bug 3 — Nilai Tertinggi

**Gejala:** Program menghasilkan nilai tertinggi 0.

**Lokasi:** Fungsi `nilai_tertinggi()`.

**Akar penyebab:** Variabel `tertinggi` diawali dengan 0 dan perbandingan menggunakan operator `<`, sehingga nilai yang lebih besar tidak tersimpan.

**Perbaikan:** Variabel `tertinggi` diinisialisasi dengan elemen pertama dan operator perbandingan diubah menjadi `>`.

## 4. Hasil Retest

Setelah ketiga bug diperbaiki, seluruh test case dijalankan kembali.

| ID | Expected | Actual Setelah Perbaikan | Status |
|---|---|---|---|
| T1 | 75.0 | 75.0 | Lulus |
| T2 | 90.0 | 90.0 | Lulus |
| T3 | Lulus | Lulus | Lulus |
| T4 | Tidak lulus | Tidak lulus | Lulus |
| T5 | 90 | 90 | Lulus |

Hasil pengujian menunjukkan bahwa kelima test case berhasil memperoleh hasil yang sesuai dengan nilai yang diharapkan.

## 5. Cara Menjalankan

Jalankan perintah berikut melalui terminal dari folder utama proyek:

```bash
python praktik/praktik_4_debugging.py
```

## 6. Refleksi

Melalui praktik ini, saya belajar bahwa kesalahan logika dapat menyebabkan program menghasilkan output yang tidak sesuai meskipun program tetap dapat dijalankan. Pengujian menggunakan beberapa test case membantu menemukan kesalahan, terutama pada kondisi batas. Proses debugging juga membantu memahami penyebab kesalahan sehingga perbaikan dapat dilakukan dengan tepat.
