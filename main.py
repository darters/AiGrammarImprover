import os
import re
from dotenv import load_dotenv
from services.ai_service import AiService

load_dotenv()
OPENAI_API_KEY = os.getenv('AI_API_KEY')

def main():
    get_correct_sentence()

def get_correct_sentence():
    ai_service = AiService(OPENAI_API_KEY)
    sentence = input("Sentence: ")
    response = ai_service.send_sentence_to_ai(sentence)

    corrected_match = re.search(r"1\)\s*(.+)", response).group(1)
    speaker_match = re.search(r"2\)\s*(.+)", response).group(1)
    print(f"\n✅ {corrected_match}")
    print(f"🔊 {speaker_match}")

if __name__ == '__main__':
    while True:
        main()
