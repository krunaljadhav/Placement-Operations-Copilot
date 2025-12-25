import re

def analyze_feedback(feedback_text):
    text = feedback_text.lower()

    strengths = set()
    gaps = set()

    skill_map = {
        "communication": {
            "keywords": ["communication"],
            "positive": ["confident", "clear", "articulate", "well explained"],
            "negative": ["nervous", "hesitant", "unclear", "rambling","weak","bad"],
            "strength_label": "Clear and confident communication",
            "gap_label": "Communication clarity and confidence"
        },
        "sql": {
            "keywords": ["sql"],
            "positive": ["strong", "good", "excellent"],
            "negative": ["weak", "struggled", "basic","bad"],
            "strength_label": "Strong SQL fundamentals",
            "gap_label": "SQL fundamentals"
        },
        "python": {
            "keywords": ["python"],
            "positive": ["strong", "good", "clean"],
            "negative": ["weak", "slow", "confused"],
            "strength_label": "Good Python problem-solving skills",
            "gap_label": "Python problem-solving"
        },
        "statistics": {
            "keywords": ["statistics", "probability"],
            "positive": ["strong", "clear"],
            "negative": ["average", "weak", "confused"],
            "strength_label": "Solid understanding of statistics",
            "gap_label": "Statistical reasoning"
        },
        "machine learning": {
            "keywords": ["machine learning", "ml"],
            "positive": ["strong", "good", "hands-on"],
            "negative": ["theoretical", "weak", "no hands-on","bad"],
            "strength_label": "Practical machine learning knowledge",
            "gap_label": "Practical machine learning application"
        },
        "dashboard": {
            "keywords": ["dashboard", "power bi", "tableau"],
            "positive": ["strong", "good", "impressive"],
            "negative": ["basic", "weak","bad"],
            "strength_label": "Strong data visualization skills",
            "gap_label": "Advanced dashboarding skills"
        }
    }

    # Split feedback into clauses to link sentiment with skill
    clauses = re.split(r",|and|but|\.", text)

    for clause in clauses:
        for skill, rules in skill_map.items():
            if any(k in clause for k in rules["keywords"]):
                if any(p in clause for p in rules["positive"]):
                    strengths.add(rules["strength_label"])
                if any(n in clause for n in rules["negative"]):
                    gaps.add(rules["gap_label"])

    # Fallbacks
    if not strengths:
        strengths.add("Basic understanding of core concepts")

    if not gaps:
        gaps.add("No major technical gaps identified")

    # ---------------- DYNAMIC 7-DAY PLAN ----------------
    plan = []

    if "Communication clarity and confidence" in gaps:
        plan.append("Day 1: Communication drills and mock explanations")

    if "SQL fundamentals" in gaps:
        plan.append("Day 2: SQL joins, subqueries, and optimization")

    if "Python problem-solving" in gaps:
        plan.append("Day 3: Python DSA and debugging exercises")

    if "Statistical reasoning" in gaps:
        plan.append("Day 4: Probability, distributions, and case questions")

    if "Practical machine learning application" in gaps:
        plan.append("Day 5: ML mini-project and model evaluation")

    plan.append("Day 6: Full mock interview (technical + HR)")
    plan.append("Day 7: Resume refinement and confidence preparation")

    return list(strengths), list(gaps), plan
