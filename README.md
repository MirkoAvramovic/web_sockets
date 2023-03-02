# web_sockets
I've created three python scripts in this repository: two for the server and one for a client.

#client
A client connects to a server on the defined port and sends a message. After that, the client prints the response of the server.

#server_echo.py
The server is listening on the defined port. When the client is connected, the server receives a message from the client and sends him back the same message.

#server_echo_broadcast.py
The message received from the client is sent to all other clients but not back to the sender.
