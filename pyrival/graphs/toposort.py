# from heapq import heappop, heappush


def toposort(graph):
    n = len(graph)

    res, found = [], [0] * n
    for i in range(n):
        if found[i]:
            continue
        stack = [i]
        while stack:
            node = stack.pop()
            if node < 0:
                res.append(~node)
            elif not found[node]:
                found[node] = 1
                stack.append(~node)
                for nei in graph[node]:
                    if not found[nei]:
                        stack.append(nei)

    # cycle check
    for node in res:
        if any(found[nei] for nei in graph[node]):
            return None
        found[node] = 0

    return res[::-1]


def kahn(graph):
    n = len(graph)

    indeg, idx = [0] * n, [0] * n
    for i in range(n):
        for e in graph[i]:
            indeg[e] += 1

    q, res = [], []
    for i in range(n):
        if indeg[i] == 0:
            q.append(i)  # heappush(q, -i)

    nr = 0
    while q:
        res.append(q.pop())  # res.append(-heappop(q))
        idx[res[-1]], nr = nr, nr + 1
        for e in graph[res[-1]]:
            indeg[e] -= 1
            if indeg[e] == 0:
                q.append(e)  # heappush(q, -e)

    return res, idx, nr == n
