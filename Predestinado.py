import random
students = []
for p in range(0, 56):
    student = input(f'Informe o nome do {p+1}º student:')
    students.append(student)
predestinado = random.choice(students)
print(f'O aluno sorteado foi= {predestinado}')