from ll import Node, LinkedList
from canciones import canciones
from memory_profiler import profile
import time

@profile
def creacion_playlist():
    playlist = LinkedList()
    for nombre, artista, album in canciones:
        playlist.insert_at_end(Node(nombre, artista, album))
    return playlist

playlist = creacion_playlist()
print(f"Total de canciones cargadas: {len(playlist)}")


# time profiling
deltas = []

for _ in range(1000):

    start_time = time.time()
    creacion_playlist()
    end_time = time.time()
    delta_time = end_time - start_time
    deltas.append(delta_time)

avg_time = sum(deltas) / len(deltas)
    
print(f'La función tomó: {round(avg_time, 4)}s en ejecutarse.')
