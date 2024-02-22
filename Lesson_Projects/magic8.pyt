#A magic 8-ball who will give you an answer to all life's questions

import random

#Declare starting variables

name = "Collin"
question = "Do dinosaurs still live??"
answer = ""
random_number = random.randint(1,9)

# the meaning of life question

if question == "What is the meaning of life?":
  random_number = 10


# potential answers with conditionals
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say so"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "42"
else:
  answer = "Error"

# return answer
print(name, " asks: ", question)
print("Magic 8-Ball's answer: ", answer)