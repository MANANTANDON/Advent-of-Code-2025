def StarFifteen():
    def distance(p1, p2):
        return sum((a-b)**2 for a, b in zip(p1, p2)) ** 0.5

    def find(parent, i):
        if parent[i] != i:
            parent[i] = find(parent, parent[i])
        return parent[i]

    points = [tuple(map(int, line.strip().split(','))) 
              for line in open('input.txt')]

    edges = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            edges.append((distance(points[i], points[j]), i, j))

    edges.sort()

    parent = list(range(len(points)))
    size = [1] * len(points)

    target_connections = 1000
    
    for k, (dist, i, j) in enumerate(edges):
        if k >= target_connections:
            break
        ri, rj = find(parent, i), find(parent, j)
        if ri != rj:
            parent[rj] = ri
            size[ri] += size[rj]

    circuits = {}
    for i in range(len(points)):
        root = find(parent, i)
        circuits[root] = circuits.get(root, 0) + 1

    top3 = sorted(circuits.values(), reverse=True)[:3]
    print(top3[0] * top3[1] * top3[2])

def StarSixteen():
    def distance(p1, p2):
        return sum((a-b)**2 for a, b in zip(p1, p2)) ** 0.5

    def find(parent, i):
        if parent[i] != i:
            parent[i] = find(parent, parent[i])
        return parent[i]

    # Read input
    points = [tuple(map(int, line.strip().split(','))) 
              for line in open('input.txt')]

    n = len(points)
    
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            edges.append((distance(points[i], points[j]), i, j))

    edges.sort()

    parent = list(range(n))
    num_components = n

    for dist, i, j in edges:
        ri, rj = find(parent, i), find(parent, j)
        if ri != rj:
            parent[rj] = ri
            num_components -= 1
            
            if num_components == 1:
                result = points[i][0] * points[j][0]
                print(result)
                break


if __name__ == "__main__":
    StarFifteen()
    StarSixteen()