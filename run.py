from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = []


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/projects")
def about():
    return render_template('projects.html', title='Projects')


if __name__ == '__main__':
    app.run(debug=True)
