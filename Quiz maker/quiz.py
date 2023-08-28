quiz = {
      "Question1": {
            "question": "What is 1 + 3? ",
            "answer": 4
      },
      "Question2": {
            "question": "What is 1 * 3? ",
            "answer": 3
      },
      "Question3": {
            "question": "What is 5 + 3? ",
            "answer": 8
      },
      "Question4": {
            "question": "What is 9 / 3? ",
            "answer": 3
      },
      "Question5": {
            "question": "What is 55 - 3? ",
            "answer": 52
      }
}

score = 0

for key, value in quiz.items():
      print(value["question"])
      answer = int(input("What is answer? "))
      
      
     
 
      if answer == value["answer"] :
            print("Correct!!")
            score = score + 1
            print(f"Your score is {score}")
            print("")
                  
                  
      else:
            print("Wrong!!! )")
            print(f"The answer is: {value['answer']}")
            print(f"Your score is: {score}")
            print("")
                  
            
            
print(f"You got {score} out of 5 questions correcly!!")
print(f"Your percentage is {int(score/5 *100)}%")            