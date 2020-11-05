from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'quiz'
    players_per_group = None
    num_rounds = 3

    question1 = models.IntegerField(
        label = "1. Which of the following is true?",
        widget=widgets.RadioSelect,
        choices=[[1, "a.    I will be on the same firm throughout the entire experiment session and my identity will be revealed to others"],
                 [2, "b.    I will be on the same firm throughout the entire experiment session and my identity will not be revealed to others"],
                 [3, "c.    I will not be on the same firm throughout the entire experiment session and my identity will be revealed to others"],
                 [4, "d.    I will not be on the same firm throughout the entire experiment session and my identity will not be revealed to others"]]
    )

    question2 = models.IntegerField(
        label = "2.     My role will remain constant throughout the experiment session.  That is, if I am a manager in Period 1, I will be a manager in all subsequent periods.  Likewise, if I am Employee A in Period 1, I will be Employee A in all subsequent periods.",
        widget=widgets.RadioSelect,
        choices=[[1, "True"],
                 [2, "False"]]
    )

    questions = [question1, question2]

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            self.session.vars['questions'] = Constants.questions.copy()

class Group(BaseGroup):
    pass


class Player(BasePlayer):

    submitted_answer = models.IntegerField(widget = widgets.RadioSelect)

    def submitted_answer_choices(self):
        qd = self.current_question()
        return [
            qd['choice1'],
            qd['choice2'],
            qd['choice3'],
            qd['choice4'],
        ]

    def current_question(self):
        return self.session.vars['questions'][self.round_number - 1]

