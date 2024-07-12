from flask import Flask, request, jsonify
from flask_cors import CORS
from rag import mainRAG

app = Flask(__name__)
cors = CORS(app, resources={r"/chat": {"origins": "http://localhost:5500"}}, supports_credentials=True, expose_headers=["Content-Type"], allow_headers=["Content-Type"])

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    question = data['message']
    
    return jsonify({'response': mainRAG(question)})


if __name__ == '__main__':
    app.run(debug=True)
