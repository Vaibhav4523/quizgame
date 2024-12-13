
# Questions for the quiz
questions = ("1. What is the first programming language? ", 
            "2. What is the full form of RAM? ", 
            "3. What is the size of 1 byte in bits? ")

# Options for the questions
options = (("A. C Language","B. Assembly","C. Python","D. C++"),
          ("A. Random Access Memory","B. Read Access Memory","C. Random Assign Memory","D. Read Only Memory"),
          ("A. 14","B. 6","C. 4","D. 8"))

# Correct answers
answer = ("B", "A", "D")

# Variables

guesses = []
score = 0
question_number = 0

# Looping through the questions

for question in questions:
    print("-----------------------Questions And Options-------------------------")
    print(question)
    
# Displaying the options
    
    for option in options[question_number]:
        print(option)
        
# Getting the user's input
    
    guess = input("Enter your option(A,B,C,D): ").upper()
    guesses.append(guess)


# Checking the answer

    if guess.upper() == answer[question_number]:
        score += 1
        print("Correct Answer!")
# If the answer is wrong, display the correct answer
    else:
        print("Wrong Answer!")
        print(f"{answer[question_number]} is the correct answer.")

# Moving to the next question
        
    question_number += 1
    
    
# Displaying the final score
print("-----------------------Final Score-------------------------")
# Displaying the score
print(f"Your score is {score} out of {len(questions)}")

# Displaying the answers given by the user
print("-----------------------Your Answers-------------------------")
print(guesses)

# Displaying the correct answers
print("-----------------------Correct Answers-------------------------")
print(answer)

