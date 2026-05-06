import pandas as pd
import matplotlib.pyplot as plt

file_name = "fall_data.csv"

# -------------------------------
# MANUAL SAFE READ
# -------------------------------
rows = []

with open(file_name, "r") as file:
    for line in file:
        line = line.strip()

        # Skip empty lines or session markers
        if not line or "NEW SESSION" in line:
            continue

        parts = line.split(",")

        # Only keep valid sensor rows (must have 6 columns)
        if len(parts) == 6 and parts[0] != "time":
            rows.append(parts)

# Create dataframe manually
df = pd.DataFrame(rows, columns=["time", "ax", "ay", "az", "accMag", "status"])

# Convert numeric
df["accMag"] = pd.to_numeric(df["accMag"], errors="coerce")
df = df.dropna(subset=["accMag"])

df["index"] = range(len(df))

# -------------------------------
# FALL DETECTION POINTS
# -------------------------------
fall_points = df[df["status"].str.contains("FALL", na=False)]

# -------------------------------
# PLOT
# -------------------------------
plt.figure(figsize=(10,5))

plt.plot(df["index"], df["accMag"], linewidth=2)
plt.scatter(fall_points["index"], fall_points["accMag"], s=80)

plt.xlabel("Time (samples)")
plt.ylabel("accMag")
plt.title("Fall Detection Graph")

plt.grid(True)

plt.show()