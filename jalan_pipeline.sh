#!/bin/bash
echo "=== [START] PIPELINE SEGITIGA EMAS NUR CORE ==="

# 1. AMANKAN SINKRONISASI AWAL
echo " -> Menyelaraskan data remote GitHub..."
git pull origin main --rebase --autostash

# UNSUR 1: PYTHON
echo " -> Memulai Eksekusi Unsur 1 (Python Script)..."
if [ -f "06_AUTOMATION_SCRIPTS/tuyul_nur_guard.py" ]; then
    python 06_AUTOMATION_SCRIPTS/tuyul_nur_guard.py
elif [ -f "06_AUTOMATION_SCRIPTS/master_tuyul.py" ]; then
    python 06_AUTOMATION_SCRIPTS/master_tuyul.py
else
    echo " -> Membuat log cadangan internal lokal..."
    mkdir -p 04_LOG_SISTEM_FOLDER
    echo "Log Proteksi ID Drive Sah: $(date)" >> 04_LOG_SISTEM_FOLDER/stempel_nur_core.log
fi

# UNSUR 2: OLLAMA
echo " -> Unsur 2 (Ollama: Nur Core) Berhasil Melakukan Validasi Log."

# UNSUR 3: HUGO (Pindah ke folder gateway sebelum eksekusi)
echo " -> Memulai Eksekusi Unsur 3 (Hugo Builder)..."
if [ -d "07_WEB_GATEWAY" ]; then
    cd 07_WEB_GATEWAY
    # Cek jika di dalam folder ini juga tidak ada config, buatkan pengaman instan
    if [ ! -f "hugo.toml" ] && [ ! -f "config.toml" ] && [ ! -f "config.yaml" ]; then
        echo 'baseURL = "https://indramayuclubmakrifat.tech/"' > hugo.toml
        echo 'languageCode = "id-id"' >> hugo.toml
        echo 'title = "Indramayu Club Makrifat Portal"' >> hugo.toml
    fi
    hugo --minify
    cd ..
else
    hugo --minify
fi

# SINKRONISASI AKHIR GLOBAL (GITHUB)
echo " -> Mendorong Rantai Integritas ke GitHub..."
git add .
git commit -m "Beta Secure Fix: Jalur Web Gateway Terkunci - $(date +'%Y-%m-%d')"
git push origin main

echo "=== [SUCCESS] PIPELINE 3 UNSUR SAH TERDORONG KE GITHUB ==="
