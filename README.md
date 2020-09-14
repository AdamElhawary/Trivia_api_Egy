# Full Stack API Final Project

Originally this was a project of the Full stack nano degree offered by udacity. 

Udacity : https://udacity.com/. 

### questionsPerPlay = 3; ### 

I would recommend trying their Nano Degree as it would add a lot to your experience. 

I will leave their intro as it is ;)



## Full Stack Trivia

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a  webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out. 

That's where you come in! Help them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

1) Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer. {Done}
2) Delete questions. {Done}
3) Add questions and require that they include question and answer text. {Done}
4) Search for questions based on a text query string. {Done}
5) Play the quiz game, randomizing either all questions or within a specific category. {Done}

### Additional done tasks:-
1) Css Changed! 
2) "Next Question" button's text changes after answering the last question to "Result?" QuizView.js line 151.
3) Fixed Regex.  QuizView.js line 47.
4) Added missing alt attr to img tags.
5) Fixed the Logo.
6) Added an alert after adding a new question.
7) React Compiled successfully! No warnings.
8) Added Icons next to categories "Play mode".

Required dependancies & to Start the project:-  

### Backend:-
Kindly refer to [a relative link](backend\README.md) which contains a completed Flask and SQLAlchemy server.

### Frontend
Kindly refer to [a relative link](frontend\README.md) which contains a complete React frontend to consume the data from the Flask server.

### ..... ###

### About this API :-

Based on: REST principles! each endpoint returns a JSON metadata.

Base Uri: "Your_local_Host:Port/".

## Allowed HTTP methods "For now":-
GET:	Retrieves resources
POST:	Creates resources
DELETE:	Deletes resources

### EndPoints:-

GET '/categories'
GET '/questions'
GET'/categories/category_id/questions'
POST '/questions/searchTerm'
POST 'questions/new'
POST '/quizzes/next'
DELETE '/questions/id'

### GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}

### GET '/questions'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding
  string of the category,
  A list of dictionaries of Questions in which the keys are the ids, answer and difficulty and category and the value is self explanatory,
  A list of Integers of the current categories ids,
  total questions which is an int.
- Request Arguments: None
- Returns: 
    An object just like the example below.
{
    categories: {1: "Science", 2: "Art", 3: "Geography", 4: "History", 5: "Entertainment", 6: "Sports"}
    current_category: (4) [3, 4, 5, 6]
    questions: (10) [{…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}]
    success: true
    total_questions: 22
}

### GET'/categories/category_id/questions'
- Fetches a dictionary of questions based on the category id.
- Request Arguments: None
- Returns: 
    An object just like the example below.
{
    questions: (3) [{…}, {…}, {…}]
    success: true
}
# Notice:-
Obj.questions[1] =
 {
    answer: "Apollo 13",
    category: 5,
    difficulty: 4,
    id: 2,
    question: "What movie earned Tom Hanks his third.."
}

### POST '/questions/searchTerm'
-Takes a string "SearchTerm" and returns a list of dictionaries of questions.
- Request Arguments: String
- Returns: 
    An object just like the example below.
{
    questions: [{…}],
    success: true
}
# Notice:-
Obj.questions[1] =
 {
    answer: "Apollo 13",
    category: 5,
    difficulty: 4,
    id: 2,
    question: "What movie earned Tom Hanks his third.."
}

### POST 'questions/new'

- Sends a request to add a new question.
- Request Arguments: a dictionary just like the example below "SAME KEYS".
 {
    answer: "Apollo 13",
    category: 5,
    difficulty: 4,
    id: 2,
    question: "What movie earned Tom Hanks his third.."
}
- Returns: None


### POST '/quizzes/next'
- Sends a request to get the next question during the play mode.
- Request Arguments: an object just like the example below "SAME KEYS".
{
    'previous_questions': [22, 29, 27],
     'quiz_category': {'type': 'Science', 'id': '1'}
}
- Returns: an object that contains a random question just like the example below
{
    question: 
    {
        answer: "Alexan....",
        category: 1,
        difficulty: 3,
        id: 21,
        question: "Who discovered..."
    },
    success: true
} 

### DELETE '/questions/id'
- Sends a delete request using a question's id.
- Request Arguments: integer "Valid question id".
- Returns: None.

### ................ ###

I enjoyed working on this project and I've learnt a lot too. 
I left all the TODOS so that anyone can try his luck.

#Thanks Udacity!