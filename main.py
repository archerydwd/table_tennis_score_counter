import RPi.GPIO as GPIO
import pyttsx, time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

team_1_pin = 25
team_2_pin = 24
GPIO.setup(team_1_pin, GPIO.IN)
GPIO.setup(team_2_pin, GPIO.IN)

engine = pyttsx.init()
engine.runAndWait()


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
	global engine
	self.engine = engine
        self.team_1 = Team()
        self.team_2 = Team()

    def increment_team_1(self):
        score1 = self.team_1.get_score()
        score2 = self.team_2.get_score()
        if score1 == 9 and score2 == 10:
            self.deuce()
            self.engine.say('Deuce')
	    print "Deuce"
        elif score1 == 10 and score2 == 11:
            self.deuce()
            self.engine.say('Deuce')
	    print "Deuce"
        elif score1 == 10 and score2 == 10:
            self.team_1.increment_score()
            self.engine.say('Advantage team 1')
	    print "Advantage team 1"
        elif score1 == 10 and score2 < 10:
            self.reset()
            self.engine.say('Team 1 wins')
	    print "Team 1 wins"
        elif score1 == 11:
            self.team_1.increment_score()
            self.reset()
            self.engine.say('Team 1 wins')
	    print "Team 1 wins"
        elif score1 < 10:
            self.team_1.increment_score()
	    self.engine.say(str(self.team_1.get_score()) + ", " + str(self.team_2.get_score()))
	    print str(self.team_1.get_score()) + ", " + str(self.team_2.get_score())

    def increment_team_2(self):
        score1 = self.team_2.get_score()
        score2 = self.team_1.get_score()
        if score1 == 9 and score2 == 10:
            self.deuce()
            self.engine.say('Deuce')
	    print "Deuce"
        elif score1 == 10 and score2 == 11:
            self.deuce()
            self.engine.say('Deuce')
	    print "Deuce"
        elif score1 == 10 and score2 == 10:
            self.team_2.increment_score()
            self.engine.say('Advantage team 2')
	    print "Advantage team 2"
        elif score1 == 10 and score2 < 10:
            self.reset()
            self.engine.say('Team 2 wins')
	    print "Team 2 wins"
        elif score1 == 11:
            self.team_2.increment_score()
            self.reset()
            self.engine.say('Team 2 wins')
	    print "Team 2 wins"
        elif score1 < 10:
            self.team_2.increment_score()
	    self.engine.say(str(self.team_1.get_score()) + ", " + str(self.team_2.get_score()))
	    print str(self.team_1.get_score()) + ", " + str(self.team_2.get_score())

    def deuce(self):
        self.team_1.set_score(10)
        self.team_2.set_score(10)

    def reset(self):
        self.team_1.set_score(0)
        self.team_2.set_score(0)

game = Game()

while True:
    if not GPIO.input(team_1_pin):
        game.increment_team_1()
        engine.runAndWait()
    elif not GPIO.input(team_2_pin):
        game.increment_team_2()
    time.sleep(0.5)
    game.engine.runAndWait()

