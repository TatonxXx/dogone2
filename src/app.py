from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html",
                           student_id="670832",
                           name="Tepnarin")

@app.route("/git")
def git_page():
    return render_template("git.html")

@app.route("/docker")
def docker_page():
    return render_template("docker.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
