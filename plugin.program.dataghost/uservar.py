import os, xbmc, xbmcaddon, base64

#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = 'Dataghosts Wizard'
EXCLUDES       = [ADDON_ID]
# Text File with build info in it.
exec("import re;import base64");exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("NygiNSBjOzUgNCIpOzcoKDIgMTEsMTA6KDIgMTMsYixmOmMuZSgxMyxiLGYpKSgxOCIoWzAtMTctZl0rKSIsMiAxNDoxMSgxNCwxMCksNC4zKCIxOT09IikpKSgyIGEsYjpiW2QoIjE1IithLjkoMSksMTYpXSwiMWF8M3w2fDR8OCIuMTIoInwiKSkp")))(lambda a,b:b[int("0x"+a.group(1),16)],"0|1|lambda|b64decode|base64|import|BUILDFILE|exec|ZGw9MQ|group|a|b|re|int|sub|f|y|p|split|o|m|0x|16|9a|r|MiAgICAgID0gMy4xICgnMC80PT0nKQ|aHR0cHM6Ly93d3cuZHJvcGJveC5jb20vcy9wcHR2M2d3cGhmMWFiNXQvYnVpbGRzMjAxNy50eHQ".split("|")))
# How often you would list it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with apk info in it.
exec("import re;import base64");exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("NigiNSBjOzUgMyIpOzYoKDIgMTAsMTU6KDIgMTEsYixmOmMuZCgxMSxiLGYpKSgxYSIoWzAtMTctZl0rKSIsMiAxMjoxMCgxMiwxNSksMy40KCIxOD0iKSkpKDIgYSxiOmJbZSgiMTMiK2EuOSgxKSwxNildLCIxOXw0fDd8M3w4Ii4xNCgifCIpKSk=")))(lambda a,b:b[int("0x"+a.group(1),16)],"0|1|lambda|base64|b64decode|import|exec|APKFILE|ZGw9MQ|group|a|b|re|sub|int|f|p|o|m|0x|split|y|16|9a|MiAgICAgICAgPSAzLjEoJzAvND09Jyk|aHR0cHM6Ly93d3cuZHJvcGJveC5jb20vcy90YXVic2xvaXBiaWh6OWwvYXBrMS50eHQ|r".split("|")))
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE   = 'Guides And Tutorials'
exec("import re;import base64");exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("NygiNSAxMzs1IDMiKTs3KCgxOCAxNSwxNDooMTggMTAsYixmOjEzLmMoMTAsYixmKSkoMTkiKFswLWUtZl0rKSIsMTggMTE6MTUoMTEsMTQpLDMuNCgiMj09IikpKSgxOCBhLGI6YltkKCIxMiIrYS44KDEpLDE2KV0sIjE3fDZ8NHwzIi45KCJ8IikpKQ==")))(lambda a,b:b[int("0x"+a.group(1),16)],"0|1|MSAgICA9IDMuMignMD0nKQ|base64|b64decode|import|YOUTUBEFILE|exec|group|split|a|b|sub|int|9a|f|o|m|0x|re|y|p|16|aHR0cHM6Ly93d3cuZHJvcGJveC5jb20vcy9uejJkazc5ejJxdmNodWkvaGVscDEudHh0P2RsPTE|lambda|r".split("|")))
# Text File for addon installer.  Leave as 'http://' to ignore
exec("import re;import base64");exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("NygiNSAxMzs1IDMiKTs3KCgxOCAxNSwxNDooMTggMTAsYixmOjEzLmMoMTAsYixmKSkoMTkiKFswLWUtZl0rKSIsMTggMTE6MTUoMTEsMTQpLDMuNCgiMj0iKSkpKDE4IGEsYjpiW2QoIjEyIithLjgoMSksMTYpXSwiMTd8NHw2fDMiLjkoInwiKSkp")))(lambda a,b:b[int("0x"+a.group(1),16)],"0|1|MiAgICAgID0gMy4xKCcwJyk|base64|b64decode|import|ADDONFILE|exec|group|split|a|b|sub|int|9a|f|o|m|0x|re|y|p|16|aHR0cHM6Ly93d3cuZHJvcGJveC5jb20vcy9yNHB1NnpuajNidHFmbnAvYWRkb24xLnR4dD9kbD0x|lambda|r".split("|")))
# Text File for advanced settings.  Leave as 'http://' to ignore
exec("import re;import base64");exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("NygiNSAxNDs1IDMiKTs3KCgxNyAxMCwxNTooMTcgMTEsYixmOjE0LmMoMTEsYixmKSkoMTkiKFswLWQtZl0rKSIsMTcgMTI6MTAoMTIsMTUpLDMuNCgiMj0iKSkpKDE3IGEsYjpiW2UoIjEzIithLjgoMSksMTYpXSwiMTh8Nnw0fDMiLjkoInwiKSkp")))(lambda a,b:b[int("0x"+a.group(1),16)],"0|1|MSAgID0gMy4yKCcwJyk|base64|b64decode|import|ADVANCEDFILE|exec|group|split|a|b|sub|9a|int|f|p|o|m|0x|re|y|16|lambda|aHR0cHM6Ly93d3cuZHJvcGJveC5jb20vcy9hMGIybGRveDZ6cTAyOW8vYWR2YW5jZWQxLnR4dD9kbD0x|r".split("|")))

# Dont need to edit just here for icons stored locally
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = 'http://'
ICONMAINT      = 'http://'
ICONAPK        = 'http://'
ICONADDONS     = 'http://'
ICONYOUTUBE    = 'http://'
ICONSAVE       = 'http://'
ICONTRAKT      = 'http://'
ICONREAL       = 'http://'
ICONLOGIN      = 'http://'
ICONCONTACT    = 'http://'
ICONSETTINGS   = 'http://'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '='

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'dodgerblue'
COLOR2         = 'white'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+'][B][I]([COLOR '+COLOR2+']Dataghost[/COLOR])[/B][/COLOR] [COLOR '+COLOR2+']%s[/COLOR][/I]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR1+']Current Build:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR1+']Current Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = 'Thank you for choosing Dataghosts wizard'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = 'http://'
CONTACTFANART  = 'http://'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'No'
# Url to wizard version
WIZARDFILE     = ''
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'No'
# Addon ID for the repository
REPOID         = ''
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = ''
# Url to folder zip is located in
REPOZIPURL     = ''
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'Yes'
# Url to notification file
exec("import re;import base64");exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("NygiNiAxNDs2IDMiKTs3KCgxNyAxMCwxNTooMTcgMTEsYixmOjE0LmMoMTEsYixmKSkoMTkiKFswLWQtZl0rKSIsMTcgMTI6MTAoMTIsMTUpLDMuNCgiMj0iKSkpKDE3IGEsYjpiW2UoIjEzIithLjgoMSksMTYpXSwiMTh8NXw0fDMiLjkoInwiKSkp")))(lambda a,b:b[int("0x"+a.group(1),16)],"0|1|MSAgID0gMy4yKCcwJyk|base64|b64decode|NOTIFICATION|import|exec|group|split|a|b|sub|9a|int|f|p|o|m|0x|re|y|16|lambda|aHR0cHM6Ly93d3cuZHJvcGJveC5jb20vcy9kaGk1c3k5ZmwycW5ucnovbWVzc2FnZXMxLnR4dD9kbD0x|r".split("|")))
# Use either 'Text' or 'Image'
HEADERTYPE     = ''
HEADERMESSAGE  = ''
# url to image if using Image 424x180
HEADERIMAGE    = ''
# Background for Notification Window
BACKGROUND     = ''
#########################################################
