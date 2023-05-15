# Job Tool Store

## Description

This Python program simulates a simple job tool store. The application lists five different jobs, each associated with a specific set of tools (represented by emojis). The user is asked to input the number corresponding to their job, and the program then displays the tools associated with that job.

## How It Works

1. The program starts with an infinite loop, allowing the user to continue selecting jobs and viewing their associated tools indefinitely.

2. It prints a welcome message and then displays a menu of five different jobs: Firefighter, Software engineer, Electrician, Librarian, and Doctor.

3. The user is prompted to enter the number associated with their job.

4. Based on the user's input, the program prints the emojis representing the tools associated with the selected job. For example, if the user enters `1` for Firefighter, the program prints the emojis for a fire truck, a firefighter, and an axe.

5. If the user enters a number that doesn't correspond to any of the listed jobs, the program prints a message: "I have no idea what you do!".

6. After displaying the tools for the selected job (or the 'no idea' message), it prints a line of dashes to visually separate this selection from the next.

## Notes

This program is a simple demonstration of Python's `while` loop and `if`-`elif`-`else` conditional statements. It does not currently handle non-numeric input or provide an exit condition for the loop. As a result, the program continues running until it's manually interrupted. To make this program more robust, you might consider adding error checking for non-numeric input and providing a way for the user to exit the loop.