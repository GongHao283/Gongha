# Based on students score, we will give letter grade. Use the fowwing WKU score.
one = 93
two = 90
three = 87
four = 84
five = 80
six = 77
seven = 70
eight = 60

score = int(input("Enter your score:"))
if score >= one:
    print("Your grade is A.")
elif score >= two:
    print("Your grade is A-.")  
elif score >= three:
    print("Your grade is B+.")
elif score >= four:
    print("Your grade is B.")
elif score >= five:
    print("Your grade is B-.")
elif score >= six:
    print("Your grade is C+.")
elif score >= seven:
    print("Your grade is C.")
elif score >= eight:
    print("Your grade is D.")
else:
    print("Your grade is F.")
