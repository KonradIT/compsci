import random

m = 3 # number of questions
n = 3 # number of players

class Question():
    """question with answers"""

    def __init__(self, question, answers, correct):
        self.question = question
        self.answers = answers
        self.correct = correct

    def ask(self):
        """print question and possible answers"""
        print("\n" + self.question + "\n")
        for i in range(len(self.answers)):
            print("\t" + str(i+1) + ". " + self.answers[i])

    def check(self, response):
        """check possible response with actual answer"""
        if self.answers[response] == self.answers[self.correct]:
            print("\nCorrect!\n+1 point")
            return(1)
        else:
            print("\nIncorrect!")
            return(0)

Q1 = Question("Which The Legend of Zelda game has the fewest dungeons?",
                ["A Link to The Past", "Skyward Sword", "Majora's Mask",
                    "Minish Cap"], 2)

Q2 = Question("Which weapon does the fewest damage in CSGO?",
                ["Glock 18", "PP-Bizon", "USP-S", "Dual Berettas"], 1)

Q3 = Question("How many tracks are there in Mario Kart 64?",
                ["12", "20", "18", "16"], 3)

Q4 = Question("Which meme is Gabe the dog known for?",
                ["Advice Dog", "Bork", "Doge", "This is fine"], 1)

Q5 = Question("Which is not the name of a Pokémon?",
                ["Voltaile", "KlingKlang", "Luvdisc", "Lampent"], 0)

questionLib = [Q1, Q2, Q3, Q4, Q5]
quiz = random.sample(questionLib, m)
scores = [0] * n

for q in quiz:
    q.ask()
    responses = []
    print()
    for i in range(n):
        responses.append(int(input("Player " + str(i+1) + ", enter response: ")) - 1)
    for i in range(n):
        scores[i] += q.check(responses[i])

print("\n *** SCORE TIME *** ")
for i in range(n):
    maxScore = max(scores)
    maxPosition = scores.index(maxScore)
    print("", (i+1), "- player", (maxPosition+1), "score:", maxScore)
    scores[maxPosition] = -1
print(" ****************** ")
