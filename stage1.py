from google import genai

client = genai.Client()  

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain what an API is in 2 sentences.",
)

print(response.text)