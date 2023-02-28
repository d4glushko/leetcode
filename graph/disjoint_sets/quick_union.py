class DisjSetQuickUnion:
    def __init__(self):
        self.__disj_set = []

    # O(N)
    def union(self, elem1: int, elem2: int) -> None:
        print(f"Union {elem1}, {elem2}")
        self.__prefill(max(elem1, elem2))

        root1 = self.find(elem1)
        root2 = self.find(elem2)
        if root1 != root2:
            self.__disj_set[root2] = root1

    # O(N)
    def find(self, elem: int):
        while elem != self.__disj_set[elem]:
            elem = self.__disj_set[elem]

        return elem

    def __str__(self) -> str:
        res = "Parent: " + str(self.__disj_set) + "\n"
        res = res + "Vertex: [" + ", ".join([str(i) for i in range(len(self.__disj_set))]) + "]\n"
        return res

    def __prefill(self, elem: int):
        if len(self.__disj_set) < elem + 1:
            for i in range(len(self.__disj_set), elem + 1):
                self.__disj_set.append(i)
        