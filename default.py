################################################################################
#      This file is part of OpenELEC - http://www.openelec.tv
#      Copyright (C) 2009-2012 Stephan Raue (stephan@openelec.tv)
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with OpenELEC.tv; see the file COPYING.  If not, write to
#  the Free Software Foundation, 51 Franklin Street, Suite 500, Boston, MA 02110, USA.
#  http://www.gnu.org/copyleft/gpl.html
################################################################################

import xbmc, xbmcaddon, time, os, subprocess

def ensure_dir(f):
  d = os.path.dirname(f)
  if not os.path.exists(d):
    os.makedirs(d)

__scriptname__ = "HTS TVheadend Service"
__author__ = "Innbox"
__url__ = "http://www.innbox.net"
__settings__   = xbmcaddon.Addon(id='service.multimedia.tvheadend')
__cwd__        = __settings__.getAddonInfo('path')
__start__      = xbmc.translatePath( os.path.join( __cwd__, 'bin', "tvheadend.start") )
__stop__       = xbmc.translatePath( os.path.join( __cwd__, 'bin', "tvheadend.stop") )
__home_dir__   = xbmc.translatePath( os.path.join('special://home/', 'userdata/addon_data/service.multimedia.innbox.tvheadend') )
__home__       = os.getenv("HOME")
__env__        = os.path.join( __home__, '.hts', 'tvheadend.env')

## ensure __env__ dir
ensure_dir(__env__)

## remove any old __env__ file
if os.path.isfile(__env__):
  os.remove(__env__)

## open __env__ file
env_file = open(__env__, "w+")

## write into enviroment variables into __env__
env_file.write("ADDON_DIR=\""+__cwd__+"\"\n")
env_file.write("ADDON_HOME=\""+__home_dir__+"\"\n")

## write xbmc's library path into env file
env_file.write("XBMC_LIBRARY_PATH=\"/data/data/org.xbmc.xbmc/lib/\"\n")

## close __env__ file
env_file.close()

#make binary files executable in adson bin folder
os.system("chmod 755 " + __cwd__ + "/bin/*")

os.system(__start__)

while (not xbmc.abortRequested):
  time.sleep(0.250)

os.system(__stop__)
