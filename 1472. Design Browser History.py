class Node:
    def __init__(self, data):
        self.val = data
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)

    def visit(self, url: str) -> None:
        new = Node(url)
        self.curr.next = new
        new.prev = self.curr
        self.curr = new

    def back(self, steps: int) -> str:
        for i in range(steps):
            if not self.curr.prev:
                return self.curr.val
            self.curr = self.curr.prev
        return self.curr.val 

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if not self.curr.next:
                return self.curr.val
            self.curr = self.curr.next
        return self.curr.val
