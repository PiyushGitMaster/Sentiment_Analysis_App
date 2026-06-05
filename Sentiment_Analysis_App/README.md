# Sentiment Analysis Web App

A Flask web application that performs sentiment analysis on user-entered text using TextBlob. The app classifies text as Positive, Negative, or Neutral and displays polarity and subjectivity scores.

## Features

- 🔍 Accepts user input via a simple web form
- 😊 Classifies sentiment as Positive, Negative, or Neutral
- 📊 Shows **Polarity Score** (-1 to +1) – how positive or negative the text is
- 💭 Shows **Subjectivity Score** (0 to 1) – how factual vs opinionated the text is
- 🎨 Clean, responsive UI with gradient background
- ⚡ Fast, lightweight, and easy to use

## Tech Stack

- **Flask** – Web framework (backend)
- **TextBlob** – NLP library for sentiment analysis
- **HTML/CSS** – Frontend (templates)

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Steps

1. **Clone or download** this project folder.

2. **Open Terminal** in the project root directory.

3. **Create a virtual environment (optional but recommended)**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On macOS/Linux