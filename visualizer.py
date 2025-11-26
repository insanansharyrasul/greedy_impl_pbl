import matplotlib.pyplot as plt
import math
from typing import List, Optional, Dict, Tuple
from graph import VillageGraph


class GraphVisualizer:
    
    def __init__(self, graph: VillageGraph):
        self.graph = graph
        self.pos: Optional[Dict[int, Tuple[float, float]]] = None
    
    def _compute_layout(self):
        if self.pos is None:
            villages = self.graph.get_all_villages()
            N = len(villages)
            self.pos = {}
            
            for i, village_id in enumerate(sorted(villages)):
                angle = 2 * math.pi * i / N
                self.pos[village_id] = (math.cos(angle) * 3, math.sin(angle) * 3)
    
    def visualize_network(self, filename: str = "output/village_network.png", 
                         show: bool = False) -> None:
        self._compute_layout()
        
        plt.figure(figsize=(14, 10))
        ax = plt.gca()
        
        drawn_edges = set()
        for village in self.graph.get_all_villages():
            for neighbor, weight in self.graph.get_neighbors(village):
                edge = tuple(sorted((village, neighbor)))
                if edge not in drawn_edges:
                    drawn_edges.add(edge)
                    x1, y1 = self.pos[village]
                    x2, y2 = self.pos[neighbor]
                    
                    plt.plot([x1, x2], [y1, y2], 'gray', linewidth=2, alpha=0.6, zorder=1)
                    
                    mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
                    plt.text(mid_x, mid_y, f"{weight} km", 
                            fontsize=8, ha='center', va='center',
                            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='none', alpha=0.7),
                            zorder=2)
        
        for village_id in self.graph.get_all_villages():
            x, y = self.pos[village_id]
            
            circle = plt.Circle((x, y), 0.3, color='lightblue', ec='black', linewidth=2, zorder=3)
            ax.add_patch(circle)
            
            village_name = self.graph.get_village_name(village_id)
            plt.text(x, y, village_name, fontsize=10, fontweight='bold',
                    ha='center', va='center', zorder=4)
        
        plt.title("Jaringan Jalan Antar Desa", fontsize=16, fontweight='bold', pad=20)
        plt.axis('equal')
        plt.axis('off')
        plt.tight_layout()
        
        plt.savefig(filename, dpi=300, bbox_inches='tight', facecolor='white')
        
        if show:
            plt.show()
        else:
            plt.close()
    
    def visualize_path(self, path: List[int], filename: str = "output/shortest_path.png",
                      show: bool = False, title: Optional[str] = None) -> None:
        if len(path) < 2:
            print("Path terlalu pendek untuk divisualisasikan")
            return
        
        self._compute_layout()
        
        plt.figure(figsize=(14, 10))
        ax = plt.gca()
        
        path_edges = set()
        for i in range(len(path) - 1):
            edge = tuple(sorted((path[i], path[i + 1])))
            path_edges.add(edge)
        
        drawn_edges = set()
        for village in self.graph.get_all_villages():
            for neighbor, weight in self.graph.get_neighbors(village):
                edge = tuple(sorted((village, neighbor)))
                if edge not in drawn_edges:
                    drawn_edges.add(edge)
                    x1, y1 = self.pos[village]
                    x2, y2 = self.pos[neighbor]
                    
                    is_in_path = edge in path_edges
                    color = 'red' if is_in_path else 'lightgray'
                    linewidth = 4 if is_in_path else 1.5
                    alpha = 0.8 if is_in_path else 0.3
                    
                    plt.plot([x1, x2], [y1, y2], color=color, linewidth=linewidth, 
                            alpha=alpha, zorder=2 if is_in_path else 1)
                    
                    if is_in_path:
                        mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
                        plt.text(mid_x, mid_y, f"{weight} km", 
                                fontsize=9, fontweight='bold', ha='center', va='center',
                                color='red',
                                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                                         edgecolor='red', alpha=0.9),
                                zorder=3)
        
        for village_id in self.graph.get_all_villages():
            x, y = self.pos[village_id]
            
            if village_id == path[0]:
                color = 'lightgreen'  
            elif village_id == path[-1]:
                color = 'lightcoral'  
            elif village_id in path:
                color = 'gold'  
            else:
                color = 'lightgray' 
            
            circle = plt.Circle((x, y), 0.3, color=color, ec='black', linewidth=2, zorder=4)
            ax.add_patch(circle)
            
            village_name = self.graph.get_village_name(village_id)
            plt.text(x, y, village_name, fontsize=10, fontweight='bold',
                    ha='center', va='center', zorder=5)
        
        if title is None:
            start_name = self.graph.get_village_name(path[0])
            end_name = self.graph.get_village_name(path[-1])
            title = f"Rute Terpendek: {start_name} → {end_name}"
        
        plt.title(title, fontsize=16, fontweight='bold', pad=20)
        
        legend_elements = [
            plt.Line2D([0], [0], marker='o', color='w', 
                      markerfacecolor='lightgreen', markersize=12, 
                      label='Desa Awal', markeredgecolor='black', markeredgewidth=2),
            plt.Line2D([0], [0], marker='o', color='w', 
                      markerfacecolor='lightcoral', markersize=12, 
                      label='Desa Tujuan', markeredgecolor='black', markeredgewidth=2),
            plt.Line2D([0], [0], marker='o', color='w', 
                      markerfacecolor='gold', markersize=12, 
                      label='Desa di Jalur', markeredgecolor='black', markeredgewidth=2),
            plt.Line2D([0], [0], color='red', linewidth=3, label='Jalur Terpendek')
        ]
        plt.legend(handles=legend_elements, loc='upper right', fontsize=10)
        
        plt.axis('equal')
        plt.axis('off')
        plt.tight_layout()
        
        plt.savefig(filename, dpi=300, bbox_inches='tight', facecolor='white')
        
        if show:
            plt.show()
        else:
            plt.close()
    
    def create_multiple_visualizations(self, routes_with_paths: List[tuple],
                                      prefix: str = "route") -> None:
        for idx, (start, end, path, distance) in enumerate(routes_with_paths, 1):
            start_name = self.graph.get_village_name(start)
            end_name = self.graph.get_village_name(end)
            
            filename = f"output/{prefix}_case{idx}.png"
            title = f"Rute {idx}: {start_name} → {end_name} ({distance:.1f} km)"
            
            self.visualize_path(path, filename=filename, title=title)
