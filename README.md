# SmartCashier-Tkinter-Desktop
Sebuah aplikasi desktop berbasis Python & Tkinter untuk melacak dan menghitung pesanan pada restoran Ayam Geprek 99 agar efektif dan efisien.

# 🍗 SmartCashier - Ayam Geprek 99 POS System

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![Status](https://img.shields.io/badge/status-completed-success.svg)

## 📌 Project Overview
**SmartCashier** adalah sebuah aplikasi Point of Sale (POS) berbasis desktop yang dikembangkan menggunakan Python dan pustaka GUI **Tkinter**. Aplikasi ini dirancang untuk mempermudah operasional kasir di rumah makan "Ayam Geprek 99" dengan mengotomatisasi perhitungan total pesanan, pajak layanan, manajemen metode pembayaran, hingga pencetakan struk digital.

Projek ini dikembangkan sebagai bentuk implementasi logika pemrograman Python dalam menciptakan *User Interface* (UI) yang fungsional dan interaktif.

## ✨ Fitur Utama
* **Menu Interaktif:** Pemilihan menu makanan (varian ayam geprek) dan minuman menggunakan sistem *checkbox* dan *entry* dinamis.
* **Kalkulasi Otomatis:** Menghitung *Sub Total*, *Service Tax* (10%), dan *Total Harga* secara otomatis (Real-time).
* **Sistem Pembayaran:**
    * **Cash:** Dilengkapi kalkulator kembalian otomatis jika nominal uang tunai diinput.
    * **QR:** Penyesuaian sistem tanpa kembalian untuk pembayaran non-tunai.
* **Digital Receipt (Struk):** Membuat rincian struk pembelian lengkap dengan Nomor Tagihan (Bill Number) dan Tanggal transaksi.
* **Save Receipt:** Fitur untuk menyimpan struk digital ke dalam penyimpanan lokal perangkat dengan format `.txt`.
* **One-Click Reset:** Membersihkan seluruh kolom input dan area struk untuk memulai transaksi baru.

## 📸 Screenshots
*(💡 Ganti teks ini dengan gambar screenshot aplikasimu saat dijalankan)*
> `![Tampilan Utama Aplikasi](link-gambar-screenshot-utama.png)`
> `![Tampilan Struk Transaksi](link-gambar-screenshot-struk.png)`

## 🛠️ Teknologi yang Digunakan
* **Bahasa Pemrograman:** Python 3.x
* **Libraries:** * `tkinter` (Standard GUI library)
    * `random` (Bill number generator)
    * `time` (Timestamp formatting)

## 🚀 Instalasi & Cara Penggunaan

Karena aplikasi ini sepenuhnya menggunakan pustaka bawaan (*built-in libraries*) dari Python, kamu tidak perlu menginstal *dependencies* tambahan dari pihak ketiga (seperti `pip install`).

**Langkah-langkah menjalankan aplikasi:**
1. Pastikan **Python 3.x** sudah terinstal di perangkatmu.
2. *Clone* repositori ini ke komputer lokalmu:
   ```bash
   git clone [https://github.com/username-kamu/SmartCashier-AyamGeprek99.git](https://github.com/username-kamu/SmartCashier-AyamGeprek99.git)
