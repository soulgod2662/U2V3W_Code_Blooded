def compare_skills(resume_skills, jd_skills):
    matched = list(set(resume_skills) & set(jd_skills))
    missing = list(set(jd_skills) - set(resume_skills))
    match_score = round((len(matched) / len(jd_skills)) * 100, 2) if jd_skills else 0
    return matched, missing, match_score

def suggest_skills(missing_skills):
    suggestions = {
        "TensorFlow": "Try learning via Coursera or Kaggle",
        "REST APIs": "Practice building APIs with Flask or FastAPI",
        "Leadership": "Mention team projects or club roles",
        "Communication": "Highlight presentations or group work",
        "Docker": "Build and deploy a sample app using Docker",
        "Kubernetes": "Explore tutorials on container orchestration",
        "SQL": "Practice queries on sample databases like Chinook or Sakila",
        "AWS": "Try deploying a Flask app on AWS EC2 or Lambda"
    }
    return {skill: suggestions.get(skill, "Consider learning this skill and adding it to your Resume") for skill in missing_skills}