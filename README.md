# README.md

## How to Install and Run This Project

1. **Clone the project from GitHub**

   Open Command Prompt or Terminal and run:

   ```
   git clone https://github.com/Boypanu/Fridays.git
   ```

2. **Navigate to the project folder**

   ```
   cd Fridays
   ```

3. **Install required dependencies**

   It is recommended to use a Python virtual environment:

   ```
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```
   python app.py
   ```

5. **Test the API**

   Open your browser or use a tool like Postman and go to  
   [http://127.0.0.1:5000/api_1](http://127.0.0.1:5000/api_1)

---
**Note:**  
- Make sure you have Python 3.7 or higher installed.
- If you don't have a `requirements.txt` file, add the required libraries such as `flask`.

# Two APIs with Docker Compose

## 📦 Setup

1. Clone this repository
2. Run:

   ```bash
   docker-compose up --build
   ```