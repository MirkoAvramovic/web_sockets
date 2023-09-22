## web_sockets

This repository contains Python scripts for implementing WebSocket communication. It consists of two server scripts and one client script.

### client.py

The "client.py" script establishes a connection to a WebSocket server on a defined port and sends a message to the server. It then prints the response received from the server.

### server_echo.py

The "server_echo.py" script acts as a WebSocket server that listens on a specified port. When a client connects, the server receives a message from the client and promptly sends the same message back to the client.

### server_echo_broadcast.py

The "server_echo_broadcast.py" script functions as a WebSocket server, just like "server_echo.py." However, it has an additional feature: when a client sends a message, the server broadcasts that message to all other connected clients, excluding the sender.
