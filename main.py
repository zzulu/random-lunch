from math import ceil
from random import shuffle
from variables import members, previous_groups


MAX_MEMBER_PER_GROUP = 4
GROUP_COUNT = ceil(len(members) / MAX_MEMBER_PER_GROUP)


groups = [[] for _ in range(GROUP_COUNT)]


previous_pairs = {}
for group in previous_groups:
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
    shuffle(groups)
    for group in groups:
        if can_be_grouped(group, user) and len(group) < MAX_MEMBER_PER_GROUP:
            group.append(user)
            break
    else:
        for group in groups:
            if len(group) < MAX_MEMBER_PER_GROUP:
                group.append(user)
                break


for group in groups:
    print(' '.join(group))
