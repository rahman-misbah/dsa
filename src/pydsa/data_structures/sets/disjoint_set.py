from typing import Any

class DisjointSet:
    def __init__(self):
        """Initialize the Disjoint Set data structure."""
        
        self.__item_map = {}    # Map named items to indices
        self.__parents = []     # Parent pointers for each item
        self.__ranks = []       # Ranks for union by rank optimization
        self.__count = 0        # Count of disjoint sets
        self.__item_count = 0   # Count of items in the Disjoint Set

    def __len__(self) -> int:
        """Return the number of disjoint sets."""
        return self.__count
    
    def __str__(self) -> str:
        """Return a string representation of the Disjoint Set."""
        sets = {}
        for item in self.__item_map:
            root = self.find(item)
            if root not in sets:
                sets[root] = []
            sets[root].append(item)
        
        result = ""

        for disjoint_set in sets.values():
            result += "{" + ", ".join(map(str, disjoint_set)) + "},\n"
        
        return f"{{\n{result.strip()[:-1]}\n}}"

    @property
    def count(self) -> int:
        """Return the number of disjoint sets."""
        return self.__count
    
    @property
    def item_count(self) -> int:
        """Return the number of items in the Disjoint Set."""
        return self.__item_count

    def make_set(self, item: Any) -> None:
        """Create a new set containing the given item.
        
        Args:
            item: The item to be added as a new set.
        
        Raises:
            ValueError: If the item already exists in the Disjoint Set.
        """

        if item in self.__item_map:
            raise ValueError(f"Item '{item}' already exists in the Disjoint Set.")
        
        index = len(self.__parents)
        self.__item_map[item] = index
        self.__parents.append(index)  # Initially, each item is its own parent
        self.__ranks.append(0)       # Initial rank is 0
        self.__item_count += 1
        self.__count += 1

    def find(self, item: Any) -> Any:
        """Find the representative (root) of the set containing the given item.
        
        Args:
            item: The item to find the representative for.
        
        Returns:
            The representative of the set containing the item.
        
        Raises:
            ValueError: If the item does not exist in the Disjoint Set.
        """

        if item not in self.__item_map:
            raise ValueError(f"Item '{item}' does not exist in the Disjoint Set.")

        index = self.__item_map[item]
        while index != self.__parents[index]:
            self.__parents[index] = self.__parents[self.__parents[index]]  # Path compression
            index = self.__parents[index]

        return index

    def union(self, item1: Any, item2: Any) -> None:
        """Union the sets containing the given items.
        
        Args:
            item1: The first item.
            item2: The second item.
        
        Raises:
            ValueError: If either item does not exist in the Disjoint Set.
        """

        if item1 not in self.__item_map or item2 not in self.__item_map:
            raise ValueError("Both items must exist in the Disjoint Set.")

        root1 = self.find(item1)
        root2 = self.find(item2)

        if root1 != root2:
            # Union by rank
            if self.__ranks[root1] > self.__ranks[root2]:
                self.__parents[root2] = root1
            elif self.__ranks[root1] < self.__ranks[root2]:
                self.__parents[root1] = root2
            else:
                self.__parents[root2] = root1
                self.__ranks[root1] += 1
            self.__count -= 1
