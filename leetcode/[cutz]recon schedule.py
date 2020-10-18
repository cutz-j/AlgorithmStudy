from collections import defaultdict, deque


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # graph
        adj = defaultdict(deque)
        for depart, arrival in tickets:
            adj[depart].append(arrival)
            adj[depart] = deque(sorted(adj[depart]))

        route = []

        def dfs(a):
            while adj[a]:
                dfs(adj[a].popleft())
            route.append(a)

        dfs("JFK")
        return route[::-1]



