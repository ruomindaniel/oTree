from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Question(Page):
    pass

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Question, Results]
