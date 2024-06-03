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
        choices=[('', 'All'), ('Python', 'Python'), ('PowerBI', 'PowerBI'), ('Tableau', 'Tableau'),   ('HTML', 'HTML'), ('CSS', 'CSS'), ('Looker Studio', 'Looker Studio'),('Javascript', 'Javascript')])

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
@app.route('/downloadresume')
def download_file():
    #file path to download resume
    file_path = "static/downloads/resume.pdf"
    return send_file(file_path, as_attachment=True)


@app.route('/download-persistence-report')
def download_pbi_file():
    #file path to download sample PBI report
    file_path = "static/downloads/FY23_Persistence_Dashboard.pbix"
    return send_file(file_path, as_attachment=True)

@app.route('/download-nweamap-report')
def download_twbx_file():
    #file path to download sample tableau report
    file_path = "static/downloads/nwea_map_spring_2019_report.twbx"
    return send_file(file_path, as_attachment=True)

#Launch App
if __name__ == '__main__':
    app.run(debug=True)
