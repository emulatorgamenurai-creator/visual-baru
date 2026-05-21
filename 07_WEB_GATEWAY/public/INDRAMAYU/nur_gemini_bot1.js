const { GoogleGenerativeAI } = require("@google/generative-ai");
const readline = require("readline");

// Masukkan API Key Anda di sini
const genAI = new GoogleGenerativeAI("AIzaSyCarAUGTXAENWx56ETkTykaYmZ9pmNEQzw");
const model = genAI.getGenerativeModel({ model: "gemini-2.5-flash" });

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

async function chat() {
  console.log("\n--- Sistem Tanya Jawab Indramayu Club Makrifat ---");
  console.log("Ketik 'keluar' untuk berhenti.\n");

  const askQuestion = () => {
    rl.question("Tanya: ", async (userInput) => {
      if (userInput.toLowerCase() === "keluar") {
        console.log("Sistem dimatikan. Sampai jumpa!");
        rl.close();
        return;
      }

      try {
        const result = await model.generateContent(userInput);
        const response = await result.response;
        console.log("\nGemini:", response.text(), "\n");
      } catch (error) {
        console.error("\nTerjadi kesalahan:", error.message);
      }

      // Tanya lagi setelah jawaban muncul
      askQuestion();
    });
  };

  askQuestion();
}

chat();

