from typing import List, Optional


class Intersection:
    def __init__(self, t: float, object: object):
        self.t = t
        self.object = object


def hit(xs: List[Intersection]) -> Optional[Intersection]:
    positive_intersections = [x for x in xs if x.t >= 0]
    if not positive_intersections:
        return None
    return min([x for x in positive_intersections], key=lambda x: x.t)
