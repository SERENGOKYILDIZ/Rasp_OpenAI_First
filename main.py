from openai import OpenAI

# Reading API_KEY
with open("API_KEY.txt", "r", encoding="utf-8") as dosya:
    API_KEY = dosya.read()
    print(API_KEY)

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Hello World!"},
        {"role": "user", "content": "Say your name"},
    ]
)

output = response.choices[0].message.content

print(output)
