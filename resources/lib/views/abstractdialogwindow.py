import os

import pyxbmct.addonwindow as pyxbmct

from resources.lib.di.requiredfeature import RequiredFeature


class AbstractDialogWindow(pyxbmct.AddonDialogWindow):
    COLOR_FO = '0xFFE0B074'
    COLOR_NF = '0xFF808080'
    COLOR_HEADING = '0xFFD6D6D6'
    COLOR_DETAILS = '0xFF707070'
    COLOR_SELECTED = '0xFFF1F1F1'

    plugin = RequiredFeature('plugin')
    core = RequiredFeature('core')

    def __init__(self, title=''):
        super(AbstractDialogWindow, self).__init__(title)
        background = None
        if self.core.get_active_skin() == 'skin.osmc':
            media_path = '/usr/share/kodi/addons/skin.osmc/media'
            if os.path.exists(media_path):
                background = os.path.join(media_path, 'dialogs/DialogBackground_old.png')

        if background is not None:
            self.background.setImage(background)
            self.removeControl(self.title_background)
            self.removeControl(self.window_close_button)
            self.removeControl(self.title_bar)

        self.setGeometry(1280, 720, 12, 6, padding=60)
        self.connect(pyxbmct.ACTION_NAV_BACK, self.close)

    def setAnimation(self, control):
        control.setAnimations(
                [
                    ('WindowOpen', 'effect=fade start=0 end=100 time=500',),
                    ('WindowClose', 'effect=fade start=100 end=0 time=500',)
                ]
        )
