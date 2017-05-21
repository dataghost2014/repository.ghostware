# -*- coding: utf-8 -*-
#------------------------------------------------------------
# https://www.youtube.com/c/GhostwareSupport
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.GhostTube'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID = "UC0j1U3QzGciIodKLuFHr8jA"

# Entry point
def run():
    plugintools.log("fullycharged.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        pass
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("fullycharged.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="Ghostware Videos, Help & Support Section",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID+"/",
        thumbnail=icon,
        folder=True )

run()