import random
from enum import Enum

class QuestionStrategyEnum(Enum):
    SORTED = 1
    SHUFFLED = 2

class QuestionStrategy:
  @staticmethod
  def execute(questions, sort = True):
    option = 1 if sort else 2

    if option == QuestionStrategyEnum.SORTED.value:
       questions.sort(key=lambda x:(x.category, x.difficulty))
    else:
      random.shuffle(questions)