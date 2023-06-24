n = int(input())
volumes = list(map(int, input().split()))

max_value_of_acid = volumes[0]
counter = 0

for i in range(1, len(volumes)):
    if volumes[i] > max_value_of_acid:
        max_value_of_acid = volumes[i]

for i in range(len(volumes) - 1, -1, -1):
    if volumes[i] == max_value_of_acid:
        continue

    elif volumes[i] < max_value_of_acid:
        k = max_value_of_acid - volumes[i]
        slice_to_update = volumes[0:i+1]
        for j in range(k):
            for idx, element in enumerate(slice_to_update):
                volumes[idx] += 1
            counter += 1

    elif volumes[i] > max_value_of_acid:
        counter = -1
        break

    else:
        counter = -1
        break

print(counter)