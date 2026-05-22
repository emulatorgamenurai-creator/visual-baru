import os
import json
import urllib.request

# Path mundur satu langkah dari folder 06_AUTOMATION_SCRIPTS ke folder utama Hugo
OUTPUT_FOLDER = "../content/member"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def panggil_qwen_lokal(nama_member, skor):
    """Menghubungkan ke pembungkus Ollama lokal di Termux (100% Offline)"""
    url = "http://localhost:11434/api/generate"
    prompt = f"Berikan satu kalimat motivasi keuangan pendek untuk {nama_member} dengan skor {skor}. Langsung kalimatnya saja."
    
    payload = {
        "model": "qwen2.5:0.5b",
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.0}
    }
    
    try:
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=5) as response:
            res_body = json.loads(response.read().decode("utf-8"))
            return res_body.get("response", "").strip()
    except Exception:
        # Cadangan teks jika Qwen sedang sibuk merespons
        return "Kelola aset digital Anda dengan bijak untuk stabilitas jangka panjang."

print("🤖 [Master Tuyul] Mulai memproses 100 member offline...")

# Loop otomatis membuat 100 file markdown member ke folder content Hugo
for i in range(1, 101):
    username = f"member_{i}"
    nama = f"Anggota Sukses ke-{i}"
    total_skor = i * 25  # Simulasi rumus kalkulator internal
    
    # Ambil teks pintar dari Qwen lokal
    analisis_text = panggil_qwen_lokal(nama, total_skor)
    print(f"   ➔ Sukses cetak halaman: {username} (Skor: {total_skor})")

    file_path = os.path.join(OUTPUT_FOLDER, f"{username}.md")
    konten_markdown = f"""---
title: "Dashboard Member: {nama}"
date: 2026-05-22
username: "{username}"
total_skor: {total_skor}
layout: "single_member"
---

### Hasil Kalkulator AI Anda:
*   ID Member: `@{username}`
*   Total Skor Kontribusi: **{total_skor}**

> 🧠 **Analisis Qwen Lokal (Bebas Sinyal Kalimantan):** 
> "{analisis_text}"
"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(konten_markdown)

print("\n🚀 SELESAI! 100 file member sukses dikloning ke folder content/member/")

