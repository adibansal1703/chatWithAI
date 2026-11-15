from google import genai
from google.genai import types

client = genai.Client(http_options=types.HttpOptions(api_version="v1beta"))

with open("notes.txt", "r", encoding="utf-8") as f:
    document = f.read()

system_prompt = (
    "Answer only using the document below. "
    "If the answer is not in it, say 'I can't find that in the document.'\n\n"
    f"<document>\n{document}\n</document>"
)

chat = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(system_instruction=system_prompt, temperature=2
    ),
)

while True:
    question = input("\nYou (type 'quit' to exit): ")
    if question.lower() == "quit":
        break
    response = chat.send_message(question)
    print("\nGemini:", response.text)