class LRUCache:

    from collections import deque

    def __init__(self, capacity: int):
        self.cap = capacity
        self.que = deque()
        self.vmap = {}
        

    def get(self, key: int) -> int:
        if key not in self.vmap:
            return -1
        self.que.remove(key)
        self.que.append(key)
        return self.vmap[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.vmap:
            self.que.remove(key)
        
        if len(self.que)==self.cap:
            del self.vmap[self.que.popleft()]
        
        self.vmap[key] = value
        self.que.append(key)
