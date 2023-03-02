# Importing the relevant libraries
import websockets
import asyncio

PORT = 7890

print("Started server and it's listening on Port " + str(PORT))

async def echo(websocket, path):
    print("A client just connected")
    try:
        async for message in websocket:
            print("Recived message from client: " + message)
            await websocket.send("Pong:" + message)
    except websockets.exceptions.ConnectionClosed as e:
        print("A client just disconnected")
        print(e)

start_server = websockets.serve(echo, "localhost", PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()