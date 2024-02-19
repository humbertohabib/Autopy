import chainlit as cl


@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...
    if ("python" in message.content.lower()):
        resposta = "Parabéns"
    else:
        resposta = "Ok, então"

    # Send a response back to the user
    await cl.Message(
        content=resposta,
    ).send() 