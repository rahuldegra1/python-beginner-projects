
question1 = { 
    "question": "What is the chemical symbol for gold on the periodic table?",
    "options": ["Ag", "Au", "Pb", "Fe"],
    "answer": "Au"
}
question2 = { 
    "question": "What is the capital city of Australia?",
    "options": ["sydney", "Melbourne", "delhi", "canberra"],
    "answer": "canberra"
}
question3 = { 
    "question": "Excluding the polar regions, which is the largest desert in the world?",
    "options": ["gobi desert", "arabian desert", "sahara desert", "kalahari desert"],
    "answer": "sahara desert"
}
question4 = { 
    "question": "Which acclaimed director is known for his work on the mind-bending films Inception, Interstellar, and Oppenheimer?",

    "options": ["steave spielberg", "quentin tarantino", "martin scorsese", "christopher nolan"],
    "answer": "christopher nolan"
}
questions = [question1, question2, question3, question4]
score = 0

      
for question in questions:
    print(question["question"])
    for option in question["options"]:
        print(option)
    user = input("your answer: ")

    if user.lower() == question["answer"].lower():
        print("correct!")
        score += 1
    else:
        print("Wrong. The answer was", question["answer"])
        
print(f"you scored {score} out of {len(questions)}")