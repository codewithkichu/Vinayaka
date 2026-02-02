#Online Exam Evaluation System

# Correct answers
correct_answers = ['A', 'C', 'B', 'D', 'A']
student_answers = []

# Function to validate answers
def validate_answers():
    print("\nEnter your answers (A/B/C/D):")
    for i in range(len(correct_answers)):
        ans = input(f"Q{i+1}: ").upper()
        while ans not in ['A', 'B', 'C', 'D']:
            print("❌ Invalid choice! Enter A/B/C/D only.")
            ans = input(f"Q{i+1}: ").upper()
        student_answers.append(ans)
    print("✅ Answers submitted successfully!")

# Function to calculate score
def calculate_score():
    score = 0
    for i in range(len(correct_answers)):
        if student_answers[i] == correct_answers[i]:
            score += 1
    return score

# Function to generate grade
def generate_grade(score):
    percentage = (score / len(correct_answers)) * 100

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "Fail"

    print("\n📊 Exam Result")
    print("Correct Answers:", score, "/", len(correct_answers))
    print("Percentage:", percentage, "%")
    print("Grade:", grade)

# Main Program
def main():
    validate_answers()
    score = calculate_score()
    generate_grade(score)

# Run program
main()