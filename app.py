from surveys import *
from flask import Flask, request, render_template 
from flask_debugtoolbar import DebugToolbarExtension

app=Flask(__name__)

app.config['SECRET_KEY'] = 'FOO'
app.debug=True
debug=DebugToolbarExtension(app)





@app.route('/')
def survey_start_page():
    global responses
    global q_number
    global title
    global instructions
    global questions
    global q_idx
    responses = []
    q_number = 0
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    questions = [question for question in satisfaction_survey.questions]
    q_idx=0
    return render_template('index.html', survey_title=title, survey_instructions=instructions)

@app.route('/questions/<int:q_number>', methods=["GET","POST"])
def questions_page(q_number, questions):
    
    q_num=request.form["q_number"]
    num_q=len(questions)
    if q_idx < num_q:
        q_idx += 1
        return render_template('questions.html',num_q=q_idx)
    else:
        return render_template ('thank_you.html')

