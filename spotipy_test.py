from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import json
import spotipy
import sys
import pprint

client_id = "9b6d1b481b6c4fbb8f6e4a08019b124a"
client_secret = "51fcbeb5347945d89be206713622124a"
username = 'andrewmaclellan225'
redirect_uri = 'http://localhost/'
scope = 'user-read-currently-playing'

#token = util.oauth2.SpotifyClientCredentials(client_id, client_secret)
token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
cache_token = token.get_access_token()
#client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(auth=token)
sp.trace=False

song_name = currentsong['item']['name']
song_artist = currentsong['item']['artists'][0]['name']
print("Now playing {} by {}".format(song_name, song_artist))
#dev = sp.devices()

#if len(sys.argv) > 1:
    #artist_name = ' '.join(sys.argv[1:])
    #results = sp.search(q=artist_name, limit=50)
    #tids = []
    #for i, t in enumerate(results['tracks']['items']):
        #print(' ', i, t['name'])
        #tids.append(t['uri'])
