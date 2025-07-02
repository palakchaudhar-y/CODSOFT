from tkinter import *
from tkinter import messagebox, ttk
import sqlite3 as sql
from datetime import datetime


def add_task():
    task_string = task_field.get().strip()
    if not task_string:
        messagebox.showwarning('Error', 'Task cannot be empty.')
        return
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    the_cursor.execute('INSERT INTO tasks (title, status, created_at) VALUES (?, ?, ?)',
                        (task_string, 'Pending', time_now))
    the_connection.commit()
    task_field.delete(0, END)
    list_update()


def list_update():
    clear_list()
    for row in the_cursor.execute('SELECT rowid, title, status, created_at FROM tasks'):
        task_listbox.insert('', 'end', values=row)


def delete_task():
    selected = task_listbox.selection()
    if not selected:
        messagebox.showwarning('Error', 'No Task Selected.')
        return
    for item in selected:
        task_id = task_listbox.item(item)['values'][0]
        the_cursor.execute('DELETE FROM tasks WHERE rowid = ?', (task_id,))
    the_connection.commit()
    list_update()


def mark_complete():
    selected = task_listbox.selection()
    if not selected:
        messagebox.showwarning('Error', 'No Task Selected.')
        return
    for item in selected:
        task_id = task_listbox.item(item)['values'][0]
        the_cursor.execute('UPDATE tasks SET status = ? WHERE rowid = ?', ('Completed', task_id))
    the_connection.commit()
    list_update()


def delete_all_tasks():
    confirm = messagebox.askyesno('Delete All', 'Are you sure to delete all tasks?')
    if confirm:
        the_cursor.execute('DELETE FROM tasks')
        the_connection.commit()
        list_update()


def clear_list():
    task_listbox.delete(*task_listbox.get_children())


def close_app():
    confirm = messagebox.askyesno("Exit", "Do you really want to exit?")
    if confirm:
        guiWindow.destroy()


if __name__ == "__main__":
    guiWindow = Tk()
    guiWindow.title("Advanced To-Do List")
    guiWindow.geometry("850x500")
    guiWindow.resizable(False, False)
    guiWindow.configure(bg="#A9CCE3")


    the_connection = sql.connect('listOfTasks.db')
    the_cursor = the_connection.cursor()
    the_cursor.execute(
        'CREATE TABLE IF NOT EXISTS tasks (title TEXT, status TEXT, created_at TEXT)')

  
    frame = Frame(guiWindow, bg="#D6EAF8", pady=10, padx=10)
    frame.pack(expand=True, fill="both")

  
    Label(frame, text="Task:", font=("Arial", 14), bg="#D6EAF8").grid(row=0, column=0, sticky="w", padx=5, pady=5)

    task_field = Entry(frame, font=("Arial", 14), width=50)
    task_field.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    add_button = Button(frame, text="Add Task", font=("Arial", 12, "bold"), bg="#82E0AA",
                         command=add_task)
    add_button.grid(row=0, column=2, padx=5, pady=5, sticky="w")

    columns = ("ID", "Task", "Status", "Created At")
    task_listbox = ttk.Treeview(frame, columns=columns, show="headings", height=12)
    for col in columns:
        task_listbox.heading(col, text=col)
        if col == "Task":
            task_listbox.column(col, width=300, anchor='center')
        elif col == "Created At":
            task_listbox.column(col, width=200, anchor='center')
        else:
            task_listbox.column(col, width=100, anchor='center')

    task_listbox.grid(row=1, column=0, columnspan=3, pady=10, padx=5)


    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=task_listbox.yview)
    task_listbox.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=3, sticky='ns')


    mark_button = Button(frame, text="Mark as Completed", font=("Arial", 12, "bold"), bg="#F7DC6F",
                          command=mark_complete)
    mark_button.grid(row=2, column=0, pady=10, padx=5, sticky="w")

    delete_button = Button(frame, text="Delete Selected", font=("Arial", 12, "bold"), bg="#F1948A",
                            command=delete_task)
    delete_button.grid(row=2, column=1, pady=10, padx=5, sticky="w")

    delete_all_button = Button(frame, text="Delete All", font=("Arial", 12, "bold"), bg="#E59866",
                                command=delete_all_tasks)
    delete_all_button.grid(row=2, column=2, pady=10, padx=5, sticky="w")

    exit_button = Button(frame, text="Exit", font=("Arial", 12, "bold"), bg="#AAB7B8",
                           width=60, command=close_app)
    exit_button.grid(row=3, column=0, columnspan=3, pady=10)

   
    list_update()

    guiWindow.mainloop()
    the_connection.commit()
    the_cursor.close()
