import websockets
import asyncio

# Define the port on which the WebSocket server will listen.
PORT = 7890

# Print a message indicating that the server has started and is listening on the specified port.
print("Started server and it's listening on Port " + str(PORT))

# Create a set to keep track of connected clients.
connected = set()

# Define an asynchronous WebSocket communication handler named "echo."
async def echo(websocket, path):
    print("A client just connected")

    # Add the connected client's WebSocket object to the set.
    connected.add(websocket)
    try:
        # Continuously listen for messages from the connected client.
        async for message in websocket:
            print("Recived message from client: " + message)

            # Broadcast the received message to all connected clients except the sender.
            for conn in connected:
                if conn != websocket:
                    await conn.send("Someone said: " + message)
    except websockets.exceptions.ConnectionClosed as e:
        # Handle client disconnection and print relevant information.
        print("A client just disconnected")
        print(e)
    finally:
        # Remove the disconnected client's WebSocket object from the set.
        connected.remove(websocket)

# Create a WebSocket server and bind it to "localhost" and the specified port.
start_server = websockets.serve(echo, "localhost", PORT)

# Start the event loop to run the WebSocket server indefinitely.
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()