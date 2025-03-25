# Get three test scores and calculate the total and average with proper message
score1 = float(input("Enter the first test score:"))
score2 = float(input("Enter the second test score:")) 
score3 = float(input("Enter the third test score:"))
total = score1 + score2 + score3
print(f"The total score is {total}")
average = total / 3
print(f"The average score is {average:.2f}")