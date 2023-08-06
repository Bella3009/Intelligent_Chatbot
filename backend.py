import openai


class Chatbot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self, user_input):
        responses = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=4000,
            temperature=0.5
        ).choices[0].text
        return responses
