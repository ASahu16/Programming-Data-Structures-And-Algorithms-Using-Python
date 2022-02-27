'''
Course outline
How does an NPTEL online course work?
Week 1 : Introduction
Week 1 Quiz
Week 2: Basics of Python
Week 2 Quiz
Week 2 Programming Assignment
Week 3: Lists, inductive function definitions, sorting
Week 3 Programming Assignment
Week 4: Sorting, Tuples, Dictionaries, Passing Functions, List Comprehension
Week 4 Quiz
Week 4 Programming Assignment
Week 5: Exception handling, input/output, file handling, string processing
Week 5 Programming Assignment
Week 5 Programming Assignment
Not Started
Week 6: Backtracking, scope, data structures; stacks, queues and heaps
Text Transcripts
Books
Download Videos
 
Week 5 Programming Assignment
Due on 2022-03-03, 23:59 IST
For this assignment, you have to write a complete Python program. Paste your code in the window below.

You may define additional auxiliary functions as needed.
In all cases you may assume that the input to your program has the expected format, so your program does not have to check for malformed inputs.
There are some public test cases and some (hidden) private test cases.
"Compile and run" will evaluate your submission against the public test cases.
"Submit" will evaluate your submission against the hidden private test cases. There are 6 private test cases, with equal weightage. You will get feedback about which private test cases pass or fail, though you cannot see the actual test cases.
Ignore warnings about "Presentation errors".
The academic office at the Hogwarts School of Witchcraft and Wizardry has compiled data about students' grades. The data is provided as text from standard input in three parts: information about courses, information about students and information about grades. Each part has a specific line format, described below..

Information about courses
Line format: Course Code~Course Name~Semester~Year~Instructor
Information about students
Line format: Roll Number~Full Name
Information about grades
Line format: Course Code~Semester~Year~Roll Number~Grade
The possible grades are A, AB, B, BC, C, CD, D with corresponding grade points 10, 9, 8, 7, 6, 5 and 4. The grade point average of a student is the sum of his/her grade points divided by the number of courses. For instance, if a student has taken two courses with grades A and C, the grade point average is 8.50 = (10+7)÷2. If a student has not completed any courses, the grade point average is defined to be 0.

You may assume that the data is internally consistent. For every grade, there is a corresponding course code and roll number in the input data.

Each section of the input starts with a line containing a single keyword. The first section begins with a line containing Courses. The second section begins with a line containing Students. The third section begins with a line containing Grades. The end of the input is marked by a line containing EndOfInput.

Write a Python program to read the data as described above and print out a line listing the grade point average for each student in the following format:
> Roll Number~Full Name~Grade Point Average

Your output should be sorted by Roll Number. The grade point average should be rounded off to 2 digits after the decimal point. Use the built-in function round().

'''
# Task_1: Read student data
# Task_2: Sort according to roll number, and we can also bundle grades together in this step
# Task_3: Calculate the average
# Task_4: Print the output


students = [] # list to store the students data              
grade = [] # list to store the students grade data 


# function to take the input of the string
def get_student_data_input():
    data = input()
    while data != 'Grades':
        data = data.split('~')
        data.append(0)   # appending 0 as the grade marks
        students.append(data)
        data = input()


# function to take the grades of the students
def get_grade_data_input():
    data = input()
    while data != 'EndOfInput':
        data = data.split('~')
        data = data[len(data)-2:]
        grade.append(data)
        data = input()


def get_grade_point(grade):
    if grade == 'A':
        return 10
    elif grade == 'AB':
        return 9
    elif grade == 'B':
        return 8
    elif grade == 'BC':
        return 7
    elif grade == 'C':
        return 6
    elif grade == 'CD':
        return 5
    else:
        return 4


def calculate_avg():
    global students, grade
    for i in students:   # i is a list containg the name and roll of a student
        j = 0
        sum = 0
        while j < len(grade):
            if i[0] == grade[j][0]:     # if the roll matchs
                sum += get_grade_point(grade[j][1])
                grade.pop(j)
                i[2] += 1
            else:
                j += 1
        if sum != 0:
            i[2] = round(sum/i[2], 2)
        print(i[0],'~',i[1],'~', i[2], sep='')


# main function starts here
x = input()
# Initial inputs for the course can be ignored
while x != 'Students':           
    x = input()
get_student_data_input()
students.sort()
get_grade_data_input()
calculate_avg()
