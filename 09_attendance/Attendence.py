#!/usr/bin/env python3
print("Welcome to Classroom Attendance.")
print("⎯"*79)
students = ["Raina", "Alyson", "Kiana", "Coleen", "Isabella", "Hazel", "Izzy", "Jack", "Rory"]

number_present = 0
number_absent = 0

for student in students:
	answer = input(f"Is {student} here? (y/n): ")
	
	if answer == "y":
		number_present = number_present + 1
	else:
		number_absent = number_absent + 1

all_students = number_absent + number_present

print(f"{number_present}/{all_students} students are here and {number_absent}/{all_students} students are absent today.")		

if number_present > number_absent:
	print("📚 More than half the students are here today. 📚")
else:
	print("🦠 Less than half the students are here today. 🦠")