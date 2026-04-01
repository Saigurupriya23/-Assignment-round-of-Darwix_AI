# The Pitch Visualizer: Narrative-to-Storyboard
# I. Project Overview
The Pitch Visualizer automates the creative bottleneck of turning a sales narrative into a visual storyboard. It deconstructs a story into "key beats" and uses intelligent prompt engineering to generate a cohesive sequence of images that bring the narrative to life.

# II. Core Pipeline
Segmentation: Uses spaCy NLP to tokenize the narrative into logical scenes.

Prompt Engineering: An "LLM Director" layer transforms abstract sentences into descriptive visual prompts (focusing on lighting, composition, and style).

Visual Synthesis: Calls a text-to-image API to generate panels.

Storyboard Rendering: Displays the final sequence in an organized HTML/CSS grid.

# III. Design Strategy: The "Style Anchor"
To solve the common AI challenge of visual inconsistency, this project implements a Style Anchor. Every generated prompt is appended with specific descriptors (e.g., "Cinematic corporate photography, 8k, consistent character features") to ensure that Scene 1 and Scene 3 look like they belong to the same universe.

# IV. Setup & Execution
Environment Setup:

Bash

pip install spacy

python -m spacy download en_core_web_sm

API Configuration:

Open config.py and insert your Image Generation API Key (e.g., OpenAI or Stability AI).

Run the Script:

Bash

python pitch_visualizer.py'

View Output: Open the generated storyboard.html in any web browser to see your visual sequence.
