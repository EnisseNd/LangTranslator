# Simple GUI Application for Language Translation, uses Google Translate API

import asyncio
from googletrans import LANGUAGES, Translator
from tkinter import *
from tkinter import ttk

# Create the main window (using root)
root = Tk()
root.geometry('1200x600')
root['bg'] = 'purple'
root.title('Language Translator')

#title label
Label(
    root, text='Language Translator', font=('Times New Roman', 20), bg='purple', fg='white').pack(pady=10)

#Label for enter text
Label(
    root, text='Enter Text:', font=('Times New Roman', 15), bg='purple', fg='white').place(x=20, y=60)

Input_text = Entry(
    root, width=50, font=('Times New Roman', 15))

Input_text.place(x=25, y=100)

# translated text
Label(
    root, text='Translated Text:', font=('Times New Roman', 15), bg='purple', fg='white').place(x=20, y=210)
Output_text = Text(
    root, width=50, height=10, font=('Times New Roman', 15))
Output_text.place(x=25, y=250)

language = list(LANGUAGES.values())
# Create a list of languages for user selection (dropdown menu)
dest_lang = ttk.Combobox(root, values=language, font=('Times New Roman', 15), width=20)
dest_lang.place(x=25, y=150)
dest_lang.set('Select Language')  

# Function to translate text
def Translate():
    async def do_translate():
        try:
            translator = Translator()
             # Get the language code from the selected language name
            selected_lang = dest_lang.get()
            if selected_lang == 'Select Language' or not selected_lang:
                Output_text.delete(1.0, END)
                Output_text.insert(END, "Please select a language.")
                return
            lang_code = [code for code, name in LANGUAGES.items() if name.lower() == selected_lang.lower()]
            if not lang_code:
                Output_text.delete(1.0, END)
                Output_text.insert(END, "Invalid language selected.")
                return
            translation = await translator.translate(Input_text.get(), dest=lang_code[0])
            Output_text.delete(1.0, END)
            Output_text.insert(END, translation.text)
        except Exception as e:
            Output_text.delete(1.0, END)
            Output_text.insert(END, f"Translation Error: {e}")
    
    asyncio.run(do_translate())

    

# initiate translation button
trans_button = Button(
    root, text='Translate', font=('Times New Roman', 15), bg='purple', fg='white', command=Translate, activebackground= 'yellow')
trans_button.place(x=25, y=500)

#exit button
exit_button = Button(
    root, text='Exit', font=('Times New Roman', 15), bg='purple', fg='white', command=root.quit, activebackground= 'pink')
exit_button.place(x=200, y=500)

# Run the main loop
root.mainloop()

