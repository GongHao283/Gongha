# You have to write a program that determine whether you will accept loan application or reject. You will determine acceptence based on annual salary and year of work. Acceptance standard is annual salary >= 500,000 yuan and >= 5 year of work in current work
# But this time you have to tell them why their application has rejected and tell them how much salary or tear of work or  both salary and year of work needed more.
annual_salary = int(input("Enter your annual salary:"))
year_work = int(input("Enter your year of work:"))

if annual_salary >= 500000:
    if year_work >= 5:
        print("Your application is accepted.")
    else:
        print("Sorry, your year work is not qualified, so your application is rejected.")
else:
    if year_work >=5:    
        print("Sorry, your anuual salary is not qualified, so your application is rejected.")
    else:
        print("Sorry, both of your annual salary and year work are not qualified, so your application is rejected.")