import re
import tkinter as tk
from tkinter import messagebox

def palindrome_checker(x):
    
    mot_phrase_t = re.sub(r'[^a-zA-Z0-9]', '', x)
    mot_phrase_t = mot_phrase_t.lower()
    
    if mot_phrase_t == mot_phrase_t[::-1]:
        
        return True
    else:
        return False

def show_message_box():
    if palindrome_checker:
        messagebox.showinfo("Message", "Palindrome")
    else:
        messagebox.showinfo("Message", "Pas palindrome")

def main():
    my_window = tk.Tk()
    my_window.title("Vérificateur de palindrome")
    my_window.geometry("600x200") 

    mot_phrase = tk.Frame(my_window, pady=20)
    mot_phrase_label = tk.Label(mot_phrase, text="Entrez le mot ou la phrase à vérifier :")
    mot_phrase_label.pack(side="left")
    mot_phrase_input = tk.Entry(mot_phrase)
    mot_phrase_input.pack(side="left")
    mot_phrase.pack()

    button_verif = tk.Button(my_window, text="Vérifier",
                                        command=lambda: palindrome_checker(mot_phrase_input.get()))
 
    button_verif.pack()

    my_window.mainloop()

if __name__ == "__main__":
    main()
