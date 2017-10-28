# Creates a playlist for a user

import pprint
import sys
import os
import subprocess
import json

import spotipy
import spotipy.util as util

device_id = "9194bd6f8cb71719478a4eeeebefdc5336db6b5c"
username = "andrewmaclellan225"
scope = "user-modify-playback-state user-read-playback-state"
client_secret="51fcbeb5347945d89be206713622124a"
client_id="9b6d1b481b6c4fbb8f6e4a08019b124a"
redirect_uri = "http://localhost/"
token = util.prompt_for_user_token(username=username, scope=scope,
        client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)

happy_uri = "spotify:user:cgwest23:playlist:7asgcWtFGTbpZjl87J1OZJ"
sad_uri = "spotify:user:noraselnes:playlist:4RPP4RcIn51WPIRFhF0pQL"

if token:
    sp = spotipy.Spotify(auth=token)
    #print(sp.currently_playing())
    sp.shuffle(state=True, device_id=device_id)
    sp.start_playback(device_id=device_id, context_uri=sad_uri)
    #sp.trace = False
    #print sp.start_playback(device_id="1b08f32d97b4ae36dc6ea73629dc509ac16a114d")
    #sp.user_playlist_create(username, "playlist", "playlist-desc")
    #pprint.pprint(playlists)
else:
    print("Can't get token for", username)