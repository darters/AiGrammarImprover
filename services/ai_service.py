from openai import OpenAI

class AiService:
    def __init__(self, openai_api_key):
        self.client = OpenAI(api_key=openai_api_key)        

    def send_sentence_to_ai(self, sentence):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You correct grammar and improve sentence naturalness Reply with two versions: 1)Just the grammatically corrected version 2)A more natural native-like version"},
            {
                "role": "user",
                "content": sentence
            }]
        )

        return response.choices[0].message.content

