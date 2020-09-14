import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={'/': {'origins': '*'}})
    '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization, true')
        # No need to add the OPTIONS/PATCH/PUT Methods.
        response.headers.add(
            'Access-Control-Allow-Methods', 'GET, POST, DELETE')
        return response

    '''
  @TODO:
  Create an endpoint to handle GET requests
  for all available categories.
  '''
    # Helper Fuunction I found myself typing the same line of code a lot.
    def format_data(data):
        my_data = [d.format() for d in data]
        return my_data

    # I want this to work with any request as it's required for the Home page.
    @app.route('/categories')
    def get_all_categories():
        try:
            categories = Category.query.all()
            categories_to_dict = {}
            for category in categories:
                categories_to_dict[category.id] = category.type
            return jsonify({
                'success': True,
                'categories': categories_to_dict
            }), 200
        except Exception:
            abort(500)

    '''
  @TODO:
  Create an endpoint to handle GET requests for questions,
  including pagination (every 10 questions).
  This endpoint should return a list of questions,
  number of total questions, current category, categories.
  '''

    # I want this to work with any request as it's required for the Home page.
    @app.route('/questions')
    def get_questions():
        page = request.args.get('page', 1, type=int)
        questions = Question.query.order_by(
            Question.id).paginate(page, 10, False).items
        if len(questions) == 0:
            abort(404)
        # helper function line 35 instead of repeating the next line again.
        questions_ready = format_data(questions)
        # questions_ready = [q.format() for q in questions]
        categories = Category.query.all()
        categories_ready = {}
        for category in categories:
            categories_ready[category.id] = category.type

        total_question = len(Question.query.all())

        current_category = list(set([q['category'] for q in questions_ready]))

        return jsonify({
            'success': True,
            'questions': questions_ready,
            'total_questions': total_question,
            'categories': categories_ready,
            'current_category': current_category
        })

    '''
  @TODO:
  Create an endpoint to DELETE question using a question ID.
  '''
    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        question = Question.query.filter_by(id=question_id).one_or_none()
        if not question:
            abort(404)
        question.delete()
        return jsonify({
            'success': True
        })
    '''
  @TODO:
  Create an endpoint to POST a new question,
  which will require the question and answer text,
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab,
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.
  '''
    @app.route('/questions/new', methods=['POST'])
    def create_question():
        error = True
        try:
            body = request.get_json()
            new_question = Question(
                question=body.get('question'),
                answer=body.get('answer'),
                category=body.get('category'),
                difficulty=int(body.get('difficulty'))
            )
            new_question.insert()
            error = False
            return jsonify({
                'success': True
            })
        except error:
            abort(400)
        finally:
            return

    '''
  @TODO:
  Create a POST endpoint to get questions based on a search term.
  It should return any questions for whom the search term
  is a substring of the question.
  TEST: Search by any phrase. The questions list will update to include
  only question that include that string within their question.
  Try using the word "title" to start.
  '''
    # Not quite sure why should I use title,
    # I understand that the searchTerm is sent already within the body.
    @app.route('/questions/<string:searchTerm>', methods=['POST'])
    def search_question(searchTerm):
        error = True
        try:
            questions = Question.query.filter(
                Question.question.ilike('%'+searchTerm+'%')).all()
            questions_ready = format_data(questions)
            error = False
            return jsonify({
                'success': True,
                'questions': questions_ready
            })

        except error:
            abort(400)
        finally:
            return
    '''
  @TODO:
  Create a GET endpoint to get questions based on category.

  TEST: In the "List" tab / main screen, clicking on one of the
  categories in the left column will cause only questions of that
  category to be shown.
  '''
    @app.route('/categories/<int:category_id>/questions')
    def get_category_questions(category_id):
        category = Category.query.filter_by(id=category_id).one_or_none()
        if not category:
            abort(404)
        questions = Question.query.filter_by(category=category_id)
        questions_ready = format_data(questions)
        return jsonify({
            'success': True,
            'questions': questions_ready
        })

    '''
  @TODO:
  Create a POST endpoint to get questions to play the quiz.
  This endpoint should take category and previous question parameters
  and return a random questions within the given category,
  if provided, and that is not one of the previous questions.

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not.
  '''
    @app.route('/quizzes/next', methods=['POST'])
    def get_quiz_question():
        body = request.get_json()
        # print(body)
        category = body.get('quiz_category', None)
        previous_questions = body.get('previous_questions')
        if category['id'] != 0:
            category_all = Category.query.filter_by(
                id=category['id']).one_or_none()
            if not category_all:
                abort(404)
            questions = Question.query.filter_by(category=category_all.id)
        else:
            questions = Question.query.all()
            my_questions = []
            for question in questions:
                exsited = False
                for p in previous_questions:
                    if p == question.id:
                        exsited = True
                        break
                if not exsited:
                    my_questions.append(question)
            random_index = random.randint(0, len(my_questions)-1)
            return jsonify({
                'success': True,
                'question': my_questions[random_index].format()
            })

    '''
  @TODO:
  Create error handlers for all expected errors
  including 404 and 422.
  '''
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': "Not Found"
        }), 404

    @app.errorhandler(422)
    def un_processable_entitiy(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': "un processable entitiy"
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': "bad request"
        }), 400

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': "internal server error"
        }), 500

    return app
