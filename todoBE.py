import json
import todoDB as db

def load_todos():
    """Tải dữ liệu todos từ database"""
    data = db.get_all_todos()
    return data

def load_groups():
    """Tải dữ liệu groups từ database"""
    groups = db.get_all_groups()
    return groups

def add_todo(title, description, group, due_date, due_time, location, priority, is_important, url, image_path):
    print('Inserting!')
    db.add_todos(title, description, group, due_date.isoformat() if due_date else None, due_time.strftime('%H:%M') if due_time else None, location, priority, is_important, url, image_path)
    print('Inserted!')

def update_todo(todo_id, title, description, group, due_date, due_time, location, priority, is_important, url, image_path):
    print('Updating!')
    db.update_todo(todo_id, title, description, group, due_date.isoformat() if due_date else None, due_time.strftime('%H:%M') if due_time else None, location, priority, is_important, url, image_path)
    print('Updated!')

def delete_todo(todo_id):
    print('Deleting!')
    db.delete_todo(todo_id)
    print('Deleted!')

def toggle_complete(todo_id, completed):
    print('Toggling!')
    db.update_todo_completion(todo_id, completed)
    print('Toggled!')

def filter_todos(search_term="", selected_group="", filter_date=None, show_completed=True):
    data = db.get_all_todos()
    if search_term != "":
        data = [todo for todo in data if search_term.lower() in todo['title'].lower()]
    if selected_group != "Tất cả":
        data = [todo for todo in data if todo['group'] == selected_group]
    if filter_date != None:
        data = [todo for todo in data if todo['due_date'] == filter_date.isoformat()]
    if not show_completed:
        data = [todo for todo in data if not todo['completed']]
    return data

def add_group(name):
    db.add_group(name)
