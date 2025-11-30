"""
CP1404/CP5632 Practical - Flask Web Application
Temperature Converter using Flask
Student: Zhaozhang Huang
"""
from flask import Flask

app = Flask(__name__)

def convert_celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.

    Args:
        celsius (float): Temperature in Celsius

    Returns:
        float: Temperature in Fahrenheit
    """
    return celsius * 9.0 / 5 + 32


@app.route('/')
def hello_world():
    """Home page route."""
    return '<h1>Hello World! :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name="Zhaozhang Huang"):
    """
    Greet the user with optional name parameter.

    Args:
        name (str): Optional name parameter

    Returns:
        str: Greeting message
    """
    return f"Hello {name}"


@app.route('/celsius_to_fahrenheit')
@app.route('/celsius_to_fahrenheit/<celsius_str>')
def celsius_to_fahrenheit_route(celsius_str="0"):
    """
    Convert Celsius to Fahrenheit via URL parameter.

    Args:
        celsius_str (str): Celsius temperature as string

    Returns:
        str: Conversion result with helpful text
    """
    try:
        celsius = float(celsius_str)
        fahrenheit = convert_celsius_to_fahrenheit(celsius)

        # Return formatted result with helpful text
        return f'''
        <h1>Temperature Converter</h1>
        <p><strong>Input:</strong> {celsius}° Celsius</p>
        <p><strong>Result:</strong> {fahrenheit:.2f}° Fahrenheit</p>
        <p><em>Conversion formula: (°C × 9/5) + 32 = °F</em></p>
        <br>
        <p>Try other values by changing the URL:</p>
        <p>http://127.0.0.1:5000/celsius_to_fahrenheit/<strong>100.2</strong></p>
        '''

    except ValueError:
        return '''
        <h1>Error</h1>
        <p>Please provide a valid number in the URL.</p>
        <p>Example: http://127.0.0.1:5000/celsius_to_fahrenheit/<strong>25</strong></p>
        '''


if __name__ == '__main__':
    app.run(debug=True)