from tkinter import filedialog, messagebox


# =========================================================
# MODULE 4: OUTPUT & REPORT MANAGEMENT
# =========================================================

def save_report(result_box):

    report = result_box.get(
        "1.0",
        "end"
    ).strip()

    if report == "":
        messagebox.showwarning(
            "Warning",
            "Please analyze the text first!"
        )
        return

    filename = filedialog.asksaveasfilename(
        title="Save Report",
        defaultextension=".txt",
        filetypes=[
            ("Text Files", "*.txt")
        ]
    )

    if filename:
        try:
            with open(
                filename,
                "w",
                encoding="utf-8"
            ) as file:
                file.write(report)

            messagebox.showinfo(
                "Success",
                "Report saved successfully!"
            )

        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e)
            )


def clear_all(text_box, result_box):

    text_box.delete(
        "1.0",
        "end"
    )

    result_box.delete(
        "1.0",
        "end"
    )


# =========================================================
# BUTTON HOVER EFFECT
# =========================================================

def on_enter(button, color):
    button.config(
        bg=color
    )


def on_leave(button, color):
    button.config(
        bg=color
    )