import RPi.GPIO as GPIO
import pyttsx

engine = pyttsx.init()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

team_1_pin = 25
team_2_pin = 24
GPIO.setup(team_1_pin, GPIO.IN)
GPIO.setup(team_2_pin, GPIO.IN)

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-30)
volume = engine.getProperty('volume')
engine.setProperty('volume', volume+0.25)
engine.setProperty('gender', 'female')

voices = engine.getProperty('voices')
for voice in voices:
    engine.setProperty('voice', voice.id)
    engine.say('The quick brown fox jumped over the lazy dog.')
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
        self.team_1 = Team()
        self.team_2 = Team()

    def increment_team_1(self):
        score1 = self.team_1.get_score()
        score2 = self.team_2.get_score()
        if score1 == 9 and score2 == 10:
            self.deuce()
            engine.say('Deuce')
        elif score1 == 10 and score2 == 11:
            self.deuce()
            engine.say('Deuce')
        elif score1 == 10 and score2 == 10:
            self.team_1.increment_score()
            engine.say('Advantage to team 1')
        elif score1 == 10 and score2 < 10:
            self.reset()
            engine.say('Team 1 wins')
        elif score1 == 11:
            self.team_1.increment_score()
            self.reset()
            engine.say('Team 1 wins')
        elif score1 < 10:
            self.team_1.increment_score()
            if self.team_1.get_score() > self.team_2.get_score():
                engine.say("The score is " + str(self.team_1.get_score()) + ", " + str(self.team_2.get_score()) + " to team 1")
            else:
                engine.say("The score is " + str(self.team_2.get_score()) + ", " + str(self.team_1.get_score()) + " to team 2")


    def increment_team_2(self):
        score1 = self.team_2.get_score()
        score2 = self.team_1.get_score()
        if score1 == 9 and score2 == 10:
            self.deuce()
            engine.say('Deuce')
        elif score1 == 10 and score2 == 11:
            self.deuce()
            engine.say('Deuce')
        elif score1 == 10 and score2 == 10:
            self.team_2.increment_score()
            engine.say('Advantage to team 2')
        elif score1 == 10 and score2 < 10:
            self.reset()
            engine.say('Team 2 wins')
        elif score1 == 11:
            self.team_2.increment_score()
            self.reset()
            engine.say('Team 2 wins')
        elif score1 < 10:
            self.team_2.increment_score()
            if self.team_1.get_score() > self.team_2.get_score():
                engine.say("The score is " + str(self.team_1.get_score()) + ", " + str(self.team_2.get_score()) + " to team 1")
            else:
                engine.say("The score is " + str(self.team_2.get_score()) + ", " + str(self.team_1.get_score()) + " to team 2")

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
    elif not GPIO.input(team_2_pin):
        game.increment_team_2()
    engine.runAndWait()
