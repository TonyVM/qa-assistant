PROMPTS = {
    "User Stories": "Act as a QA analyst. From the following requirement text, extract multiple user stories and number each one in the format: 1. As a <role>, I want to <goal> so that <benefit>'. Separate each with a line break:",
    "Test Scenarios": "Act as a QA engineer. Analyze each requirement and generate multiple detailed test scenarios. Separate each scenario with a line break and enumerate them. Make sure each requirement can have more than one scenario:",
    "Test Cases": "Act as a senior QA tester. For each requirement described below, generate several test cases (positive cases, negative cases, edge cases), use the following format:\\n\n    ID: TC-001\n    Title: <Short title>\n    Steps:\n    1. Step one\n    2. Step two\n    Expected Result: <What should happen>\n\nSeparate each test case with two line breaks.",
}
