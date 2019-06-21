class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        songs = set()
        next_song = self

        while next_song:
            if next_song in songs:
                return True
            else:
                songs.add(next_song)
                next_song = next_song or None

        return True


first = Song("Hello")
second = Song("Eye of the tiger")

first.next_song(second);
second.next_song(first);

print(first.is_repeating_playlist())
