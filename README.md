# Codline AI

🎙️ **Codline AI** — a WIP voice-to-voice chatbot project,  
starting out as a terminal-based chat application with **sliding window memory** and **summarization memory**.

---

## 🚀 Project Description

Codline AI is designed to evolve into a natural voice-based conversational agent. The project is beginning as a simple, text-based terminal chatbot to build a strong, clean memory system foundation before layering on real-time voice input and output.

---

## 📦 Features

- ✅ Basic DeepSeek V3 LLM connection via Chutes.ai
- 🔁 Sliding window **text memory** (conversation turns buffer)
- 🔁 Basic **summarization memory** (periodic conversation compression)
- 🔁 Core Chatbot engine (`Chatbot` class)
- 🔁 Prompt building using dynamic context
- 🔁 Async summarization updater
- ❌ Voice input (Whisper)
- ❌ Voice output (CSM-1B)
- ❌ Streaming real-time voice conversations

---

## 🛠️ Setup

Clone the repository:

```bash
git clone https://github.com/yourusername/codline-ai.git
cd codline-ai
conda create -n codline_ai python=3.9
conda activate codline_ai
pip install -r requirements.txt
```

You can now run Codline AI locally on your machine (when I have a working terminal chatbot prototype working). However, you must have a Chutes API key to do so. Furthermore, when STT is implemented, you must also have Faster-Whisper installed on your system and running from on the default port.

Each person's preference will be different when it comes to setting up Whisper, from what model you use to how you use your CPU threads. Thankfully, Faster-Whisper should be easy to run with most any of its models due to the efficiency and speed of those models. For the technically inclined, I encourage exploriong how to create your optimal Faster-Whisper setup.

The Faster-Whisper Github repo can be found [here](https://github.com/SYSTRAN/faster-whisper). I encourage giving it a read! It's great stuff.

---

## 🔐 API Key
Codline AI aims to be run on any hardware, as seen by me wanting to use the Faster-Whisper project for audio transcription. As such, I want to take advantage of the [Chutes AI Platform](https://chutes.ai) for inference of both DeepSeek V3 0324 and Sesame's CSM-1B model.

For Chutes API requests to work, you must have an API key. Here are the steps to get such a key.
- Go to the Chutes website (already linked above)
- Create an account - this will also provide you with a fingerprint, which is necessary for logging into Chutes later if desired, so keep this in a safe place
- Click on the user profile icon on the top-right - this should take you directly to your profile
- You should now see a few tabs - click on the one that says 'API'
- You should now see your keys - create one if you want, or use the default key if it exists

Now you need to export the key as an environment variable on your system. Do this in whatever way is required for your system. The environment variable should be called CHUTES\_API_TOKEN.

There you have it! You should now be able to run Codline AI without having to provide your Chutes API key each time!

---

## ✏️ Usage
To use the Codline AI app, you mustfirst be in its root directory and have activated your conda environment. You can then run the following command:
```bash
python main.py
```

upon running this command, the chatbot should start. You can now converse with it in the terminal! If you want to stop talking to Codline AI, simply type `/exit` and send. This will end the chat and kill the program.

While this command-line interface isn't implemented right now, it will be in the future. I'll update this README for each completed step of the roadmap.

---

## 🖥️ Tech Stack
- 🖥️ Chutes AI - Serverless AI inference platform (used to inference DeepSeek V3 0324 and (one day) CSM-1B)
- ✏️ Faster-Whisper - Will be used for fast, local transcription
- ⛓️ Langchain - Used to facilitate memory management and LLM usage
- 🐋 DeepSeek V3 - LLM backbone of the project (used via Chutes AI)
- 📢 CSM-1B - Sesame's state of the art text-to-speech model that will be used for voice replies
