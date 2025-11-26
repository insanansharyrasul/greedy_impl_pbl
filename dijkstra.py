import heapq
from typing import Dict, List, Optional
from graph import VillageGraph


class DijkstraResult:

    def __init__(self, distance: float, path: List[int], success: bool = True):
        self.distance = distance
        self.path = path
        self.success = success
    
    def __repr__(self):
        if self.success:
            return f"DijkstraResult(distance={self.distance}, path={self.path})"
        return "DijkstraResult(no path found)"

class DijkstraAlgorithm:
    
    def __init__(self, graph: VillageGraph):
        self.graph = graph
    
    def find_shortest_path(self, start: int, end: int) -> DijkstraResult:
        distances: Dict[int, float] = {v: float('infinity') 
                                       for v in self.graph.get_all_villages()}
        distances[start] = 0
        
        parent: Dict[int, Optional[int]] = {v: None 
                                            for v in self.graph.get_all_villages()}
        
        pq = [(0, start)]
        
        visited = set()
        
        while pq:
            current_dist, current = heapq.heappop(pq)
            
            if current in visited:
                continue
            
            visited.add(current)
            
            if current == end:
                break
            
            if current_dist > distances[current]:
                continue
            
            for neighbor, weight in self.graph.get_neighbors(current):
                distance = current_dist + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    parent[neighbor] = current
                    heapq.heappush(pq, (distance, neighbor))
        
        if distances[end] == float('infinity'):
            return DijkstraResult(0, [], success=False)
        
        path = self._reconstruct_path(parent, start, end)
        return DijkstraResult(distances[end], path)
    
    def _reconstruct_path(self, parent: Dict[int, Optional[int]], 
                         start: int, end: int) -> List[int]:
        path = []
        current = end
        
        while current is not None:
            path.append(current)
            if current == start:
                break
            current = parent[current]
        
        path.reverse()
        return path
