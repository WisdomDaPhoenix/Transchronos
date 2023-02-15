print("Welcome to Transchronos")

import customtkinter
from translate import Translator

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

mainwindow = customtkinter.CTk()
mainwindow.geometry("980x600")
mainwindow.title("TRANSCHRONOS TRANSLATOR")

def execute():
    t = Translator(from_lang="en",to_lang="es")
    usertext = phrasebox.get()
    meaning = t.translate(usertext)

    response = customtkinter.CTkLabel(master=mainframe, width=250, height=145,
                                      corner_radius=7, text=meaning, text_font=("Calibri",23))
    response.pack(pady=7, padx=10)





mainframe = customtkinter.CTkFrame(master=mainwindow, width=760, height=560,
                                   corner_radius=7, border_width=4,
                                   border_color="lightgreen")
mainframe.pack(pady=40, padx=15)

getstarted_box = customtkinter.CTkLabel(master=mainframe, width=150, height=45, text="Translate from English to Spanish""")
getstarted_box.pack(pady=12, padx=10)

phrasetitle = customtkinter.CTkLabel(master=mainframe, width=150, height=45, text=f"Translate a Phrase")
phrasetitle.pack(pady=7, padx=10)

phrasebox = customtkinter.CTkEntry(master=mainframe, width=250, height=45, placeholder_text="Enter Phrase to translate...")
phrasebox.pack(pady=7, padx=10)

submit = customtkinter.CTkButton(master=mainframe, width=150, height=45, text="Translate" ,command=execute)
submit.pack(pady=7, padx=10)


mainwindow.mainloop()

