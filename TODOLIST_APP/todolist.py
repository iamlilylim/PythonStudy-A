#To do list application🙊

#tkinter: 파이썬에서 창을 만들고 버튼, 글상자 등 GUI 구성하는 모듈
import tkinter as tk
from tkinter import messagebox # 알림창 띄우는데 사용


#To do list 담은 app class 만들기
class TodoApp: #paskal
    def __init__(self, root):
        #app에 창만들기
        self.root = root #첫화면(변수)
        self.root.title("🧾I am Lily's To Do ListTo Do ListTo Do List🐴") #창의 제목
        self.root.geometry("400x500") #창의 크기 지정(with:400, height: 500pixel)
        #empty list for saving todo list
        self.tasks = []
        #--------------[Step1] 할일 입력칸 만들기------------------#
        #글자 입력할 수 있는 Entry(한줄입력창) 만들기
        self.task_entry = tk.Entry(root, font = ("Arial", 14)) #텍스트 입력창 만들기
        self.task_entry.pack(pady = 30) #위아래 여백(픽셀)
 #--------------[Step2] ㅂㅓ튼 만들박스만들기-----------------#
        btn_frame = tk.Frame(root) # organising buttons in a frame
        btn_frame.pack() #창에 올리기
    #추가버튼만들기
        self.add_btn = tk.Button(btn_frame, text = "➕add", width = 10, command = self.add_task)
        self.add_btn.grid(row = 0, column = 0, padx = 5)
    #삭제버튼만들기
        self.delete_btn = tk.Button(btn_frame, text='➖Delete', width = 10, command=self.delete_task)
        self.delete_btn.grid(row=0, column=1, padx=5)
    #수정버튼 만들기
        self.update_btn = tk.Button(btn_frame, text='➰Update', width = 10, command=self.update_task)
        self.update_btn.grid(row=0, column=2, padx=5)


        self.listbox = tk.Listbox(root,
            selectmode=tk.SINGLE,
            font=('Arial',12),
            width=40,
            height=15
        )
        self.listbox.pack(pady=10)
    def add_task(self):
        # 입력창에 적힌 내용 가져오기
        task = self.task_entry.get().strip()  # strip은 앞뒤 공백제거
        if task:  # 만약 비어있지 않다면
            self.tasks.append(task)  # 메모리(list)에 저장
            self.listbox.insert(tk.END, task)  # 화면에 list box에도 추가됨
            self.task_entry.delete(0, tk.END)  # 입력창 초기화
        else:
            # 비어있는 입력창에 추가버튼을 눌렀을 때 경고창 표시
            messagebox.showwarning("Error", "Forgot to type?")

    def delete_task(self):
        # 선택한 항목번호 가져오기
        selected = self.listbox.curselection()
        if selected:  # 만약 뭔가 선택되었다면
            index = selected[0]
            self.listbox.delete(index) #화면에서 삭제
            del self.tasks[index] #리스트에서도 삭제
        else:
            # 선택없이 삭제버튼을 눌렀을 때 경고창 표시
            messagebox.showwarning("Error", "Nothing to choose?")


    def update_task(self):
        # 선택된 항목의 인덱스
        try:
            selected_index = listbox.curselection()[0]
            new_task = entry.get()

            # 리스트박스에서 기존 항목 삭제
            listbox.delete(selected_index)

            # 새로운 항목 삽입
            listbox.insert(selected_index, new_task)

            # 입력창 초기화
            entry.delete(0, tk.END)

        except IndexError:
            print("항목을 선택해주세요.")

    # 기본 설정
    root = tk.Tk()
    root.geometry("300x300")



    # 예제 항목 추가



    # 업데이트 버튼
    btn_update = tk.Button(root, text="Update Task", command=update_task)
    btn_update.pack()

    root.mainloop()

            # --------------[Step3] 할일 목록 보여줄 리스트박스 만들기------------------#




        #defining functions


#실행 코드: 프로그램 시작부분
if __name__ == "__main__":
  root = tk.Tk()
  root.configure(bg="#FF5733")
  app = TodoApp(root)
  root.mainloop()