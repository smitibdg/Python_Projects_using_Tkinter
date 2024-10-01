import tkinter as tk
from tkinter import messagebox
from googletrans import Translator

class EnglishToHindiConverter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("English to Hindi Converter")
        self.geometry("400x200")

        self.label = tk.Label(self, text="Enter text in English:")
        self.label.pack()

        self.entry = tk.Entry(self, width=50)
        self.entry.pack()

        self.convert_button = tk.Button(self, text="Translate", command=self.translate)
        self.convert_button.pack()

        self.output_label = tk.Label(self, text="Hindi Translation:")
        self.output_label.pack()

        self.output = tk.Entry(self, width=50)
        self.output.pack()

    def translate(self):
        text = self.entry.get()
        if not text:
            messagebox.showwarning("Warning", "Please enter text to translate.")
            return

        translator = Translator()
        try:
            translation = translator.translate(text, src='en', dest='hi')
            if translation.text:
                self.output.delete(0, tk.END)  # Clear the output field
                self.output.insert(tk.END, translation.text)  # Insert the translated text
            else:
                messagebox.showwarning("Translation Failed",
                                       "Unable to translate the text. Please try again.")
        except AttributeError as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            print(f"AttributeError: {str(e)}")

if __name__ == "__main__":
    app = EnglishToHindiConverter()
    app.mainloop()
