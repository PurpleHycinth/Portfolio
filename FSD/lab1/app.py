from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/calculate')
def calculate():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    operator = request.args.get('operator', 'add')

    if operator == 'add':
        result = a + b
        operator_str = '+'
    elif operator == 'subtract':
        result = a - b
        operator_str = '-'
    elif operator == 'multiply':
        result = a * b
        operator_str = '*'
    elif operator == 'divide':
        if b == 0:
            return "Error: Division by zero"
        result = a / b
        operator_str = '/'

    calculation = f"{a} {operator_str} {b} = {result}"
    return render_template('calculator.html',result=calculation)

if __name__ == '__main__':
    app.run(debug=False)
    
# http://127.0.0.1:5000/calculate?a=1&b=1&operator=add
