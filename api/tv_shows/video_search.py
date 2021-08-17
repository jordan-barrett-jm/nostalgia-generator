from youtubesearchpython import VideosSearch

def getVideoLink(query):
    search = VideosSearch(query, limit=1).result()
    if search['result']:
        return search['result'][0]['link']