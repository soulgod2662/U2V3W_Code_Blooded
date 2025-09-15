from flask import Flask, render_template, request
import os
from utils.parser import extract_text_from_pdf, extract_text_from_docx
from utils.extractor import load_skills, extract_skills
from utils.comparator import compare_skills
from utils.comparator import compare_skills, suggest_skills



app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    resume_file = request.files['resume']
    job_description = request.form['job_description']

    # Save uploaded resume
    resume_path = os.path.join(app.config['UPLOAD_FOLDER'], resume_file.filename)
    resume_file.save(resume_path)

    # Extract resume text
    if resume_file.filename.endswith('.pdf'):
        resume_text = extract_text_from_pdf(resume_path)
    elif resume_file.filename.endswith('.docx'):
        resume_text = extract_text_from_docx(resume_path)
    else:
        resume_text = ""

    # Load skill list
    skill_list = load_skills()

    # Extract skills
    resume_skills = extract_skills(resume_text, skill_list)
    jd_skills = extract_skills(job_description, skill_list)

    # Compare
    matched, missing, score = compare_skills(resume_skills, jd_skills)

    # Suggestions
    suggestions = suggest_skills(missing)

    # Cleanup
    os.remove(resume_path)

    # Render results
    return render_template(
        'index.html',
        matched_skills=matched,
        missing_skills=missing,
        match_score=score,
        resume_text=resume_text,
        job_description=job_description,
        suggestions=suggestions
    )

@app.route('/download', methods=['POST'])
def download():
    from flask import make_response
    matched = request.form['matched'].split(',')
    missing = request.form['missing'].split(',')
    score = request.form['score']

    result_text = f"Matched Skills: {', '.join(matched)}\n"
    result_text += f"Missing Skills: {', '.join(missing)}\n"
    result_text += f"Match Score: {score}%\n"

    response = make_response(result_text)
    response.headers["Content-Disposition"] = "attachment; filename=skill_comparison.txt"
    response.headers["Content-Type"] = "text/plain"
    return response

if __name__ == '__main__':
    app.run(debug=True)