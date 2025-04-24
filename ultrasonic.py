import RPi.GPIO as GPIO
import time
import sqlite3

GPIO.setmode(GPIO.BCM)

trig = 23
echo = 24

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

LOW = 0
HIGH = 1
SPEED_OF_SOUND = 34300  # cm/s
ALERT_THRESHOLD_CM = 15

def measure_distance():
    GPIO.output(trig, HIGH)
    time.sleep(0.00001)  # 10 microsecond pulse
    GPIO.output(trig, LOW)

    pulse_start_time = time.time()
    pulse_end_time = time.time()
    while GPIO.input(echo) == LOW:
        pulse_start_time = time.time()
    while GPIO.input(echo) == HIGH:
        pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time
    distance_cm = (pulse_duration * SPEED_OF_SOUND) / 2
    return distance_cm

def check_and_alert(distance):
    if distance <= ALERT_THRESHOLD_CM:
        print("ALERT! Object is within 15 cm.")


i = 0
con=sqlite3.connect('ultrasonic_dist_db.db')
cursor=con.cursor()
while i < 20:  
    distance = measure_distance()
    print(f"Distance: {distance:.2f} cm (iteration {i+1})")
    check_and_alert(distance)
    status = 'NORMAL' if distance > ALERT_THRESHOLD_CM else 'Object detected within 15 cm'
    cursor.execute('''INSERT INTO DISTANCE_DATA_BASE(DISTANCE, STATUS) VALUES (?, ?)''', (distance, status))
    con.commit()    
    time.sleep(0.5)  
    i += 1

GPIO.cleanup()