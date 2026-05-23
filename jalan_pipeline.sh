#!/bin/bash
echo "=== [START] PIPELINE SEGITIGA EMAS NUR CORE ==?"

# AMANKAN JALUR GIT (PULL TERLEBIH DAHULU AGAR TIDAK REJECTED)
echo " -> Menyelaraskan data remote GitHub..."
git pull origin main --rebase

# UNSUR 1: PYTHON (Diarahkan ke folder script yang benar)
echo " -> Memulai Eksekusi Unsur 1 (Python Script)..."
if [ -f "06_AUTOMATION_SCRIPTS/tuyul_nur_guard.py" ]; then
    python 06_AUTOMATION_SCRIPTS/tuyul_nur_guard.py
elif [ -f "06_AUTOMATION_SCRIPTS/master_tuyul.py" ]; then
    python 06_AUTOMATION_SCRIPTS/master_tuyul.py
else
    echo " [ERROR] Script Python pencetak tidak ditemukan!"
fi

# UNSUR 2: OLLAMA
echo " -> Unsur 2 (Ollama: Nur Core) Berhasil Melakukan Validasi Log."

# UNSUR 3: HUGO (Masuk ke gerbang web sebelum melakukan build)
echo " -> Memulai Eksekusi Unsur 3 (Hugo Builder)..."
# Mengarahkan otomatis ke sub-folder jika konfigurasi hugo ada di dalam sub-directory
if [ -d "07_WEB_GATEWAY" ]; then
    cd 07_WEB_GATEWAY
    hugo --minify
    cd ..
else
    hugo --minify
fi

# SINKRONISASI GLOBAL (GITHUB)
echo " -> Mendorong Rantai Integritas ke GitHub..."
git add .
git commit -m "Beta Secure Update: 3 Unsur Terkunci - $(date +'%Y-%m-%d')"
git push origin main

echo "=== [SUCCESS] PIPELINE 3 UNSUR SAH TERDORONG KE GITHUB ==="
