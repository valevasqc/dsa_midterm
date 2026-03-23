from ll import Node, LinkedList
from canciones import canciones

playlist = LinkedList()

for nombre, artista, album in canciones:
	playlist.insert_at_end(Node(nombre, artista, album))

if playlist.start is None:
	print("La playlist esta vacia.")
else:
	actual = playlist.start
	print(f"Total de canciones cargadas: {len(playlist)}")

	while True:
		print("\nReproduciendo ahora:")
		print(f"- Cancion: {actual.data['nombre']}")
		print(f"- Artista: {actual.data['artista']}")
		print(f"- Album: {actual.data['album']}")
		print(f"Shuffle: {'ON' if playlist.shuffle_mode else 'OFF'}")

		print("\nOpciones: [s] toggle shuffle | [n] siguiente | [p] anterior | [q] salir")
		opcion = input("Selecciona una opcion: ").strip().lower()

		if opcion == "s":
			playlist.toggle_shuffle()
			print(f"Shuffle: {'ON' if playlist.shuffle_mode else 'OFF'}")
		elif opcion == "n":
			if playlist.shuffle_mode:
				actual = playlist.next_node(actual)
			elif actual.next is None:
				print("Ya estas en la ultima cancion.")
			else:
				actual = playlist.next_node(actual)
		elif opcion == "p":
			if actual.prev is None:
				print("Ya estas en la primera cancion.")
			else:
				actual = actual.prev
		elif opcion == "q":
			print("Saliendo de la playlist.")
			break
		else:
			print("Opcion invalida. Usa s, n, p o q.")
