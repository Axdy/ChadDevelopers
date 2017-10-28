# Creates a playlist for a user

import pprint
import sys
import os
import subprocess

import spotipy
import spotipy.util as util


username = "12102036088"
scope = "user-modify-playback-state"
client_secret="12b8b4d3362447d686c812b435ae6e71"
client_id="63535d7c99f64320a211e80190aec7c8"
redirect_uri = "http://localhost/"
token = util.prompt_for_user_token(username=username, scope=scope,
        client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)

if token:
    sp = spotipy.Spotify(auth=token)
    #sp.trace = False
    print sp.start_playback(device_id="1b08f32d97b4ae36dc6ea73629dc509ac16a114d")
    #sp.user_playlist_create(username, "playlist", "playlist-desc")
    #pprint.pprint(playlists)
else:
    print("Can't get token for", username)
