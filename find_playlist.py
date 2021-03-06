# Creates a playlist for a user

import pprint
import sys
import os
import subprocess
import json

import spotipy
import spotipy.util as util

def find_emotion_playlist(emotion):

    #device_id = "9194bd6f8cb71719478a4eeeebefdc5336db6b5c"
    username = "andrewmaclellan225"
    scope = "user-modify-playback-state user-read-playback-state"
    client_secret=""
    client_id=""
    redirect_uri = "http://localhost/"
    token = util.prompt_for_user_token(username=username, scope=scope,
            client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
    playlists = {}
    playlists['HAPPY'] = "spotify:user:andrewmaclellan225:playlist:4c4vZDOGFrLtCXdUu5WdII"
    playlists['SAD'] = "spotify:user:andrewmaclellan225:playlist:3F2ciuEvu80QZXZxzOIjpa"
    playlists['CONFUSED'] = "spotify:user:andrewmaclellan225:playlist:6ZoCqo5SE6hBe7ctgoF7GI"
    playlists['ANGRY'] = "spotify:user:andrewmaclellan225:playlist:1tbvxwYl8UTCTEuBOUYpDH"
    playlists['DEFAULT'] = "spotify:user:andrewmaclellan225:playlist:7MC5mw9ZFEUCgufyyiNPjP"

    playlist_uri = playlists.get(emotion)

    if token:
        sp = spotipy.Spotify(auth=token)
        device_id = sp.devices().get('devices')[0].get('id')
        sp.shuffle(state=True, device_id=device_id)
        sp.start_playback(device_id=device_id, context_uri=playlist_uri)
        #sp.next_track(device_id=device_id)
    else:
        print("Can't get token for", username)
