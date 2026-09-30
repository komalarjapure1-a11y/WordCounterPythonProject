import re
from tkinter import filedialog, messagebox


# =========================================================
# MODULE 1: INPUT & FILE HANDLING
# =========================================================

def get_words(text):
    return re.findall(r"\b[a-zA-Z]+\b", text.lower())


def open_file(text_box):
    filename = filedialog.askopenfilename(
        title="Open Text File",
        filetypes=[
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ]
    )

    if filename:
        try:
            with open(
                filename,
                "r",
                encoding="utf-8"
            ) as file:
                text = file.read()

            text_box.delete(
                "1.0",
                "end"
            )

            text_box.insert(
                "end",
                text
            )

        except Exception as e:
            messagebox.showerror(
                "Error",
                "Unable to open file.\n" + str(e)
            )