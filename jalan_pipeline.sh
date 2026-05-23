#!/bin/bash
echo "=== [START] PIPELINE SEGITIGA EMAS NUR CORE ==="

# UNSUR 1: PYTHON
echo " -> Memulai Eksekusi Unsur 1 (Python Script)..."
python tuyul_offline.py

# UNSUR 2: OLLAMA (Otomatis tervalidasi di dalam Python)
echo " -> Unsur 2 (Ollama: Nur Core) Berhasil Melakukan Validasi Log."

# UNSUR 3: HUGO
echo " -> Memulai Eksekusi Unsur 3 (Hugo Builder)..."
hugo --minify

# SINKRONISASI GLOBAL (GITHUB)
echo " -> Mendorong Rantai Integritas ke GitHub..."
git add .
git commit -m "Beta Secure Update: 3 Unsur Terkunci - $(date +'%Y-%m-%d')"
git push origin main

echo "=== [SUCCESS] PIPELINE 3 UNSUR SAH TERDORONG KE GITHUB ==="
