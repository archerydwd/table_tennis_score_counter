import RPi.GPIO as GPIO
import time, os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

button_pin = 25
GPIO.setup(button_pin, GPIO.IN)


class Team:
    score = 0

    def __init__(self):
        self.score = 0

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score

    def increment_score(self):
        self.score += 1


class Game:
    team_1 = Team()
    team_2 = Team()

    def __init__(self):
        self.team_1 = Team()
        self.team_2 = Team()

    def increment_team_1(self):
        score1 = self.team_1.get_score()
        score2 = self.team_2.get_score()
        if score1 == 9 and score2 == 10:
            self.deuce()
            print "deuce"
        elif score1 == 10 and score2 == 11:
            self.deuce()
            print "deuce"
        elif score1 == 10 and score2 == 10:
            self.team_1.increment_score()
            print "advantage to team 1"
        elif score1 == 10 and score2 < 10:
            self.reset()
            print "team 1 win"
        elif score1 == 11:
            self.team_1.increment_score()
            self.reset()
            print "team 1 win"
        elif score1 < 10:
            self.team_1.increment_score()
            print "team 1: " + str(self.team_1.get_score()) + " team 2: " + str(self.team_2.get_score())

    def increment_team_2(self):
        score1 = self.team_2.get_score()
        score2 = self.team_1.get_score()
        if score1 == 9 and score2 == 10:
            self.deuce()
            print "deuce"
        elif score1 == 10 and score2 == 11:
            self.deuce()
            print "deuce"
        elif score1 == 10 and score2 == 10:
            self.team_2.increment_score()
            print "advantage to team 2"
        elif score1 == 10 and score2 < 10:
            self.reset()
            print "team 2 win"
        elif score1 == 11:
            self.team_2.increment_score()
            self.reset()
            print "team 2 win"
        elif score1 < 10:
            self.team_2.increment_score()
            print "team 2: " + str(self.team_2.get_score()) + " team 1: " + str(self.team_1.get_score())

    def deuce(self):
        self.team_1.set_score(10)
        self.team_2.set_score(10)

    def reset(self):
        self.team_1.set_score(0)
        self.team_2.set_score(0)

game = Game()

# if team 1 button pressed
#       increment_team_1
# else team 2 button pressed
#       increment_team_2
# else reset button pressed
#       reset()

while True:
    if not GPIO.input(button_pin):
        print "button pressed"
        time.sleep(1)
    else:
        os.system('clear')
        print "waiting for you to press the button"


