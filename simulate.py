import helper
import numpy as np

n = 20

hospital_match_avg_rank = []
student_match_avg_rank = []

for i in range(1000):
    students = list(np.random.permutation(n))

    student_prefs = helper.random_preferences(n)
    hospital_prefs = helper.random_preferences(n)

    M = helper.match(student_prefs, hospital_prefs, students)

    hospital_ranks = helper.get_hospital_match_ranks(M, hospital_prefs)
    student_ranks = helper.get_student_match_ranks(M, student_prefs)

    hospital_match_avg_rank.append(np.mean(list(hospital_ranks.values())))
    student_match_avg_rank.append(np.mean(list(student_ranks.values())))

print('Average hospital match rank:', np.mean(hospital_match_avg_rank))
print('Average student match rank:', np.mean(student_match_avg_rank))
