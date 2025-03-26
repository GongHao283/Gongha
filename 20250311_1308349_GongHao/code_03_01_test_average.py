# This program gets three test score and display their average
# If score is greater than high score, then provide congratuation message

# Set high score
high_score = 95
# Get test score 1
score1 = int(input("Enter the first test score:"))
# Get test score 2
score2 = int(input("Enter the second test score:"))
# Get test score 3
score3 = int(input("Enter the third test score:"))
# Calculate the average of the three score
average = (score1 + score2 + score3) / 3
# Test the average score is greater than high_score
# Display "Congratulation!" message with unser's average score
if average > high_score:
    print("Congratulation!")
    print(f"Your average score is {average:.2f}")
else:
    print(f"Your average score is {average:.2f}")
# Eng program