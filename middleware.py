
import ssl
import socket
import os

# For logging
def log_request(method, path, client_address):
    print(f"Received {method} request for {path} from {client_address}")
    return 

# For security
Blocked_ips = {
    '192.168.1.100',
    '10.0.0.5',
    '45.77.136.0',   
    '198.51.100.0'
}

def security_check(client_address, method):
    if client_address in Blocked_ips:
        print(f"Blocked request from {client_address}")
        return False
    
    if method not in ['GET', 'POST', 'PUT', 'DELETE']:
        print(f"Blocked request with unsupported method {method} from {client_address}")
        return False
    
    return True  


def enable_TLS(server_socket, cert_path="ssl"):
    certificate = os.path.join(cert_path, "./cert.pem")
    keyfile = os.path.join(cert_path, "./key.pem")

    if not os.path.exists(certificate) and not os.path.exists(keyfile):
        print(f"Certificate files not found: {certificate}, {keyfile}")
        print("Running without TLS encryption")
        return server_socket
    
    try:
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(certfile=certificate, keyfile=keyfile)
        secure_server = context.wrap_socket(server_socket, server_side=True)
        print("TLS encryption enabled")
        return secure_server
    except Exception as e:
        print(f"Failed to enable TLS: {e}")
        return server_socket

def apply_middlewares(method, path, client_ip, headers):
 
    log_request(method, path, client_ip)

    if not security_check(client_ip, method):
        return False, """\
HTTP/1.1 403 Forbidden\r
Content-Type: text/html\r
Content-Length: 51\r
\r
<html><body><h1>403 Forbidden</h1></body></html>"""

    return True, None