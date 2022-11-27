from graph import Graph 
from typing import Optional
import sys
from generic_search import bfs, Node, node_to_path

sys.path.insert(0, '..')
    
def shortest_path(initial_point: str, final_point: str, city: Graph):
    bfs_result: Optional[Node[str]] = bfs(initial_point, 
                                            lambda x: x == final_point, 
                                            city.neighbors_for_vertex)
    if bfs_result is None:
        print("No solution found using breadth-first search!")
    else:
        path: list[str] = node_to_path(bfs_result)
        print(f"Path from {initial_point} to {final_point}:")
        print(path)

