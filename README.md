# UAV Flight Data Analyzer

A Python-based tool for analyzing UAV flight telemetry from CSV data.

The analyzer processes time-series flight data, derives basic performance metrics, classifies flight phases, detects takeoff and landing events, quantifies attitude variation, and generates a flight-analysis dashboard.

## Features

- Reads flight telemetry from CSV files
- Calculates climb and descent rate
- Detects basic flight phases:
  - Ground
  - Climb
  - Level Flight
  - Descent
- Detects takeoff and landing times
- Calculates airborne time
- Calculates flight performance metrics
- Quantifies attitude variation using pitch and roll standard deviation
- Generates a flight-analysis dashboard
- Saves the dashboard automatically as an image

## Current Metrics

The analyzer currently calculates:

- Maximum altitude
- Maximum airspeed
- Average airspeed
- Maximum climb rate
- Maximum descent rate
- Roll standard deviation
- Pitch standard deviation
- Takeoff time
- Landing time
- Airborne time

## Sample Data

The included `data/sample_flight.csv` file contains synthetic flight telemetry used to test and demonstrate the analyzer's functionality.

The current dataset includes:

- Time
- Altitude
- Airspeed
- Pitch
- Roll
- Yaw
- X-axis acceleration
- Y-axis acceleration
- Z-axis acceleration

The current version is designed around CSV-formatted telemetry. Real ArduPilot flight-log support is planned as a future improvement.

## Technologies

- Python
- Pandas
- Matplotlib

## Project Structure

```text
uav-flight-data-analyzer/
├── data/
│   └── sample_flight.csv
├── plots/
│   └── flight_summary.png
├── src/
│   └── analyzer.py
├── .gitignore
├── README.md
└── requirements.txt