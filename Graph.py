graph = {
    "a" : ["c","d"],
    "b" : ["d","e"],
    "c" : ["a","e"],
    "d" : ["a","b"],
    "e" : ["b","c"],
    "f" : ["c","d"],

}

def define_edges(graph):
    edges = []
    for vertices in graph:
        for nn in graph[vertices]:
            edges.append((vertices,nn))
    return edges


if __name__ == "__main__":
    print(define_edges(graph))