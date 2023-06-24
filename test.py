n = int(input())
min_income = list(map(int, input().split()))
edu_req = list(map(int, input().split()))
parents = list(map(int, input().split()))
classmates = int(input())
class_income = list(map(int, input().split()))
class_edu = list(map(int, input().split()))
class_parent = list(map(int, input().split()))

country_indexes = {}
mates_indexes = {}
results = []
temp = []

for i in range(n):
    country_indexes[i] = i + 1

for mate in range(classmates):
    mates_indexes[mate] = mate + 1

for mate in range(classmates):

    if class_parent[mate] != 0 and parents[class_parent[mate] - 1] != 0:
        temp.append(class_parent[mate])

    for country in range(n):
        if class_income[mate] >= min_income[country] and class_edu[mate] >= edu_req[country]:
            temp.append(country + 1)

    if len(temp) == 0:
        temp.clear()
        results.append(0)
        continue

    sorted_val = sorted(temp)
    temp.clear()
    results.append(sorted_val[0])

print(" ".join(map(str, results)))