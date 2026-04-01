import spacy
from IPython.display import HTML, display

# Load NLP for segmentation
nlp = spacy.load("en_core_web_sm")

def segment_text(text):
    """Breaks text into logical scenes."""
    doc = nlp(text)
    return [sent.text.strip() for sent in doc.sents]

def engineer_prompt(segment, style="Digital Art"):
    """
    STRETCH GOAL: This simulates an LLM 'refining' the prompt.
    In a full app, you'd send this to Gemini/GPT-4.
    """
    # Simple expansion logic: add descriptive keywords and style consistency
    enhanced = f"A high-quality {style} of: {segment}. Detailed textures, professional lighting, cinematic composition, consistent character design."
    return enhanced

def generate_storyboard_html(scenes):
    """Creates a coherent visual sequence in HTML."""
    html_template = """
    <div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: center; background: #f4f4f9; padding: 20px;">
        {panels}
    </div>
    """
    panel_template = """
    <div style="width: 300px; background: white; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); overflow: hidden;">
        <img src="{img_url}" style="width: 100%; height: 200px; object-fit: cover;">
        <div style="padding: 15px; font-family: sans-serif; font-size: 14px; color: #333;">
            <strong>Scene {idx}:</strong> {text}
        </div>
    </div>
    """
    
    panels_html = ""
    for i, scene in enumerate(scenes):
        # MOCK IMAGE URL for demonstration (Replace with your actual API call)
        # In the real version, you'd call DALL-E or Stable Diffusion here
        mock_url = f"https://picsum.photos/seed/{hash(scene)}/400/300"
        
        panels_html += panel_template.format(
            img_url=mock_url, 
            idx=i+1, 
            text=scene
        )
        
    return html_template.format(panels=panels_html)

# --- EXECUTION ---
pitch = "Our client was struggling with money shortage. We implemented our new AI dashboard. Now, their income has tripled."

scenes = segment_text(pitch)
print(f"Detected {len(scenes)} scenes.")

# Display the Storyboard
html_output = generate_storyboard_html(scenes)
display(HTML(html_output))
