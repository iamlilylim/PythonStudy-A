import tkinter as tk
from tkinter import messagebox
class ToCk:
    def __init__(self, root):
        self.root = root
        self.root.title("Iamlily's ToDo List")
        self.root.geometry("400x500")
        self.tasks = []

        self.task_entry = tk.Entry(root, font = ("Arial", 13))
        self.task_entry.pack(pady =30, padx = 20)

        button_frame = tk.Frame(root)
        button_frame.pack(padx =5, pady =5)

        self.add_btn = tk.Button(button_frame, text = "📝Add", width = 10, command = self.add_task)
        self.add_btn.grid(row=0, column=0, padx=5)

        self.del_btn = tk.Button(button_frame, text="📝Del", width=10, command=self.del_task)
        self.del_btn.grid(row=0, column=1, padx=5)

        self.udt_btn = tk.Button(button_frame, text="📝Update", width=10, command=self.udt_task)
        self.udt_btn.grid(row=0, column=2, padx=5)
        self.listbox = tk.Listbox(root,
             selectmode=tk.SINGLE,
              font=('Arial',12),
               width=30,
              height=15
            )
        self.listbox.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0,tk.END)

        else:
            messagebox.showwarning("Error", "Write your 'to do' first.")

    def del_task(self):
        chosen = self.listbox.curselection()
        if chosen:
            index=chosen[0]
            self.listbox.delete(index)
            del self.tasks[index]

        else:
            messagebox.showwarning("Error", "Click what you want to delete.")

    def udt_task(self):
        clicked = self.listbox.curselection()
        new_task = self.task_entry.get().strip()
        if clicked:
            indx = clicked[0]
            new_task = self.task_entry.get().strip()
            if new_task:
                self.tasks[indx] = new_task
                self.listbox.delete(indx)
                self.listbox.insert(indx, new_task)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Error", "Enter a new task")

        else:
            messagebox.showwarning("Error", "Select what you want to modify")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToCk(root)
    root.mainloop()