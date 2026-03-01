# 🚀 GitHub Profile Fetcher

A professional web application built with **Python** and **Streamlit** that utilizes the **GitHub REST API** to retrieve and display user profile data in a clean, interactive dashboard.

---

## ✨ Features
* **Real-time API Integration:** Fetches live data from GitHub servers.
* **Interactive Dashboard:** Displays user avatars, bios, and locations.
* **Live Metrics:** Uses `st.metric` for Repo counts, Followers, and Following.
* **Direct Profile Linking:** Clickable Markdown links to visit profiles instantly.
* **Error Handling:** Built-in alerts for "User Not Found" and connection timeouts.

---

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Framework:** Streamlit
* **Libraries:** Requests (HTTP Client)

---

## 🚀 Installation & Setup

1. Clone the Project:
   ```git clone https://github.com/Ilyan321/Python-Learning.git```
2. Goto Project folder
   ```cd Python-Learning/Project```

3. Install Dependencies:
   pip install streamlit requests

4. Run the Application:
   streamlit run main.py

---

## 📖 How to Use
1. Launch the app in your browser (usually at http://localhost:8501).
2. Type any valid GitHub username (e.g., Ilyan321) into the text box.
3. Click the "Fetch Profile" button to generate the profile card.

---

## 🛠️ Code Overview
The application follows a modular structure:
* fetch_github(): Handles the API request, status code validation, and JSON parsing.
* UI Layer: Uses Streamlit's columns and metrics for a responsive layout.
* Error Management: Implements try-except blocks to prevent app crashes.

---
**Developed by [Ilyan Khan](https://github.com/Ilyan321)**
