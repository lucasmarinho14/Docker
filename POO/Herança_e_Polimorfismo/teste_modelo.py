from modelo import Filme, Serie, Playlist

vingadores = Filme("vingadores - guerra infinita", 2018, 160)
vingadores.dar_like()

atlanta = Serie("atlanta", 2018, 2)
atlanta.dar_like()
atlanta.dar_like()

tmep = Filme("todo mundo em pânico", 1999, 100)
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()

demolidor = Serie("demolidor", 2016, 2)

demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]

playlist_fim_de_semana = Playlist("fim de semana", filmes_e_series)

print(f"Tamanho da playlist: {len(playlist_fim_de_semana)}")

print(len(playlist_fim_de_semana))

for programa in playlist_fim_de_semana:
    print(programa)




