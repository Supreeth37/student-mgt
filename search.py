# search.py

def search_by_name(students, name):
    results = [s for s in students if s.name.lower() == name.lower()]
    return results

def search_by_grade(students, grade):
    results = [s for s in students if s.grade.lower() == grade.lower()]
    return results
