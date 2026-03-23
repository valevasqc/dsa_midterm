from ll import Node, LinkedList
from canciones import canciones

playlist = LinkedList()

for nombre, artista, album in canciones:
	playlist.insert_at_end(Node(nombre, artista, album))
