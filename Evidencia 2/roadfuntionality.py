from graph import Graph 
from typing import Optional
import sys
from generic_search import bfs, Node, node_to_path

sys.path.insert(0, '..')

city: Graph[tuple] = Graph([(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(1,10),(1,11),(1,12),(1,13),(1,14),(1,15),(1,16),(1,17),(1,18),(1,19),(1,20),(1,21),(1,22),(1,23),
                                        (2,1),(2,6),(2,7),(2,13),(2,14),(2,16),(2,17),(2,19),(2,22),(2,23),
                                        (3,1),(3,6),(3,7),(3,13),(3,14),(3,16),(3,17),(3,22),(3,23),
                                        (4,1),(4,5),(4,6),(4,7),(4,12),(4,13),(4,14),(4,16),(4,17),(4,22),(4,23),
                                        (5,1),(5,6),(5,7),(5,13),(5,14),(5,16),(5,17),(5,21),(5,22),(5,23),
                                        (6,1),(6,6),(6,7),(6,13),(6,14),(6,16),(6,17),(6,22),(6,23),
                                        (7,1),(7,6),(7,7),(7,10),(7,13),(7,14),(7,16),(7,17),(7,22),(7,23),
                                        (8,1),(8,2),(8,3),(8,4),(8,5),(8,6),(8,7),(8,8),(8,9),(8,10),(8,11),(8,12),(8,13),(8,14),(8,15),(8,16),(8,17),(8,18),(8,19),(8,20),(8,21),(8,22),(8,23),
                                        (9,1),(9,2),(9,3),(9,4),(9,5),(9,6),(9,7),(9,8),(9,9),(9,10),(9,11),(9,12),(9,13),(9,14),(9,15),(9,16),(9,17),(9,18),(9,19),(9,20),(9,21),(9,22),(9,23),
                                        (10,1),(10,13),(10,17),(10,22),
                                        (11,1),(11,2),(11,3),(11,4),(11,5),(11,6),(11,7),(11,8),(11,9),(11,10),(11,11),(11,12),(11,13),(11,14),(11,15),(11,16),(11,17),(11,18),(11,19),(11,20),(11,21),(11,22),(11,23),
                                        (12,1),(12,2),(12,3),(12,4),(12,5),(12,6),(12,7),(12,8),(12,9),(12,10),(12,11),(12,12),(12,13),(12,14),(12,15),(12,16),(12,17),(12,18),(12,19),(12,20),(12,21),(12,22),(12,23),
                                        (13,1),(13,6),(13,7),(13,13),(13,14),(13,16),(13,17),(13,22),(13,23),
                                        (14,1),(14,6),(14,7),(14,13),(14,14),(14,16),(14,17),(14,18),(14,22),(14,23),
                                        (15,1),(15,2),(15,5),(15,6),(15,7),(15,12),(15,13),(15,14),(15,16),(15,17),(15,22),(15,23),
                                        (16,1),(16,6),(16,7),(16,13),(16,14),(16,16),(16,17),(16,22),(16,23),
                                        (17,1),(17,2),(17,3),(17,4),(17,5),(17,6),(17,7),(17,8),(17,9),(17,10),(17,11),(17,12),(17,13),(17,14),(17,16),(17,17),(17,22),(17,23),
                                        (18,1),(18,2),(18,3),(18,4),(18,5),(18,6),(18,7),(18,8),(18,9),(18,10),(18,11),(18,12),(18,13),(18,14),(18,16),(18,17),(18,22),(18,23),
                                        (19,1),(19,3),(19,13),(19,14),(19,16),(19,17),(19,22),(19,23),
                                        (20,1),(20,12),(20,13),(20,14),(20,16),(20,17),(20,18),(20,22),(20,23),
                                        (21,1),(21,13),(21,14),(21,16),(21,17),(21,22),(21,23),
                                        (22,1),(22,3),(22,13),(22,14),(22,16),(22,17),(22,21),(22,22),(22,23),
                                        (23,1),(23,2),(23,3),(23,4),(23,5),(23,6),(23,7),(23,8),(23,9),(23,10),(23,11),(23,12),(23,13),(23,14),(23,15),(23,16),(23,17),(23,18),(23,19),(23,20),(23,21),(23,22),(23,23)

                                    ])
    
def shortest_path(initial_point: str, final_point: str):
    bfs_result: Optional[Node[str]] = bfs(initial_point, 
                                            lambda x: x == final_point, 
                                            city.neighbors_for_vertex)
    if bfs_result is None:
        print("No solution found using breadth-first search!")
    else:
        path: list[str] = node_to_path(bfs_result)
        #print(f"Path from {initial_point} to {final_point}:")
        #print(path)
        return(path)



#LINEA AMARILLA IZQ
city.add_edge_by_vertices((23,1), (22,1))
city.add_edge_by_vertices((22,1), (21,1))
city.add_edge_by_vertices((21,1), (20,1))
city.add_edge_by_vertices((20,1), (19,1))
city.add_edge_by_vertices((19,1), (18,1)) #AQUI
city.add_edge_by_vertices((18,1), (17,1)) #AQUI
city.add_edge_by_vertices((17,1), (16,1))
city.add_edge_by_vertices((16,1), (15,1))
city.add_edge_by_vertices((15,1), (15,2)) #UNION AL ESTACIONAMIENTO
city.add_edge_by_vertices((15,1), (14,1))
city.add_edge_by_vertices((14,1), (13,1))
city.add_edge_by_vertices((13,1), (12,1)) #AQUI
city.add_edge_by_vertices((12,1), (11,1)) #AQUI
city.add_edge_by_vertices((11,1), (10,1))
city.add_edge_by_vertices((10,1), (9,1)) #AQUI
city.add_edge_by_vertices((9,1), (8,1)) #AQUI
city.add_edge_by_vertices((8,1), (7,1))
city.add_edge_by_vertices((7,1), (6,1))
city.add_edge_by_vertices((6,1), (5,1))
city.add_edge_by_vertices((5,1), (4,1))
city.add_edge_by_vertices((4,1), (3,1))
city.add_edge_by_vertices((3,1), (2,1))
city.add_edge_by_vertices((2,1), (1,1))

#LINEA AMARILLA SUR
city.add_edge_by_vertices((1,1), (1,2))
city.add_edge_by_vertices((1,2), (1,3))
city.add_edge_by_vertices((1,3), (1,4))
city.add_edge_by_vertices((1,4), (1,5))
city.add_edge_by_vertices((1,5), (1,6))
city.add_edge_by_vertices((1,6), (1,7))
city.add_edge_by_vertices((1,6), (2,6))
city.add_edge_by_vertices((1,7), (1,8))
city.add_edge_by_vertices((1,7), (2,7))
city.add_edge_by_vertices((1,8), (1,9))
city.add_edge_by_vertices((1,9), (1,10))
city.add_edge_by_vertices((1,10), (1,11))
city.add_edge_by_vertices((1,11), (1,12))
city.add_edge_by_vertices((1,12), (1,13))
city.add_edge_by_vertices((1,13), (2,13))
city.add_edge_by_vertices((1,13), (1,14))
city.add_edge_by_vertices((1,14), (2,14))
city.add_edge_by_vertices((1,14), (1,15))
city.add_edge_by_vertices((1,15), (1,16))
city.add_edge_by_vertices((1,16), (2,16))
city.add_edge_by_vertices((1,16), (1,17))
city.add_edge_by_vertices((1,17), (1,18))
city.add_edge_by_vertices((1,18), (1,19))
city.add_edge_by_vertices((1,19), (2,19))
city.add_edge_by_vertices((1,19), (1,20))
city.add_edge_by_vertices((1,20), (1,21))
city.add_edge_by_vertices((1,21), (1,22))
#city.add_edge_by_vertices((1,22), (1,23))

#LINEA MORADA DERECHA
city.add_edge_by_vertices((1,22), (2,22))
city.add_edge_by_vertices((2,22), (3,22))
city.add_edge_by_vertices((3,22), (4,22))
city.add_edge_by_vertices((4,22), (5,22))
city.add_edge_by_vertices((5,22), (5,21))
city.add_edge_by_vertices((5,22), (6,22))
city.add_edge_by_vertices((6,22), (7,22))
city.add_edge_by_vertices((7,22), (8,22))
city.add_edge_by_vertices((8,22), (8,21))
city.add_edge_by_vertices((8,22), (9,22))
city.add_edge_by_vertices((9,22), (9,21))
city.add_edge_by_vertices((9,22), (10,22))
city.add_edge_by_vertices((10,22), (11,22))
city.add_edge_by_vertices((11,22), (11,21))
city.add_edge_by_vertices((11,22), (12,22))
city.add_edge_by_vertices((12,22), (13,22))
city.add_edge_by_vertices((12,22), (12,21))
city.add_edge_by_vertices((13,22), (14,22))
city.add_edge_by_vertices((14,22), (15,22))
city.add_edge_by_vertices((15,22), (16,22))
city.add_edge_by_vertices((16,22), (17,22))
city.add_edge_by_vertices((17,22), (18,22))
city.add_edge_by_vertices((18,22), (19,22))
city.add_edge_by_vertices((19,22), (20,22))
city.add_edge_by_vertices((20,22), (21,22))
city.add_edge_by_vertices((21,22), (22,22))
city.add_edge_by_vertices((22,22), (23,22))

#Linea morada norte
city.add_edge_by_vertices((23,22), (23,21))
city.add_edge_by_vertices((23,21), (23,20))
city.add_edge_by_vertices((23,20), (23,19))
city.add_edge_by_vertices((23,19), (23,18))
city.add_edge_by_vertices((23,18), (23,17))
city.add_edge_by_vertices((23,17), (22,17))
city.add_edge_by_vertices((23,17), (23,16))
city.add_edge_by_vertices((23,16), (23,15))
city.add_edge_by_vertices((23,16), (22,16))
city.add_edge_by_vertices((23,16), (23,15))
city.add_edge_by_vertices((23,15), (23,14))
city.add_edge_by_vertices((23,14), (23,13))
city.add_edge_by_vertices((23,13), (22,13))#aqui
city.add_edge_by_vertices((23,13), (23,12))
city.add_edge_by_vertices((23,12), (23,11))
city.add_edge_by_vertices((23,11), (23,10))
city.add_edge_by_vertices((23,10), (23,9))
city.add_edge_by_vertices((23,9), (23,8))
city.add_edge_by_vertices((23,8), (23,7))
city.add_edge_by_vertices((23,7), (23,6))
city.add_edge_by_vertices((23,6), (23,5))
city.add_edge_by_vertices((23,5), (23,4))
city.add_edge_by_vertices((23,4), (23,3))
city.add_edge_by_vertices((23,3), (22,3))
city.add_edge_by_vertices((23,3), (23,2))
city.add_edge_by_vertices((23,2), (23,1))

#LINEA MORADA CENTRO
city.add_edge_by_vertices((22,13), (21,13))
city.add_edge_by_vertices((21,13), (20,13))
city.add_edge_by_vertices((20,13), (19,13))
city.add_edge_by_vertices((20,13), (20,12))
city.add_edge_by_vertices((19,13), (18,13))
city.add_edge_by_vertices((18,13), (17,13))
city.add_edge_by_vertices((18,13), (18,12))
city.add_edge_by_vertices((17,13), (16,13))
city.add_edge_by_vertices((17,13), (17,12))
city.add_edge_by_vertices((16,13), (15,13))
city.add_edge_by_vertices((15,13), (14,13))
city.add_edge_by_vertices((15,13), (15,12))
city.add_edge_by_vertices((14,13), (13,13))
city.add_edge_by_vertices((13,13), (12,13))
city.add_edge_by_vertices((12,13), (11,13))
city.add_edge_by_vertices((12,13), (12,12))
city.add_edge_by_vertices((11,13), (10,13))
city.add_edge_by_vertices((11,13), (11,12))
city.add_edge_by_vertices((10,13), (9,13))
city.add_edge_by_vertices((9,13), (8,13))
city.add_edge_by_vertices((9,13), (9,12))
city.add_edge_by_vertices((8,13), (7,13))
city.add_edge_by_vertices((8,13), (8,12))
city.add_edge_by_vertices((7,13), (6,13))
city.add_edge_by_vertices((6,13), (5,13))
city.add_edge_by_vertices((5,13), (4,13))
city.add_edge_by_vertices((4,13), (3,13))
city.add_edge_by_vertices((4,13), (4,12))
city.add_edge_by_vertices((3,13), (2,13))

#DOBLE LL AMARILLA CENTRO
city.add_edge_by_vertices((23,14), (22,14))
city.add_edge_by_vertices((22,14), (21,14))
city.add_edge_by_vertices((21,14), (20,14))
city.add_edge_by_vertices((20,14), (19,14))
city.add_edge_by_vertices((19,14), (18,14))
city.add_edge_by_vertices((18,14), (17,14))
city.add_edge_by_vertices((17,14), (16,14))
city.add_edge_by_vertices((16,14), (15,14))
city.add_edge_by_vertices((15,14), (14,14))
city.add_edge_by_vertices((14,14), (13,14))
city.add_edge_by_vertices((13,14), (12,14))
city.add_edge_by_vertices((12,14), (12,15))
city.add_edge_by_vertices((12,15), (12,16))
city.add_edge_by_vertices((12,16), (12,17))
city.add_edge_by_vertices((12,17), (13,17))
city.add_edge_by_vertices((13,17), (14,17))
city.add_edge_by_vertices((14,17), (14,18))
city.add_edge_by_vertices((14,17), (15,17))
city.add_edge_by_vertices((15,17), (16,17))
city.add_edge_by_vertices((16,17), (17,17))
city.add_edge_by_vertices((17,17), (18,17))
city.add_edge_by_vertices((18,17), (19,17))
city.add_edge_by_vertices((19,17), (20,17))
city.add_edge_by_vertices((20,17), (20,18))
city.add_edge_by_vertices((20,17), (21,17))
city.add_edge_by_vertices((21,17), (22,17))
city.add_edge_by_vertices((12,17), (12,18))
city.add_edge_by_vertices((12,18), (12,19))
city.add_edge_by_vertices((12,19), (12,20))
city.add_edge_by_vertices((12,20), (12,21))
city.add_edge_by_vertices((12,17), (11,17))
city.add_edge_by_vertices((11,17), (10,17))
city.add_edge_by_vertices((10,17), (9,17))
city.add_edge_by_vertices((9,17), (8,17))
city.add_edge_by_vertices((8,17), (7,17))
city.add_edge_by_vertices((7,17), (6,17))
city.add_edge_by_vertices((6,17), (5,17))
city.add_edge_by_vertices((5,17), (4,17))
city.add_edge_by_vertices((4,17), (3,17))
city.add_edge_by_vertices((3,17), (2,17))
city.add_edge_by_vertices((2,17), (1,17))
city.add_edge_by_vertices((2,16), (3,16))
city.add_edge_by_vertices((3,16), (4,16))
city.add_edge_by_vertices((4,16), (5,16))
city.add_edge_by_vertices((5,16), (6,16))
city.add_edge_by_vertices((6,16), (7,16))
city.add_edge_by_vertices((7,16), (8,16))
city.add_edge_by_vertices((8,16), (9,16))
city.add_edge_by_vertices((8,16), (9,16))
city.add_edge_by_vertices((2,14), (3,14))
city.add_edge_by_vertices((3,14), (4,14))
city.add_edge_by_vertices((4,14), (5,14))
city.add_edge_by_vertices((5,14), (6,14))
city.add_edge_by_vertices((6,14), (7,14))
city.add_edge_by_vertices((7,14), (8,14))

#LINEA AMARILLA SUR MEDIO DERECHO
city.add_edge_by_vertices((2,14), (3,14))
city.add_edge_by_vertices((3,14), (4,14))
city.add_edge_by_vertices((4,14), (5,14))
city.add_edge_by_vertices((5,14), (6,14))
city.add_edge_by_vertices((6,14), (7,14))
city.add_edge_by_vertices((7,14), (8,14))
city.add_edge_by_vertices((8,14), (9,14))

#lINEA AMARILLA SUR HORIZONTAL
city.add_edge_by_vertices((9,1), (9,2))
city.add_edge_by_vertices((9,2), (9,3))
city.add_edge_by_vertices((9,3), (9,4))
city.add_edge_by_vertices((9,4), (9,5))
city.add_edge_by_vertices((9,5), (9,6))
city.add_edge_by_vertices((9,6), (9,7))
city.add_edge_by_vertices((9,7), (9,8))
city.add_edge_by_vertices((9,8), (9,9))
city.add_edge_by_vertices((9,9), (9,10))
city.add_edge_by_vertices((9,10), (9,11))
city.add_edge_by_vertices((9,11), (9,12))
city.add_edge_by_vertices((9,12), (9,13))
city.add_edge_by_vertices((9,13), (9,14))
city.add_edge_by_vertices((9,14), (9,15))
city.add_edge_by_vertices((9,15), (9,16))
city.add_edge_by_vertices((9,16), (9,17))
city.add_edge_by_vertices((9,17), (9,18))
city.add_edge_by_vertices((9,18), (9,19))
city.add_edge_by_vertices((9,19), (9,20))
city.add_edge_by_vertices((9,20), (9,21))
city.add_edge_by_vertices((9,21), (9,22))

#lINEA MORADA SUR HORIZONTAL
city.add_edge_by_vertices((8,1), (8,2))
city.add_edge_by_vertices((8,2), (8,3))
city.add_edge_by_vertices((8,3), (8,4))
city.add_edge_by_vertices((8,4), (8,5))
city.add_edge_by_vertices((8,5), (8,6))
city.add_edge_by_vertices((8,6), (8,7))
city.add_edge_by_vertices((8,7), (8,8))
city.add_edge_by_vertices((8,8), (8,9))
city.add_edge_by_vertices((8,9), (8,10))
city.add_edge_by_vertices((8,10), (7,10))
city.add_edge_by_vertices((8,11), (8,12))
city.add_edge_by_vertices((8,12), (8,13))

#lINEA MORADA SUR VERTICAL
city.add_edge_by_vertices((8,6), (7,6))
city.add_edge_by_vertices((7,6), (6,6))
city.add_edge_by_vertices((6,6), (5,6))
city.add_edge_by_vertices((5,6), (4,6))
city.add_edge_by_vertices((4,6), (4,5))
city.add_edge_by_vertices((4,6), (3,6))
city.add_edge_by_vertices((3,6), (2,6))
city.add_edge_by_vertices((2,6), (1,6))

#lINEA AMARILLA SUR VERTICAL
city.add_edge_by_vertices((8,7), (7,7))
city.add_edge_by_vertices((7,7), (6,7))
city.add_edge_by_vertices((6,7), (5,7))
city.add_edge_by_vertices((5,7), (4,7))
city.add_edge_by_vertices((4,7), (3,7))
city.add_edge_by_vertices((3,7), (2,7))
city.add_edge_by_vertices((8,7), (7,7))

#lINEA AMARILLA NORTE HORIZONTAL
city.add_edge_by_vertices((18,1), (18,2))
city.add_edge_by_vertices((18,2), (18,3))
city.add_edge_by_vertices((18,3), (19,3))
city.add_edge_by_vertices((18,3), (18,4))
city.add_edge_by_vertices((18,4), (18,5))
city.add_edge_by_vertices((18,5), (18,6))
city.add_edge_by_vertices((18,6), (18,7))
city.add_edge_by_vertices((18,7), (18,8))
city.add_edge_by_vertices((18,8), (18,9))
city.add_edge_by_vertices((18,9), (18,10))
city.add_edge_by_vertices((18,10), (18,11))
city.add_edge_by_vertices((18,11), (18,12))
city.add_edge_by_vertices((18,12), (18,13))

#LINEA MORADA NORTE HORIZONTAL
city.add_edge_by_vertices((17,13), (17,12))
city.add_edge_by_vertices((17,12), (17,11))
city.add_edge_by_vertices((17,11), (17,10))
city.add_edge_by_vertices((17,10), (17,9))
city.add_edge_by_vertices((17,9), (17,8))
city.add_edge_by_vertices((17,8), (17,7))
city.add_edge_by_vertices((17,7), (17,6))
city.add_edge_by_vertices((17,6), (17,5))
city.add_edge_by_vertices((17,5), (17,4))
city.add_edge_by_vertices((17,4), (17,3))
city.add_edge_by_vertices((17,3), (17,2))
city.add_edge_by_vertices((17,2), (17,1))

#lINEA MORADA CENTRO HORIZONTAL
city.add_edge_by_vertices((11,1), (11,2))
city.add_edge_by_vertices((11,2), (11,3))
city.add_edge_by_vertices((11,3), (11,4))
city.add_edge_by_vertices((11,4), (11,5))
city.add_edge_by_vertices((11,5), (11,6))
city.add_edge_by_vertices((11,6), (11,7))
city.add_edge_by_vertices((11,7), (11,8))
city.add_edge_by_vertices((11,8), (11,9))
city.add_edge_by_vertices((11,9), (11,10))
city.add_edge_by_vertices((11,10), (11,11))
city.add_edge_by_vertices((11,11), (11,12))
city.add_edge_by_vertices((11,12), (11,13))
city.add_edge_by_vertices((11,13), (11,14))
city.add_edge_by_vertices((11,14), (11,15))
city.add_edge_by_vertices((11,15), (11,16))
city.add_edge_by_vertices((11,16), (11,17))
city.add_edge_by_vertices((11,17), (11,18))
city.add_edge_by_vertices((11,18), (11,19))
city.add_edge_by_vertices((11,19), (11,20))
city.add_edge_by_vertices((11,21), (11,22))
city.add_edge_by_vertices((11,6), (12,6))
city.add_edge_by_vertices((12,6), (13,6))
city.add_edge_by_vertices((13,6), (14,6))
city.add_edge_by_vertices((14,6), (15,6))
city.add_edge_by_vertices((15,6), (16,6))
city.add_edge_by_vertices((16,6), (17,6))


if __name__ == '__main__':
    #print(city)
    #shortest_path((22,3),(2,19),city)
    #shortest_path((22,3),(19,3))
    ...
