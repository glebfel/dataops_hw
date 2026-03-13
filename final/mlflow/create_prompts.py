import mlflow

mlflow.set_tracking_uri("http://localhost:5000")

# Prompt v1
mlflow.register_prompt(
    name="diabetes_risk_assessment",
    template=(
        "You are a medical assistant. Based on the following patient data:\n"
        "Age: {{age}}, BMI: {{bmi}}, Blood Pressure: {{bp}}\n"
        "Provide a brief diabetes risk assessment."
    ),
    commit_message="v1: basic risk assessment prompt",
)

# Prompt v2
mlflow.register_prompt(
    name="diabetes_risk_assessment",
    template=(
        "You are an experienced endocrinologist AI assistant.\n"
        "Patient data: Age={{age}}, Sex={{sex}}, BMI={{bmi}}, BP={{bp}}, "
        "S1={{s1}}, S2={{s2}}, S3={{s3}}, S4={{s4}}, S5={{s5}}, S6={{s6}}\n"
        "Predicted progression value: {{prediction}}\n\n"
        "Provide a detailed diabetes risk assessment with recommendations."
    ),
    commit_message="v2: detailed prompt with all features and prediction",
)

# Prompt v3
mlflow.register_prompt(
    name="diabetes_risk_assessment",
    template=(
        "Role: Senior endocrinologist AI\n"
        "Task: Analyze diabetes progression risk\n\n"
        "Patient profile:\n"
        "- Age: {{age}}, Sex: {{sex}}\n"
        "- BMI: {{bmi}}, Blood Pressure: {{bp}}\n"
        "- Serum measurements: S1={{s1}}, S2={{s2}}, S3={{s3}}, S4={{s4}}, S5={{s5}}, S6={{s6}}\n"
        "- Model prediction (progression index): {{prediction}}\n\n"
        "Please provide:\n"
        "1. Risk level (low / medium / high)\n"
        "2. Key risk factors identified\n"
        "3. Recommended lifestyle changes\n"
        "4. Suggested follow-up timeline"
    ),
    commit_message="v3: structured output with risk level and recommendations",
)

# Second prompt - data quality
mlflow.register_prompt(
    name="data_quality_check",
    template=(
        "Review the following patient input data for potential issues:\n"
        "{{input_json}}\n\n"
        "Check for: missing values, outliers, physiologically impossible values.\n"
        "Return a JSON with fields: is_valid (bool), issues (list of strings)."
    ),
    commit_message="v1: data quality validation prompt",
)

print("Prompts created successfully!")
