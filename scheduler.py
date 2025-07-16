from apscheduler.schedulers.background import BackgroundScheduler
import sqlite3
from datetime import datetime
import paho.mqtt.publish as publish

def check_schedule():
    now = datetime.now().strftime("%H:%M")
    conn = sqlite3.connect("database.db")
    rows = conn.execute("SELECT * FROM schedule WHERE time=?", (now,)).fetchall()
    for row in rows:
        device_id, action = row[1], row[3]
        device = conn.execute("SELECT name FROM devices WHERE id=?", (device_id,)).fetchone()
        if device:
            publish.single(f"home/device/{device[0]}", action, hostname="localhost")
            conn.execute("UPDATE devices SET status=? WHERE id=?", (action, device_id))
    conn.commit()
    conn.close()

scheduler = BackgroundScheduler()
scheduler.add_job(check_schedule, 'interval', minutes=1)
scheduler.start()
