from flask import Flask, render_template, url_for, request, send_file
from flask_wtf import FlaskForm
#import separate dictionry from projects.py
from projects import projects
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField,SelectField, HiddenField
import os
import pandas as pd

#Create secret key + app configuration
app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


#convert dictionary into dataframe
#Create dropdown form of skills to filter on the project page
class SkillForm(FlaskForm):
    skills =  SelectField('Skills', \
        choices=[('', 'All'),  ('HTML', 'HTML'), ('CSS', 'CSS'), ('Python', 'Python'),('Pandas', 'Pandas'), ('PowerBI', 'PowerBI'), ('Tableau', 'Tableau'), ('Looker Studio', 'Looker Studio'),('Javascript', 'Javascript')])

#Start app routes
#home page
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

#Projects page
@app.route("/projects", methods=['GET', 'POST'])
def project():
    form = SkillForm()
    selected_value = ''
    # Get the data for the current page
    if request.method == 'POST' and form.validate():
        selected_value = form.skills.data
    return render_template('projects.html', title='Projects', form=form, projects= projects, selected_value = selected_value)

#Download Resume
@app.route('/download')
def download_file():
    # Replace 'example.txt' with the path to the file you want to serve
    file_path = "static/resume.pdf"
    return send_file(file_path, as_attachment=True)

#Launch App
if __name__ == '__main__':
    app.run(debug=True)
