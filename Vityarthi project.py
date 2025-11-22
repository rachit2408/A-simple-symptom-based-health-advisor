import tkinter as tk
from tkinter import messagebox

Illness = {
    "cold": "Rest, drink plenty of fluids, and consider taking cold relief tablet (eg- use tablets like acetaminophem).",
    "headache": "take Rest , Reduce Screentime, Ensure 8 Hours Of sleep and Ensure you are well-hydrated.",
    "stomach ache": "For indigestion or general upset, try an antacid (like Pentop D or meftal Spas) , Avoid spicy and junk food, Take Rest",
    "sore throat": "Gargle with warm salt water, and use penicillin if there is any type of throat pain",
    "fever": "Take tablets like Dolo or Paracetamol. Stay hydrated and monitor your temperature. See a doctor if the fever is very high or lasts more than 24-48 hours.",
    "allergy": "Take tablets of antihistamine that can help relieve symptoms like sneezing and itching.",
}

def get_advice(entry_widget, result):
    # ...
    user_illness=entry_widget.get().strip()
    illness_key=user_illness.lower()
    
    entry_widget.delete(0, tk.END) 
    
    if not user_illness: 
        advice="Please enter an illness..."
        
    elif illness_key in Illness:
        advice_text=Illness[illness_key]
        advice=f"Based on '{user_illness.title()}':\n {advice_text}"
    else:
        advice=f"I am sorry, I do not have a specific suggestion for '{user_illness.title()}'.\n Safety First: Please consult a licensed medical professional or doctor. For common issues, try 'headache' or 'cold'."

    
    result.config(text=advice)
    
def setup_gui():
    """Sets up the main application window and widgets."""
    root=tk.Tk()
    root.title("Basic Illness Advisor")
    root.geometry("600x400")
    root.configure(bg="#e0f7fa") 
    
    padding_options={'padx': 15, 'pady': 15}
    
    title_label = tk.Label(root, 
                           text=" Basic Home Symptom Advisor", 
                           font=("Helvetica", 18, "bold"), 
                           bg="#e0f7fa", 
                           fg="#004d40")
    title_label.pack(**padding_options)

    disclaimer_label = tk.Label(root, 
                                text="Disclaimer: This tool provides *general* OTC advice only. It is NOT a substitute for professional medical consultation.", 
                                font=("Helvetica", 10, "italic"),
                                bg="#e0f7fa", 
                                fg="#c62828", 
                                wraplength=550)
    disclaimer_label.pack(pady=(0, 10))

    input_frame=tk.Frame(root, bg="#e0f7fa")
    input_frame.pack(**padding_options)
    
    prompt_label=tk.Label(input_frame, 
                            text="Enter your symptom (e.g., Cold, Headache):", 
                            font=("Helvetica", 12),
                            bg="#e0f7fa", 
                            fg="#004d40")
    prompt_label.pack(side=tk.LEFT, padx=5)

    illness_entry=tk.Entry(input_frame, width=30, font=("Helvetica", 12))
    illness_entry.pack(side=tk.LEFT, padx=5)
    
    result_label=tk.Label(root, 
                            text="Type a symptom and click 'Get Advice'.", 
                            font=("Helvetica", 11),
                            bg="#ffffff", 
                            fg="#37474f", 
                            justify=tk.LEFT, 
                            wraplength=550, 
                            relief=tk.RIDGE, 
                            bd=2, 
                            height=8, 
                            width=65, 
                            anchor="nw") 
    result_label.pack(**padding_options)
    
    advice_button=tk.Button(root, 
                              text="Get Advice", 
                              command=lambda: get_advice(illness_entry, result_label),
                              font=("Helvetica", 12, "bold"),
                              bg="#00796b", 
                              fg="#ffffff", 
                              activebackground="#004d40")
    advice_button.pack(pady=(0, 15))
    
    root.mainloop()
if __name__ == "__main__":
    setup_gui()