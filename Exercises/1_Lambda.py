students = [
    ('Alice', 88),
    ('Bob', 95),
    ('Charlie', 70),
    ('Diana', 82)
]

# Fill out the lambda, so that this expression sorts by score descending
# Hint: https://github.com/SoliGabiAnn/Functional-programming-course/wiki/3.-Anonymous-Functions-%E2%80%90-Lambda#lambda-in-sorted
sorted_students = sorted(students, key=lambda ..., reverse=True)

for name, score in sorted_students:
    print(f"{name}: {score}")

'''
Expected output:

Bob: 95
Alice: 88
Diana: 82
Charlie: 70
'''
