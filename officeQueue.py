class OfficeQueue:
    def __init__(self):
        self.queue = []
        self.q_max = 0

    def push(self, priority: int = 0) -> int:
        # Zmienną "new_number" zastosowałem tyłko dla lepszej czytelności kodu.
        new_number = self.q_max + 1
        self.queue.append((priority, new_number))
        self.q_max = new_number
        return new_number

    def pop(self) -> int:
        if len(self.queue):
            next_n: tuple = [element for element in self.queue if element[0] == max(self.queue)[0]][0]
            # Znajduję najwyższy element, filtruję kolejkę po max[0] i zwracam pierwszy element listy.
            self.queue.remove(next_n)
            return next_n[1]
        return None
