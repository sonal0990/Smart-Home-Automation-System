from flask import Flask, render_template, redirect
import sqlite3
import os

app = Flask(__name__)

def get_devices():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # 🔍 Debug info
    tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    print("🧩 Tables in DB:", tables)

    devices = cursor.execute("SELECT * FROM devices").fetchall()
    print("📦 Devices loaded:", devices)

    conn.close()
    return devices

@app.route("/")
def dashboard():
    devices = get_devices()
    return render_template("dashboard.html", devices=devices)

@app.route("/toggle/<int:device_id>")
def toggle_device(device_id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT status FROM devices WHERE id=?", (device_id,))
    status = cursor.fetchone()[0]
    new_status = "OFF" if status == "ON" else "ON"
    cursor.execute("UPDATE devices SET status=? WHERE id=?", (new_status, device_id))
    conn.commit()
    conn.close()

    return redirect("/")

if __name__ == "__main__":
    print("✅ Current working directory:", os.getcwd())
    print("✅ Database exists:", os.path.exists("database.db"))
    app.run(debug=True)
