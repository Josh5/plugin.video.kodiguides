#!/usr/bin/env python
#
##########################################################################
#                                                                        #
#                        ** YouTube URL Lister **                        #
#                                                                        #
#   Written by:		Josh.5 (jsunnex@gmail.com)                       #
#   Date:		12 July, 2015                                    #
#                                                                        #
#   Credits:                                                             #
#          - bromix (https://github.com/bromix/)                         #
#          - sphere (https://github.com/dersphere/)                      #
#                                                                        #
#   License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)              #
#                                                                        #
##########################################################################

import xbmc, xbmcaddon, xbmcgui, xbmcplugin

## Plugin Info ##
ID               = 'plugin.video.kodiguides'
ADDON            = xbmcaddon.Addon( ID )
ADDON_ID         = ADDON.getAddonInfo('id')
ADDON_NAME       = ADDON.getAddonInfo('name')
ADDON_ICON       = ADDON.getAddonInfo('icon')
ADDON_VERSION    = ADDON.getAddonInfo('version')
ADDON_DATA       = xbmc.translatePath( "special://profile/addon_data/%s/" % ID )
ADDON_DIR        = ADDON.getAddonInfo( "path" )
ICON_DIR         = ADDON.getAddonInfo( "path" )+'/icons/'
ADDON_SETTINGS   = xbmc.translatePath( "special://profile/addon_data/%s/" % ID )


def getSetting(setting):
    return xbmcaddon.Addon(id = ID).getSetting(setting)


playlists = []

if getSetting('XBMCONNECT_TVADD') == 'true':
  pl_dict = {
    'name' : 'XBMCONNECT - TvAddons.Ag >>>',
    'icon' : ADDON_ICON,
    'playlist_id' : 'PLy1Uif0Sq_gD_6Wtje3uWjSggT_vI-8bB',
  }
  playlists.append(pl_dict)

if getSetting('XBMCONNECT_XUN') == 'true':
  pl_dict = {
    'name' : 'XBMCONNECT - Xunitytalk >>>',
    'icon' : ADDON_ICON,
    'playlist_id' : 'PLy1Uif0Sq_gBYWTdQgKHY-l6Hk8fLkdY1',
  }
  playlists.append(pl_dict)

if getSetting('XBMCONNECT_LIVE') == 'true':
  pl_dict = {
    'name' : 'XBMCONNECT - Live Tv  >>>',
    'icon' : ADDON_ICON,
    'playlist_id' : 'PLy1Uif0Sq_gDKDnhXXM-2VqDJYZ7j076y',
  }
  playlists.append(pl_dict)

if getSetting('XBMCONNECT_TT') == 'true':
  pl_dict = {
    'name' : 'XBMCONNECT - Tips & Tricks  >>>',
    'icon' : ADDON_ICON,
    'playlist_id' : 'PLy1Uif0Sq_gD7oKxBsAuOsjYLDE_S19Yl',
  }
  playlists.append(pl_dict)

if getSetting('XBMCONNECT_AEON') == 'true':
  pl_dict = {
    'name' : 'XBMCONNECT - Aeon Nox   >>>',
    'icon' : ADDON_ICON,
    'playlist_id' : 'PLy1Uif0Sq_gDzbRfl-CWKQmfIy6WrFf5g',
  }
  playlists.append(pl_dict)

if getSetting('XBMCONNECT_TX') == 'true':
  pl_dict = {
    'name' : 'XBMCONNECT - TotalXbmc.Tv   >>>',
    'icon' : ADDON_ICON,
    'playlist_id' : 'PLy1Uif0Sq_gAaecR41heejdlZQyPxIvK8',
  }
  playlists.append(pl_dict)

if getSetting('XBMCONNECT_SKIN') == 'true':
  pl_dict = {
    'name' : 'XBMCONNECT - Customize Your Skin   >>>',
    'icon' : ADDON_ICON,
    'playlist_id' : 'PLy1Uif0Sq_gABhXDpuiUwL0S-bhqwZrJ7',
  }
  playlists.append(pl_dict)

if getSetting('XBMCONNECT_MUS') == 'true':
  pl_dict = {
    'name' : 'XBMCONNECT - Music Addons   >>>',
    'icon' : ADDON_ICON,
    'playlist_id' : 'PLy1Uif0Sq_gDL_lOnTtkdQ-UP4VsalOh6',
  }
  playlists.append(pl_dict)

if getSetting('HASHAM_KODI') == 'true':
  pl_dict = {
    'name' : 'Husham Memar  - Kodi   >>>',
    'icon' : ADDON_ICON,
    'playlist_id' : 'PLSt21BXKwMKLgstMkE_xBriNFf_SnzMz-',
  }
  playlists.append(pl_dict)

if getSetting('KABORATECH_KODI') == 'true':
  pl_dict = {
    'name' : 'KABORATECH - XBMC KODI   >>>',
    'icon' : ADDON_ICON,
    'playlist_id' : 'PLZp1gtnD7l8yTZgFiVFVQtFpfG0GeLU9d',
  }
  playlists.append(pl_dict)

if getSetting('SUPACHARGEDIOS_TUT') == 'true':
  pl_dict = {
    'name' : 'SUPACHARGEDIOS - Kodi Tutorial Videos   >>>',
    'icon' : ADDON_ICON,
    'playlist_id' : 'PL5g1KMPtodzvWON5OLSk-eWoHklRHzTwg',
  }
  playlists.append(pl_dict)

playlists.sort()

for p in playlists:
  playback_url = 'plugin://plugin.video.youtube/playlist/'+p['playlist_id']+'/'
  item = xbmcgui.ListItem(p['name'], iconImage=p['icon'], path=playback_url)
  xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=playback_url, listitem=item, isFolder=True)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
