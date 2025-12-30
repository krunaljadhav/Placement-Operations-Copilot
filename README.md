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

## 🎯 Tech Stack
<p align="center"> <!-- Core Language & Backend --> <img src="https://img.shields.io/badge/Python-Core%20Language-3776AB?style=for-the-badge&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/Flask-Backend%20Engine-black?style=for-the-badge&logo=flask"/>  </p> <p align="center"> <!-- Frontend --> <img src="https://img.shields.io/badge/HTML5-UI%20Structure-E34F26?style=for-the-badge&logo=html5&logoColor=white"/> <img src="https://img.shields.io/badge/CSS3-Premium%20UI-1572B6?style=for-the-badge&logo=css3&logoColor=white"/> <img src="https://img.shields.io/badge/Jinja2-Templating-B41717?style=for-the-badge"/> </p> <p align="center"> <!-- AI & Data --> <img src="https://img.shields.io/badge/Rule--Based%20AI-Agentic%20Logic-yellow?style=for-the-badge"/> <img src="https://img.shields.io/badge/Numpy-Scoring%20Logic-013243?style=for-the-badge&logo=numpy&logoColor=white"/> </p> <p align="center"> <!-- Tooling --> <img src="https://img.shields.io/badge/GitHub-Version%20Control-181717?style=for-the-badge&logo=github"/> </p>


---
## 📸 Application Screenshots

Below are selected screenshots showcasing the key workflows and UI of the **Placement Operations Copilot**.

---

### 🧠 Agentic Workflow Overview
> High-level view of the agentic decision-support modules used in the system.

![Agentic Workflows](screenshots/Screenshot%202025-12-31%20011737.png)

---

### 🎯 Candidate Skill Input Dashboard
> Structured input interface for capturing multi-skill assessment scores.

![Candidate Skill Scores](screenshots/Screenshot%202025-12-31%20011759.png)

---

### 🔁 End-to-End Evaluation Flow and 🗣️ Mock Interview Feedback Input
> Complete flow from candidate input to final placement recommendation.
> Text-based interview feedback used for qualitative analysis.

![End-to-End Flow](screenshots/Screenshot%202025-12-31%20012908.png)

---

### 📊 Candidate Readiness & Weighted Score
> Overall readiness evaluation with weighted scoring and reasoning.
![Role Suitability](screenshots/Screenshot%202025-12-31%20012603.png)


---

### ✅ Role Suitability Recommendations
> Recommended and blocked roles with explicit skill gap explanations.

![Candidate Readiness](screenshots/Screenshot%202025-12-31%20012438.png)

---

### 🧠 Interview Feedback Analysis & 📅 7-Day Focused Preparation Plan
> Extracted strengths, improvement areas, and targeted preparation insights.
> Structured preparation roadmap generated from feedback analysis.

![Preparation Plan](screenshots/Screenshot%202025-12-31%20012634.png)

---


### 🚀 Placement Action Summary
> Final consolidated decision-support output with prioritized next actions.

![Placement Action Summary](screenshots/Screenshot%202025-12-31%20012644.png)

---



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
---

### 🧩 Role Skill Requirements
> Minimum skill thresholds defined for each supported role.

![Role Skill Requirements](screenshots/Screenshot%202025-12-31%20011940.png)

---
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
## 📂 Project Structure


```

placement-operations-copilot/
│
├── app.py
├── requirements.txt
├── README.md
│
├── agents/
│ ├── readiness_agent.py
│ ├── role_agent.py
│ ├── feedback_agent.py
│ ├── action_agent.py
│
├── rules/
│ ├── scoring_rules.py
│ ├── role_requirements.py
│
├── templates/
│ ├── index.html
│ ├── result.html
│ ├── requirements.html
│
└── static/
└── style.css
```

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


    







