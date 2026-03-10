class Solution(object):
    def canVisitAllRooms(self, rooms):
        q=deque()
        q.append(0)
        visited={}
        visited[0]=True

        while q:
            cur_v=q.popleft()
            for v in rooms[cur_v]:
                if v not in visited:
                    q.append(v)
                    visited[v]=True
        
        for i in range(len(rooms)):
            if i not in visited:
                return False
        
        return True
