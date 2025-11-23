import tkinter as tk
from tkinter import messagebox



quizStuff = {
    "Easy": [
        {"q": "Which is the capital city of France?", "opts": ["Lyon", "Marseille", "Paris", "Strasbourg"], "a": 2},
        {"q": "Which animal is known as the 'Ship of the Desert'?", "opts": ["Lion", "Camel", "Elephant", "Oryx"], "a": 1},
        {"q": "Which is the largest ocean on Earth?", "opts": ["Pacific", "Atlantic", "Indian", "Arctic"], "a": 0},
        {"q": "What is the tallest mountain in the world?", "opts": ["K2", "Kangchenjunga", "Kilimanjaro", "Everest"], "a": 3},
        {"q": "Which planet is known as the 'Red Planet'?", "opts": ["Venus", "Mars", "Saturn", "Uranus"], "a": 1},
        {"q": "What is the chemical symbol for water?", "opts": ["H2O", "CH4", "O2", "H2"], "a": 0},
        {"q": "How many legs does a spider have?", "opts": ["10", "8", "3", "12"], "a": 1},
        {"q": "Which organ in the human body pumps blood?", "opts": ["Liver", "Kidney", "Heart", "Skin"], "a": 2},
        {"q": "How many colors are there in a rainbow?", "opts": ["3", "12", "7", "15"], "a": 2},
        {"q": "In which direction does the sun rise?", "opts": ["East", "North", "West", "South"], "a": 0},
    ],
    "Medium": [
        {"q": "What is the capital city of Australia?", "opts": ["Sydney", "Canberra", "Perth", "Melbourne"], "a": 1},
        {"q": "Which element is represented by the symbol 'Au'?", "opts": ["Copper", "Silver", "Gold", "Aluminum"], "a": 2},
        {"q": "In which year did World War II end?", "opts": ["1945", "1918", "1939", "1950"], "a": 0},
        {"q": "Who wrote the dystopian novel '1984'?", "opts": ["Huxley", "Tolkien", "Orwell", "Bradbury"], "a": 2},
        {"q": "What is the hardest natural substance on Earth?", "opts": ["Diamond", "Quartz", "Granite", "Iron"], "a": 0},
        {"q": "Which planet is the hottest in the solar system?", "opts": ["Mercury", "Jupiter", "Venus", "Mars"], "a": 2},
        {"q": "What is the largest organ in the human body?", "opts": ["Liver", "Brain", "Heart", "Skin"], "a": 3},
        {"q": "Which artist painted the 'Mona Lisa'?", "opts": ["Da Vinci", "Picasso", "Van Gogh", "Michelangelo"], "a": 0},
        {"q": "What is the currency of Japan?", "opts": ["Yen", "Yuan", "Ringgit", "Won"], "a": 0},
        {"q": "What gas do plants absorb for photosynthesis?", "opts": ["Hydrogen", "Nitrogen", "CO2", "Oxygen"], "a": 2},
    ],
    "Hard": [
        {"q": "Which letter does NOT appear in any element symbol?", "opts": ["Z", "J", "X", "Q"], "a": 1},
        {"q": "Which war is recorded as the shortest in history?", "opts": ["Six-Day War", "Anglo-Zanzibar", "Football War", "Falklands"], "a": 1},
        {"q": "Bone not connected to any other bone?", "opts": ["Femur", "Hyoid", "Coccyx", "Stapes"], "a": 1},
        {"q": "First woman to win a Nobel Prize?", "opts": ["Mother Teresa", "Rosalind Franklin", "Jane Addams", "Marie Curie"], "a": 3},
        {"q": "Which planet rotates clockwise?", "opts": ["Jupiter", "Mars", "Saturn", "Venus"], "a": 3},
        {"q": "What is the capital city of Turkey?", "opts": ["Antalya", "Izmir", "Ankara", "Istanbul"], "a": 2},
        {"q": "What was the first 'computer bug' caused by?", "opts": ["Moth", "Wire", "Drink", "Virus"], "a": 0},
        {"q": "Which country is 'Doubly Landlocked'?", "opts": ["Liechtenstein", "Paraguay", "Nepal", "Switzerland"], "a": 0},
        {"q": "Who wrote the novel 'Frankenstein'?", "opts": ["Mary Shelley", "Bram Stoker", "Poe", "H.G. Wells"], "a": 0},
        {"q": "Number 1 followed by 100 zeros?", "opts": ["Infinity", "Zillion", "Googol", "Centillion"], "a": 2},
    ]
}


currentQs = []
qIndex = 0
points = 0


def wipe():

    for w in mainWindow.winfo_children():
        w.destroy()


def home_screen():
    wipe()
    tk.Label(mainWindow, text="Welcome to the Quiz Game", font=("Helvetica", 24, "bold"), pady=20).pack()

    tk.Button(mainWindow, text="Start Game", font=("Arial", 14), width=20,
              command=pick_diff, bg="#4CAF50", fg="white").pack(pady=10)

    tk.Button(mainWindow, text="Exit", font=("Arial", 14), width=20,
              command=mainWindow.quit, bg="#f44336", fg="white").pack(pady=10)


def pick_diff():
    wipe()
    tk.Label(mainWindow, text="Select Difficulty", font=("Helvetica", 20, "bold"), pady=20).pack()


    tk.Button(mainWindow, text="Easy", font=("Arial", 14), width=15,
              command=lambda: prep_game("Easy")).pack(pady=5)
    tk.Button(mainWindow, text="Medium", font=("Arial", 14), width=15,
              command=lambda: prep_game("Medium")).pack(pady=5)
    tk.Button(mainWindow, text="Hard", font=("Arial", 14), width=15,
              command=lambda: prep_game("Hard")).pack(pady=5)


def prep_game(diff):
    global currentQs, qIndex, points
    currentQs = quizStuff[diff]
    qIndex = 0
    points = 0
    show_q()


def show_q():
    wipe()


    if qIndex >= len(currentQs):
        end_screen()
        return

    qObj = currentQs[qIndex]


    tk.Label(mainWindow, text="Question " + str(qIndex + 1) + "/10", font=("Arial", 10)).pack(pady=5)
    tk.Label(mainWindow, text=qObj["q"], font=("Helvetica", 16, "bold"), wraplength=500).pack(pady=15)


    for i, op in enumerate(qObj["opts"]):
        tk.Button(
            mainWindow,
            text=op,
            font=("Arial", 12),
            width=30,
            pady=4,
            command=lambda x=i: verify(x)
        ).pack(pady=4)


def verify(choice):
    global points, qIndex

    right = currentQs[qIndex]["a"]

    if choice == right:
        points += 1
        messagebox.showinfo("Result", "Correct! Great Job.")
    else:

        messagebox.showinfo("Result", "Wrong Answer!")

    qIndex += 1
    show_q()


def end_screen():
    wipe()

    tk.Label(mainWindow, text="Game Over", font=("Helvetica", 24, "bold"), pady=20).pack()


    resultLine = "You got " + str(points) + " out of 10!"
    tk.Label(mainWindow, text=resultLine, font=("Arial", 18), pady=10).pack()


    if points < 5:
        msg = "You can do better next time!"
    else:
        msg = "Congratulations, you did good!"

    tk.Label(mainWindow, text=msg, font=("Arial", 14, "italic"), fg="blue").pack(pady=10)

    tk.Button(mainWindow, text="Play Again", font=("Arial", 14), width=20,
              command=home_screen, bg="#2196F3", fg="white").pack(pady=15)

    tk.Button(mainWindow, text="Close", font=("Arial", 14), width=20,
              command=mainWindow.quit).pack(pady=5)


mainWindow = tk.Tk()
mainWindow.title("Quiz Master")
mainWindow.geometry("600x500")

home_screen()
mainWindow.mainloop()
