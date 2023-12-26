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


    def play_song(self):
        if self.top is None:
            raise Exception('There is no song in the playlist.')
        if self.top == self.buttom:
            self.buttom = None
        top_song = self.top
        self.top = self.top.next
        self.length -= 1
        return top_song.value
    

    def get_playlist(self):
        current = self.top
        playlist = []
        while current is not None:
            playlist.append(current.value)
            current = current.next
        return playlist


playlist = Playlist()
playlist.add_song('Sprinter')
playlist.add_song('Yellow Ferrari')
playlist.add_song('Phospholipid')
print(playlist.length)  # 3

print(playlist.play_song())  # Phospholipid
print(playlist.play_song())  # Yellow Ferrari
print(playlist.length)  # 1

print(playlist.get_playlist())

print(playlist.play_song())
print(playlist.length)  # 0
print(playlist.play_song())  # Exception: There is no song in the playlist.
