name = input("What is your name? ")
birth_year = int(input("What year were you born in? "))

teen_year = birth_year + 13
drive_year = birth_year + 16
grad_8th_grade = birth_year + 14
grad_high_school = birth_year + 18
job_year = birth_year + 22
old_year = birth_year + 100

print(f"Hello, {name} here is your life story. . .")
print("👇" * 80)

print(f"You will be a teenager in {teen_year} 🍟.")
print(f"You will learn to drive a 🚙 in {drive_year}.")
print(f"You will graduate high school in {grad_high_school} 👩🏽‍🎓.")
print(f"You will get a job in {job_year} 👩🏻‍💼.")
print(f"You will be old in {old_year} 👴🏼.")
print("👆" * 80)
print("Good luck, with that!")