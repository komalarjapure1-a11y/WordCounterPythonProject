#  Word Counter & Text Analyzer

A **Python-based desktop application** that analyzes text and provides meaningful statistics such as word count, character count, sentence count, paragraph count, unique words, and word frequency.

The application provides a simple and user-friendly **Graphical User Interface (GUI)** built with **Tkinter**. It also includes frequency visualization using **Matplotlib**, allowing users to understand which words are most frequently used in a text.

---

## Project Overview

**Word Counter & Text Analyzer** is designed to make text analysis quick, simple, and interactive.

Instead of manually counting words, sentences, or characters, users can enter or open a text file and instantly view detailed statistics.

The application also performs **word frequency analysis** and displays the **Top 10 most frequently used words** through a graphical representation.

###  Main Goal

The main objective of this project is to develop a simple and efficient text analysis tool that can:

* Analyze textual content automatically
* Generate useful text statistics
* Identify frequently used words
* Visualize word frequency
* Open and analyze text files
* Generate and save an analysis report

---

#  Features

###  Text Statistics

The application calculates:

* **Total Words** – Number of words present in the text
* **Total Characters** – Number of characters in the text
* **Total Sentences** – Number of sentences detected
* **Total Paragraphs** – Number of paragraphs
* **Unique Words** – Number of different words used

###  Word Frequency Analysis

The application analyzes how often each word appears in the given text.

It provides:

* Word frequency count
* Most frequently used words
* **Top 10 frequently used words**

###  Frequency Visualization

The Top 10 most frequently used words are displayed using a **graph**, making the results easier to understand visually.

###  File Handling

Users can:

* Enter text manually
* Open existing text files
* Analyze file content directly

###  Report Management

The application allows users to:

* Save the generated analysis report
* Clear the input text
* Clear the output/results

###  User-Friendly Interface

The application provides an easy-to-use GUI with:

* Input area
* Analysis/output section
* Buttons for different operations
* Button hover effects
* Graph visualization

---

#  Project Modules

The project is divided into four major modules.

## Module 1 – Input & File Handling

This module manages all text input and file-related operations.

### Responsibilities:

* Accept text from the user
* Open text files
* Read file contents
* Display the text in the application

---

## Module 2 – Text Processing & Statistics

This module processes the entered text and calculates important statistics.

### Responsibilities:

* Count total words
* Count total characters
* Count sentences
* Count paragraphs
* Identify unique words
* Process text using Regular Expressions

---

## Module 3 – Frequency Analysis & Visualization

This module performs detailed word-frequency analysis.

### Responsibilities:

* Calculate word frequency
* Sort words according to frequency
* Identify Top 10 frequently used words
* Generate frequency graphs using Matplotlib

---

## Module 4 – Output & Report Management

This module manages the final output and application controls.

### Responsibilities:

* Display analysis results
* Save analysis reports
* Clear input text
* Clear output/results
* Provide button hover effects

---

#  Technologies Used

| Technology                   | Purpose                              |
| ---------------------------- | ------------------------------------ |
| **Python**                   | Core programming language            |
| **Tkinter**                  | GUI development                      |
| **Regular Expressions (re)** | Text processing and pattern matching |
| **Collections Counter**      | Word-frequency calculation           |
| **Matplotlib**               | Graph and data visualization         |

---

#  Application Workflow

The basic working process of the application is:

```text
        Start Application
               ↓
        Enter / Open Text
               ↓
        Process Text Data
               ↓
     ┌─────────┴─────────┐
     ↓                   ↓
Text Statistics     Frequency Analysis
     ↓                   ↓
Word Count          Word Frequency
Character Count     Top 10 Words
Sentence Count           ↓
Paragraph Count     Frequency Graph
Unique Words
     ↓                   ↓
     └─────────┬─────────┘
               ↓
        Display Results
               ↓
       Save Analysis Report
               ↓
              End
```

---

# Project Structure

A suggested project structure is:

```text
Word-Counter-Text-Analyzer/
│
├── main.py
├── README.md
├── requirements.txt
│
└── screenshots/
    ├── home.png
    ├── analysis.png
    └── graph.png
```

> If your project contains additional Python files, images, or folders, add them to this structure accordingly.

---

#  Installation & Setup

## 1. Install Python

Make sure **Python 3.x** is installed on your computer.

Check the installation using:

```bash
python --version
```

---

## 2. Clone or Download the Project

Download the project files to your computer.

Open the project folder in **VS Code** or another Python-supported IDE.

---

## 3. Install Required Libraries

Install Matplotlib using:

```bash
pip install matplotlib
```

### Tkinter

Tkinter is generally included with standard Python installations on Windows.

---

# How to Run

Open the project folder in the terminal and execute:

```bash
python main.py
```

The application window will open.

### Basic Usage

1. Enter or paste text into the input area.
2. Click the **Analyze** button.
3. View the generated text statistics.
4. Check the word-frequency results.
5. View the Top 10 frequency graph.
6. Save the analysis report if required.
7. Use **Clear** to reset the input and output.

---

#  Example Analysis

For example, if the input contains:

```text
Python is easy to learn.
Python is powerful and easy to use.
```

The application can provide information such as:

```text
Total Words       : 10
Total Characters  : ...
Total Sentences   : 2
Total Paragraphs  : 1
Unique Words      : ...
```

It can also identify frequently occurring words and display the **Top 10 Words** in a graph.

---

#  Objectives

The major objectives of this project are:

1. To develop a simple text analysis application using Python.
2. To calculate important text statistics automatically.
3. To analyze word frequency efficiently.
4. To visualize frequently used words using graphs.
5. To provide text-file handling functionality.
6. To generate and save analysis reports.
7. To create an easy-to-use graphical interface.

---

#  Advantages

* Simple and easy-to-use interface
* Fast text analysis
* Automatic calculation of statistics
* Supports text-file input
* Provides word-frequency analysis
* Graphical representation of data
* Report-saving functionality
* Useful for students, writers, and basic text analysis tasks

---

#  Future Enhancements

The project can be improved further by adding:

* Support for multiple file formats such as PDF and DOCX
*  Stop-word removal
*  Sentiment analysis
*  Word cloud generation
*  Additional charts and statistics
*  Multi-language text analysis
*  Keyword extraction
* Readability score calculation
*  Export reports in PDF and Excel formats
* AI-based text summarization

---

# Learning Outcomes

Through this project, the developer gains practical knowledge of:

* Python programming
* GUI development using Tkinter
* File handling
* Regular Expressions
* Text processing
* Data structures
* Word-frequency analysis
* Data visualization
* Modular programming
* Basic software development concepts

---

# Project Scope

The application can be useful in different areas such as:

* **Education** – Basic text and assignment analysis
* **Writing** – Checking word and character counts
* **Content Creation** – Understanding frequently used words
* **Data Analysis** – Basic textual data processing
* **Programming Learning** – Demonstrating Python GUI and text-processing concepts

---

# Testing

The application can be tested using different types of input:

| Test Case           | Expected Result                   |
| ------------------- | --------------------------------- |
| Empty input         | Shows zero/empty statistics       |
| Single word         | Counts one word                   |
| Multiple sentences  | Correctly counts sentences        |
| Multiple paragraphs | Correctly identifies paragraphs   |
| Repeated words      | Calculates frequency              |
| Text file           | Opens and analyzes file content   |
| Clear button        | Removes input/output              |
| Save report         | Creates analysis report           |
| Large text          | Processes and displays statistics |

---

# Project Information

**Project Name:** Word Counter & Text Analyzer
**Language:** Python
**Interface:** Tkinter GUI
**Visualization:** Matplotlib
**Text Processing:** Regular Expressions
**Frequency Analysis:** Collections Counter

---

# Conclusion

**Word Counter & Text Analyzer** is a practical Python application that combines **text processing, statistical analysis, file handling, GUI development, and data visualization** into a single user-friendly tool.

The project demonstrates how Python can be used to transform raw text into meaningful information through automated analysis and graphical representation.

It provides a strong foundation for developing more advanced applications involving **Natural Language Processing (NLP), data analysis, and intelligent text-processing systems** in the future.



