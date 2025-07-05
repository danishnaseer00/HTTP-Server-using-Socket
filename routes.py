import json

def handle_routes(path):
    if path == '/':
        return homepage()
    elif path == '/about':
        return about_page()
    elif path == '/api/info':
        return api_info()
    elif path == '/admin':
        return admin_page()
    elif path == '/contact':
        return contact_page()
    else:
        return not_found()


def homepage():
    body = """
        <html>
    <head>
    <title>Home</title>
    <style>
        body {
        font-family: 'Segoe UI', sans-serif;
        background: #f4f6f8;
        color: #333;
        text-align: center;
        padding: 50px;
        margin: 0;
        }

        h1 {
        color: #2c3e50;
        font-size: 2.5rem;
        }

        p {
        font-size: 1.2rem;
        margin: 20px 0;
        }

        a {
        display: inline-block;
        margin: 10px;
        padding: 12px 20px;
        text-decoration: none;
        background-color: #3498db;
        color: white;
        border-radius: 8px;
        transition: background-color 0.3s;
        }

        a:hover {
        background-color: #2980b9;
        }

        .container {
        max-width: 600px;
        margin: auto;
        background: white;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
    </style>
    </head>
    <body>
    <div class="container">
        <h1> Welcome to My HTTP Web Server</h1>
        <p>This is a simple and custom-built Python web server.</p>
        <p>Explore the available pages:</p>
        <a href="/about">About Page</a>
        <a href="/admin">Admin Page</a>
        <a href="/contact">Contact Page</a>
    </div>
    </body>
    </html>
    """

    return f"""\
HTTP/1.1 200 OK\r
Content-Type: text/html\r
Content-Length: {len(body.encode('utf-8'))}\r
\r
{body}"""


def about_page():
    body = """
     <html>
<head>
  <title>About</title>
  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
      background: #f4f6f8;
      color: #333;
      text-align: center;
      padding: 50px;
      margin: 0;
    }

    h1 {
      color: #2c3e50;
      font-size: 2.5rem;
    }

    p {
      font-size: 1.2rem;
      margin: 20px 0;
    }

    a {
      display: inline-block;
      margin: 10px;
      padding: 12px 20px;
      text-decoration: none;
      background-color: #2ecc71;
      color: white;
      border-radius: 8px;
      transition: background-color 0.3s;
    }

    a:hover {
      background-color: #27ae60;
    }

    .container {
      max-width: 600px;
      margin: auto;
      background: white;
      padding: 30px;
      border-radius: 12px;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
  </style>
</head>
<body>
  <div class="container">
    <h1> About Us</h1>
    <p>We are learning how to build fast, lightweight web servers using Python socket programming.</p>
    <a href="/">Go back to Home</a>
  </div>
</body>
</html>
"""
    return f"""\
HTTP/1.1 200 OK\r
Content-Type: text/html\r
Content-Length: {len(body.encode('utf-8'))}\r
\r
{body}"""


def admin_page():
    body = """
     <html>
<head>
  <title>Admin</title>
  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
      background: #fdf6f0;
      color: #333;
      text-align: center;
      padding: 50px;
      margin: 0;
    }

    h1 {
      color: #c0392b;
      font-size: 2.5rem;
    }

    p {
      font-size: 1.2rem;
      margin: 20px 0;
    }

    a {
      display: inline-block;
      margin: 10px;
      padding: 12px 20px;
      text-decoration: none;
      background-color: #e74c3c;
      color: white;
      border-radius: 8px;
      transition: background-color 0.3s;
    }

    a:hover {
      background-color: #c0392b;
    }

    .container {
      max-width: 600px;
      margin: auto;
      background: white;
      padding: 30px;
      border-radius: 12px;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
  </style>
</head>
<body>
  <div class="container">
    <h1> Admin Panel</h1>
    <p>This section is for administrators only. Please proceed with caution.</p>
    <a href="/">Go back to Home</a>
  </div>
</body>
</html>
"""
    return f"""\
HTTP/1.1 200 OK\r
Content-Type: text/html\r
Content-Length: {len(body.encode('utf-8'))}\r
\r
{body}"""


def api_info():
    info = {
        'version': '1.0',
        'author': 'You!',
        'description': 'This is a simple HTTP web server built in Python.'
    }
    response_body = json.dumps(info)
    return f"""\
HTTP/1.1 200 OK\r
Content-Type: application/json\r
Content-Length: {len(response_body.encode('utf-8'))}\r
\r
{response_body}"""

def contact_page():
    body = """
      <html>
<head>
  <title>Contact</title>
  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
      background: #f0f9ff;
      color: #333;
      text-align: center;
      padding: 50px;
      margin: 0;
    }

    h1 {
      color: #1e3a8a;
      font-size: 2.5rem;
    }

    p {
      font-size: 1.2rem;
      margin: 20px 0;
    }

    .container {
      max-width: 600px;
      margin: auto;
      background: white;
      padding: 30px;
      border-radius: 12px;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }

    a {
      display: inline-block;
      margin-top: 20px;
      padding: 12px 20px;
      text-decoration: none;
      background-color: #2563eb;
      color: white;
      border-radius: 8px;
      transition: background-color 0.3s;
    }

    a:hover {
      background-color: #1d4ed8;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1> Contact Us</h1>
    <p>You can reach us at <strong>danish@example.com</strong></p>
    <p>Or connect with us on social media!</p>
    <a href="/">Go back to Home</a>
  </div>
</body>
</html>

     """
    return f"""\
HTTP/1.1 200 OK\r
Content-Type: text/html\r
Content-Length: {len(body.encode('utf-8'))}\r
\r
{body}"""


def not_found():
    body = """
<html>
<head><title>404 Not Found</title></head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you're looking for does not exist.</p>
    <p><a href="/">Return Home</a></p>
</body>
</html>
"""
    return f"""\
HTTP/1.1 404 Not Found\r
Content-Type: text/html\r
Content-Length: {len(body.encode('utf-8'))}\r
\r
{body}"""
