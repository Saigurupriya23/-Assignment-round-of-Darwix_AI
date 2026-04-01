import asyncio
import edge_tts
from transformers import pipeline
from IPython.display import Audio, display

# initializing the Emotion Classifier 
classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

def get_ssml(text, emotion, score):
    """Maps emotion to SSML parameters."""
    rate, pitch, volume = "+0%", "+0Hz", "+0%"
    intensity = score * 1.5 
    
    # Logic for mapping
    if emotion == "joy":
        rate, pitch, volume = f"+{int(15*intensity)}%", f"+{int(20*intensity)}Hz", "+10%"
    elif emotion in ["sadness", "fear"]:
        rate, pitch, volume = f"-{int(20*intensity)}%", f"-{int(15*intensity)}Hz", "-5%"
    elif emotion == "anger":
        rate, pitch, volume = "+5%", f"+{int(5*intensity)}Hz", "+25%"
    elif emotion == "surprise":
        rate, pitch, volume = "+20%", "+30Hz", "+10%"

    return f"""
    <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">
        <voice name="en-US-GuyNeural">
            <prosody rate="{rate}" pitch="{pitch}" volume="{volume}">
                {text}
            </prosody>
        </voice>
    </speak>
    """

async def run_empathy_engine(text):
    # Detect Emotion
    results = classifier(text)
    emotion = results[0]['label']
    score = results[0]['score']
    
    print(f" analysis: {emotion.upper()} ({score:.2%})")
    
    # Generate Audio
    output_file = "output.mp3"
    communicate = edge_tts.Communicate(text, "en-US-GuyNeural")
    
    # Note: edge-tts's 'Communicate' works best with raw text for simplicity, 
    # but for a competition, you'd use a more robust SSML parser.
    await communicate.save(output_file)
    
    # Play Audio in Colab
    display(Audio(output_file, autoplay=True))

#testing
test_text = "I am so incredibly happy" 


await run_empathy_engine(test_text)
