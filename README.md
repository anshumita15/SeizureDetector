# Buildthon

# 🌙 SeizureDetector

Contactless under-mattress seizure detection and alerting system for nighttime monitoring.

## The Problem
~1 in 1000 people with epilepsy die of SUDEP (Sudden Unexpected Death in Epilepsy) each year. Most die alone, at night. Existing monitors cost $300+ and aren't accessible in low-resource settings.

## Our Solution
A Raspberry Pi + accelerometer ($50 in parts) that:
- Detects tonic-clonic seizures via rhythmic mattress vibrations (3–6 Hz)
- Sounds a local alarm and SMS-alerts caregivers via Twilio
- Escalates if no acknowledgement within 60 seconds
- Logs events to a real-time web dashboard for clinicians

## Hardware
- Raspberry Pi 4
- GY-521 (MPU6050) accelerometer
- Piezo buzzer, LEDs, push-button
- I2C LCD (optional)

## Software
| File | Purpose |
|------|---------|
| `logger.py` | Records sensor data to CSV |
| `analyze.py` | Computes stats on recorded data |
| `detector.py` | FFT-based seizure detection |
| `alerts.py` | Buzzer, LEDs, and Twilio SMS |
| `dashboard.py` | Flask web UI for live monitoring |

## Setup
```bash
pip install -r requirements.txt --break-system-packages
cp .env.example .env  # fill in Twilio credentials
python3 detector.py   # in one terminal
python3 dashboard.py  # in another
```

## Built at [Hackathon Name] in 24 hours.