import numpy as np

def get_ranks(prefs):
    ranks = {}
    for h in prefs:
        ranks[h] = {}
        for i in range(len(prefs[h])):
            ranks[h][prefs[h][i]] = i

    return ranks

def match(student_prefs, hospital_prefs, students):
    if set(students) != set(student_prefs.keys()):
        raise ValueError('students and student_prefs.keys() do not agree')

    hospitals = hospital_prefs.keys()
    if len(students) != len(hospitals):
        raise ValueError('different number of students and hospitals')

    for s in student_prefs:
        if set(student_prefs[s]) != set(hospitals):
            raise ValueError('invalid student preference list')

    for h in hospital_prefs:
        if set(hospital_prefs[h]) != set(students):
            raise ValueError('invalid hospital preference list')


    hospital_rank = get_ranks(hospital_prefs)

    # reverse prefs for convenience in implementation
    student_offers = {}
    for s in student_prefs:
        student_offers[s] = student_prefs[s][::-1]

    free_students = list(students)  # initialize list of free students
    M = {}                          # initialize matching dictionary

    while len(free_students) > 0:
        s = free_students.pop()
        # if s has not proposed to everyone
        if len(student_offers[s]) > 0:
            # get the top remaining preference
            h = student_offers[s].pop()
            if h not in M:
                M[h] = s
            else:
                s2 = M[h]
                if hospital_rank[h][s] < hospital_rank[h][s2]:
                    M[h] = s
                    free_students.append(s2)
                else:
                    # s is still free
                    free_students.append(s)
    return M

def random_preferences(n):
    preferences = {}
    for i in range(n):
        preferences[i] = list(np.random.permutation(n))
    return preferences

def get_hospital_match_ranks(M, hospital_prefs):
    hospital_ranks = {}
    for h in M:
        s = M[h]
        hospital_ranks[h] = hospital_prefs[h].index(s) + 1

    return hospital_ranks

def get_student_match_ranks(M, student_prefs):
    student_ranks = {}
    for h in M:
        s = M[h]
        student_ranks[s] = student_prefs[s].index(h) + 1

    return student_ranks
