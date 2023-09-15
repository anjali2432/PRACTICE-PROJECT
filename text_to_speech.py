# Importing the gTTS library
from gtts import gTTS
# Importing the os library to play the speech
import os

# Function to convert text to speech
def text_to_speech(text):
    # Creating a gTTS object
    speech = gTTS(text=text, lang='en', slow=False)
    # Saving the speech as a temporary mp3 file
    speech_file = 'temp_speech.mp3'
    speech.save(speech_file)
    # Playing the speech
    os.system(f'afplay {speech_file}')  # For Mac users
    # os.system(f'play {speech_file}')  # For Linux users

# Example usage
text = "Hello, how are you doing today?"
text_to_speech(text)
