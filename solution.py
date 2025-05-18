# Simple GUI Application for Language Translation, uses Google Translate API

from googletrans import LANGUAGES
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
    root, text='Translated Text:', font=('Times New Roman', 15), bg='purple', fg='white').place(x=20, y=150)
Output_text = Text(
    root, width=50, height=10, font=('Times New Roman', 15))
Output_text.place(x=25, y=200)

language = list(LANGUAGES.values())
# Create a list of languages for user selection (dropdown menu)
dest_lang = ttk.Combobox(root, values=language, font=('Times New Roman', 15), width=20)
dest_lang.place(x=25, y=450)
dest_lang.set('Select Language')  

# Function to translate text
def Translate():
    try:
        translator = translator(to_lang=dest_lang.get())
        translation = translator.translate(Input_text.get())
        Output_text.delete(1.0, END)
        Output_text.insert(END, translation)
    except Exception as e:
        print(f"Translation Error: {e}")

# initiate translation button
trans_button = Button(root, text='Translate', font=('Times New Roman', 15), bg='purple', fg='white', command=Translate, activebackground= 'yellow')
trans_button.place(x=25, y=500)

#exit button
exit_button = Button(root, text='Exit', font=('Times New Roman', 15), bg='purple', fg='white', command=root.quit, activebackground= 'pink')
exit_button.place(x=200, y=500)

# Run the main loop
root.mainloop()

