# web_sockets

This repository contains Python scripts for implementing WebSocket communication. It consists of two server scripts and one client script.

## Client

The "client.py" script establishes a connection to a WebSocket server on a defined port and sends a message to the server. It then prints the response received from the server.

## Server Echo

### server_echo.py

The "server_echo.py" script acts as a WebSocket server that listens on a specified port. When a client connects, the server receives a message from the client and promptly sends the same message back to the client.

## Server Echo Broadcast

### server_echo_broadcast.py

The "server_echo_broadcast.py" script functions as a WebSocket server, just like "server_echo.py." However, it has an additional feature: when a client sends a message, the server broadcasts that message to all other connected clients, excluding the sender.

Feel free to explore these scripts to understand WebSocket communication in action and how to build WebSocket clients and servers in Python.

## Usage

To use these scripts:

1. Clone this repository to your local machine.
2. Ensure you have Python and the `websockets` library installed.
3. Run the desired server script(s) based on your requirements.
4. Run the "client.py" script to connect to the server and test the WebSocket communication.

Enjoy exploring WebSocket communication with Python!