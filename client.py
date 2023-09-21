import websockets
import asyncio

# Define an asynchronous function named "listen" to manage WebSocket communication.
async def listen():
    # Specify the WebSocket server's URL (change as needed).
    url = "ws://127.0.0.1:7890/"

    # Establish a WebSocket connection as a context manager.
    async with websockets.connect(url) as ws:
        # Send an initial message to the server (customize as needed).
        await ws.send("Hello Server!")
        # Continuously listen for incoming messages from the server.
        while True:
            # Receive a message from the WebSocket server.
            msg = await ws.recv()

            # Print the received message to the console.
            print(msg)

# Run the "listen" function within an event loop to start the WebSocket client.
asyncio.get_event_loop().run_until_complete(listen())