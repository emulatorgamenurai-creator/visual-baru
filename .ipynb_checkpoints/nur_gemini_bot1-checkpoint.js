const { GoogleGenerativeAI } = require("@google/generativeai");
const readline = require("readline");

// API Key Unrestricted yang baru dimasukkan secara utuh di sini
const genAI = new GoogleGenerativeAI("AIzaSyAnZXNnQmcjIoBv9qzWohmsY99qFSQNQNU");
const model = genAI.getGenerativeModel({ model: "gemini-2.5-flash" });


const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

async function chat() {
  console.log("\n--- Sistem Tanya Jawab IndramayuCLUB ---");
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
        console.log(`Jawab: ${response.text()}\n`);
      } catch (error) {
        console.error("Terjadi kesalahan sistem:", error.message);
      }

      // Panggil fungsi lagi untuk membuat loop obrolan terus berjalan
      askQuestion();
    });
  };

  askQuestion();
}

chat();

