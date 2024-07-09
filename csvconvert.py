import csv

headers = ['TYPE', 'CONTENT', 'DESCRIPTION', 'PRIORITY', 'INDENT', 'DATE', 'DATE_LANG', 'TIMEZONE', 'DURATION', 'DURATION_UNIT']

#read data
with open('ToDoVoDo_7636_Physics_2024-04-13_17-39-09.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    todoist_tasks = []

    for row in reader:
        #create todoist tasks
        todoist_task = {
            'TYPE': 'task',
            'CONTENT': row['title'],
            'DESCRIPTION': row['body_content'],

            'PRIORITY': '',
            'INDENT': '',
            'DATE': row['dueDateTime_dateTime'],
            'DATE_LANG': '',
            'TIMEZONE': row['dueDateTime_timeZone'],
            'DURATION': '',
            'DURATION_UNIT': ''
        }
        
        todoist_tasks.append(todoist_task)

#write to new file
with open('todoist_import.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(todoist_tasks)

print("Todoist CSV file generated successfully.")