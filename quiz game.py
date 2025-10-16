questions = [
    {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "answer": "Mars"
    },
    {
        "question": "What is 2 + 2?",
        "answer": "4"
    }
]

def run_quiz():
    score = 0
    total = len(questions)
    
    print("Welcome to the Quiz Game!")
    print("------------------------")
    
    for q in questions:
        answer = input(q["question"] + " ")
        if answer.lower() == q["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}")
    
    print(f"\nYou got {score} out of {total} questions correct!")
    percentage = (score / total) * 100
    print(f"Your score: {percentage}%")

run_quiz()