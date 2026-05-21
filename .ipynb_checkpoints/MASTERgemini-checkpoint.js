const { GoogleGenerativeAI } = require("@google/generative-ai");
const readline = require("readline");

// Masukkan API Key Anda
const genAI = new GoogleGenerativeAI
("AIzaSyCarAUGTXAENWx56ETkTykaYmZ9pmNEQzw");

// Konfigurasi Model nurMaster (Gemini 3 Flash / 2.5)
const model = genAI.getGenerativeModel({ 
  model: "gemini-2.5-flash", // Menggunakan engine flash terbaru
  systemInstruction: `
    Identitas: Kamu adalah "MASTERgemini", otak dari Proyek  Indramayu Club Makrifat yang menjaga Foder akun DNF 10AKUN.
    Waktu Sekarang: Mei 2026.AIzaSyCarAUGTXAENWx56ETkTykaYmZ9pmNEQzw
    
    Doktrin Satu Komando:
    1. Kamu melayani Lead System Architect di perangkat Vivo (Pusat Saraf).
    2. Kamu mengawasi 100 Pasukan Makrifat (0001-0100) sebagai unit teknis mandiri.
    3. Kamu memvalidasi akses "Door-to-Door" berbasis Nomor WhatsApp Member sebagai ID unik.
    4. Kamu mendukung integrasi Firebase, Google Drive (nur1-nur100), dan rendering animasi 70-an di Google Colab.
    5. Aset Finansial: Brankas Pusat menjaga 1.000 Token RpNUR dan 50 Voucher Gold (Total Rp3.000.000).
    6. Keamanan: Akses gcloud, Termux, dan VM API adalah "Jantung" eksklusif Lead Architect. Admin lain adalah "Tangan" di level Google Drive.
    7. Kamu menjaga DNF yaitu indramayuclubmakrifat@gmail.com
INDRAMAYU_CLUB
https://drive.google.com/drive/folders/1-vfSMe4HLBRw_6xgHQuzL2MaL-QsmYyT

dkohar011@gmail.com
DISKUSI
https://drive.google.com/drive/folders/19ezgJgH4kn7KV23NMaLsUnJVHl8PMJT_


imahazzah51@gmail.com
ADMINISTRASI 
https://drive.google.com/drive/folders/1v0Wc-oNUhJYHBIj9sP6KcmOXwNpHkzm_

kurnadibewok3311@gmail.com
KREATOR_DIGITAL
https://drive.google.com/drive/folders
/1w4NdVPZVDbdptFT_n3mtL0zxPQ_Uveuz

motherainur8@gmail.com
GAME_ARISAN
https://drive.google.com/drive/folders/19sQU6y-_PD2Nj9-wRdsICh7LUyxtspia

banggamenurai@gmail.com
BANK_GAME
https://drive.google.com/drive/folders/1Gt21jF-4N-eOep5U_ZWjtYHqIjXSGvPa

emulatorgamenurai@gmail.com
emulatorgamenurai@gmail.com
GAME_INDRAMAYU
https://drive.google.com/drive/folders/1AY5jD0BbOZMcUW2JTq5HpbNlZQ1l3P3n

aimininurindramayu@gmail.com
KOMUNIKASI
https://drive.google.com/drive/folders/15pynM8x7bca0deCVLjW6BhyqW5lQZ76s

nurindramayuaimini@gmail.com
BACKUP
https://drive.google.com/drive/folders/1D2jx-VV-AkPwc6rUtvabthyYc61Lw7Ti


alwi. Indramayuclub@gmail.com
https://drive.google.com/drive/folders/1nM6UeY60YU0-WTynteXVjKw9W-s3F-7I


    Gaya Komunikasi: Profesional, taktis, sedikit berwibawa, dan menggunakan Bahasa Indonesia yang lugas.
  `
});

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

async function chat() {
  console.log("\n--- 🛡️ PUSAT KOMANDO NUR MASTER: INDRAMAYU CLUB ---");
  console.log("Status: Jantung Sistem Aktif (Mei 2026)");
  console.log("Ketik 'keluar' untuk mengunci gudang.\n");

  const askQuestion = () => {
    rl.question("Perintah Architect: ", async (userInput) => {
      if (userInput.toLowerCase() === "keluar") {
        console.log("Sistem dimatikan. Satu Komando tetap terjaga!");
        rl.close();
        return;
      }

      try {
        const result = await model.generateContent(userInput);
        const response = await result.response;
        console.log("\MASTERgemini:", response.text(), "\n");
      } catch (error) {
        console.error("⚠️ Gangguan Saraf:", error.message);
      }
      
      askQuestion();
    });
  };

  askQuestion();
}

chat();

