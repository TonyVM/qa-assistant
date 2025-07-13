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
    elif type_ == "Gherkin User Stories":
        # Parse Gherkin features and scenarios
        features = re.split(r"\n\n(?=Feature:)", output_text.strip())
        data = []
        for feature in features:
            feature_match = re.search(r"Feature:\s*(.+)", feature)
            feature_name = feature_match.group(1) if feature_match else ""
            
            # Extract user story (As a... I want... So that...)
            user_story_lines = []
            for line in feature.split('\n')[1:]:
                if line.strip().startswith('As a') or line.strip().startswith('I want') or line.strip().startswith('So that'):
                    user_story_lines.append(line.strip())
                elif line.strip().startswith('Scenario:'):
                    break
            user_story = ' '.join(user_story_lines)
            
            # Extract scenarios
            scenarios = re.findall(r"Scenario:\s*(.+?)(?=\n\s*Scenario:|\n\s*Feature:|\Z)", feature, re.DOTALL)
            
            if not scenarios:
                # If no scenarios found, add just the feature
                data.append({
                    "Feature": feature_name,
                    "User Story": user_story,
                    "Scenario": "",
                    "Steps": ""
                })
            else:
                for scenario in scenarios:
                    scenario_lines = scenario.strip().split('\n')
                    scenario_name = scenario_lines[0] if scenario_lines else ""
                    
                    # Extract Given/When/Then steps
                    steps = []
                    for line in scenario_lines[1:]:
                        line = line.strip()
                        if line.startswith(('Given', 'When', 'Then', 'And', 'But')):
                            steps.append(line)
                    
                    data.append({
                        "Feature": feature_name,
                        "User Story": user_story,
                        "Scenario": scenario_name,
                        "Steps": ' | '.join(steps)
                    })
        
        df = pd.DataFrame(data)
    else:
        rows = output_text.strip().split("\n")
        df = pd.DataFrame({"Output": rows})

    filename = f"outputs/{type_.replace(' ', '_').lower()}_{timestamp}.csv"
    df.to_csv(filename, index=False)
    return filename
