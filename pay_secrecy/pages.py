from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class Screen1(Page):
    '''Introduction
    '''
    pass

class Screen2(Page):
    '''Role Explanation
    '''
    pass

class Screen3(Page):
    '''Introduction to the slider bar task: Same for all participants in all conditions
    '''
    pass
class Screen4(Page):
    '''[Practice] Game determining role
    '''
    form_model = 'player'

    form_fields = ['member'+str(i) for i in range(30)]
    def before_next_page(self):
        # self.player.randnum = random.randint(0,100)
        self.player.check_slider_answer()
        print(self.player.correct_ans)

class ResultsWaitPage(WaitPage):
    body_text = "Please wait until all participants have finished their tasks"
    after_all_players_arrive = 'set_roles'

class Screen5(Page):
    '''Announcing role for the practice game
    '''
    def vars_for_template(self):
        role = self.player.role()

        return {
            "role": role,
        }

class Screen6(Page):
    '''Introduction to the slider bar task: Same for all participants in all conditions
    '''
    def before_next_page(self):
        self.player.clear_slider_answer()

class Screen7(Page):
    '''Real Sliding Bar Task
    '''
    timeout_seconds = 60
    form_model = 'player'

    form_fields = ['member'+str(i) for i in range(30)]
    def before_next_page(self):
        # self.player.randnum = random.randint(0,100)
        self.player.check_slider_answer()
        print(self.player.correct_ans)

class MyWaitPage(WaitPage):

    body_text = "Please wait until all participants have finished their tasks"
    after_all_players_arrive = 'set_roles'

class Screen8(Page):
    '''Announcing role for the practice game
    '''

    def vars_for_template(self):
        role = self.player.role()

        return {
            "role": role,
        }

class Screen9(Page):
    '''Ranking information: Same in all conditions
    '''
    def vars_for_template(self):
        role = self.player.firm_role
        group_matrix = self.subsession.get_group_matrix()
        firm_num = 0
        print(group_matrix, group_matrix)
        # determine firm group
        for i in range(len(group_matrix)):
            if self.player in group_matrix[i]:
                firm_num = i + 1
                break
        return {
            "role": role,
            "firm": firm_num,
        }

class Screen10(Page):
    ''' Beginning of Stage Two: all roles and all conditions for Screens 10-15
    '''

class Screen11(Page):
    ''' Employee's Effort Choice, Ability and Output
    '''
class Screen12(Page):
    ''' Uncontrollable Shock to Output
    '''
class Screen13A(Page):
    ''' Employee and Manager Bonuses(Pay Transparent Condition)
    '''
class Screen13B(Page):
    ''' Employee and Manager Bonuses(Pay Transparent Condition)
    '''
class Screen14(Page):
    ''' Performance Feedback
    '''
class Screen15A(Page):
    ''' Bonus distribution
    '''
class Screen15B(Page):
    ''' Bonus distribution
    '''
class Screen16(Page):
    ''' Earnings
    '''
class Screen17(Page):
    ''' Payout of Earnings
    '''
class Screen18(Page):
    ''' Quiz
    '''
    form_model = 'player'
    form_fields = ['question1', 'question2', 'question3', 'question4', 'question5',
                    'question6', 'question7', 'question8', 'question9', 'question10',
                    'question11', 'question12', 'question13', 'question14', 'question15'] # this means all questions
class Results(Page):
    pass


#page_sequence = [Screen1, Screen2, Screen3, Screen4, ResultsWaitPage, Screen5, ResultsWaitPage, Screen6, Screen7, ResultsWaitPage, Screen8, Screen9, Screen10, ResultsWaitPage,Results]
# page_sequence = [Screen6, Screen7, MyWaitPage, Screen8, Screen9, Screen10]
# page_sequence = [Screen10, Screen11, Screen12, Screen13A, Screen13B]
# page_sequence = [Screen14, Screen15A, Screen15B, Screen16, Screen17, Screen18]
page_sequence = [Screen1, Screen2, Screen3, Screen4, ResultsWaitPage, Screen5, ResultsWaitPage,
                    Screen6, Screen7, MyWaitPage, Screen8, Screen9, Screen10,
                    Screen11, Screen12, Screen13A, Screen13B,
                    Screen14, Screen15A, Screen15B, Screen16, Screen17, Screen18]
