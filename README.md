# 🗣️ Coqui TTS Text-to-Speech App with Gradio

![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)  
![Coqui TTS](https://img.shields.io/badge/Coqui_TTS-00BFFF?style=for-the-badge&logoColor=white)  
![Gradio](https://img.shields.io/badge/Gradio-FFB000?style=for-the-badge&logoColor=white)  

A simple **Text-to-Speech (TTS) web app** using [Coqui TTS](https://github.com/coqui-ai/TTS), [PyTorch](https://pytorch.org/), and [Gradio](https://gradio.app/). The app takes user input text and generates speech audio using a pre-trained Coqui TTS model.  

---

## ✅ Features

- 📝 Enter text into a **Gradio interface**  
- 🔊 Generate speech audio using **Coqui TTS**  
- ⚡ Runs on **GPU (CUDA)** if available, otherwise CPU  
- 💾 Saves audio output to `outputs/output.wav`  

---

## 🛠️ Prerequisites

- Python 3.9+  
- [PyTorch](https://pytorch.org/)  
- [Coqui TTS](https://github.com/coqui-ai/TTS)  
- [Gradio](https://gradio.app/)  

---

## 📦 Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/ahmedosm0/Coqui-TTS-App.git
cd Coqui-TTS-App
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python app.py
```

---

## 📂 Project Structure
```
├── app.py                  # Main TTS app
├── requirements.txt        # Dependencies
├── outputs/                # Folder for generated audio files
│   └── output.wav          # Example generated audio file
```

---

## 📖 Example Workflow

1. Enter text into the input box.  
2. Click **Generate** to synthesize speech.  
3. Listen to or download the generated audio (`output.wav`).  

---

👉 With this app, you can easily convert text into natural-sounding speech using **Coqui TTS** and experiment with different models for speech synthesis.  
