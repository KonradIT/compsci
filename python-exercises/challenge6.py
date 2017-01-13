"""
Create a game which displays 3 questions, one at a time and each with four possible answers.
The questions are chosen randomly by the program from a set of 5 (this can be expanded later).
At the end of the game, the total number of correct answers will be displayed to the player.

EXTENSIONS
The game provides competition between multiple players
Players are given a time limit to answer a question and if are out of time will loss out on a point
Players are given/deducted points depending on how quickly/accurately they answer their questions

Syllabus Check: Functions/procedures, parameters, variables, constants
"""

"""
MIT License:
Copyright 2017 Konrad Iturbe
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import random
#variables:
questionCount=0
questionArray =["Who is/was the President of the United States of America during 2017 - 2025?","In what year was YouTube founded?","Where was the first iPhone unveiled?","What is the capital of Uganda?", "What is 38^7-100 ?"]
answersArray=[["A: Gordon Ramsey","B: Donald J. Trump","C: Leonardo DiCaprio","D: Rick Astley"],["A: 1969","B: 2016","C: 2006","D: 2005"],["A: Helsinki","B: New York","C: San Francisco","D: Miami"],["A: Freetown","B: Nairobi","C: Kigali","D: Kampala"],["A: 215526793728","B: 114415582492","C: 114415582491","D: 114415586492"]]
print("Question Game")
while questionCount != 3:
     questionCount += 1
     questionRandom=random.randint(1,3)
     print(questionArray[questionRandom])
     print(answersArray[questionRandom])
     answer=input("Enter your answer: ")
     if answer in answersArray[questionRandom]:
         print("Correct!!")
