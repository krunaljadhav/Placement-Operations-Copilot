from rules.scoring_rules import (
    SKILL_WEIGHTS,
    READINESS_THRESHOLDS,
    MIN_SKILL_SCORE
)

def evaluate_readiness(scores, feedback_text):
    reasons = []
    suggestions = []

    # Weighted score calculation
    weighted_score = 0
    for skill, score in scores.items():
        weight = SKILL_WEIGHTS.get(skill, 0)
        weighted_score += score * weight

        if score < MIN_SKILL_SCORE:
            reasons.append(f"{skill} score is below minimum expected level")
            suggestions.append(f"Revise fundamentals of {skill}")

    # Readiness classification
    if weighted_score >= READINESS_THRESHOLDS["READY"]:
        status = "Ready"
    elif weighted_score >= READINESS_THRESHOLDS["ALMOST_READY"]:
        status = "Almost Ready"
    else:
        status = "Not Ready"

    # Feedback-based reasoning
    feedback = feedback_text.lower()

    if "communication" in feedback or "explain" in feedback:
        reasons.append("Communication clarity needs improvement")
        suggestions.append("Practice explaining solutions aloud")

    if not reasons:
        reasons.append("Strong and balanced performance across skills")

    return {
        "status": status,
        "final_score": round(weighted_score, 2),
        "reasons": reasons,
        "suggestions": list(set(suggestions))[:3]
    }
