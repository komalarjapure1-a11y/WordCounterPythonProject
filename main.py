import ctypes

# Make Tkinter application sharp on Windows
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except:
    try:
        ctypes.windll.user32.SetProcessDPIAware()
    except:
        pass

import tkinter as tk
from tkinter import messagebox
from collections import Counter

from module1_input import get_words, open_file
from module2_processing import analyze_text_data
from module3_statistics import show_graph
from module4_output import save_report, clear_all


# =========================================================
# MAIN WINDOW
# =========================================================

root = tk.Tk()

root.title(
    "Word Counter & Text Analyzer"
)

root.geometry(
    "1100x780"
)

root.minsize(
    900,
    650
)

root.configure(
    bg="#E8F0FE"
)


# =========================================================
# ANALYZE BUTTON FUNCTION
# =========================================================

def analyze_text():

    text = text_box.get(
        "1.0",
        tk.END
    ).strip()

    if text == "":
        messagebox.showwarning(
            "Warning",
            "Please enter some text first!"
        )
        return

    (
        words,
        total_words,
        total_characters,
        total_sentences,
        total_paragraphs,
        total_unique_words,
        frequency
    ) = analyze_text_data(text)

    result_box.delete(
        "1.0",
        tk.END
    )

    # Header
    result_box.insert(
        tk.END,
        "╔══════════════════════════════════════════════════════╗\n"
    )

    result_box.insert(
        tk.END,
        "        WORD COUNTER & TEXT ANALYZER RESULT\n"
    )

    result_box.insert(
        tk.END,
        "╚══════════════════════════════════════════════════════╝\n\n"
    )

    # Statistics
    result_box.insert(
        tk.END,
        "📊 TEXT STATISTICS\n"
    )

    result_box.insert(
        tk.END,
        "──────────────────────────────────────────────────────\n"
    )

    result_box.insert(
        tk.END,
        f"  Total Words          : {total_words}\n"
    )

    result_box.insert(
        tk.END,
        f"  Total Characters     : {total_characters}\n"
    )

    result_box.insert(
        tk.END,
        f"  Total Sentences      : {total_sentences}\n"
    )

    result_box.insert(
        tk.END,
        f"  Total Paragraphs     : {total_paragraphs}\n"
    )

    result_box.insert(
        tk.END,
        f"  Unique Words         : {total_unique_words}\n"
    )

    result_box.insert(
        tk.END,
        "\n"
    )

    # Top 5
    result_box.insert(
        tk.END,
        "🏆 TOP 5 MOST USED WORDS\n"
    )

    result_box.insert(
        tk.END,
        "──────────────────────────────────────────────────────\n"
    )

    for i, (word, count) in enumerate(
        frequency.most_common(5),
        start=1
    ):
        result_box.insert(
            tk.END,
            f"  {i}. {word:<20} → {count} times\n"
        )

    result_box.insert(
        tk.END,
        "\n"
    )

    # Complete frequency
    result_box.insert(
        tk.END,
        "📚 COMPLETE WORD FREQUENCY\n"
    )

    result_box.insert(
        tk.END,
        "──────────────────────────────────────────────────────\n"
    )

    for word, count in frequency.most_common():
        result_box.insert(
            tk.END,
            f"  {word:<25} : {count}\n"
        )


# =========================================================
# OPEN FILE BUTTON
# =========================================================

def open_file_button():
    open_file(text_box)


# =========================================================
# GRAPH BUTTON
# =========================================================

def show_graph_button():

    text = text_box.get(
        "1.0",
        tk.END
    ).strip()

    if text == "":
        messagebox.showwarning(
            "Warning",
            "Please enter or open some text first!"
        )
        return

    words = get_words(text)

    if len(words) == 0:
        messagebox.showwarning(
            "Warning",
            "No words found!"
        )
        return

    frequency = Counter(words)

    show_graph(frequency)


# =========================================================
# SAVE BUTTON
# =========================================================

def save_report_button():
    save_report(result_box)


# =========================================================
# CLEAR BUTTON
# =========================================================

def clear_all_button():
    clear_all(
        text_box,
        result_box
    )


# =========================================================
# TITLE
# =========================================================

title = tk.Label(
    root,
    text="WORD COUNTER & TEXT ANALYZER",
    font=("Segoe UI", 25, "bold"),
    fg="#1A237E",
    bg="#E8F0FE"
)

title.pack(
    pady=(18, 5)
)


# =========================================================
# SUBTITLE
# =========================================================

description = tk.Label(
    root,
    text="Analyze words, characters, sentences, paragraphs and word frequency",
    font=("Segoe UI", 11),
    fg="#455A64",
    bg="#E8F0FE"
)

description.pack(
    pady=(0, 12)
)


# =========================================================
# INPUT FRAME
# =========================================================

input_frame = tk.Frame(
    root,
    bg="white",
    bd=2,
    relief="groove"
)

input_frame.pack(
    padx=25,
    pady=5,
    fill="both",
    expand=False
)


input_label = tk.Label(
    input_frame,
    text="📝  ENTER YOUR TEXT",
    font=("Segoe UI", 13, "bold"),
    fg="#283593",
    bg="white"
)

input_label.pack(
    anchor="w",
    padx=15,
    pady=(10, 5)
)


# =========================================================
# INPUT TEXT BOX
# =========================================================

text_box = tk.Text(
    input_frame,
    height=8,
    font=("Segoe UI", 12),
    wrap=tk.WORD,
    bg="#F8FAFF",
    fg="#263238",
    insertbackground="#1A237E",
    selectbackground="#9FA8DA",
    selectforeground="black",
    relief="flat",
    padx=10,
    pady=10
)

text_box.pack(
    padx=15,
    pady=(0, 15),
    fill="both"
)


# =========================================================
# BUTTON FRAME
# =========================================================

button_frame = tk.Frame(
    root,
    bg="#E8F0FE"
)

button_frame.pack(
    pady=15
)


button_font = (
    "Segoe UI",
    10,
    "bold"
)


# =========================================================
# ANALYZE BUTTON
# =========================================================

analyze_button = tk.Button(
    button_frame,
    text="🔍 Analyze",
    command=analyze_text,
    font=button_font,
    bg="#3949AB",
    fg="white",
    activebackground="#303F9F",
    activeforeground="white",
    width=15,
    height=2,
    relief="flat",
    cursor="hand2"
)

analyze_button.grid(
    row=0,
    column=0,
    padx=6
)


# =========================================================
# OPEN FILE BUTTON
# =========================================================

open_button = tk.Button(
    button_frame,
    text="📂 Open File",
    command=open_file_button,
    font=button_font,
    bg="#00897B",
    fg="white",
    activebackground="#00796B",
    activeforeground="white",
    width=15,
    height=2,
    relief="flat",
    cursor="hand2"
)

open_button.grid(
    row=0,
    column=1,
    padx=6
)


# =========================================================
# GRAPH BUTTON
# =========================================================

graph_button = tk.Button(
    button_frame,
    text="📊 Show Graph",
    command=show_graph_button,
    font=button_font,
    bg="#8E24AA",
    fg="white",
    activebackground="#7B1FA2",
    activeforeground="white",
    width=15,
    height=2,
    relief="flat",
    cursor="hand2"
)

graph_button.grid(
    row=0,
    column=2,
    padx=6
)


# =========================================================
# SAVE BUTTON
# =========================================================

save_button = tk.Button(
    button_frame,
    text="💾 Save Report",
    command=save_report_button,
    font=button_font,
    bg="#FB8C00",
    fg="white",
    activebackground="#EF6C00",
    activeforeground="white",
    width=15,
    height=2,
    relief="flat",
    cursor="hand2"
)

save_button.grid(
    row=0,
    column=3,
    padx=6
)


# =========================================================
# CLEAR BUTTON
# =========================================================

clear_button = tk.Button(
    button_frame,
    text="🗑 Clear",
    command=clear_all_button,
    font=button_font,
    bg="#E53935",
    fg="white",
    activebackground="#C62828",
    activeforeground="white",
    width=15,
    height=2,
    relief="flat",
    cursor="hand2"
)

clear_button.grid(
    row=0,
    column=4,
    padx=6
)


# =========================================================
# RESULT FRAME
# =========================================================

result_frame = tk.Frame(
    root,
    bg="white",
    bd=2,
    relief="groove"
)

result_frame.pack(
    padx=25,
    pady=5,
    fill="both",
    expand=True
)


result_label = tk.Label(
    result_frame,
    text="📊  ANALYSIS RESULT",
    font=("Segoe UI", 13, "bold"),
    fg="#283593",
    bg="white"
)

result_label.pack(
    anchor="w",
    padx=15,
    pady=(10, 5)
)


# =========================================================
# RESULT BOX
# =========================================================

result_box = tk.Text(
    result_frame,
    font=("Consolas", 11),
    wrap=tk.WORD,
    bg="#F8FAFF",
    fg="#263238",
    insertbackground="#1A237E",
    selectbackground="#9FA8DA",
    selectforeground="black",
    relief="flat",
    padx=15,
    pady=10
)

result_box.pack(
    padx=15,
    pady=(0, 15),
    fill="both",
    expand=True
)


# =========================================================
# FOOTER
# =========================================================

footer = tk.Label(
    root,
    text="Python Project | Word Counter & Text Analyzer",
    font=("Segoe UI", 9),
    fg="#607D8B",
    bg="#E8F0FE"
)

footer.pack(
    pady=5
)


# =========================================================
# RUN PROGRAM
# =========================================================

root.mainloop()