def quiz_game():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
            "answer": "C"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
            "answer": "B"
        },
        {
            "question": "Who wrote 'Hamlet'?",
            "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Jane Austen", "D) Mark Twain"],
            "answer": "B"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["A) Atlantic", "B) Indian", "C) Arctic", "D) Pacific"],
            "answer": "D"
        },
        {
            "question": "Which element has the chemical symbol 'O'?",
            "options": ["A) Oxygen", "B) Gold", "C) Silver", "D) Iron"],
            "answer": "A"
        }
    ]

    score = 0

    print("Welcome to the Quiz Game!\n")

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        user_answer = input("Enter your answer (A, B, C, or D): ").upper()

        if user_answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}\n")

    print(f"Quiz Over! Your final score is: {score}/{len(questions)}")

# Run the quiz game
quiz_game()

