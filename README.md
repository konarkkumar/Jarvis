🤖 JARVIS AI ASSISTANT

Jarvis is a voice-activated AI assistant that performs tasks like opening websites, playing songs, and responding to general queries using OpenAI's GPT model. It also uses speech recognition and text-to-speech functionalities.

✨ FEATURES

🎙️ Voice recognition using Google Speech Recognition

🧠 AI responses using OpenAI API

🌐 Open popular websites like Google, YouTube, and Facebook

🎵 Play songs using a music library

🔊 Text-to-speech using gTTS and PyGame

🛠️ Prerequisites

Ensure you have the following installed on your system:

🐍 Python 3.8 or higher

📦 Pip (Python package manager)

🚀 Installation

Clone this repository:

git clone https://github.com/your-username/jarvis-ai-assistant.git
cd jarvis-ai-assistant

Install the required dependencies:

pip install speechrecognition webbrowser pyttsx3 pygame gtts openai

Install PocketSphinx for offline recognition (optional):

pip install pocketsphinx

Ensure your microphone is working properly.

🔧 CONFIGURATION

API Key: Update your OpenAI API key in the aiProcess() function.

client = OpenAI(api_key="your-openai-api-key")

Music Library: Ensure the musicliberary.py file has a dictionary like:

music = {"song_name": "song_url"}

🕹️ USAGE

Run the assistant:

python jarvis.py

Say "Jarvis" to activate the assistant.

Give your command, e.g.:

"Open Google"

"Play [song name]"

Jarvis will respond using GPT-based AI or perform the requested task.

🧑‍🔧 TROUBLESHOOTING 

Ensure your microphone has permission to record audio.

If speech recognition fails, try adjusting the microphone volume.

If the GPT response doesn't work, check your API key and internet connection.
