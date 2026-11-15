from google import genai
from google.genai import types

client = genai.Client(http_options=types.HttpOptions(api_version="v1beta"))

with open("notes.txt", "r", encoding="utf-8") as f:
    document = f.read()

system_prompt = (
    "Answer only using the document provided. "
    "If the answer is not in the document, say 'I can't find that in the document.'"
)

question = input("Ask a question: ")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(system_instruction=system_prompt),
    contents=f"<document>\n{document}\n</document>\n\nQuestion: {question}",
)

print(response.text)