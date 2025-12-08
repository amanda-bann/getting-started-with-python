class Song:
    def __init__(self, title, length):
        self.title = title
        self.length = length

    def track(self):
        print("The song " + self.title + " is " + self.length + " long.")

song1 = Song("A Soul With No King", "4:24")

print(song1.track())