class DisjSetQuickUnionPathCompression:
    def __init__(self):
        self.__disj_set = []

    # worst (once) - O(N), average O(logN)
    def union(self, elem1: int, elem2: int) -> None:
        print(f"Union {elem1}, {elem2}")
        self.__prefill(max(elem1, elem2))

        root1 = self.find(elem1)
        root2 = self.find(elem2)
        if root1 != root2:
            self.__disj_set[root2] = root1

    # worst (once) - O(N), average O(logN)
    def find(self, elem: int):
        if elem == self.__disj_set[elem]:
            return elem

        self.__disj_set[elem] = self.find(self.__disj_set[elem])
        return self.__disj_set[elem]

    def __str__(self) -> str:
        res = "Parent: " + str(self.__disj_set) + "\n"
        res = res + "Vertex: [" + ", ".join([str(i) for i in range(len(self.__disj_set))]) + "]\n"
        return res

    def __prefill(self, elem: int):
        if len(self.__disj_set) < elem + 1:
            for i in range(len(self.__disj_set), elem + 1):
                self.__disj_set.append(i)
        