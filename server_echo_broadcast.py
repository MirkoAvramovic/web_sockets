# Importing the relevant libraries
import websockets
import asyncio

PORT = 7890

print("Started server and it's listening on Port " + str(PORT))

connected = set()

async def echo(websocket, path):
    print("A client just connected")
    connected.add(websocket)
    try:
        async for message in websocket:
            print("Recived message from client: " + message)
            for conn in connected:
                if conn != websocket:
                    await conn.send("Someone said: " + message)
    except websockets.exceptions.ConnectionClosed as e:
        print("A client just disconnected")
        print(e)
    finally:
        connected.remove(websocket)

start_server = websockets.serve(echo, "localhost", PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()