# server.py
import os
import socket
from dotenv import load_dotenv
from routes import handle_routes
import threading
from middleware import enable_TLS, apply_middlewares

load_dotenv()

Port = int(os.getenv('Port', 8000))
address = os.getenv('Address', '127.0.0.1') 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((address, Port))
server.listen(5)

print(f"Server is listening on http://{address}:{Port}")

try:
    server = enable_TLS(server,cert_path="ssl")
    print("TLS enabled successfully")
except Exception as e:
    print(f"TLS setup failed: {e}. Running without TLS.")

def client_handling(client_connection, Client_address):
    try:
        request_data = client_connection.recv(1024).decode('utf-8')
        if not request_data:
            print(f"No request data received from {Client_address}. Closing connection.")
            client_connection.close()
            return
        
        print(f"Received request from {Client_address}:\n{request_data}")
        
        
        lines = request_data.split('\n')
        if not lines:
            print("Invalid request format")
            client_connection.close()
            return
            
        first_line = lines[0].strip()
        if not first_line:
            print("Empty first line in request")
            client_connection.close()
            return
            
        parts = first_line.split(' ')
        if len(parts) < 3:
            print("Invalid HTTP request line")
            client_connection.close()
            return
            
        Method, path, HTTP_version = parts[0], parts[1], parts[2]
        print(f"Method: {Method}, Path: {path}, HTTP Version: {HTTP_version}")

      
        headers = {}
        for line in lines[1:]:
            line = line.strip()
            if ': ' in line:
                key, value = line.split(': ', 1)
                headers[key] = value.strip()

        # Apply middlewares
        allowed, response = apply_middlewares(Method, path, Client_address[0], headers)
        if not allowed:
            client_connection.sendall(response.encode('utf-8'))
            return
            
        print(f"Processing request for {path} from {Client_address}")       
        response = handle_routes(path)
        if not response.startswith('HTTP/'):
            response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: {len(response)}\r\n\r\n{response}"

        client_connection.sendall(response.encode('utf-8'))


    except Exception as e:
        print(f"An error occurred while handling the request from {Client_address}: {e}")
        
        error_response = """\
HTTP/1.1 500 Internal Server Error\r
Content-Type: text/html\r
Content-Length: 62\r
\r
<html><body><h1>500 Internal Server Error</h1></body></html>"""
        try:
            client_connection.sendall(error_response.encode('utf-8'))
        except:
            pass
    finally:
        client_connection.close()


while True:
    try:
        client_connection, Client_address = server.accept()
        thread = threading.Thread(target=client_handling, args=(client_connection, Client_address))
        thread.daemon = True  
        thread.start()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        server.close()
        break
    except Exception as e:
        print(f"Error accepting connection: {e}")
        continue