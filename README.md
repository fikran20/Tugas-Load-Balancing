## Cara Menjalankan dan Mengakses Server

1. Jalankan kluster dengan perintah: `docker-compose up --build -d`
2. Akses Load Balancer melalui browser di URL: [http://localhost:8099/api/v1/status](http://localhost:8099/api/v1/status)

### 3. Efek Perpindahan Warna (Visual)
Saat mengakses URL di atas, warna latar belakang teks nama server akan berubah setiap kali halaman di-refresh:
* **Tampilan Awal:** Server 1 (**Biru**)
* **Refresh 1x:** Otomatis pindah ke Server 2 (**Ungu**)
* **Refresh 2x:** Otomatis pindah ke Server 3 (**Hijau**)
* **Refresh 3x:** Kembali berulang ke Server 1 (**Biru**)
