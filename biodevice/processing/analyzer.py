class Analyzer:
    def __init__(self, llm):
        self.llm = llm

    def analyze(self, readings):
        sensor_text = "\n".join(
            f"{r['sensor_id']}: {r['value']} {r['unit']}"
            for r in readings
        )
        prompt = f"""
You are the local analysis component of an offline sensor device.

The following measurements were collected:
{sensor_text}

Describe the measurements in a concise, structured way.
Do not invent measurements.
Do not diagnose medical conditions.
Do not claim certainty when the data is incomplete.
"""
        return self.llm.generate(prompt)
