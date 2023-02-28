class DisjSetQuickUnionByRankPathCompression:
    def __init__(self):
        self.__disj_set = []
        self.__rank = []

    # O(a(N)), a(N) - Inverse Ackermann funciton. In practice O(a(N)) == O(1) on average (ammortized)
    def union(self, elem1: int, elem2: int) -> None:
        print(f"Union {elem1}, {elem2}")
        self.__prefill(max(elem1, elem2))

        root1 = self.find(elem1)
        root2 = self.find(elem2)
        if root1 != root2:
            if self.__rank[root1] > self.__rank[root2]:
                self.__disj_set[root2] = root1
            elif self.__rank[root2] > self.__rank[root1]:
                self.__disj_set[root1] = root2
            else:
                self.__disj_set[root2] = root1
                self.__rank[root1] += 1

    # O(a(N)), a(N) - Inverse Ackermann funciton. In practice O(a(N)) == O(1) on average (ammortized)
    def find(self, elem: int):
        if elem == self.__disj_set[elem]:
            return elem

        self.__disj_set[elem] = self.find(self.__disj_set[elem])
        return self.__disj_set[elem]

    def __str__(self) -> str:
        res = "Parent: " + str(self.__disj_set) + "\n"
        res = res + "Vertex: [" + ", ".join([str(i) for i in range(len(self.__disj_set))]) + "]\n"
        res = res + "Rank:   " + str(self.__rank) + "\n"
        return res

    def __prefill(self, elem: int):
        if len(self.__disj_set) < elem + 1:
            for i in range(len(self.__disj_set), elem + 1):
                self.__disj_set.append(i)
                self.__rank.append(1)
        