from pydub import AudioSegment

song = AudioSegment.from_file("Voila.mp3",format = "mp3")
cut_first = song[:111*1000]
cut_last = cut_first[-41*10000:]

cut_song = cut_last.export("Voila_cut.mp3",format = "mp3")