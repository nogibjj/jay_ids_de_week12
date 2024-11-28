# Dockerized Flask Application

This project demonstrates a simple Python Flask application running in a Docker container.

## Prerequisites

- Docker installed on your system.
- Python 3.x installed for local testing.

## How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/dockerized-flask-app.git
   cd dockerized-flask-app

2. Install dependencies:
pip install -r requirements.txt

3. Run the app:
python app.py
Calculator API
This is a simple Flask-based Calculator API that performs basic arithmetic operations such as addition, subtraction, multiplication, and division. The API is lightweight, easy to use, and provides results directly via query parameters.

## Features
Addition (/add)
Subtraction (/subtract)
Multiplication (/multiply)
Division (/divide)

### Once the server is running, the application will be available at:
http://127.0.0.1:8001/
## Endpoints
Addition:

Endpoint: /add
Query Parameters:
x: First number
y: Second number

### Example:
http://127.0.0.1:8001/add?x=5&y=3

### Response:
The result of 5.0 + 3.0 is 8.0

### Future Enhancements
Add support for more advanced mathematical functions (e.g., modulus, square root, exponents).
Integrate user authentication for more secure usage.
Provide a more user-friendly frontend.
