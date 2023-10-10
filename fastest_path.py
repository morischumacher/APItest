from dijkstar import Graph, find_path
from sqlalchemy.orm import Session
from utils import get_planet_by_id, get_connections


def calculate_cheapest_path(from_planet: int, to_planet: int, db: Session):
    graph = create_graph(db)
    cheapest_path = find_path(graph, from_planet, to_planet, cost_func=cost_func)

    used_connections = convert_edges(cheapest_path.edges)
    result = BookingOffer(cheapest_path.total_cost, used_connections, get_list_of_planets(db, cheapest_path.nodes))

    return result


def get_list_of_planets(db: Session, planet_ids):
    result = list()
    for id in planet_ids:
        planet = get_planet_by_id(db, id)
        result.append(planet)
    return result


class BookingOffer:
    total_price: int
    used_connection: list
    visited_planets: list

    def __init__(self, total_price, used_connection, visited_planets):
        self.total_price = total_price
        self.used_connection = used_connection
        self.visited_planets = visited_planets


def create_graph(db: Session):
    graph = Graph(undirected=False)

    all_edges = get_connections(db)

    for edge in all_edges:
        graph.add_edge(edge.from_planet_id, edge.to_planet_id, (edge.price, edge))

    return graph


def cost_func(u, v, edge, prev_edge):
    length, name = edge
    cost = length
    if prev_edge:
        prev_name = prev_edge[1]
    else:
        prev_name = None
    return cost


def convert_edges(edges):
    return [edge[1] for edge in edges]

