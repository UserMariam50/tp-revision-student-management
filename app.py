
from flask import Flask, render_template, request

from student_manager import (
    calculate_average,
    get_mention,
    is_admitted,
    validate_grades
)

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    average = None
    mention = None
    admitted = None
    error = None
    grades = []

    if request.method == "POST":

        raw_grades = request.form.get("grades", "").strip()

        if not raw_grades:
            error = "Veuillez saisir des notes."

        else:
            try:
                grades = [
                    float(note.strip())
                    for note in raw_grades.split(",")
                ]

                if not validate_grades(grades):
                    error = "Les notes doivent être entre 0 et 20."

                else:
                    average = calculate_average(grades)
                    mention = get_mention(average)
                    admitted = is_admitted(average)

            except ValueError:
                error = "Veuillez saisir des notes numériques valides."

    return render_template(
        "index.html",
        average=average,
        mention=mention,
        admitted=admitted,
        error=error,
        grades=grades

    )


if __name__ == "__main__":
    app.run(debug=True)
