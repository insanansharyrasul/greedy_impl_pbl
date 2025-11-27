from typing import Dict, List, Tuple


class VillageGraph:
    """
    PRIMARY PART
    """

    def __init__(self):
        self.village_names: Dict[int, str] = {}
        self.adj_list: Dict[int, List[Tuple[int, float]]] = {}

    def add_village(self, village_id: int, name: str) -> None:
        self.village_names[village_id] = name
        self.adj_list[village_id] = []

    def add_road(self, from_village: int, to_village: int, distance: float) -> None:
        self.adj_list[from_village].append((to_village, distance))
        self.adj_list[to_village].append((from_village, distance))

    def get_neighbors(self, village_id: int) -> List[Tuple[int, float]]:
        return self.adj_list.get(village_id, [])

    def get_all_villages(self) -> List[int]:
        return list(self.village_names.keys())

    """
    VISUALIZER PART
    """

    def get_village_name(self, village_id: int) -> str:
        return self.village_names.get(village_id, f"Desa {village_id}")


def create_sample_network() -> VillageGraph:
    graph = VillageGraph()

    villages = [
        (0, "Desa Makmur"),
        (1, "Desa Sejahtera"),
        (2, "Desa Subur"),
        (3, "Desa Sentosa"),
        (4, "Desa Jaya"),
        (5, "Desa Bahagia"),
        (6, "Desa Maju"),
        (7, "Desa Damai"),
    ]

    for village_id, name in villages:
        graph.add_village(village_id, name)

    roads = [
        (0, 1, 7),  # Makmur - Sejahtera
        (0, 2, 9),  # Makmur - Subur
        (0, 5, 14),  # Makmur - Bahagia
        (1, 2, 10),  # Sejahtera - Subur
        (1, 3, 15),  # Sejahtera - Sentosa
        (2, 3, 11),  # Subur - Sentosa
        (2, 5, 2),  # Subur - Bahagia
        (3, 4, 6),  # Sentosa - Jaya
        (4, 5, 9),  # Jaya - Bahagia
        (5, 6, 8),  # Bahagia - Maju
        (6, 7, 5),  # Maju - Damai
        (3, 7, 12),  # Sentosa - Damai
    ]

    for from_v, to_v, distance in roads:
        graph.add_road(from_v, to_v, distance)

    return graph
