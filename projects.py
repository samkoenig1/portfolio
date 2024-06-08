#Create a dictionary of all the projects that I want to highlight on my portfolio.
# fields to include: (1) Name (2) Description (3) Skills (4) github and (5) image
projects = [

    {
        'name': 'State Persistence Dashboard',
        'description': 'PowerBI Report to transform and visualize enrollment, persistence, and publically available data to present back 100k dataset to 13 districts from the state of Kentucky. Note that the report attached has all student data removed, and is for demonstration purposes only. This file will download to your computer as a .pwbx and you will need PowerBI Desktop to open it.',
        'link_description': 'Click to Download',
        'skills': 'PowerBI, Row Level Security, Power Query',
        #COME BACK TO ADD GITHUB LINK
        'github': '/download-persistence-report',
        'image': 'ky_persistence_data'
    },

    {
        'name': 'NWEA Map Report',
        'description': 'Tableau Report to visualize NWEA Map data for school districts in Nasvhille, TN and Jackson, MS. This data was used by over 300 staff members annually, and contained upward of 40k rows. In production, this was distributed by Tableau Service, but the following file will be downloaded as a twbx file, and you can open via Tableau Readers desktop application. All student and school data has been removed from this report.',
        'link_description': 'Click to Download',
        'skills': 'Tableau, Tableau Prep',
        #COME BACK TO ADD GITHUB LINK
        'github': '/download-nweamap-report',
        'image': 'sankey'
    },


    {
        'name': 'Automated Email Alerts',
        'description': 'Code written to pull data from PostgreSQL Warehouse, push to google sheets via python, and then send via javascript by user of the google sheet. This was used to alert our teachers of the students they needed to check in with, as well as any other celebrations, or areas for growth in their classroom. Pushing the data to google sheets allowed our training and support team to validate before sending.',
        'link_description': 'Click to Explore Github',
        'skills': 'Python, Pandas, SQL, Javascript, HTML, CSS',
        'github': 'https://github.com/samkoenig1/early-alerts-email-automation',
        'image': 'early_alert'
    },
    {
        'name': 'Student Survey Dashboard',
        'description': 'A PowerBI dashboard and data cleaning code to summarize and display key indicators from a Spring 2022 survey for a higher education non-profit.  This version uses fake data to protect student confidentiality.',
        'link_description': 'Click to Explore Github',
        'skills': 'PowerBI, Power Query, Python, Pandas, Data Cleaning',
        #COME BACK TO ADD GITHUB LINK
        'github': 'https://github.com/samkoenig1/student_survey_pbi_report/tree/main/student_end_of_year_survey_2022',
        'image': 'end_of_year_survey'
    },

    {
        'name': 'Enrollment Dashboard',
        'description': 'A Looker Studio dashboard that cleanly presented National Student Clearinghouse data for 25 districts in the state of Illinois, so that school leaders could understand their student enrollment and persistence data broken down by subgroups such as Race / Ethnicity, Gender Identity, ELL and graduating class. Before pointing to the visualization layer, we used R to clean / transform the ~million row raw data file into a format readable by Looker Studio.',
        'link_description': 'Click to Explore Github',
        'skills': 'Looker Studio, R',
        'github': 'https://github.com/samkoenig1/nsc_data_cleaning',
        'image': 'persistence'
    },
    {
        'name': 'Illinois Report Card - Webscraping / cleaning',
        'description': 'Python code to scrape the Illinois report card publically available data, downdload relevant files, and tranform dataset to columnar data suitable for a BI layer for metrics such as 9th Grade On Track, High School Graduation, Early College Coursework, Attendance, and Postsecondary Enrollment.',
        'link_description': 'Click to Explore Github',
        'skills': 'Python, Pandas, Selenium',
        #COME BACK TO ADD GITHUB LINK
        'github': 'https://github.com/samkoenig1/illinois_report_card_transform/blob/main/il.py',
        'image': 'ilreportcard'
    },
    {
        'name': 'Strava Tracker',
        'description': 'This is a simple python dash application to pull data from your strava application, and display back simple stats such as (1) Total Distance (2) Avg miles per hour (3) Number of Activities and (4) Average Speed all over time by month. This application is set up so that you can bring in your own strava account if you are interested.',
        'link_description': 'Click to Explore Github',
        'skills': 'Python Dash, Plotly, JSON, APIs',
        'github': 'https://github.com/samkoenig1/strava-tracker',
        'image': 'strava'

    },
    {
        'name': 'Portfolio',
        'description': 'This is the website you are currently browsing! I built this using Python Flask, HTML, CSS, as a way to showcase some of the projects of which I am most proud.',
        'link_description': 'Click to Explore Github',
        'skills': 'Flask, HTML, CSS, Bootstrap',
        'github': 'https://github.com/samkoenig1/portfolio',
        'image': 'portfolio'
    },
    {
        'name': 'Canvas Self-Onboarding Pop-Up',
        'description': 'A javascript pop-up that lives on top of any Canvas LMS system that takes three URL parameters (1) Join Code, (2) Name, and (3) Email and autopopulates upon open. This was used from a redirected form, to ensure that the student uses the same email address from the welcome form to them joining the course.',
        'link_description': 'Click to Explore Github',
        'skills': 'Javascript',
        'github': 'https://github.com/samkoenig1/canvas-onboarding',
        'image': 'canvas_onboarding'
    },
    {
        'name': 'Mainstay / Salesforce Validation',
        'description': 'Python code to compare two separate files; one from Mainstay and one from Salesforce, to create a data quality report. Code lived in organizational sharefile account, and our team created an azure function and used Power automate to run the code anytime the reports from the respective sources were updated.',
        'link_description': 'Click to Explore Github',
        'skills': 'Python, Pandas, Azure, Power Automate',
        'github': 'https://github.com/samkoenig1/mainstay-sf-validation-code/tree/main',
        'image': 'validation'
    }
    ]
