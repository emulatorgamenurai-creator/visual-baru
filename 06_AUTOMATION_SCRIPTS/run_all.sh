#!/bin/bash
### ===================================================================
### SKRIP INDUK (RUN ALL): PENGGERAK UTAMA PASUKAN OTOMASI LOKAL
### Lokasi: ~/NUR_MASTER_BARU/06_AUTOMATION_SCRIPTS/run_all.sh
### ===================================================================

# Berhenti otomatis jika ada salah satu proses yang mengalami error fatal
set -e

# Pastikan berada di markas script automation
cd /data/data/com.termux/files/home/NUR_MASTER_BARU/06_AUTOMATION_SCRIPTS

echo "=================================================="
echo "=== MEMULAI OPERASI UTAMA INDRAMAYU CLUB GLOBAL ==="
echo "=================================================="
date
echo "--------------------------------------------------"

# LANGKAH 1: Patroli Siber & Pembersihan Jalur Cache
echo "[LANGKAH 1] Memanggil Tuyul Nur Guard..."
python tuyul_nur_guard.py
echo "--------------------------------------------------"

# LANGKAH 2: Eksekusi Bot untuk Ambil Data & Cetak File Bersih
echo "[LANGKAH 2] Memanggil Bot Python untuk Menarik Konten Link..."
# Catatan: Silakan ganti ke master_tuyul.py jika itu engine utama penarik data Anda
python bot_ambil_data.py
echo "✓ Pengambilan data selesai dan dicetak ke 10_CETAK_PRINT."
echo "--------------------------------------------------"

# LANGKAH 3: Sinkronisasi HereDoc EOF & Kompilasi Web Hugo
echo "[LANGKAH 3] Menjalankan Sinkronisasi EOF & Kompilasi Hugo..."
if [ -f "./sinkron_hugo_eof.sh" ]; then
    bash ./sinkron_hugo_eof.sh
else
    echo "[Error] Skrip sinkron_hugo_eof.sh tidak ditemukan di folder ini!"
    exit 1
fi

echo "--------------------------------------------------"
echo "=== OPERASI RUN ALL SELESAI: SITUS GLOBAL AKTIF ==="
echo "=================================================="

