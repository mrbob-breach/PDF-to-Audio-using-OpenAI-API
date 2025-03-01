from openai import OpenAI
from pathlib import Path
import os
import warnings
from PyPDF2 import PdfReader

Authorization = os.environ.get("OPENAI_API_KEY")
url = "https://api.openai.com/v1/chat/completions"

headers = OpenAI(
    organization=os.environ.get("organization"),
    project=os.environ.get("project"),
)

warnings.filterwarnings("ignore", category=DeprecationWarning)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

speech_file_path = Path(__file__).parent / "speech.mp3"

reader = PdfReader("PDF to read.pdf")
text_to_read = reader.pages[0].extract_text()

response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=text_to_read
)

response.stream_to_file(speech_file_path)

