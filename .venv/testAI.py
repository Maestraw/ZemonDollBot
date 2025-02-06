from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "where can i find harare"}
  ]
)

print(completion.choices[0].message)
