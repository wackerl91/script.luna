import os
import subprocess
import threading

import re
from xbmcswift2 import xbmc, xbmcaddon

from resources.lib.di.component import Component
from resources.lib.di.requiredfeature import RequiredFeature
from resources.lib.util.libgamestream import LibGameStream


def loop_lines(dialog, iterator):
    """
    :type dialog:   DialogProgress
    :type iterator: iterator
    """
    for line in iterator:
        dialog.update(0, line)

def pair_func(dialog, host):
    gs = LibGameStream()
    
    if gs.connect_server(host):
        if not gs.isPaired():
            gs.pair("1234")

class MoonlightHelper(Component):
    plugin = RequiredFeature('plugin')
    config_helper = RequiredFeature('config-helper')
    logger = RequiredFeature('logger')

    regex_connect = '(Connect to)'
    regex_moonlight = '(Moonlight Embedded)'

    def __init__(self):
        self.internal_path = xbmcaddon.Addon().getAddonInfo('path')

    def create_ctrl_map(self, dialog, map_file):
        """
        :type dialog:   DialogProgress
        :type map_file: str
        """
        mapping_proc = subprocess.Popen(
                ['stdbuf', '-oL', self.config_helper.get_binary(), 'map', map_file, '-input',
                 self.plugin.get_setting('input_device', unicode)], stdout=subprocess.PIPE)

        lines_iterator = iter(mapping_proc.stdout.readline, b"")

        mapping_thread = threading.Thread(target=loop_lines, args=(dialog, lines_iterator))
        mapping_thread.start()

        success = False

        # TODO: Make a method or function from this
        while True:
            xbmc.sleep(1000)
            if not mapping_thread.isAlive():
                dialog.close()
                success = True
                break
            if dialog.iscanceled():
                mapping_proc.kill()
                dialog.close()
                success = False
                break

        if os.path.isfile(map_file) and success:

            return True
        else:

            return False

    def pair_host(self, dialog):
        """
        :type dialog: DialogProgress
        """
        self.logger.info('[MoonlightHelper] - Attempting to pair host: ' + self.config_helper.get_host())
        
        pairing_thread = threading.Thread(target=pair_func, args=(dialog, self.config_helper.get_host()))
        pairing_thread.start()

        success = False

        while True:
            xbmc.sleep(1000)
            if not pairing_thread.isAlive():
                success = True
                break
            if dialog.iscanceled():
                dialog.close()
                success = False
                break
        
        if success:
            dialog.update(0, 'Checking if pairing has been successful.')
            xbmc.sleep(1000)
            
            gs = LibGameStream()
            gs.connect_server(self.config_helper.get_host())
            
            dialog.close()
            if gs.isPaired():
                return True
        else:
            return False

    def launch_game(self, game_id):
        """
        :type game_id: str
        """
        self.config_helper.configure()
        subprocess.call([
            self.internal_path + '/resources/lib/launchscripts/osmc/launch-helper-osmc.sh',
            self.internal_path + '/resources/lib/launchscripts/osmc/launch.sh',
            self.internal_path + '/resources/lib/launchscripts/osmc/moonlight-heartbeat.sh',
            game_id,
            self.config_helper.get_config_path()
        ])

    def list_games(self):
        gs = LibGameStream()
        
        if not gs.connect_server(self.config_helper.get_host()):
            return []
        
        if not gs.isPaired():
            return []
        
        game_list = []

        for id, name in gs.applist():
            game_list.append(name)
        
        return game_list
