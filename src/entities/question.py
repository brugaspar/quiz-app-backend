import random
import json

class Question:
  def __init__(self, description, options, answer, category, difficulty) -> None:
    self.id = random.randint(1, 100)
    self.description = description
    self.options = options
    self.answer = answer
    self.category = category
    self.difficulty = difficulty

  def to_json(self):
    return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)