students_heights = input().split()
for i in range(0, len(students_heights)):
    students_heights[i] = int(students_heights[i])

total_height = 0
for height  in students_heights:
    total_height += height
average_height = total_height / len(students_heights)   
print(f"Total height: {total_height}")
print("Average Height is :", average_height)

numberOfStudent = 0
for  student in students_heights:
    numberOfStudent += 1
print(f"The number of students: {numberOfStudent}")
