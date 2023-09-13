from flask import Flask, request, jsonify
from flask_cors import CORS
import json

from entities.quiz import Quiz

app = Flask(__name__)
CORS(app)

quiz = Quiz()

@app.route('/start-quiz', methods=['GET'])
def start_quiz():
  response = quiz.create('questions.json')

  questions = [{
    'id': question.id,
    'description': question.description,
    'options': question.options,
    'category': question.category,
    'difficulty': question.difficulty
  } for question in response]

  return jsonify({ 'questions': questions })

@app.route('/get-question', methods=['GET'])
def get_question():
  question = quiz.get_question()
  return jsonify(question.to_dict())

@app.route('/avaliate', methods=['POST'])
def avaliate():
  answer = request.json['answer']
  quiz.avaliate(answer)
  result = quiz.get_result()
  return jsonify({ 'result': result })

if __name__ == '__main__':
    app.run(debug=True)
