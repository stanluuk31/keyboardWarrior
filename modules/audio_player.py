import vlc

player: vlc.MediaPlayer | None = None

def play_music(path):
    global player
    if player is not None:
        player.stop() # this code stop old music (if exist) before starting new one

    player = vlc.MediaPlayer(path)
    player.play()



def stop_music():
    global player
    if type(player) == vlc.MediaPlayer:
        player.stop()
