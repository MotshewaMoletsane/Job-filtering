from flask import Flask, render_template, request

app = Flask(__name__)

# Sample job data (job_id, title, location, company, job_type, industry, description, responsibilities, qualifications, experience)
jobs = [
    (1, "Data Analyst", "Johannesburg", "GlobalTech", "Full-Time", "Technology",
     "Analyze large datasets to provide business insights and recommendations.",
     "Responsibilities:\n- Analyze complex datasets\n- Build data visualizations\n- Present findings to stakeholders",
     "Qualifications:\n- BSc in Data Science, Computer Science or related field\n- Proficiency in SQL and Python\n- Experience with data visualization tools (Power BI, Tableau)",
     "Experience: 2+ years in data analytics"),
    
    (2, "Web Developer", "Cape Town", "InnovateX", "Full-Time", "Technology",
     "Develop and maintain dynamic websites and web applications for clients.",
     "Responsibilities:\n- Write clean, scalable code\n- Develop front-end and back-end components\n- Troubleshoot and debug applications",
     "Qualifications:\n- BSc in Computer Science or related field\n- Experience with HTML, CSS, JavaScript, Python (Flask/Django)\n- Familiarity with database management systems",
     "Experience: 3+ years in web development"),

    (3, "Marketing Manager", "Durban", "BrightStart", "Part-Time", "Finance",
     "Lead the marketing team to promote the company's financial products.",
     "Responsibilities:\n- Create and execute marketing strategies\n- Lead marketing campaigns\n- Manage the marketing budget",
     "Qualifications:\n- Bachelor’s degree in Marketing, Business, or related field\n- Strong leadership and project management skills\n- Knowledge of digital marketing tools",
     "Experience: 5+ years in marketing management"),

    (4, "Teacher", "Pretoria", "LearnNow", "Contract", "Education",
     "Teach Mathematics and Science to high school students.",
     "Responsibilities:\n- Prepare and deliver lessons\n- Grade student assignments\n- Collaborate with parents and other teachers",
     "Qualifications:\n- Bachelor’s degree in Education or subject-specific qualification\n- Teaching certification\n- Strong communication skills",
     "Experience: 2+ years teaching experience"),

    (5, "Nurse", "Port Elizabeth", "HealthCare Inc", "Full-Time", "Healthcare",
     "Provide patient care and assist doctors in a healthcare facility.",
     "Responsibilities:\n- Administer medication\n- Monitor patient conditions\n- Assist in surgeries",
     "Qualifications:\n- Nursing Diploma/Degree\n- Registered with the South African Nursing Council\n- Knowledge of medical procedures",
     "Experience: 3+ years in nursing or healthcare"),

    (6, "Software Engineer", "Remote", "DevSolutions", "Internship", "Technology",
     "Develop software solutions for clients and internal projects.",
     "Responsibilities:\n- Design, develop, and maintain software systems\n- Collaborate with development teams\n- Debug and troubleshoot issues",
     "Qualifications:\n- BSc in Software Engineering, Computer Science, or related field\n- Knowledge of Python, JavaScript, or Java\n- Understanding of software development life cycle",
     "Experience: No experience required, internship"),

    (7, "Financial Analyst", "Johannesburg", "FutureFinance", "Full-Time", "Finance",
     "Analyze financial data and provide recommendations for investments.",
     "Responsibilities:\n- Analyze market trends and financial reports\n- Prepare investment reports\n- Collaborate with stakeholders",
     "Qualifications:\n- BCom in Finance or related field\n- Strong analytical skills\n- Proficiency in Excel and financial modeling",
     "Experience: 3+ years in financial analysis"),

    (8, "Operations Manager", "Polokwane", "Polokwane Logistics", "Full-Time", "Logistics",
     "Manage daily operations of the logistics company, including staff and transportation.",
     "Responsibilities:\n- Supervise logistics operations\n- Ensure timely delivery of goods\n- Manage staff and budget",
     "Qualifications:\n- Bachelor’s degree in Operations Management or related field\n- Strong leadership skills\n- Familiarity with supply chain management",
     "Experience: 5+ years in operations management"),

    (9, "Sales Consultant", "Cape Town", "RetailWave", "Part-Time", "Retail",
     "Engage with customers and drive sales in a retail store environment.",
     "Responsibilities:\n- Assist customers in finding products\n- Process sales transactions\n- Maintain store presentation",
     "Qualifications:\n- High school diploma\n- Strong communication skills\n- Ability to work flexible hours",
     "Experience: 1+ year in sales or customer service"),

    (10, "Civil Engineer", "Bloemfontein", "CityBuild", "Full-Time", "Construction",
     "Design, plan, and oversee construction projects, including roads and infrastructure.",
     "Responsibilities:\n- Create construction plans and designs\n- Supervise construction projects\n- Ensure compliance with safety regulations",
     "Qualifications:\n- Bachelor’s degree in Civil Engineering\n- Registered with ECSA\n- Proficiency in AutoCAD and other design tools",
     "Experience: 4+ years in civil engineering")
]


@app.route('/')
def index():
    return render_template('index.html', jobs=jobs)

# Job Filter Route
@app.route('/filter', methods=['GET'])
def filter_jobs():
    title = request.args.get('title', '').lower()
    company = request.args.get('company', '').lower()
    location = request.args.get('location', '')
    job_type = request.args.get('job_type', '')
    industry = request.args.get('industry', '')

    filtered_jobs = jobs

    # Filter by title
    if title:
        filtered_jobs = [job for job in filtered_jobs if title in job[1].lower()]

    # Filter by company
    if company:
        filtered_jobs = [job for job in filtered_jobs if company in job[3].lower()]

    # Filter by location (South African cities)
    if location:
        filtered_jobs = [job for job in filtered_jobs if location == job[2]]

    # Filter by job type
    if job_type:
        filtered_jobs = [job for job in filtered_jobs if job_type == job[4]]

    # Filter by industry
    if industry:
        filtered_jobs = [job for job in filtered_jobs if industry == job[5]]

    return render_template('index.html', jobs=filtered_jobs)

if __name__ == '__main__':
    app.run(debug=True)

from flask import request, redirect, url_for

@app.route('/apply', methods=['POST'])
def apply_for_job():
    job_title = request.form.get('job_title')
    # Process the application (e.g., save to a database, send notification)
    print(f"User applied for: {job_title}")
    
    # Redirect to a confirmation page or back to the job listings
    return redirect(url_for('show_jobs'))  # Redirect back to job listings or another route
  

   

