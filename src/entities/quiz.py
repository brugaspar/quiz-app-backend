import json
import os

from factories.question_factory import QuestionFactory
from strategies.question_strategy import QuestionStrategy

class Quiz:
  _instance = None

  def __init__(self):
    self.questions = []
    self.count = 0
    self.result = 0

  def __new__(cls):
    if cls._instance is None:
      cls._instance = super().__new__(cls)

    return cls._instance

  def create(self, filename, sort = True):
    file = open(os.path.abspath(filename))
    data = file.read().encode('windows-1252')
    questions = json.loads(data)
    self.questions = [QuestionFactory.create(question) for question in questions]
    QuestionStrategy.execute(self.questions, sort)
    return self.questions

  def get_question(self):
    if self.count == len(self.questions):
      return None

    return self.questions[self.count]

  def avaliate(self, answer):
    if self.questions[self.count].answer == answer:
      self.result += 1

    self.count += 1

  def get_result(self):
    return self.result
