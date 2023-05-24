questions = [
    "What is the capital of France?",
    "What is the largest planet in our solar system?",
    "In which year did World War II end?",
    "What is the chemical symbol for the element gold?",
    "What is the capital of Pakistan?"
]

options = [['Rome', 'Paris', 'Berlin', 'London'],
 ['Saturn', 'Neptune', 'Mars', 'Jupiter'],
 ['1939', '1950', '1945', '1918'],
 ['Fe', 'Au', 'Cu', 'Ag'],
 ['Karachi', 'Lahore', 'Islamabad', 'Peshawar']
 ]


answers = [
    "Paris",
    "Jupiter",
    "1945",
    "Au",
    "Islamabad"
]

score = 0
n=int(input("Are you ready to start quiz?\nType 1 "))
if n==1:
    while True:
        x = input(f"\n{questions[0]}\nFour choices are: {options[0]} \nType your answer here: ")
        if x.capitalize()==answers[0]:
            print("\nRight Answer\nGreat!")
            score = score+1
            print("Your score is: ",score)
        else:
            print("\nWrong Answer\nTry Again!")
            print("The correct answer is: ",answers[0])
            score = score-1
            print("Your score is: ",score)

        x = input(f"\n{questions[1]}\nFour choices are: {options[1]} \nType your answer here: ")
        if x.capitalize()==answers[1]:
            print("\nRight Answer\nGreat!")
            score = score+1
            print("Your score is: ",score)
        else:
            print("\nWrong Answer\nTry Again!")
            print("The correct answer is: ",answers[1])
            score = score-1
            print("Your score is: ",score)

        x = input(f"\n{questions[2]}\nFour choices are: {options[2]} \nType your answer here: ")
        if x.capitalize()==answers[2]:
            print("\nRight Answer\nGreat!")
            score = score+1
            print("Your score is: ",score)
        else:
            print("\nWrong Answer\nTry Again!")
            print("The correct answer is: ",answers[2])
            score = score-1
            print("Your score is: ",score)

        x = input(f"\n{questions[3]}\nFour choices are: {options[3]} \nType your answer here: ")
        if x.capitalize()==answers[3]:
            print("\nRight Answer\nGreat!")
            score = score+1
            print("Your score is: ",score)
        else:
            print("\nWrong Answer\nTry Again!")
            print("The correct answer is: ",answers[3])
            score = score-1
            print("Your score is: ",score)

        x = input(f"\n{questions[4]}\nFour choices are: {options[4]} \nType your answer here: ")
        if x.capitalize()==answers[4]:
            print("\nRight Answer\nGreat!")
            score = score+1
            print("Your score is: ",score)
            print(f"\nYou have earned {score} points out of 5")
            break
        else:
            print("\nWrong Answer\nTry Again!")
            print("The correct answer is: ",answers[4])
            score = score-1
            print("Your score is: ",score)
            print(f"\nYou have earned {score} points out of 5")
            break

else:
    print("Type valid key to start")
    
            


