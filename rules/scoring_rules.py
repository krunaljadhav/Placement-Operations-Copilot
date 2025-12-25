# rules/scoring_rules.py

# Weightage of each skill in overall readiness
SKILL_WEIGHTS = {
    "Excel": 0.15,
    "SQL": 0.20,
    "Python": 0.20,
    "Statistics & Probability": 0.20,
    "Machine Learning": 0.15,
    "Tableau & Power BI": 0.10
}

# Readiness thresholds
READINESS_THRESHOLDS = {
    "READY": 75,
    "ALMOST_READY": 60
}

# Minimum acceptable score per skill
MIN_SKILL_SCORE = 50
