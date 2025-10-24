from flask import Flask, render_template, request, redirect, url_for, session
from questions import QUESTIONS
from utils import evaluate_quiz

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        answers = {q: request.form.get(q) for q in QUESTIONS.keys()}
        score = evaluate_quiz(answers)
        session["score"] = score
        return redirect(url_for("result"))
    return render_template("index.html", questions=QUESTIONS)

@app.route("/result")
def result():
    score = session.get("score", 0)
    return render_template("result.html", score=score, total=len(QUESTIONS))

if __name__ == "__main__":
    app.run(debug=True)
