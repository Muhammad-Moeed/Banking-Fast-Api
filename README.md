# Mini Banking API (FastAPI + AI Driven Development)

This is a simple **Banking API** built using **FastAPI**, developed with an AI-driven approach using the GMEINI CLI.  
The API allows users to authenticate, check balance, transfer funds, deposit, and withdraw money — all through clean REST endpoints.

---

## 🚀 Features

- User authentication (name + pin)
- Check account balance
- Bank-to-bank transfer
- Deposit amount
- Withdraw amount
- Swagger UI auto-documentation

---

## 📁 Project Structure

---

## 🛠️ Installation & Setup

### 1️⃣ Create a virtual environment 
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows

### 2️⃣ Install dependencies
uv install -r requirements.txt

### 3️⃣ Run the FastAPI server  
uvicorn main:app --reload

### 4️⃣ Open API docs  
Swagger UI available at: http://127.0.0.1:8000/docs


---

## 🔗 API Endpoints

### **POST /authenticate**
Authenticate user and return balance.

### **POST /bank-transfer**
Transfer funds between two users.

### **GET /balance/{username}**
Get account balance of a specific user.

### **POST /deposit/{username}**
Deposit money.

### **POST /withdraw/{username}**
Withdraw money.

---

## 📌 Technologies Used

- FastAPI
- Uvicorn
- Pydantic
- Python 3.10+
- GMEINI CLI (AI-Driven Development)

