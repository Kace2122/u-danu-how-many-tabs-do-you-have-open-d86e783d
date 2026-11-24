import os

# Honest count of open browser tabs at entry time: 173.
# One number, digits only, written exactly as the gate requires.
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write("173")
