students_scores = input().split()
for i  in range(0, len(students_scores)):
    students_scores[i] = int[students_scores[i]]    

highest_score = 0
for score  in students_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")

