# Based on students score,we will give letter grade. Use the following schema
#A_SCORE = 90
#B_SCORE = 80
#C_SCORE = 70
#D_SCORE = 60
#< 60 = F
A = 90
B = 80
C = 70
D = 60
# Get a score
score = int(input("Enter your score:"))
# Determine the grade
if score >= A:
    print("Your grade is A.")
elif score >= B:
    print("Your grade is B.")  
elif score >= C:
    print("Your grade is C.")
elif score >= D:
    print("Your grade is D.")
else:
    print("Your grade is F.")