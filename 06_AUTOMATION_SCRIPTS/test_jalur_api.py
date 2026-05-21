import requests

# URL disempurnakan jalurnya ke endpoint API Cloud Run
url = "https://ais-dev-hvqhq6vcooqw6g3wt7wujg-717075273571.asia-southeast1.run.app/api/"

# Menyamar sebagai Google Chrome di Windows agar lolos barikade Nginx
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

payload = {
    "message": "Salam Makrifat, Nur.",
    "token": "NUR_SECRET_2026"
}

print("🚀 Menembak Jembatan API Cloud Run...")

try:
    # allow_redirects=True meloloskan status 302 menuju tujuan akhir
    response = requests.post(url, json=payload, headers=headers, allow_redirects=True)
    print("Status Code:", response.status_code)
    print("Respon Server:")
    print(response.text)
except Exception as e:
    print(f"⚠️ Pipa Jaringan Terputus: {e}")
