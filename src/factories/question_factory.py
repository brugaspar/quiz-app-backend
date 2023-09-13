from entities.question import Question

class QuestionFactory:
  @staticmethod
  def create(question) -> Question:
    return Question(
      question['description'],
      question['options'],
      question['answer'],
      question['category'],
      question['difficulty']
    )