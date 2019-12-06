universe = []


class OrbittingObject:
    def __init__(self, name):
        universe.append(self)
        self.name = name
        self.orbittees = []
        self.parent = None

    @property
    def path_to_centre(self):
        path, ptr = [self], self.parent
        while ptr != None:
            path.append(ptr)
            ptr = ptr.parent
        return path

    def count_orbittees(self):
        return len(self.path_to_centre) - 1


for parent_name, child_name in [line.strip().split(")") for line in open('input.txt')]:
    parent = next((o for o in universe if o.name == parent_name), OrbittingObject(parent_name))
    child = next((o for o in universe if o.name == child_name), OrbittingObject(child_name))
    parent.orbittees.append(child)
    child.parent = parent

print("Part 1: " + str(sum(map(lambda o: o.count_orbittees(), universe))))

santa, you = next(o for o in universe if o.name == "SAN"), next(o for o in universe if o.name == "YOU")
santa_relative, you_relative = next(
    (a, b) for (a, b) in zip(santa.path_to_centre[::-1], you.path_to_centre[::-1]) if a != b)

print("Part 2: " + str(santa.path_to_centre.index(santa_relative) + you.path_to_centre.index(you_relative)))
