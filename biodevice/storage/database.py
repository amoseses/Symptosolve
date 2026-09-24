import sqlite3

class Database:
    def __init__(self, database_path):
        self.connection = sqlite3.connect(database_path, check_same_thread=False)
        self.create_tables()

    def create_tables(self):
        self.connection.execute("""
            CREATE TABLE IF NOT EXISTS sensor_readings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                sensor_id TEXT NOT NULL,
                value REAL NOT NULL,
                unit TEXT NOT NULL
            )
        """)
        self.connection.commit()

    def save_readings(self, readings):
        for reading in readings:
            self.connection.execute(
                "INSERT INTO sensor_readings (timestamp, sensor_id, value, unit) VALUES (?, ?, ?, ?)",
                (reading.timestamp, reading.sensor_id, reading.value, reading.unit)
            )
        self.connection.commit()

    def recent_readings(self, limit=20):
        cursor = self.connection.execute(
            "SELECT timestamp, sensor_id, value, unit FROM sensor_readings ORDER BY id DESC LIMIT ?",
            (limit,)
        )
        return [
            {"timestamp": r[0], "sensor_id": r[1], "value": r[2], "unit": r[3]}
            for r in cursor.fetchall()
        ]
