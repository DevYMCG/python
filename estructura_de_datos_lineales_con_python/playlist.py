class MediaPlayer:
    
    def __init__(self):
        self.items = []
        self.size = 0

    # añadir canciones
    def add_track(self, track):
        self.items.insert(0,track)
        self.size += 1
    
    def delete_track(self):
        data = self.items.pop()
        self.size -=1
        return data

    # repoducir canción
    def play(self):
        total_items = self.size

        print(f'Coun: {total_items}')

        for item in range(total_items-1, -1, -1):
            print(f'Now playing {self.items[item]}')

if __name__ == "__main__": 
    track1 =MediaPlayer()
    track1.add_track('Highway to hell')
    track1.add_track('Go!')
    track1.add_track('Light years')
    track1.add_track('Heartbreaker')
    track1.add_track("Breath me")
    track1.add_track("How to dissappear completely")
    track1.play()
