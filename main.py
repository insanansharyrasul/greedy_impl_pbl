from graph import create_sample_network
from dijkstra import DijkstraAlgorithm
from visualizer import GraphVisualizer


def main():
    graph = create_sample_network()
    
    dijkstra = DijkstraAlgorithm(graph)
    
    visualizer = GraphVisualizer(graph)
    visualizer.visualize_network("output/village_network.png")
    
    test_cases = [
        (0, 4),
        (0, 7),
        (1, 6),
        (0, 3),
    ]
    
    routes_for_visualization = []
    
    for start, end in test_cases:
        
        result = dijkstra.find_shortest_path(start, end)
        
        
        if result.success:
            routes_for_visualization.append(
                (start, end, result.path, result.distance)
            )
    
    visualizer.create_multiple_visualizations(routes_for_visualization, prefix="route")
    

if __name__ == "__main__":
    main()
