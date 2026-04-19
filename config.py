# GPIO pins
BUZZER, BTN = 17, 27
GREEN_LED, YELLOW_LED, RED_LED = 22, 23, 24

# Detection tuning
FS = 50
WINDOW_SEC = 4
BAND = (3, 6)
SEIZURE_CONFIRM_SEC = 10
RATIO_THRESHOLD = 0.4
AMP_MULTIPLIER = 5

# Shared files
DATA_FILE = "/tmp/seizureguard_data.json"
EVENTS_FILE = "/tmp/seizureguard_events.json"