from openai import OpenAI

# Your OpenAI API key
client = OpenAI(api_key="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")

messages=[ {"role": "system", "content": "You are a intelligent assistant."} ]

# Create a new session
session = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[ {"role": "system", "content": "You are a intelligent assistant."} ]
)

while True: 
	message = input("User : ") 
	if message: 
		messages.append( 
			{"role": "user", "content": message}, 
		)
		chat = client.chat.completions.create(
			model="gpt-3.5-turbo", messages=messages 
		)
	response = session.choices[0].message.content
	print(f"ChatGPT: {response}") 
	messages.append({"role": "assistant", "content": response})