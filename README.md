# -Assignment-round-of-Darwix_AI
# Project Description

"Empathy Engine converts text into emotionally expressive speech..."

# Features
Emotion detection (VADER / Transformers)
Dynamic speech modulation
Audio generation
# How to Run
pip install -r requirements.txt
python app.py
# Design Choices
# Explaination:

I chose VADER initially because it’s lightweight, fast, and sufficient for basic sentiment classification. However, I designed the system modularly so it can be upgraded to transformer-based models for more nuanced emotion detection.

The pitch, rate, and volume mappings are based on real human speech patterns—happy speech tends to be faster and higher-pitched, while sad speech is slower and lower. This helps make the synthesized voice feel more natural and emotionally aligned.

The main trade-offs involve speed vs accuracy in emotion detection, and simplicity vs expressiveness in TTS. My system balances these by starting simple but remaining extensible for more advanced implementations.
