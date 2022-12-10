import pafy, os
from youtube_search import YoutubeSearch

def ytplay(name, *url):
    url = " ".join(url)
    try:
        v = pafy.new(url)
    except:
        videos = YoutubeSearch(url, max_results=1).to_dict()
        v = pafy.new(videos[0]['id'])
    a = v.getbestaudio().url
    os.system("ffplay -autoexit \"" + a + "\"")

def init(shell, *argv):
    shell.addcmd("ytplay", ytplay)