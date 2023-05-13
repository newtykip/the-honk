# note: On Windows, pip install windows-curses
from __future__ import annotations
from urllib.request import urlopen
from json import loads as loadJson
from webbrowser import open_new_tab as browserOpen
from typing import List
from re import search as searchRegex
from pickle import load as pickleLoad, dump as pickleDump
from os.path import join as pathJoin, exists as pathExists
from sys import path as sysPath
import curses

class InvalidID(Exception): pass

class Playlist:
    def __init__(self, nickname: str):
        self.__nickname = nickname
        self.__videos: List[Video] = []
        self.__file = Playlist.getPath(nickname)

        if pathExists(self.__file):
            with open(self.__file, "rb") as f:
                self.__videos = pickleLoad(f)

    @staticmethod
    def getPath(nickname: str) -> str:
        return pathJoin(sysPath[0], f"{nickname}.playlist")

    def getName(self) -> str:
        return self.__nickname

    def addVideo(self, video: Video):
        self.__videos.append(video)
        return self.__save()

    def __save(self):
        with open(self.__file, "wb") as f:
            pickleDump(self.__videos, f)

        return self

    def __getitem__(self, index: int):
        if index > len(self.__videos) - 1:
            raise IndexError("Out of bounds")

        return self.__videos[index]

    def __delitem__(self, index: int):
        if index > len(self.__videos) - 1:
            raise IndexError("Out of bounds")

        del self.__videos[index]
        self.__save()

    def __len__(self):
        return len(self.__videos)

class Video:
    def __init__(self, id: str):
        self.__id = id
        self.__url = f"https://youtu.be/{self.__id}"

        try:
            with urlopen(f"https://www.youtube.com/oembed?url=https://youtu.be/{self.__id}&format=json") as response:
                data = response.read()
                
                data = loadJson(data)
                self.__title = data["title"]
                self.__author = data["author_name"]
        except:
            raise InvalidID(f"{id} is not a valid ID!")

    def __str__(self):
        return f"{self.__author} - {self.__title}"

    def open(self):
        browserOpen(self.__url)

# Initialise curses
screen = curses.initscr()
screen.keypad(True)
curses.cbreak()
curses.noecho()

# Initialise colours
curses.start_color()
curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)

black, white, red = curses.color_pair(1), curses.color_pair(2), curses.color_pair(3)

def selectMenu(screen, options: List[str]):
    selectedIndex = 0
    optionCount = len(options)

    while True:
        screen.clear()
        screen.addstr("Pick an option:\n\n", curses.A_BOLD)

        for i in range(optionCount):
            screen.addstr(f"{i + 1}. ")
            screen.addstr(f"{options[i]}\n", black if i == selectedIndex else white)

        c = screen.getch()

        if c == curses.KEY_UP or c == curses.KEY_LEFT:
            selectedIndex -= 1 - optionCount
            selectedIndex %= optionCount
        
        elif c == curses.KEY_DOWN or c == curses.KEY_RIGHT:
            selectedIndex += 1
            selectedIndex %= optionCount

        elif c == curses.KEY_ENTER or chr(c) in '\n\r':
            return selectedIndex + 1

def addVideo(screen, playlist: Playlist):
    hasErrored = False

    while True:
        screen.clear()
        screen.addstr(0, 0, "Please enter a YouTube URL/ID:", curses.A_BOLD)

        # Display the error message if necessary
        if hasErrored:
            screen.addstr(3, 0, "Please make sure you have entered a valid URL/ID.", red | curses.A_BOLD)

        # Fetch the inputted data
        curses.echo()
        videoId = screen.getstr(1, 0, 50).decode("utf-8")
        curses.noecho()

        # Attempt to extract a video ID
        parsed = searchRegex(r"(?:youtu\.be\/|youtube\.com(?:\/embed\/|\/v\/|\/watch\?v=|\/user\/\S+|\/ytscreeningroom\?v=))([\w\-]{10,12})\b", videoId)

        if parsed:
            videoId = parsed.group(1)

        # Attempt to add the video to the playlist
        try:
            video = Video(str(videoId))
            playlist.addVideo(video)

            break
        except InvalidID:
            hasErrored = True

def viewPlaylist(screen, playlist: Playlist):
    selectedIndex = 0
    selectedPlay = True
    playlistLength = len(playlist)

    while True:
        screen.clear()
        screen.addstr(f"{playlist.getName()} playlist\n", curses.A_BOLD)
        screen.addstr("Press the backspace key to exit this menu.\n\n")

        if playlistLength == 0:
            screen.addstr("There is nothing here!\n")
            c = screen.getch()
        else:
            for i in range(playlistLength):
                screen.addstr(f"{i + 1}. {playlist[i]}  ")
                screen.addstr("[PLAY]", black if selectedPlay and selectedIndex == i else white)
                screen.addstr("  ")
                screen.addstr("[DELETE]\n", black if not selectedPlay and selectedIndex == i else white)

            c = screen.getch()
            
            if c == curses.KEY_UP:
                selectedIndex -= 1 - playlistLength
                selectedIndex %= playlistLength
        
            elif c == curses.KEY_DOWN:
                selectedIndex += 1
                selectedIndex %= playlistLength

            elif c == curses.KEY_LEFT:
                selectedPlay = True

            elif c == curses.KEY_RIGHT:
                selectedPlay = False

            elif c == curses.KEY_ENTER or chr(c) in '\n\r':
                if selectedPlay:
                    playlist[selectedIndex].open()
                else:
                    del playlist[selectedIndex]
                    playlistLength -= 1
                    selectedIndex = 0 if selectedIndex == 0 else selectedIndex - 1  
            
        if c == 8 or c == 127 or c == curses.KEY_BACKSPACE:
            break

# todo: add custom playlist names

if __name__ == "__main__":
    playlist = Playlist("main")

    while True:
        choice = selectMenu(screen, ["Add a video to the playlist", "View the playlist", "Exit"])

        if choice == 1:
            addVideo(screen, playlist)
        elif choice == 2:
            viewPlaylist(screen, playlist)
        elif choice == 3:
            break
    
    # Exit curses
    curses.nocbreak()
    screen.keypad(False)
    curses.echo()
    curses.endwin()