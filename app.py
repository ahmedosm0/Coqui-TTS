import torch
from TTS.api import TTS
import gradio as gr

device = "cuda" if torch.cuda.is_available() else "cpu"

def generate_audio(text= "Hello, welcome to Coqui TTs!"):
    tts = TTS(model_name="tts_models/en/ljspeech/fast_pitch").to(device)
    tts.tts_to_file(text=text, file_path="outputs/output.wav")
    return 'outputs/output.wav'

# print(generate_audio())

demo = gr.Interface(fn=generate_audio,
                    inputs=gr.Textbox(lines=2, placeholder="Enter text here..."),
                    outputs=gr.Audio(type="file"),
                    title="Coqui TTS Text-to-Speech",
                    description="Enter text and generate speech using Coqui TTS model."
                   )

demo.launch()