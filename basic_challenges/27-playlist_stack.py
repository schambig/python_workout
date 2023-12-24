#!/usr/bin/python3
from stack_node import PlaylistNode


''' This module works in conjunction with `stack_node.py` module '''


class Playlist:
    def __init__(self):
        self.top = None
        self.buttom = None
        self.length = 0


    def add_song(self, song):
        new_song = PlaylistNode(song)
        if self.length == 0:
            self.top = new_song
            self.buttom = new_song
        else:
            new_song.next = self.top
            self.top = new_song
        self.length += 1


playlist = Playlist()
playlist.add_song('Sprinter')
playlist.add_song('Yellow Ferrari')
print(playlist.length)  # 2
