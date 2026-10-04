import pandas as pd
import matplotlib.pyplot as plt

# Load flight data
data = pd.read_csv("data/sample_flight.csv")

# Create derived flight variable
data["climb_rate"] = data["altitude"].diff() / data["time"].diff()

def classify_phase(row):
    if row["airspeed"] == 0 and row["altitude"] == 0:
        return "Ground"
    elif row["climb_rate"] > 1:
        return "Climb"
    elif row["climb_rate"] < -1:
        return "Descent"
    else:
        return "Level Flight"

data["flight_phase"] = data.apply(classify_phase, axis=1)

# Detect takeoff
takeoff_rows = data[
    (data["flight_phase"] == "Climb") &
    (data["airspeed"] > 0)
]

if not takeoff_rows.empty:
    takeoff_time = takeoff_rows.iloc[0]["time"]
else:
    takeoff_time = None

# Detect landing
ground_rows = data[
    (data["flight_phase"] == "Ground") &
    (data["time"] > 0)
]

if not ground_rows.empty:
    landing_time = ground_rows.iloc[-1]["time"]
else:
    landing_time = None

phase_counts = data["flight_phase"].value_counts()

print("\nFLIGHT PHASE SUMMARY")
print("----------------------")

for phase, count in phase_counts.items():
    print(phase + ":", count, "seconds")

print("Takeoff Time:", takeoff_time, "s")
print("Landing Time:", landing_time, "s")

if takeoff_time is not None and landing_time is not None:
    airborne_time = landing_time - takeoff_time
    print("Airborne Time:", airborne_time, "s")




# Create 4 stacked graphs
fig, axes = plt.subplots(4, 1, figsize=(10, 10))

# -------------------------
# Altitude
# -------------------------
axes[0].plot(data["time"], data["altitude"])
axes[0].set_xlabel("Time (s)")
axes[0].set_ylabel("Altitude (m)")
axes[0].set_title("Altitude vs Time")
axes[0].grid()

# -------------------------
# Airspeed
# -------------------------
axes[1].plot(data["time"], data["airspeed"])
axes[1].set_xlabel("Time (s)")
axes[1].set_ylabel("Airspeed (m/s)")
axes[1].set_title("Airspeed vs Time")
axes[1].grid()

# -------------------------
# Pitch and Roll
# -------------------------
axes[2].plot(data["time"], data["pitch"], label="Pitch")
axes[2].plot(data["time"], data["roll"], label="Roll")

axes[2].set_xlabel("Time (s)")
axes[2].set_ylabel("Angle (deg)")
axes[2].set_title("Pitch and Roll vs Time")
axes[2].legend()
axes[2].grid()

# -------------------------
# Climb Rate
# -------------------------
axes[3].plot(data["time"], data["climb_rate"])

axes[3].set_xlabel("Time (s)")
axes[3].set_ylabel("Vertical Speed (m/s)")
axes[3].set_title("Climb Rate vs Time")
axes[3].grid()

# -------------------------
# Flight performance calculations
# -------------------------
max_altitude = data["altitude"].max()
max_airspeed = data["airspeed"].max()
average_airspeed = data["airspeed"].mean()

roll_std = data["roll"].std()
pitch_std = data["pitch"].std()

max_climb_rate = data["climb_rate"].max()
max_descent_rate = data["climb_rate"].min()

# -------------------------
# Flight summary
# -------------------------
print("\nFLIGHT SUMMARY")
print("----------------------")
print("Maximum Altitude:", max_altitude, "m")
print("Maximum Airspeed:", max_airspeed, "m/s")
print("Average Airspeed:", round(average_airspeed, 2), "m/s")
print("Roll Std Dev:", round(roll_std, 2), "deg")
print("Pitch Std Dev:", round(pitch_std, 2), "deg")
print("Maximum Climb Rate:", round(max_climb_rate, 2), "m/s")
print("Maximum Descent Rate:", round(max_descent_rate, 2), "m/s")

# Make graphs fit nicely
plt.tight_layout()

# Display graphs
plt.savefig("plots/flight_summary.png", dpi=300)
plt.show()