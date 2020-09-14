import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format(
            'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        print("Test Completed! \n")
        pass

    """
    TODO
    Write at least one test for each test for successful operation and
     for expected errors.
    """
    # Get_categories Endpoint!

    def test_get_categories(self):
        result = self.client().get('/categories')
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)

    # Get_paginated Quz Endpoint "200"!
    def test_get_paginated_questions(self):
        result = self.client().get('/questions')
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))

    # Get_paginated Quz Endpoint "404"!
    def test_paginated_questions_404(self):
        result = self.client().get('/questions?page=1234')
        data = json.loads(result.data)
        self.assertEqual(resultult.status_code, 404)
        self.assertEqual(data['success'], False)

    # Delete_Quz "200"
    def test_delete_question_by_ID(self):
        # Creates a ques to delete it later on!
        new_question = Question(
            question=self.question['question'],
            answer=self.question['answer'],
            category=self.question['category'],
            difficulty=self.question['difficulty']
        )
        new_question.insert()
        result = self.client().delete('/questions/{}'.format(new_question.id))
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)

    # Delete a not found Quz "404"
    def test_delete_question_404(self):
        result = self.client().delete('/question/1234')
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 404)
        self.assertEqual(data['success'], False)

    # Create a Q
    def test_create_question(self):
        result = self.client().post('/questions', json=self.question)
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)

    # Get all Q in a Category
    def test_getAll_questions_in_category(self):
        result = self.client().get('/categories/1/questions')
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])

    # Get Qes from a not found category!
    def get_questions_in_category_404(self):
        result = self.client().get('/categories/1234/questions')
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 404)
        self.assertEqual(data['success'], False)

    # get Q play mode.
    def test_get_quiz_question(self):
        # post req with the required params.
        result = self.client().post('/quizzes',
                                    json={'quiz_category':
                                          {'type': 'Science', 'id': '1'},
                                          'previous_questions': []})
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question'])

    def test_quiz_question_404(self):
        # post req with the required params.
        result = self.client().post('/quizzes',
                                    json={'quiz_category':
                                          {'type': 'none', 'id': '8888'},
                                          'previous_questions': []})
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 404)
        self.assertEqual(data['success'], False)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
