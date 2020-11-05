from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import csv

author = 'Your name here'

doc = """
the number of pages in the game
is determined by the number of questions in the CSV.
See the comment below about how to randomize the order of pages.
"""


class Constants(BaseConstants):
    name_in_url = 'simple_quiz'
    players_per_group = None

    with open('simple_quiz/quiz.csv') as questions_file:
        questions = list(csv.DictReader(questions_file))

    num_rounds = 15 #len(questions)


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            self.session.vars['questions'] = Constants.questions.copy()
            ## ALTERNATIVE DESIGN:
            ## to randomize the order of the questions, you could instead do:

            # import random
            # randomized_questions = random.sample(Constants.questions, len(Constants.questions))
            # self.session.vars['questions'] = randomized_questions

            ## and to randomize differently for each participant, you could use
            ## the random.sample technique, but assign into participant.vars
            ## instead of session.vars.

        for p in self.get_players():
            question_data = p.current_question()
            p.question_id = int(question_data['id'])
            p.question = question_data['question']
            p.solution = question_data['solution']
            p.showed_solution = question_data['showed_solution']


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    question_id = models.IntegerField()
    question = models.StringField()
    solution = models.StringField()
    showed_solution = models.StringField()
    submitted_answer = models.StringField(widget=widgets.RadioSelect)

    def submitted_answer_choices(self):
        qd = self.current_question()
        if(qd['choice3']==''):
            return [
                qd['choice1'],
                qd['choice2'],
            ]
        if(qd['choice4']==''):
            return [
                qd['choice1'],
                qd['choice2'],
                qd['choice3']
            ]
        return [
            qd['choice1'],
            qd['choice2'],
            qd['choice3'],
            qd['choice4'],
        ]


    is_correct = models.BooleanField()

    def current_question(self):
        return self.session.vars['questions'][self.round_number - 1]

    def check_correct(self):
        self.is_correct = (self.submitted_answer == self.solution)
