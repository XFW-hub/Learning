from IPython.display import HTML
from IPython.display import Video, Audio, display


def perform():
    return Video("ikun_vol2.mp4")


def singing(text):
     return display(Audio(rf'./lyrics/{text}.mp3'))


if __name__ == '__main__':
    pass
