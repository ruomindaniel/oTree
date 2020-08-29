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
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'pay_secrecy'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def set_roles(self):
        players = self.get_players()
        all_num = [p.correct_ans for p in players]
        max_num = max(all_num)
        for p in players:
            if p.correct_ans == max_num:
                p.firm_role = 'manager'

        roles = ['Employee A','Employee B','Employee C']

        for p in players:
            if p.firm_role != 'manager':
                index = random.randint(0,100) % len(roles)
                p.firm_role = roles[index]
                roles.pop(index)



def make_field():
    return models.IntegerField()

class Player(BasePlayer):
    correct_ans = models.IntegerField(initial = 0);
    firm_role = models.StringField();

    member0 = make_field()
    member1 = make_field()
    member2 = make_field()
    member3 = make_field()
    member4 = make_field()
    member5 = make_field()
    member6 = make_field()
    member7 = make_field()
    member8 = make_field()
    member9 = make_field()
    member10 = make_field()
    member11 = make_field()
    member12 = make_field()
    member13 = make_field()
    member14 = make_field()
    member15 = make_field()
    member16 = make_field()
    member17 = make_field()
    member18 = make_field()
    member19 = make_field()
    member20 = make_field()
    member21 = make_field()
    member22 = make_field()
    member23 = make_field()
    member24 = make_field()
    member25 = make_field()
    member26 = make_field()
    member27 = make_field()
    member28 = make_field()
    member29 = make_field()

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

    question3 = models.IntegerField(
        label = "3. If Employee A chooses an effort level of 20, his/her firm output will increase by:",
        widget=widgets.RadioSelect,
        choices=[[1, "a.    20 units"],
                 [2, "b.    80 units"],
                 [3, "c.    100 units"],
                 [4, "d.    160 units"]]
    )

    question4 = models.IntegerField(
        label = "4. If Employee C chooses an effort level of 20, his/her firm output will increase by:",
        widget=widgets.RadioSelect,
        choices=[[1, "a.    20 units"],
                 [2, "b.    80 units"],
                 [3, "c.    100 units"],
                 [4, "d.    160 units"]]
    )

    question5 = models.IntegerField(
        label = "5. If each of the three employees chooses an effort level of 20 points, the total firm output will be:",
        widget=widgets.RadioSelect,
        choices=[[1, "a.    240 units"],
                 [2, "b.    300 units[show the computation when an answer is submitted, whether it is right or wrong: 20*5+20*5+20*5=300 points]"],
                 [3, "c.    360 units"],
                 [4, "d.    None of the above"]]
    )

    question6 = models.IntegerField(
        label = "6. The Manager will receive a higher bonus when the firm output is 360 units than when it is 240 units. ",
        widget=widgets.RadioSelect,
        choices=[[1, "a.    True because the Manager’s bonus is proportional to the firm output"],
                 [2, "b.    False because the Manager’s bonus is fixed and will not vary regardless of the firm output level"]]
    )

    question7 = models.IntegerField(
        label = "7. [Pay Transparent Conditions] If the firm output is 360, the total employee bonus pool will contain:",
        widget=widgets.RadioSelect,
        choices=[[1, "a.    30 points"],
                 [2, "b.    54 points (pay transparent condition) [show the computation when an answer is submitted, whether it is right or wrong: 360*15%=54 points]"],
                 [3, "c.    144 points"],
                 [4, "d.    Not enough information "]]
    )

    question8 = models.IntegerField(
        label = "8. [Pay Secret Conditions] The higher the firm output, the bigger the employee bonus pool will be:",
        widget=widgets.RadioSelect,
        choices=[[1, "a.    True"],
                 [2, "b.    False"]]
    )

    question9 = models.IntegerField(
        label = "9. Suppose an employee’s ability is 5 and she chooses an effort level of 8. With the effect of an uncontrollable shock, her final output is 50. How much individual bonus will this employee receive in this period?   ",
        widget=widgets.RadioSelect,
        choices=[[1, "a.    40 points"],
                 [2, "b.    6 points"],
                 [3, "c.    7.5 points [show the computation when an answer is submitted, whether it is right or wrong: 50*15%=7.5 points]"],
                 [4, "d.    50 points"]]
    )

    question10 = models.IntegerField(
        label = "10.    Suppose an employee’s ability is 5 and she chooses an effort level of 8. With the effect of an uncontrollable shock, her final output is 50. Besides the individual bonus, she is also allocated 14 points from the employee bonus pool. What would be her total earnings for that period (including the initial balance of 20 points he/she gets each period)?",
        widget=widgets.RadioSelect,
        choices=[[1, "a.    33.5 points [show the computation when an answer is submitted, whether it is right or wrong: 20-8+7.5+14 = 33.5 points]"],
                 [2, "b.    14 points"],
                 [3, "c.    21.5 points"],
                 [4, "d.    26 points"]]
    )

    question11 = models.IntegerField(
        label = "11.    Which of the following about the employee bonus pool is true?",
        widget=widgets.RadioSelect,
        choices=[[1, "a.    It is distributed equally among the three employees in the firm"],
                 [2, "b.    It is entirely up to the three employees in the firm to determine how to distribute it among the three employees"],
                 [3, "c.    It is entirely up to the Manager to determine how to distribute it among the three employees"]]
    )

    question12 = models.IntegerField(
        label = "12.    Which of the following about the employee bonus pool is true?",
        widget=widgets.RadioSelect,
        choices=[[1, "a.    Both the Manager and the employees will know the exact size of the employee bonus pool. (pay transparent condition) "],
                 [2, "b.   Only the Manager knows the exact size of the employee bonus pool. (pay secret condition)"],
                 [3, "c.    Only the employees know the exact size of the employee bonus pool."]]
    )

    question13 = models.IntegerField(
        label = "13.    Which of the following about uncontrollable shocks is true?",
        widget=widgets.RadioSelect,
        choices=[[1, "a.    The manager AND employees are both informed the exact effect of the uncontrollable shocks"],
                 [2, "b.    Only the manager is informed about the exact effect of the uncontrollable shocks"],
                 [3, "c.    Only the affected employees themselves know the exact effect of the uncontrollable shocks"]]
    )

    question14 = models.IntegerField(
        label = "14. Which of the following about the distribution of employee bonus is true?",
        widget=widgets.RadioSelect,
        choices=[[1, "a.    Employees will find out how the Manager distributes the employee bonus to EACH of the three employees (pay transparent condition) "],
                 [2, "b.    Employees will only know their own bonus amount, but not other employees’ bonus amount (pay secret condition) "]]
    )

    question15 = models.IntegerField(
        label = "15. Will the Manager must allocate ALL bonus in the employee bonus pool to the three employees each period?",
        widget=widgets.RadioSelect,
        choices=[[1, "a.    True"],
                 [2, "b.    False"]]
    )

    def clear_slider_answer(self):
        self.correct_ans = 0

    def check_slider_answer(self):
        slider_answers = [self.member0, self.member1, self.member2, self.member3, self.member4, self.member5, self.member6, self.member7, self.member8, self.member9,
                        self.member10, self.member11, self.member12, self.member13, self.member14, self.member15, self.member16, self.member17, self.member18, self.member19,
                        self.member20, self.member21, self.member22, self.member23, self.member24, self.member25, self.member26, self.member27, self.member28, self.member29]
        for i in range(len(slider_answers)):
            if(slider_answers[i] == 50):
                self.correct_ans = self.correct_ans + 1

    def role(self):
        # all_num = [p.correct_ans for p in self.group.get_players()]
        # max_num = max(all_num)
        if self.firm_role == 'manager':
            # self.firm_role = "manager"
            return 'manager'
        else:
            # self.firm_role = "Employee"
            return 'employee'





            #sort players since we know emplyee randum are position 1,2,3
            # for i in range(len(all_num)-1):
            #     for j in range(i,len(all_num)-1):
            #         if all_num[i] < all_num[i+1]:
            #             #swap
            #             temp = all_num[i+1]
            #             all_num[i+1] = all_num[i]
            #             all_num[i] = temp
            # index = 0
            # for i in range(1,3):
            #     if self.randnum == all_num[i]:
            #         index = i
            #         break
            # if(index == 1):
            #     self.firm_role = "Employee A"
            # elif(index == 2):
            #     self.firm_role = "Employee B"
            # elif(index == 3):
            #     self.firm_role = "Employee C"
            # return 'employee'
