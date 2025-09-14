import pandas as pd
file_path = "Passwords.txt"  
record = []  
entry = {}   
with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
            line = line.strip()
            if line.startswith("URL:"):
                entry["url"] = line.replace("URL:", "").strip()
            elif line.startswith("USER:"):
                entry["username"] = line.replace("USER:", "").strip()
            elif line.startswith("PASS:"):
                entry["password"] = line.replace("PASS:", "").strip()
                record.append(entry)
                entry = {}
df = pd.DataFrame(record)
df = df.drop_duplicates()
print("DataFrame Rows:")
print(df)
print(f"\nTotal number of records: {len(df)}")
df.to_json("breaches.json", orient="records", lines=False)

