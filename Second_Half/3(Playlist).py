class Artist():
    def __init__(self,name:str) -> None:
        self.name = name
        self.songlist:list[Song] = []
        self.albums:list[Album] = []
        self.playlists:list[Playlist] = []
    def assign_song(self,song) -> None:
        if not isinstance(song,Song):
            return
        self.songlist.append(song)
    def assign_album(self,album) -> None:
        if not isinstance(album,Album):
            return
        self.albums.append(album)
    def assign_playlist(self,playlist) -> None:
        if not isinstance(playlist,Playlist):
            return
        self.playlists.append(playlist)




class Album():
    def __init__(self,*artists:tuple[Artist]) -> None:
        if not artists:
            various_artists = Artist('Various artists')
            artists = (various_artists,)
        self.artists = []
        if all(isinstance(x,Artist) for x in artists):
            self.artists.extend(artists)
        else:
            raise Exception('Неверный исполнитель')
        self.songs = []
    def assign_songs(self,*songs) -> None:
        if not songs:
            return
        self.songs.extend(songs)

class Song():
    def __init__(self,name:str,album:Album,*artists:tuple[Artist]) -> None:
        if not isinstance(album, Album):
            raise Exception('Неверно введён альбом')
        if not all(isinstance(x,Artist) for x in artists):
            #print(artists)
            raise Exception('Неверно введён один из исполнителей')
        self.name = name
        self.artists = artists
        self.album = album

class Playlist():
    def __init__(self,name:str,*songs:tuple[Song]) -> None:
        self.songs = []
        self.name = name
        if all(isinstance(x,Song) for x in songs):
            self.songs.extend(songs)
        else:
            raise Exception('Неверный исполнитель')
    def add_song(self,song:Song):
        if isinstance(song, Song):
            self.songs.append(song)

a = Artist('John')
al = Album(a)
s = Song('Life',al, a)
a2 = Artist('Jim')
s2 = Song('Death',al,a,a2)
a.assign_album(al)
a.assign_song(s)
a.assign_song(s2)


pl = Playlist('fav songs', s)
pl.add_song(s2)
a.assign_playlist(pl)
print(s.album,s.artists,s.name)
print(s2.album,s2.artists,s2.name)
print(pl.songs)
print(a.songlist,a.playlists,a.albums)