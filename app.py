from flask import Flask, render_template, request

from agents.readiness_agent import evaluate_readiness
from agents.role_agent import recommend_roles
from agents.feedback_agent import analyze_feedback
from agents.action_agent import generate_next_actions
from rules.scoring_rules import SKILL_WEIGHTS
from rules.role_requirements import ROLE_REQUIREMENTS

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # -------------------- INPUT SCORES --------------------
        scores = {
            "Excel": int(request.form["excel"]),
            "SQL": int(request.form["sql"]),
            "Python": int(request.form["python"]),
            "Statistics & Probability": int(request.form["stats"]),
            "Machine Learning": int(request.form["ml"]),
            "Tableau & Power BI": int(request.form["bi"])
        }

        feedback_text = request.form["feedback"]

        # -------------------- AGENT WORKFLOWS --------------------
        readiness = evaluate_readiness(scores, feedback_text)
        recommended, rejected = recommend_roles(scores)
        strengths, gaps, plan = analyze_feedback(feedback_text)
        actions = generate_next_actions(readiness, recommended)

        # -------------------- RENDER RESULT --------------------
        return render_template(
            "result.html",
            readiness=readiness,
            scores=scores,
            weights=SKILL_WEIGHTS,
            recommended=recommended,
            rejected=rejected,
            strengths=strengths,
            gaps=gaps,
            plan=plan,
            actions=actions
        )

    return render_template("index.html")


# -------------------- ROLE REQUIREMENTS PAGE --------------------
@app.route("/requirements")
def requirements():
    return render_template(
        "requirements.html",
        ROLE_REQUIREMENTS=ROLE_REQUIREMENTS
    )


if __name__ == "__main__":
    app.run(debug=True)
