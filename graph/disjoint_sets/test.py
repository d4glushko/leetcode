from disjoint_sets.quick_find import DisjSetQuickFind
from disjoint_sets.quick_union import DisjSetQuickUnion
from disjoint_sets.quick_union_rank import DisjSetQuickUnionByRank
from disjoint_sets.quick_union_path import DisjSetQuickUnionPathCompression
from disjoint_sets.quick_union_rank_path import DisjSetQuickUnionByRankPathCompression

class Test:
    def __init__(self) -> None:
        pass

    def test(self):
        disj_set_types = [
            DisjSetQuickFind,
            DisjSetQuickUnion,
            DisjSetQuickUnionByRank,
            DisjSetQuickUnionPathCompression,
            DisjSetQuickUnionByRankPathCompression
        ]
        for _, disj_set_type in enumerate(disj_set_types):
            self.__usual_test(disj_set_type)
            self.__worst_case_test(disj_set_type)

    def __usual_test(self, disj_set_type):
        print(f"Usual test {disj_set_type.__name__}")
        disj_set = disj_set_type()

        disj_set.union(1, 2)
        print(disj_set)

        disj_set.union(2, 3)
        print(disj_set)

        disj_set.union(4, 5)
        print(disj_set)

        disj_set.union(5, 6)
        print(disj_set)

        print(f"2 and 5 connected: {disj_set.find(2) == disj_set.find(5)}\n")

        disj_set.union(2, 6)
        print(disj_set)

        print(f"2 and 5 connected: {disj_set.find(2) == disj_set.find(5)}\n")

        disj_set.union(3, 6)
        print(disj_set)

    def __worst_case_test(self, disj_set_type):
        print(f"Worst Case {disj_set_type.__name__}")
        disj_set = disj_set_type()

        disj_set.union(1, 0)
        print(disj_set)

        disj_set.union(2, 0)
        print(disj_set)

        disj_set.union(3, 0)
        print(disj_set)

        disj_set.union(4, 0)
        print(disj_set)

        disj_set.union(5, 0)
        print(disj_set)
