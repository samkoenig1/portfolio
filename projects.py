#Create a dictionary of all the projects that I want to highlight on my portfolio.
# fields to include: (1) Name (2) Description (3) Skills (4) github and (5) image
projects = [
    {
        'name': 'Automated Email Alerts',
        'description': 'Code written to pull data from PostgreSQL Warehouse, push to google sheets via python, and then send via javascript by user of the google sheet. This was used to alert our teachers of the students they needed to check in with, as well as any other celebrations, or areas for growth in their classroom. Pushing the data to google sheets allowed our training and support team to validate before sending.',
        'skills': 'Python Pandas, SQL, Javascript',
        'github': 'https://github.com/samkoenig1/early-alerts-email-automation',
        'image': 'early_alert'
    },
    {
        'name': 'Enrollment Dashboard',
        'description': 'A Looker Studio dashboard that cleanly presented National Student Clearinghouse data for 25 districts in the state of Illinois, so that school leaders could understand their student enrollment and persistence data broken down by subgroups such as Race / Ethnicity, Gender Identity, ELL and graduating class. Before pointing to the visualization layer, we used R to clean / transform the ~million row raw data file into a format readable by Looker Studio. This version uses fake data to protect student confidentiality.',
        'skills': 'Looker Studio, R',
        #COME BACK TO ADD GITHUB LINK
        'github': '#',
        'image': 'persistence'
    },
    {
        'name': 'Strava Tracker',
        'description': 'This is a simple python dash application to pull data from your strava application, and display back simple stats such as (1) Total Distance (2) Avg miles per hour (3) Number of Activities and (4) Average Speed all over time by month. This application is set up so that you can bring in your own strava account if you are interested.',
        'skills': 'Python Dash, Plotly, JSON, APIs',
        'github': 'https://github.com/samkoenig1/strava-tracker',
        'image': 'strava'

    },
    {
        'name': 'Portfolio',
        'description': 'This is the website you are currently browsing! I built this using Python Flask, HTML, CSS, as a way to cleanly show my projects by my different skills.',
        'skills': 'Flask, HTML, CSS, Bootstrap',
        'github': 'https://github.com/samkoenig1/portfolio',
        'image': 'portfolio'
    },
    {
        'name': 'Canvas Self-Onboarding Pop-Up',
        'description': 'A javascript pop-up that lives on top of any Canvas LMS system that takes three URL parameters (1) Join Code, (2) Name, and (3) Email and autopopulates upon open. This was used from a redirected form, to ensure that the student uses the same email address from the welcome form to them joining the course.',
        'skills': 'Javascript',
        'github': 'https://github.com/samkoenig1/canvas-onboarding',
        'image': 'canvas_onboarding'
    },
    {
        'name': 'Mainstay / Salesforce Validation',
        'description': 'Python code to compare two separate files; one from Mainstay and one from Salesforce, to create a data quality report. Code lived in organizational sharefile account, and our team created an azure function and used Power automate to run the code anytime the reports from the respective sources were updated.',
        'skills': 'Python Pandas, Azure, Power Automate',
        'github': 'https://github.com/samkoenig1/mainstay-sf-validation-code/tree/main',
        'image': 'validation'
    }
    ]
