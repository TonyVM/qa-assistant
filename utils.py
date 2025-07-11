import pandas as pd
import os
from datetime import datetime
import re


def save_to_csv(output_text: str, type_: str) -> str:
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    os.makedirs("outputs", exist_ok=True)

    if type_ == "Test Cases":
        cases = re.split(r"\n\n+", output_text.strip())
        data = []
        for case in cases:
            id_match = re.search(r"ID:\s*(.+)", case)
            title_match = re.search(r"Title:\s*(.+)", case)
            steps_match = re.findall(r"\d+\.\s+(.+)", case)
            expected_match = re.search(r"Expected Result:\s*(.+)", case)
            data.append(
                {
                    "ID": id_match.group(1) if id_match else "",
                    "Title": title_match.group(1) if title_match else "",
                    "Steps": " | ".join(steps_match),
                    "Expected Result": (
                        expected_match.group(1) if expected_match else ""
                    ),
                }
            )
        df = pd.DataFrame(data)
    else:
        rows = output_text.strip().split("\n")
        df = pd.DataFrame({"Output": rows})

    filename = f"outputs/{type_.replace(' ', '_').lower()}_{timestamp}.csv"
    df.to_csv(filename, index=False)
    return filename
