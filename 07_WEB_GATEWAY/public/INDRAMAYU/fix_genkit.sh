#!/bin/bash

# 1. Pastikan berada di direktori yang benar
cd /data/data/com.termux/files/home/hecker2/public

# 2. Re-install dependency lokal jika perlu
echo "Memeriksa modul..."
npm install

# 3. Jalankan genkit start di background dan tunggu hingga siap
echo "Memulai Genkit Runtime..."
genkit start -- wait & 

# Beri jeda 5 detik agar port 4033/runtime siap
sleep 5

# 4. Jalankan flow secara otomatis
echo "Menjalankan flow..."
genkit flow:run <nama_flow_anda> '{"key":"value"}'
