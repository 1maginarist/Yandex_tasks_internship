sculp_amount, ideal_ice, time_left = map(int, input().split())
sculps_ice = list(map(int, input().split()))

ideal_sculps = 0
sculps_count = {}
positions = []
differences = []

# for i in range(1, len(sculps_ice) + 1):
#    sculps_count[i] = sculps_ice[i-1]

for sculp in sculps_ice:
    sculps_count[(sculps_ice.index(sculp) + 1)] = sculp

    if sculp == ideal_ice:
        ideal_sculps += 1
        positions.append(sculps_ice.index(sculp) + 1)
    else:
        differences.append(abs(sculp - ideal_ice))

sorted_differences = sorted(differences)

for sculp in sorted_differences:
    if time_left > sculp:
        time_left -= sculp
        ideal_sculps += 1
        try:
            positions.append(sculps_ice.index(sculp + ideal_ice) + 1)
        except(ValueError):
            positions.append(sculps_ice.index(ideal_ice - sculp) + 1)

    else:
        break

print(ideal_sculps)
output = " ".join(map(str, sorted(positions)))
print(output)