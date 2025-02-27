from flask import Flask, request, jsonify

from ..model.numbers import Numbers

app = Flask(__name__)
numbers = Numbers()

@app.route('/calculations/sum', methods=['POST'])
def sum_numbers():
    try:
        data = request.get_json()
        if not data or 'numbers' not in data:
            return jsonify({"error": "Campo 'numbers' é obrigatório"}), 400
        result = numbers.sum_numbers(data['numbers'])
        return jsonify({"result": result}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Erro interno"}), 500

@app.route('/calculations/average', methods=['POST'])
def average_numbers():
    try:
        data = request.get_json()
        if not data or 'numbers' not in data:
            return jsonify({"error": "Campo 'numbers' é obrigatório"}), 400
        result = numbers.average_numbers(data['numbers'])
        return jsonify({"result": result}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Erro interno"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)