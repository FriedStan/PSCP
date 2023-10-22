"""Music Lover"""


def playlist_q_ing(song_amount):
    """Queue the song"""
    playlist = {}
    for _ in range(song_amount):
        current_artist = str(input()).split("-")
        if current_artist[0] in playlist:
            playlist[current_artist[0]].append(current_artist[1])
        else:
            playlist.update({current_artist[0]: [current_artist[1]]})
    for artist, songs in playlist.items():
        print(artist)
        print(*songs, sep="\n")


playlist_q_ing(int(input()))
