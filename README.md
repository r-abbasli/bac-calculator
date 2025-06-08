# 🧪 BAC Calculator

A Flask-based web app that estimates users' Blood Alcohol Concentration (BAC) based on their gender, weight, drinking time, and alcohol intake.

## 🚀 Features
- Input gender, weight (kg/lbs), start time, and drink types/amounts.
- Calculates current BAC using the **Widmark Formula**.
- Displays time required for BAC to return to 0.
- Handles invalid input gracefully.

## 👤 Who Is It For?
- **General users**: to estimate their BAC and make safe choices.
- **Learners**: looking to understand Flask, form handling, and web app logic.
- **Recruiters**: showcases backend development and error-handling skills.

## 🛠️ Tech Stack
- Python 3
- Flask
- HTML/CSS (with Jinja2 templating)
- JavaScript (for auto time input)

## 📂 Project Structure
- `app.py`: Main Flask app logic
- `templates/`: Contains `layout.html`, `index.html`, `results.html`, and `error.html`
- `static/`: (optional, for custom styling if added)

## 🧮 How It Works
- Uses user input and time delta to calculate BAC.
- Alcohol values based on predefined drink list.
- Decrease rate: 0.016 per hour (Widmark average).

## 📺 Demo
[Watch on YouTube](https://www.youtube.com/watch?v=Tg2UdCoMSzM)
