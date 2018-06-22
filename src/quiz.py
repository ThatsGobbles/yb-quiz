import typing as tp

from flask import Flask

class PossibleAnswers(tp.NamedTuple):
    nonclinical: str
    mild: str
    moderate: str
    severe: str
    extreme: str

class Question(tp.NamedTuple):
    text: str
    possible_answers: PossibleAnswers

QUESTIONS = (
    Question(
        text='How much of your time is occupied by obsessive thoughts?',
        possible_answers=PossibleAnswers(
            'None',
            'Less than 1 hour per day',
            '1-3 hours per day',
            '3-8 hours per day',
            'More than 8 hours per day',
        ),
    ),
    Question(
        text='How much do your obsessive thoughts interfere with functioning in your social, work, or other roles?',
        possible_answers=PossibleAnswers(
            'None',
            'Slight interference, but no impairment',
            'Definite interference, but managable',
            'Substantial intereference',
            'Extreme intereference, incapacitating',
        ),
    ),
    Question(
        text='How much distress do your obsessive thoughts cause you?',
        possible_answers=PossibleAnswers(
            'None',
            'Mild, not too disturbing',
            'Moderate, disturbing, but still manageable',
            'Severe, very disturbing',
            'Extreme, near constant and disabling distress',
        ),
    ),
    Question(
        text='How much of an effort do you make to resist the obsessive thoughts?',
        possible_answers=PossibleAnswers(
            'Always make an effort to resist, or don’t even need to resist',
            'Try to resist most of the time',
            'Make some effort to resist',
            'Reluctantly yield to all obsessive thoughts',
            'Completely and willingly yield to all obsessions',
        ),
    ),
    Question(
        text='How much control do you have over your obsessive thoughts?',
        possible_answers=PossibleAnswers(
            'Complete control',
            'Much control, usually able to stop or divert obsessions with some effort and concentration',
            'Moderate control, sometimes able to stop or divert obsessions',
            'Little control, rarely successful in stopping or dismissing obsessions',
            'No control, rarely able to even momentarily alter obsessive thinking',
        ),
    ),

    Question(
        text='How much time do you spend performing compulsive behaviors?',
        possible_answers=PossibleAnswers(
            'None',
            'Less than 1 hour per day',
            '1-3 hours per day',
            '3-8 hours per day',
            'More than 8 hours per day',
        ),
    ),
    Question(
        text='How much of an effort do you make to resist the compulsions?',
        possible_answers=PossibleAnswers(
            'Always make an effort to resist, or don’t even need to resist',
            'Try to resist most of the time',
            'Make some effort to resist',
            'Reluctantly yield to all complusions',
            'Completely and willingly yield to all complusions',
        ),
    ),
    Question(
        text='How much control do you have over the compulsions?',
        possible_answers=PossibleAnswers(
            'Complete control',
            'Much control, usually able to stop or divert compulsive behavior with some effort and concentration',
            'Moderate control, sometimes able to stop or divert compulsive behavior',
            'Little control, rarely successful in stopping or dismissing compulsive behavior',
            'No control, rarely able to even momentarily alter compulsive behavior',
        ),
    ),
)

app = Flask(__name__)

@app.route('/')
def quiz():
    return str(QUESTIONS)
