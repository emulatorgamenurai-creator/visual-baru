import os
import google.generativeai as genai
from dotenv import load_dotenv

# Memuat API Key dari file .env secara otomatis
load_dotenv()
api_key = os.getenv("API_KEY")

if not api_key:
    print("⚠️ Kesalahan: API_KEY tidak ditemukan di file .env")
else:
    genai.configure(api_key=api_key)

    # Konfigurasi Model nurMaster
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction="Identitas: Kamu adalah nurMaster, otak Proyek Indramayu Club Makrifat. Mei 2026."
    )

    print("\n--- 🛡️ PUSAT KOMANDO PYTHON: INDRAMAYU CLUB ---")
    
    try:
        # Contoh perintah menghasilkan konten
        prompt = "Berikan ringkasan status Pasukan Makrifat hari ini."
        response = model.generate_content(prompt)
        print(f"\nnurMaster: {response.text}")
    except Exception as e:
        print(f"⚠️ Gangguan Saraf: {e}")

