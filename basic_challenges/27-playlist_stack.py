#!/usr/bin/python3
from stack_node import PlaylistNode


''' This module works in conjunction with `stack_node.py` module '''


class Playlist:
    def __init__(self):
        self.top = None
        self.buttom = None
        self.length = 0
