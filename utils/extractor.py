import pandas as pd
from fuzzywuzzy import fuzz

# Load skill list from CSV
def load_skills(skill_file='data/skills.csv'):
    df = pd.read_csv(skill_file)
    return df['Skill'].tolist()

# Extract skills from text using fuzzy matching
def extract_skills(text, skill_list, threshold=80):
    found_skills = []
    for skill in skill_list:
        if fuzz.partial_ratio(skill.lower(), text.lower()) >= threshold:
            found_skills.append(skill)
    return list(set(found_skills))