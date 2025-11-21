from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory database for demonstration purposes
db = {
    "moeed": {"pin_number": 1234, "bank_balance": 1000.0},
    "ali": {"pin_number": 5678, "bank_balance": 500.0},
}

class User(BaseModel):
    name: str
    pin_number: int

class Transfer(BaseModel):
    sender_name: str
    receipents_name: str
    amount: float

class DepositRequest(BaseModel):
    amount: float

class WithdrawRequest(BaseModel):
    amount: float

@app.post("/authenticate")
async def authenticate(user: User):
    """
    Authenticates a user and returns their bank balance.
    """
    if user.name not in db:
        raise HTTPException(status_code=404, detail="User not found")
    if db[user.name]["pin_number"] != user.pin_number:
        raise HTTPException(status_code=401, detail="Invalid pin number")
    return {"name": user.name, "bank_balance": db[user.name]["bank_balance"]}

@app.post("/bank-transfer")
async def bank_transfer(transfer: Transfer):
    """
    Transfers an amount from one user to another and authenticates the receiver.
    """
    if transfer.sender_name not in db:
        raise HTTPException(status_code=404, detail="Sender not found")
    if transfer.receipents_name not in db:
        raise HTTPException(status_code=404, detail="Recipient not found")
    if db[transfer.sender_name]["bank_balance"] < transfer.amount:
        raise HTTPException(status_code=400, detail="Insufficient funds")

    # Perform the transfer
    db[transfer.sender_name]["bank_balance"] -= transfer.amount
    db[transfer.receipents_name]["bank_balance"] += transfer.amount

    # Authenticate the receiver to show the updated balance
    # by calling the authenticate function directly.
    receipent_user = User(name=transfer.receipents_name, pin_number=db[transfer.receipents_name]["pin_number"])
    return await authenticate(receipent_user)

current_user = "moeed" # Simulating an authenticated user for these endpoints

@app.get("/balance/{username}")
async def get_balance(username: str):
    if username not in db:
        raise HTTPException(status_code=404, detail="User not found")
    if username != current_user:
        raise HTTPException(status_code=403, detail="Access denied")
    return {"username": username, "balance": db[username]["bank_balance"]}

@app.post("/deposit/{username}")
async def deposit(username: str, request: DepositRequest):
    if username not in db:
        raise HTTPException(status_code=404, detail="User not found")
    if username != current_user:
        raise HTTPException(status_code=403, detail="Access denied")
    if request.amount <= 0:
        raise HTTPException(status_code=400, detail="Deposit amount must be positive")
    
    db[username]["bank_balance"] += request.amount
    return {"username": username, "new_balance": db[username]["bank_balance"]}

@app.post("/withdraw/{username}")
async def withdraw(username: str, request: WithdrawRequest):
    if username not in db:
        raise HTTPException(status_code=404, detail="User not found")
    if username != current_user:
        raise HTTPException(status_code=403, detail="Access denied")
    if request.amount <= 0:
        raise HTTPException(status_code=400, detail="Withdrawal amount must be positive")
    if db[username]["bank_balance"] < request.amount:
        raise HTTPException(status_code=400, detail="Insufficient funds")
    
    db[username]["bank_balance"] -= request.amount
    return {"username": username, "new_balance": db[username]["bank_balance"]}
