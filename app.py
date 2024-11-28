from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Welcome to the Calculator API</h1>
    <p>Use the following endpoints to perform operations:</p>
    <ul>
        <li><b>/add?x=5&y=3</b> - Adds two numbers</li>
        <li><b>/subtract?x=10&y=4</b> - Subtracts two numbers</li>
        <li><b>/multiply?x=6&y=7</b> - Multiplies two numbers</li>
        <li><b>/divide?x=8&y=2</b> - Divides two numbers</li>
    </ul>
    """


@app.route("/add")
def add():
    try:
        x = float(request.args.get("x"))
        y = float(request.args.get("y"))
        result = x + y
        return f"The result of {x} + {y} is {result}"
    except (TypeError, ValueError):
        return "Invalid input. Please provide numbers for x and y."


@app.route("/subtract")
def subtract():
    try:
        x = float(request.args.get("x"))
        y = float(request.args.get("y"))
        result = x - y
        return f"The result of {x} - {y} is {result}"
    except (TypeError, ValueError):
        return "Invalid input. Please provide numbers for x and y."


@app.route("/multiply")
def multiply():
    try:
        x = float(request.args.get("x"))
        y = float(request.args.get("y"))
        result = x * y
        return f"The result of {x} * {y} is {result}"
    except (TypeError, ValueError):
        return "Invalid input. Please provide numbers for x and y."


@app.route("/divide")
def divide():
    try:
        x = float(request.args.get("x"))
        y = float(request.args.get("y"))
        if y == 0:
            return "Division by zero is not allowed."
        result = x / y
        return f"The result of {x} / {y} is {result}"
    except (TypeError, ValueError):
        return "Invalid input. Please provide numbers for x and y."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)
