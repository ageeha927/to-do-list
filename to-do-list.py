todolist = []
a = ''
marked = []

def add():
    num = int(input('How many tasks would you like to add?'))
    for i in range(0, num):
        ele = (input())
        todolist.append(ele)
    print('''
This is your current To-Do List:
      
    To-do:''')
    for task in todolist:
            print(f'''      -{task}''')
    print('''
    Marked Done:''')
    for task in marked:
            print(f'''      -{task} (completed)''')
    
def view():
    if len(todolist) >= 1:
        type = input('Would you like to view from your To-do or Marked?(To-do or Marked)')
        view = int(input('What task would you like to view individually?(Your first task is 0, second task is 1, and so on)'))
        if type.lower() == 'to-do':
            print(f'''
Task: {view}
    -{todolist[view]}''')
        elif type.lower() == 'marked':
             print(f'''
Task: {view}
    -{marked[view]} (completed)''')     
    else:
        return('You have no tasks to view. Please add tasks to view them!')

def mark():
    if len(todolist) >= 1:
        mark = int(input('What task would you like to mark?(Your first task is 0, second task is 1, and so on)'))
        marked.append(todolist[mark])
        todolist.remove(todolist[mark])
        print('''
This is your current To-Do List:
      
    To-do:''')
        for task in todolist:
            print(f'''      -{task}''')
        print('''
    Marked Done:''')
        for task in marked:
            print(f'''      -{task} (completed)''')
    else:
        return('You have no tasks to mark. Please add tasks to mark them!')
    
def delete():
    type = input('Would you like to delete from your To-do or Marked?(To-do or Marked)')
    de = int(input('What task would you like to delete?(Your first task is 0, second task is 1, and so on)'))
    if type.lower() == 'to-do':
        todolist.remove(todolist[de])
        print('''
This is your current To-Do List:
      
    To-do:''')
        for task in todolist:
            print(f'''      -{task}''')
        print('''
    Marked Done:''')
        for task in marked:
            print(f'''      -{task} (completed)''')
    elif type.lower() == 'marked':
        marked.remove(marked[de])
        print('''
This is your current To-Do List:
      
    To-do:''')
        for task in todolist:
            print(f'''      -{task}''')
        print('''
    Marked Done:''')
        for task in marked:
            print(f'''      -{task} (completed)''')
            
print('''
Welcome to your personal To-do List!
      
In your To-do List you may:
    -Add tasks
    -View tasks 
    -Mark tasks as completed 
    -Delete tasks
      
This program is not case sensitive but it is spelling sensitive.
    Please make sure you correctly spelled
    the action you want to perform before continuing!      ''')

print('''

This is your current To-Do List:
      
    To-do:
    
    Marked Done:
    ''')

while a != 'exit':
    a = input('Would you like to add, view, mark a task complete, delete a task or exit the program?(Add, View, Mark, Delete, Exit)')

    if a.lower() == 'add':
          print(add())
    
    if a.lower() == 'view':
          print(view())

    if a.lower() == 'mark':
          print(mark())

    if a.lower() == 'delete':
          print(delete())

    if a.lower() == 'exit':
          break