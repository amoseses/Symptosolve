from pathlib import Path
from datetime import datetime

class Camera:
    def __init__(self, output_directory="data/images"):
        self.output_directory = Path(output_directory)
        self.output_directory.mkdir(parents=True, exist_ok=True)

    def capture(self):
        filename = self.output_directory / f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        print(f"[CAMERA] Would capture: {filename}")
        return str(filename)
