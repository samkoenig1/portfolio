from flask import Flask, render_template, url_for
app = Flask(__name__)
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField,SelectField, HiddenField
import os

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

projects = [{
        'name': 'Strava Tracker',
        'description': 'This is a simple python dash application to pull data from your strava application, and display back simple stats such as (1) Total Distance (2) Avg miles per hour (3) Number of Activities and (4) Average Speed all over time by month. This application is set up so that you can bring in your own strava account if you are interested.',
        'skills': 'Python Dash, Plotly, JSON, APIs',
        'github': 'https://github.com/samkoenig1/strava-tracker',
        'image': 'strava'

    },
    {
        'name': 'Portfolio Website',
        'description': 'This is the website that hosts my portfolio',
        'skills': 'Flask, HTML, CSS, Bootstrap',
        'github': 'https://github.com/samkoenig1/portfolio',
        'image': 'portfolio'
    }]
class SkillForm(FlaskForm):
    skills =  SelectField('Skills', choices = ['Tableau', 'Python', 'PowerBI','SQL', 'HTML', 'Javascript'])
    submit = SubmitField('Search')

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/projects")
def about():
    form = SkillForm()
    return render_template('projects.html', title='Projects', form=form, projects = projects)


if __name__ == '__main__':
    app.run(debug=True)
