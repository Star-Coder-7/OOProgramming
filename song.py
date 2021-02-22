class Song:
    """Class to represent the song.

    Attributes:
        title (str): The title of the song.
        duration (int): The duration of the songs in seconds. May be 0.
    """

    def __init__(self, title, duration=0):
        """The initializer for the song method.

        Args:
            title (str): Initializes the title attribute.
            artist (Artist): An object representing the creator of the song.
            duration (optional(int)): The initial value for the duration attribute.
            If not specified, it will default to 0 seconds.
        """

        self.title = title
        self.duration = duration

    def getTitle(self):
        return self.title

    name = property(getTitle)


class Album:
    """Class to represent an album, using its track list.

    Attributes:
        name (str): The name of the album.
        year (int): The year the album was released.
        artist (Artist): The artist responsible for the album.
        If not specified, the artist will default to an artist with the name
        `Various Artists`.
        tracks (list[song]): A list of the songs on the album.
    Methods:
        addSong: Used to add a new song in the album's track list.
    """

    def __init__(self, name, year):
        self.name = name
        self.year = year

        self.tracks = []

    def addSong(self, song, position=None):
        """Adds a song to the track list.

        Args:
            song (str): The title of a song to add.
            position (Optional(int)): If specified, the song will be added to that position
                in the track list - inserting between other songs if necessary.
                Otherwise, the song will be added to the end of the list
        """
        songFound = findObject(song, self.tracks)
        if songFound is None:
            songFound = Song(song)
            if position is None:
                self.tracks.append(songFound)
            else:
                self.tracks.insert(position, songFound)


class Artist:
    """Basic class to store artist details.

    Attributes:
        name (str): The name of the artist.
        albums (list[album]): A list of the albums by the artist.
            The list includes only those albums in this collection it is
            not an exhaustive list of the artist's published albums.

    Methods:
        addAlbum: Used to add a new album to the artist's albums list.
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def addAlbum(self, album):
        """Add a new album to the list.

        Args:
            album (Album): Album object to add the list.
                If the album is already present, it will not be again (Although this is yet to be implemented).
        """
        self.albums.append(album)

    def addSong(self, name, year, title):
        """Add a new song to the collection of albums.

        This method will add a song to an album in the collection.
        A new album will be created in the collection if it doesn't already exist.

        Args:
            name (str): The name of the album.
            year (int): The year the album was produced.
            title (str): The title of the song.
        """
        albumFound = findObject(name, self.albums)
        if albumFound is None:
            print(name + " not found")
            albumFound = Album(name, year)
            self.addAlbum(albumFound)
        else:
            print("Found album " + name)

        albumFound.addSong(title)


def findObject(field, objectList):
    """Check 'objectList' to see an object with 'name' attribute equal to 'field' exists, return it id so

    Args:
        field ([type]): (code)
        objectList ([type]): (code)
    """
    for item in objectList:
        if item.name == field:
            return item
    return None


def loadData():

    artistList = []

    with open('albums.txt', 'r') as albums:
        for line in albums:
            # data row should consist of: (artist, album, year, song)
            artistField, albumField, yearField, songField = tuple(line.strip('\n').split('\t'))
            yearField = int(yearField)
            print(f"{artistField} : {albumField} : {yearField} : {songField}")

            newArtist = findObject(artistField, artistList)
            if newArtist is None:
                newArtist = Artist(artistField)
                artistList.append(newArtist)

            newArtist.addSong(albumField, yearField, songField)

    return artistList


def createCheckfile(artistList):
    """Create a check  file from the object data for comparison with the original file."""
    with open('checkfile.txt', 'w') as checkfile:
        for newArtist in artistList:
            for newAlbum in newArtist.albums:
                for newSong in newAlbum.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(newArtist, newAlbum, newSong),
                          file=checkfile)


if __name__ == '__main__':
    artists = loadData()
    print(f"There are {len(artists)} artists")

    createCheckfile(artists)
