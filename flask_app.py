from flask import Flask, render_template, jsonify
from tester.runner import run_all_tests
from storage import save_run, list_runs, init_db

app = Flask(__name__)

init_db()


@app.route("/")
def home():
    return "API Testing Dashboard - OK"


@app.route("/run")
def run():
    result = run_all_tests()
    save_run(result)
    return jsonify(result)


@app.route("/dashboard")
def dashboard():
    runs = list_runs()
    return render_template("dashboard.html", runs=runs)


@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "service": "api-testing-dashboard"
    })


if __name__ == "__main__":
    app.run(debug=True)
