#라이브러리 호출
import tkinter as tk
import random
from tkinter import messagebox

# 메인 화면을 만드는 함수
def create_main_window():
    root = tk.Tk()
    root.title("Memory Game For Alzheimer")
    root.geometry("640x400+100+100")
    root.resizable(False, False)

    main_label = tk.Label(root, text="치매 예방을 위한 기억력 게임", font=("Helvetica", 20))
    main_label.pack(pady=30)

    button_style = {
    "bg": "#79EDFF",            # 배경색: 파란색
    "fg": "black",              # 글꼴색: 흰색
    "font": ("Helvetica", 14),  # 글꼴: Helvetica, 크기: 14
    "width": 20,                # 버튼 가로 크기
    "height": 1                 # 버튼 세로 크기
    }

    game1_button = tk.Button(root, text="업다운 게임 시작", command=start_game1, **button_style)
    game2_button = tk.Button(root, text="숫자야구 게임 시작", command=start_game2, **button_style)
    game3_button = tk.Button(root, text="행맨 게임 시작", command=start_game3, **button_style)
    game4_button = tk.Button(root, text="숫자 기억 게임 시작", command=start_game4, **button_style)

    game1_button.pack(pady=10)
    game2_button.pack(pady=10)
    game3_button.pack(pady=10)
    game4_button.pack(pady=10)

    root.mainloop()

# 업다운 게임을 구현하는 함수
def start_game1():
    root = tk.Toplevel()
    root.title("업다운 게임")
    root.geometry("640x400+100+100")
    root.resizable(False, False)

    button_style = {
    "bg": "#79EDFF",            # 배경색: 파란색
    "fg": "black",              # 글꼴색: 흰색
    "font": ("Helvetica", 14),  # 글꼴: Helvetica, 크기: 14
    "width": 20,                # 버튼 가로 크기
    "height": 1                 # 버튼 세로 크기
    }

    target_number = random.randint(1, 100)
    attempts = 0

    def check_guess():
        nonlocal attempts
        attempts += 1
        guess = int(guess_entry.get())

        if guess < target_number:
            result_label.config(text="숫자가 작습니다. 업! 시도 횟수 : {}".format(attempts))
        elif guess > target_number:
            result_label.config(text="숫자가 큽니다. 다운! 시도 횟수 : {}".format(attempts))
        else:
            result_label.config(text="정답입니다! 정답을 {} 번만에 맞추셨습니다.".format(attempts))

    guess_label = tk.Label(root, text="1 ~ 100 중에서 하나의 숫자를 입력하세요", font=("Helvetica", 20))
    guess_label.pack(pady=20)

    guess_entry = tk.Entry(root)
    guess_entry.pack(pady=20)

    guess_button = tk.Button(root, text="확인", command=check_guess, **button_style)
    guess_button.pack(pady=20)

    result_label = tk.Label(root, text="")
    result_label.pack(pady=20)

# 숫자야구 게임을 구현하는 함수
def start_game2():
    root = tk.Toplevel()
    root.title("숫자야구 게임")
    root.geometry("640x400+100+100")
    root.resizable(False, False)

    button_style = {
    "bg": "#79EDFF",            # 배경색: 파란색
    "fg": "black",              # 글꼴색: 흰색
    "font": ("Helvetica", 14),  # 글꼴: Helvetica, 크기: 14
    "width": 20,                # 버튼 가로 크기
    "height": 1                 # 버튼 세로 크기
    }

    def generate_secret_number():
        return random.sample(range(1, 10), 3)

    secret_number = generate_secret_number()
    attempts = 0

    def check_guess():
        nonlocal attempts
        attempts += 1
        guess = guess_entry.get()
        guess_list = [int(x) for x in guess]

        strikes = sum([1 for i in range(3) if guess_list[i] == secret_number[i]])
        balls = len(set(guess_list).intersection(secret_number)) - strikes

        if strikes == 3:
            result_label.config(text="정답입니다! 정답을 {} 번만에 맞추셨습니다.".format(attempts), font=("Helvetica", 15))
        elif strikes == 0:
            result_label.config(text="아웃!", font=("Helvetica", 15))
        else:
            result_label.config(text="{} 스트라이크! {} 볼!".format(strikes, balls), font=("Helvetica", 15))

    guess_label = tk.Label(root, text="3자리 숫자를 입력하세요", font=("Helvetica", 20))
    guess_label.pack(pady=20)

    guess_entry = tk.Entry(root)
    guess_entry.pack(pady=20)

    guess_button = tk.Button(root, text="확인", command=check_guess, **button_style)
    guess_button.pack(pady=20)

    result_label = tk.Label(root, text="")
    result_label.pack(pady=20)

# 행맨 게임을 구현하는 함수
def start_game3():
    root = tk.Toplevel()
    root.title("행맨 게임")
    root.geometry("640x400+100+100")
    root.resizable(False, False)

    button_style = {
    "bg": "#79EDFF",            # 배경색: 파란색
    "fg": "black",              # 글꼴색: 흰색
    "font": ("Helvetica", 14),  # 글꼴: Helvetica, 크기: 14
    "width": 20,                # 버튼 가로 크기
    "height": 1                 # 버튼 세로 크기
    }

    word_list = ["apple", "banana", "cherry", "orange", "watermelon"]
    target_word = random.choice(word_list)
    guessed_letters = []

    def update_display():
        displayed_word = ""
        for letter in target_word:
            if letter in guessed_letters:
                displayed_word += letter
            else:
                displayed_word += "_"
            displayed_word += " "
        word_label.config(text=displayed_word)

    def guess_letter():
        guess = letter_entry.get()
        guessed_letters.append(guess)
        update_display()
        if set(target_word) == set(guessed_letters):
            result_label.config(text="정답! 단어를 맞추셨습니다.")
        elif guess not in target_word:
            attempts_label.config(text="시도 횟수 : {}".format(len(guessed_letters)))
            if len(guessed_letters) >= len(set(target_word)) + 3:
                result_label.config(text="게임 오버! 시도 횟수를 초과하였습니다.")
                guess_button.config(state=tk.DISABLED)  # 게임 오버 시 버튼 비활성화

    word_label = tk.Label(root, text="", font=("Helvetica", 20))
    word_label.pack(pady=10)

    letter_label = tk.Label(root, text="알파벳을 입력하세요 : ", font=("Helvetica", 15))
    letter_label.pack(pady=10)

    letter_entry = tk.Entry(root)
    letter_entry.pack(pady=10)

    guess_button = tk.Button(root, text="확인", command=guess_letter, **button_style)
    guess_button.pack(pady=10)

    result_label = tk.Label(root, text="")
    result_label.pack(pady=10)

    attempts_label = tk.Label(root, text="시도 횟수 : 0", font=("Helvetica", 15))
    attempts_label.pack()

    update_display()
    

# 숫자 기억 게임
def start_game4():
    root = tk.Toplevel()
    root.title("숫자 기억 게임")
    root.geometry("640x400+100+100")
    root.resizable(False, False)
    root.withdraw()
    sequence_root = tk.Toplevel()
    sequence_root.title("숫자 기억 게임")

    # 게임 로직 구현
    sequence = [random.randint(1, 9) for _ in range(5)]
    player_sequence = []

    def start_game():
        sequence.clear()
        player_sequence.clear()
        for _ in range(5):
            sequence.append(random.randint(1, 9))
        result_label.config(text="시퀀스를 기억하세요: " + " ".join(map(str, sequence)))
        sequence_root.after(2000, get_player_input)

    def get_player_input():
        result_label.config(text="시퀀스를 입력하세요.")
        player_input_entry = tk.Entry(sequence_root)
        player_input_entry.pack()
        submit_button = tk.Button(sequence_root, text="확인", command=lambda: check_sequence(player_input_entry))
        submit_button.pack()

    def check_sequence(player_input_entry):
        player_input = player_input_entry.get()
        player_input_entry.destroy()
        if player_input == " ".join(map(str, sequence)):
            result_label.config(text="정답입니다!")
            messagebox.showinfo("숫자 시퀀스 게임", "정답입니다!")
            sequence_root.destroy()
            root.deiconify()
        else:
            result_label.config(text="틀렸습니다. 정답은: " + " ".join(map(str, sequence)))

    start_button = tk.Button(sequence_root, text="게임 시작", command=start_game)
    result_label = tk.Label(sequence_root, text="게임을 시작합니다.")
    start_button.pack()
    result_label.pack()


# 메인 화면 생성
create_main_window()