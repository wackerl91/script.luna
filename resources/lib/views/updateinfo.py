import pyxbmct.addonwindow as pyxbmct

from resources.lib.views.abstractdialogwindow import AbstractDialogWindow


class UpdateInfo(AbstractDialogWindow):
    def __init__(self, update, title=''):
        super(UpdateInfo, self).__init__(title)
        self.update = update

        self.set_info_controls(update)
        self.set_active_controls()
        self.set_navigation()
        # init controls
        self.version = None
        self.changelog = None
        self.button_update = None
        self.button_cancel = None

    def set_info_controls(self, update):
        update_headline = 'Luna %s available' % update.update_version
        title_label = pyxbmct.Label(update_headline, alignment=pyxbmct.ALIGN_LEFT, font='XLarge',
                                    textColor=self.COLOR_HEADING)
        self.placeControl(title_label, 0, 0, 2, 3)

        changelog_label = pyxbmct.Label('Changelog', alignment=pyxbmct.ALIGN_LEFT, font='Med',
                                        textColor=self.COLOR_DETAILS)
        self.placeControl(changelog_label, 2, 0)

        self.changelog = pyxbmct.TextBox(font='Med')
        self.placeControl(self.changelog, 4, 0, 6, 6)
        self.changelog.setText(update.changelog)
        self.changelog.autoScroll(delay=5000, time=2000, repeat=10000)

    def set_active_controls(self):
        self.button_update = pyxbmct.Button('Update', focusTexture='', noFocusTexture='', focusedColor=self.COLOR_FO,
                                            textColor=self.COLOR_NF, font='Med', alignment=pyxbmct.ALIGN_LEFT)
        self.placeControl(self.button_update, 11, 0)
        self.connect(self.button_update, self.do_update)

        self.button_cancel = pyxbmct.Button('Cancel', focusTexture='', noFocusTexture='',
                                            focusedColor=self.COLOR_FO, textColor=self.COLOR_NF, font='Med',
                                            alignment=pyxbmct.ALIGN_LEFT)
        self.placeControl(self.button_cancel, 11, 1, columnspan=2)
        self.connect(self.button_cancel, self.cancel)

    def set_navigation(self):
        self.button_update.controlRight(self.button_cancel)
        self.button_update.controlLeft(self.button_cancel)
        self.button_cancel.controlRight(self.button_update)
        self.button_cancel.controlLeft(self.button_update)

        self.setFocus(self.button_update)

    def do_update(self):
        self.update.do_update()
        self.close()

    def cancel(self):
        self.close()
