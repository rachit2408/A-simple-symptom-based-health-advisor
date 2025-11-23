import tkinter as tk

adviceThings = {
    "cold": "maybe try some warm soup or tea and just relax a bit",
    "headache": "drink some water and maybe rest your eyes away from phone",
    "stomach ache": "dont eat spicy food and like try something light",
    "sore throat": "warm water or honey tea feels nice sometimes",
    "fever": "rest and drink water... if it keeps going you should see doctor",
    "allergy": "try to avoid dust and stuff, maybe allergy tablet if needed"
}

def showStuff(box, labelThing):
    txt = box.get()
    txt = txt.strip()
    low = txt.lower()

    box.delete(0, tk.END)

    if txt == "":
        msg = "please type something first"
    elif low in adviceThings:
    
        msg = "for " + txt + " maybe try this:\n\n" + adviceThings[low] + "\n\nhope you feel better soon"
    else:
        
        msg = "sorry i dont have info about '" + txt + "'\n\nmaybe ask a doctor if unsure\nor try typing like cold or headache"

    
    labelThing.config(text=msg)

def start():
    
    win = tk.Tk()
    win.title("symptom helper thing")
    win.geometry("600x430")
    win.configure(bg="#e9fffd")

    
    top = tk.Label(win, text="symptom helper", font=("Arial", 20), bg="#e9fffd")
    top.pack(pady=15)

    note = tk.Label(win,
        text="this isnt medical advice btw just normal ideas",
        font=("Arial", 9, "italic"),
        bg="#e9fffd",
        fg="#bb0000"
    )
    note.pack()

    frame = tk.Frame(win, bg="#e9fffd")
    frame.pack(pady=18)

    ask = tk.Label(frame, text="what symptom do you have?", font=("Arial", 12), bg="#e9fffd")
    ask.pack(side=tk.LEFT)

    entryThing = tk.Entry(frame, width=26, font=("Arial", 12))
    entryThing.pack(side=tk.LEFT, padx=8)

    output = tk.Label(win,
        text="type something above and press the button",
        font=("Arial", 11),
        bg="#ffffff",
        fg="#222",
        wraplength=550,
        justify=tk.LEFT,
        relief=tk.RIDGE,
        bd=2,
        height=12,
        width=65,
        anchor="nw"
    )
    output.pack(pady=15)

    btn = tk.Button(win,
        text="get suggestion",
        command=lambda: showStuff(entryThing, output),
        font=("Arial", 12, "bold"),
        bg="#0b8b82",
        fg="#ffffff",
        padx=10,
        pady=6
    )
    btn.pack()

    win.mainloop()
if __name__ == "__main__":
    start()
