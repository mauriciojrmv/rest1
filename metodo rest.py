from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Ruta para servir el archivo index.html
@app.route('/')
def index():
    with open('index.html', 'r') as file:
        return render_template_string(file.read())

# Método GET simple
@app.route('/hello', methods=['GET'])
def hello_world():
    return jsonify(message="Hello, World!"), 200

# Método POST simple
@app.route('/echo', methods=['POST'])
def echo():
    data = request.json
    if not data:
        return jsonify(message="No data provided"), 400
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)
