sculp_amount, ideal_ice, time_left = map(int, input().split())
sculps_ice = list(map(int, input().split()))

ideal_sculps = 0
sculps_count = {}
positions = []
differences = []

for sculp_index, sculp in enumerate(sculps_ice):
    sculps_count[sculp_index + 1] = sculp

    if sculp == ideal_ice:
        ideal_sculps += 1
        positions.append(sculp_index + 1)
    else:
        differences.append(abs(sculp - ideal_ice))

sorted_differences = sorted(differences)

for sculp in sorted_differences:
    if time_left > sculp:
        time_left -= sculp
        ideal_sculps += 1
        try:
            target_ice = ideal_ice + sculp
            if target_ice in sculps_count.values():
                positions.append(list(sculps_count.keys())[list(sculps_count.values()).index(target_ice)])
            else:
                positions.append(list(sculps_count.keys())[list(sculps_count.values()).index(ideal_ice - sculp)])
        except(ValueError):
            positions.append(list(sculps_count.keys())[list(sculps_count.values()).index(ideal_ice - sculp)])
    else:
        break

print(ideal_sculps)
output = " ".join(map(str, sorted(positions)))
print(output)