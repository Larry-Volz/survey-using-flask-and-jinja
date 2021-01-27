from surveys import *
from flask import Flask, request, render_template 
from flask_debugtoolbar import DebugToolbarExtension

app=Flask(__name__)

app.config['SECRET_KEY'] = 'FOO'
app.debug=True
debug=DebugToolbarExtension(app)

responses = []


@app.route('/')
def survey_start_page():
    global title
    global instructions
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template('index.html', survey_title=title, survey_instructions=instructions)

@app.route('/questions/<int:q_number>', methods=["GET","POST"])
def questions_page():
    q_num = POSTS.get(q_number, "Post Not Found")
    return render_template('questions.html')

