from math import ceil
from random import shuffle
from arguments import members, previous_results


MAX_MEMBER_PER_GROUP = 4
GROUP_COUNT = ceil(len(members) / MAX_MEMBER_PER_GROUP)


groups = [[] for _ in range(GROUP_COUNT)]


previous_pairs = {}
for group in previous_results[0]:
    for member in group:
        previous_pairs[member] = set(group)
        previous_pairs[member].remove(member)


def can_be_grouped(group: list, member: str):
    for group_member in group:
        if group_member in previous_pairs.get(member, set()):
            return False
    return True


shuffle(members)
for user in members:
    groups.sort(key=lambda g: len(g))
    for group in groups:
        if can_be_grouped(group, user) and len(group) < MAX_MEMBER_PER_GROUP:
            group.append(user)
            break
    else:
        for group in groups:
            if len(group) < MAX_MEMBER_PER_GROUP:
                group.append(user)
                break

for i in range(len(groups) - 1):
    while len(groups[i]) < len(groups[-1]) - 1:
        member_to_move = groups[-1].pop()
        groups[i].append(member_to_move)

for group in groups:
    print(' '.join(group))
