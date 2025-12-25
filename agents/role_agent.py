from rules.role_requirements import ROLE_REQUIREMENTS

def recommend_roles(scores):
    recommended = []
    not_recommended = {}

    for role, requirements in ROLE_REQUIREMENTS.items():
        gaps = []

        for skill, min_score in requirements.items():
            if scores.get(skill, 0) < min_score:
                gaps.append(skill)

        if not gaps:
            recommended.append(role)
        else:
            not_recommended[role] = gaps

    return recommended, not_recommended
