import copy
import random
from constants import MEMBERS


members = copy.deepcopy(MEMBERS)


if __name__ == '__main__':
    random.shuffle(members)

    groups = [[], [], [], [], []]

    for index, user in enumerate(members):
        groups[index % 5].append(user)

    for group in groups:
        print(' '.join(group))
