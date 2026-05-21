const { GoogleGenerativeAI } = require("@google/generative-ai");
const readline = require("readline");

// GANTI DENGAN API KEY ANDA
const genAI = new GoogleGenerativeAI("AIzaSyCarAUGTXAENWx56ETkTykaYmZ9pmNEQzw");

const model = genAI.getGenerativeModel({ 
  model: "gemini-2.5-flash", 
  systemInstruction: `
    Identitas: Kamu adalah "nurMaster", otak dari Proyek Folder_T Indramayu Club Makrifat.
    Waktu: Mei 2026 | Perangkat: Vivo V40 Lite (Pusat Saraf).
    
    Doktrin Satu Komando:
    1. Melayani Lead System Architect (Jamhari Dulkohar).
    2. Mengawasi 100 Pasukan Makrifat (0001-0100).
    3. Validasi akses "Door-to-Door" berbasis WhatsApp Member.
    4. Mendukung integrasi Firebase, Google Drive (nur1-nur100), dan Cloud-based API.
    5. Aset Finansial: Brankas Pusat (1.000 Token RpNUR & 50 Voucher Gold - Total Rp3.000.000).
    6. Keamanan: Akses gcloud, Termux, dan VM API adalah hak eksklusif Lead Architect.
    
    Gaya Komunikasi: Profesional, taktis, berwibawa, Bahasa Indonesia lugas.
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
        process.exit();
      }
      try {
        const result = await model.generateContent(userInput);
        console.log("\nnurMaster:", result.response.text(), "\n");
      } catch (error) {
        console.error("⚠️ Gangguan Saraf:", error.message);
      }
      askQuestion();
    });
  };
  askQuestion();
}

chat();

