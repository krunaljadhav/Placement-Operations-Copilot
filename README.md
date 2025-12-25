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

<p align="center"> <!-- Core Language & Backend --> <img src="https://img.shields.io/badge/Python-Core%20Language-3776AB?style=for-the-badge&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/Flask-Backend%20Engine-black?style=for-the-badge&logo=flask"/>  </p> <p align="center"> <!-- Frontend --> <img src="https://img.shields.io/badge/HTML5-UI%20Structure-E34F26?style=for-the-badge&logo=html5&logoColor=white"/> <img src="https://img.shields.io/badge/CSS3-Premium%20UI-1572B6?style=for-the-badge&logo=css3&logoColor=white"/> <img src="https://img.shields.io/badge/Jinja2-Templating-B41717?style=for-the-badge"/> </p> <p align="center"> <!-- AI & Data --> <img src="https://img.shields.io/badge/Rule--Based%20AI-Agentic%20Logic-yellow?style=for-the-badge"/> <img src="https://img.shields.io/badge/Numpy-Scoring%20Logic-013243?style=for-the-badge&logo=numpy&logoColor=white"/> </p> <p align="center"> <!-- Tooling --> <img src="https://img.shields.io/badge/GitHub-Version%20Control-181717?style=for-the-badge&logo=github"/> </p>>

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
flowchart LR
    A[User] --> B[Enter Skills & Feedback]

    B --> C[Readiness Evaluation]
    C --> C1[Weighted Score]
    C1 --> C2[Ready / Almost / Not Ready]

    B --> D[Role Suitability Check]
    D --> D1[Compare with Role Requirements]
    D1 --> D2[Recommended Roles]
    D1 --> D3[Rejected Roles]

    B --> E[Feedback Analysis]
    E --> E1[Strengths]
    E --> E2[Gaps]
    E --> E3[7-Day Plan]

    C2 --> F[Action Generator]
    D2 --> F
    E3 --> F

    F --> G[Final Result Dashboard]


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




