students = ['Вознесенский',
'Ерухимович', 
'Зубков', 
'Кадкина', 
'Карамянц', 
'Кетова', 
'Мариев', 
'Попов', 
'Савченко',
'Сараев', 
'Мясников', 
'Сафонов', 
'Ходнев', 
'Юсибов', 
'Гомеш', 
'Рудина']

tasks = []

for task_number in range(20):
    tasks.append(task_number + 1)
    
print(len(students))

# фамилия - 1,2,3

current_task = 0
for student in students:
    tasks_for_student = ''
    for counter in range(4):
        tasks_for_student = tasks_for_student + str(tasks[current_task]) + ','
        current_task = current_task + 1
        if (current_task == len(tasks)):
            current_task = 0
    tasks_for_student = tasks_for_student[0:-1] # срез
    print(student + ' - ' + tasks_for_student)

