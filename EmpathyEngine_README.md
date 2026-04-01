# The Empathy Engine: Emotional TTS Modulation
# I. Project Overview
The Empathy Engine is a Python-based service that bridges the gap between static text and expressive audio. By analyzing the emotional "valence" of a sentence, the engine dynamically adjusts vocal parameters—such as pitch, rate, and volume—to ensure the AI voice sounds as happy, frustrated, or calm as the text implies.

# II. Features
Nuanced Emotion Detection: Uses a DistilRoBERTa model to classify text into 7 distinct emotional states.

Dynamic SSML Generation: Programmatically builds Speech Synthesis Markup Language (SSML) tags to control the TTS engine.

Intensity Scaling: The degree of vocal modulation is tied to the confidence score of the AI model.

High-Fidelity Output: Utilizes Neural TTS voices for a natural, human-like sound.

# III. Logic & Design Choices
We mapped emotions to physical vocal characteristics based on psychoacoustic principles:

Joy: Increased pitch (+20Hz) and faster rate (+15%) to simulate high-energy physiological arousal.

Sadness: Decreased pitch and slower rate to reflect a somber, low-energy state.

Anger: Increased volume and slight pitch increase to simulate urgency and authority.

# IV. Setup & Execution
Install Dependencies:

  Bash
  
  pip install edge-tts transformers torch
  
Run the Application:

  Bash
  
  python empathy_engine.py
  
Input: Enter your text at the prompt.

Output: An output.mp3 file will be generated with the modulated voice.
