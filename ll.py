from typing import Any
import random

class Node:
    def __init__(self, nombre: str, artista: str, album: str):
        self.data = {
            "nombre": nombre,
            "artista": artista,
            "album": album
        }
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"(DATA: {self.data} | NEXT: {self.next})"

class LinkedList:
    def __init__(self):
        self.start = None
        self.shuffle_mode = False

    def __repr__(self):
        nodes = ["START"]
        for node in self:
            nodes.append(
                f"{node.data['nombre']} - {node.data['artista']} ({node.data['album']})"
            )
        nodes.append("NIL")
        return "\n" + " --> ".join(nodes)

    def __iter__(self):
        node = self.start
        while node is not None:
            yield node
            node = node.next

    def __len__(self):
        length = 0
        for _ in self:
            length += 1
        return length

    def traverse(self):
        for node in self:
            print(node.data)

    def insert_at_beginning(self, element: Node):
        element.next = self.start
        element.prev = None
        if self.start is not None:
            self.start.prev = element
        self.start = element

    def insert_at_end(self, element: Node):
        if self.start is None:
            self.start = element
            element.next = None
            element.prev = None
            return
        current = self.start
        while current.next is not None:
            current = current.next
        current.next = element
        element.prev = current
        element.next = None

    def insert_after_node(self, element: Node, node_reference: str):
        for current in self:
            if current.data["nombre"] == node_reference:
                element.next = current.next
                element.prev = current

                if current.next is not None:
                    current.next.prev = element

                current.next = element
                return

    def delete_node(self, element_data: Any):
        if self.start is None:
            return
        if self.start.data["nombre"] == element_data:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None
            return
        for current in self:
            if current.data["nombre"] == element_data:
                if current.prev is not None:
                    current.prev.next = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                return

    def search(self, element_data: Any):
        for node in self:
            if node.data["nombre"] == element_data:
                return node
        return None

    def toggle_shuffle(self):
        self.shuffle_mode = not self.shuffle_mode

    def random_node(self, current):
        while True:
            index = random.randint(0, len(self) - 1)
            node = self.start
            for _ in range(index):
                node = node.next
            if node != current:
                return node

    def next_node(self, current):
        if self.shuffle_mode:
            return self.random_node(current)
        return current.next
