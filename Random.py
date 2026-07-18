import random 

student_1 = (str(input('first sudent:')))
student_2 = (str(input('second student:')))
student_3 = (str(input('third student:')))
student_4 = (str(input('fourth student:')))
student_5 = (str(input('fifth student:')))
Lista = [student_1, student_2, student_3, student_4, student_5]
random.shuffle(Lista)
print(Lista)