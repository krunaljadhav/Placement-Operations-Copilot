# 🧠 Placement Operations Copilot
### Rule-Based Agentic AI for Placement Decision Support

Placement Operations Copilot is a **local, rule-based, explainable Agentic AI system** built to assist placement teams in making **consistent, transparent, and data-driven placement decisions**.

This project is a **decision-support copilot**, not an automated decision engine.  
All final placement decisions always remain with **human evaluators**.

---

## 🎯 Project Objective

The objective of this project is to:
- Evaluate candidate placement readiness
- Recommend suitable job roles
- Identify skill gaps transparently
- Analyze interview feedback
- Generate a structured preparation plan
- Suggest prioritized placement actions

All decisions are **fully explainable and rule-based**, avoiding black-box machine learning.

---

## 🧠 Agentic Architecture

The system follows a **modular agent-based architecture**, where each agent handles a well-defined responsibility.

### Agents Used

#### 1. Readiness Agent
- Calculates a weighted readiness score (0–100)
- Classifies candidates as:
  - Ready
  - Almost Ready
  - Not Ready
- Generates reasoning and improvement suggestions

#### 2. Role Recommendation Agent
- Matches candidate skills against predefined role requirements
- Identifies blocking skill gaps
- Recommends or rejects roles transparently

#### 3. Interview Feedback Agent
- Analyzes interview feedback text
- Extracts strengths and improvement areas
- Generates a situation-aware 7-day preparation plan

#### 4. Action Planning Agent
- Generates placement next actions
- Assigns priority (High / Medium / Low)
- Supports placement decision-making

---

## 📊 Skill Scoring Rules

```python
SKILL_WEIGHTS = {
    "Excel": 0.15,
    "SQL": 0.20,
    "Python": 0.20,
    "Statistics & Probability": 0.15,
    "Machine Learning": 0.20,
    "Tableau & Power BI": 0.10
}
```

---

## 📋 Role Requirements

```python
ROLE_REQUIREMENTS = {
    "Data Analyst": {
        "Excel": 70,
        "SQL": 70,
        "Statistics & Probability": 65,
        "Tableau & Power BI": 65
    },
    "Business Analyst": {
        "Excel": 75,
        "SQL": 60,
        "Tableau & Power BI": 70
    },
    "Data Scientist": {
        "Python": 75,
        "Statistics & Probability": 75,
        "Machine Learning": 70,
        "SQL": 60
    },
    "Junior ML Engineer": {
        "Python": 80,
        "Machine Learning": 75,
        "Statistics & Probability": 70
    },
    "BI Analyst": {
        "Excel": 75,
        "SQL": 65,
        "Tableau & Power BI": 75
    }
}
```

---

User Input → Score Analysis → Feedback Analysis
→ Readiness Evaluation → Role Suitability
→ Strengths & Gaps → Preparation Plan
→ Placement Action Summary → Final Report


## ▶️ How to Run

```bash
pip install flask
python app.py
```

Open browser at:
```
http://127.0.0.1:5000/
```

---

## 👨‍💻 Creator

**Krunal Jadhav**  
AI & Data Science Engineer

---

## ⚠️ Disclaimer

This system provides **decision support only** and does not replace human judgment.

