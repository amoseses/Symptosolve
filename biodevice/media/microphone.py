from pathlib import Path
from datetime import datetime

class Microphone:
    def __init__(self, output_directory="data/audio"):
        self.output_directory = Path(output_directory)
        self.output_directory.mkdir(parents=True, exist_ok=True)

    def record(self, duration_seconds=5):
        filename = self.output_directory / f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
        print(f"[MIC] Would record {duration_seconds}s -> {filename}")
        return str(filename)
