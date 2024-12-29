# new_dict = {new_key:new_value for item in list}  # Dict comp basit hali
# new_dict = {new_key:new_value for (key,value) in dict.items()}  # Başka bir sözlükten verileri
# alıp yeni bir sözlüğe aktarabiliriz


# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

import random

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
students_scores = {student: random.randint(1, 100) for student in names}
passed_students = {student: score for (student, score) in students_scores.items() if score >= 50}
print("Students Scores: ", students_scores)
print("Passed Students: ", passed_students)
