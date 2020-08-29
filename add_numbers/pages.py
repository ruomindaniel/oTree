from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class Addnumbers(Page):
    form_model = "player"
    form_fields = ["numbers_entered"]
    def vars_for_template(self):
        a = random.randint(0,10)
        b = random.randint(0,10)
        self.player.number = a + b;
        return {"a":a,
                "b":b,}
    def before_next_page(self):
        if(self.player.number == self.player.numbers_entered):
            self.player.payoff = Constants.win_per_round
            # self.player.total_payoff += 1

class Results(Page):
    pass

class FinalResults(Page):
    def is_displayed(self):
        if self.round_number == Constants.num_rounds:
            return True
        else:
            return False
    def vars_for_template(self):
        all_players = self.player.in_all_rounds()
        combined_payoff = 0
        for player in all_players:
            combined_payoff += player.payoff
        return {
            "combined_payoff": combined_payoff,
        }

page_sequence = [Addnumbers, FinalResults]
