from twilio.rest import Client
import RPi.GPIO as GPIO
import time

ACCOUNT_SID = "your_sid_here"
AUTH_TOKEN = "your_token_here"
FROM_NUMBER = "+1xxxxxxxxxx"
TO_NUMBERS = ["+1yyyyyyyyyy"]

BUZZER = 17
BTN = 27
GREEN, YELLOW, RED = 22, 23, 24

GPIO.setmode(GPIO.BCM)
GPIO.setup([BUZZER, GREEN, YELLOW, RED], GPIO.OUT)
GPIO.setup(BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_sms(msg):
    for num in TO_NUMBERS:
        client.messages.create(body=msg, from_=FROM_NUMBER, to=num)

def trigger_alert():
    GPIO.output(RED, True)
    GPIO.output(BUZZER, True)
    send_sms(f"🚨 Seizure detected at {time.strftime('%H:%M:%S')}. Check immediately.")
    
    # Wait up to 60s for button press
    start = time.time()
    while time.time() - start < 60:
        if GPIO.input(BTN) == GPIO.LOW:
            GPIO.output(RED, False)
            GPIO.output(BUZZER, False)
            return
        time.sleep(0.1)
    
    # No ack — escalate
    send_sms("⚠️ No acknowledgment received. Escalating.")
    GPIO.output(BUZZER, False)  # stop buzzer eventually
