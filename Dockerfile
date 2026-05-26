# 1. THE STOVE: We tell Docker to download a mini-computer that already has Python 3.10 installed.
FROM python:3.10-slim

# 2. THE KITCHEN: We create a folder inside this mini-computer called /app and move inside it.
WORKDIR /app

# 3. THE INGREDIENTS: Copy our "node_modules" equivalent list (we will create this next!)
# This is just a text file listing fastapi, pandas, scikit-learn, etc.
COPY requirements.txt .

# 4. PREP WORK: Install the exact tools needed using pip.
RUN pip install --no-cache-dir -r requirements.txt

# 5. THE RECIPE: Copy our server.py and our AI brain (.joblib file) into the mini-computer.
COPY . .

# 6. OPEN FOR BUSINESS: Tell the mini-computer exactly what command to run when it turns on.
# This is the exact same command you typed in your Windows terminal!
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]