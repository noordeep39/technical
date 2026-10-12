# Student Marks Analyzer
# Write a program that accepts the marks obtained by a student in five subjects.
# The program should determine the highest marks, lowest marks, and average marks obtained by the student, and display all three results.

# Variables to Store Highest, Lowest and Average Marks
highestMarks = 0;
lowestMarks = 100;


# Taking Marks for Five Subjects as Input
subject1 = int(input("Enter Marks for Subject 1: ")); #bug=typecasddting from string to int
subject2 = int(input("Enter Marks for Subject 2: "));#bug=typecasddting from string to int
subject3 =int(input("Enter Marks for Subject 3: "));#bug=typecasddting from string to int
subject4 = int(input("Enter Marks for Subject 4: "));#bug=typecasddting from string to int
subject5 = int(input("Enter Marks for Subject 5: "));#bug=typecasddting from string to int



# Finding the Highest Marks
if highestMarks < subject1:
    highestMarks = highestMarks + subject1;

elif highestMarks < subject2: #after if there is  elif
    highestMarks = highestMarks + subject2;

elif highestMarks < subject3:#after if there is  elif
    highestMarks = highestMarks + subject3;

elif highestMarks < subject4:#after if there is elif
    highestMarks = highestMarks + subject4;

elif highestMarks < subject5:#after if there is elif
    highestMarks = highestMarks + subject5;




# Finding the Lowest Marks
if lowestMarks < subject1:
    lowestMarks = subject1;

if lowestMarks < subject2:
    lowestMarks = subject2;

if lowestMarks < subject3:
    lowestMarks = subject3;

if lowestMarks < subject4:
    lowestMarks = subject4;

if lowestMarks < subject5:
    lowestMarks = subject5;



# Calculating the Average Marks
avg = subject1 + subject2 + subject3 + subject4 + subject5 / 5;

# Displaying the Results
print(f"Highest: {highestMarks}");
print(f"Lowest: {lowestMarks}");
print(f"Average: {avg}");