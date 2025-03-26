from openai import OpenAI
client = OpenAI(
    api_key="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",
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud."},
        {"role": "user", "content": "what is coding."}
    ]
)

print(completion.choices[0].message.content)