import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "Plan a trip for Goa"
        }
    ]
)
print(response["message"]["content"])