#!usr/bin/env python3

from PyQt5 import QtWidgets, QtGui, QtCore

class BookToolBar(QtWidgets.QToolBar):
    def __init__(self, parent=None):
        super(BookToolBar, self).__init__(parent)

        # Spacer
        spacer = QtWidgets.QWidget()
        spacer.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        self.setMovable(False)
        self.setIconSize(QtCore.QSize(22, 22))
        self.setFloatable(False)
        self.setObjectName("LibraryToolBar")

        # Buttons
        self.fullscreenButton = QtWidgets.QAction(
            QtGui.QIcon.fromTheme('view-fullscreen'), 'Fullscreen', self)
        self.fontButton = QtWidgets.QAction(
            QtGui.QIcon.fromTheme('gtk-select-font'), 'Font settings', self)
        self.settingsButton = QtWidgets.QAction(
            QtGui.QIcon.fromTheme('settings'), 'Settings', self)

        # Add buttons
        self.addAction(self.fontButton)
        self.fontButton.setCheckable(True)
        self.fontButton.triggered.connect(self.toggle_font_settings)
        self.addSeparator()
        self.addAction(self.fullscreenButton)
        self.addAction(self.settingsButton)

        # Font modification
        font_sizes = [str(i) for i in range(8, 48, 2)]
        font_sizes.extend(['56', '64', '72'])
        self.fontSizeBox = QtWidgets.QComboBox(self)
        self.fontSizeBox.setObjectName('fontSizeBox')
        self.fontSizeBox.setToolTip('Font size')
        self.fontSizeBox.addItems(font_sizes)
        self.fontSizeBox.setEditable(True)

        self.paddingUp = QtWidgets.QAction(
            QtGui.QIcon.fromTheme('format-justify-fill'),
            'Increase padding', self)
        self.paddingUp.setObjectName('paddingUp')
        self.paddingDown = QtWidgets.QAction(
            QtGui.QIcon.fromTheme('format-indent-less'),
            'Decrease padding', self)
        self.paddingDown.setObjectName('paddingDown')

        self.lineSpacingUp = QtWidgets.QAction(
            QtGui.QIcon.fromTheme('format-line-spacing-triple'),
            'Increase line spacing', self)
        self.lineSpacingUp.setObjectName('lineSpacingUp')
        self.lineSpacingDown = QtWidgets.QAction(
            QtGui.QIcon.fromTheme('format-line-spacing-double'),
            'Decrease line spacing', self)
        self.lineSpacingDown.setObjectName('lineSpacingDown')

        self.fontBox = QtWidgets.QFontComboBox()
        self.fontBox.setFontFilters(QtWidgets.QFontComboBox.ScalableFonts)
        self.fontBox.setObjectName('fontBox')

        self.colorBoxFG = FixedPushButton(self)
        self.colorBoxFG.setObjectName('fgColor')
        self.colorBoxFG.setToolTip('Set foreground color')
        self.colorBoxBG = FixedPushButton(self)
        self.colorBoxBG.setToolTip('Set background color')
        self.colorBoxBG.setObjectName('bgColor')

        profiles = ['Profile 1', 'Profile 2', 'Profile 3']
        self.profileBox = QtWidgets.QComboBox(self)
        self.profileBox.addItems(profiles)

        self.profileAction = self.addWidget(self.profileBox)
        self.fontSeparator1 = self.addSeparator()
        self.fontBoxAction = self.addWidget(self.fontBox)
        self.fontSizeBoxAction = self.addWidget(self.fontSizeBox)
        self.fontSeparator2 = self.addSeparator()
        self.fgColorAction = self.addWidget(self.colorBoxFG)
        self.bgColorAction = self.addWidget(self.colorBoxBG)
        self.fontSeparator3 = self.addSeparator()
        self.addAction(self.lineSpacingUp)
        self.addAction(self.lineSpacingDown)
        self.fontSeparator4 = self.addSeparator()
        self.addAction(self.paddingUp)
        self.addAction(self.paddingDown)

        self.fontBoxAction.setVisible(False)
        self.fontSizeBoxAction.setVisible(False)
        self.fgColorAction.setVisible(False)
        self.bgColorAction.setVisible(False)
        self.lineSpacingUp.setVisible(False)
        self.lineSpacingDown.setVisible(False)
        self.paddingUp.setVisible(False)
        self.paddingDown.setVisible(False)
        self.profileAction.setVisible(False)
        self.fontSeparator1.setVisible(False)
        self.fontSeparator2.setVisible(False)
        self.fontSeparator3.setVisible(False)
        self.fontSeparator4.setVisible(False)

        self.searchBar = FixedLineEdit(self)
        self.searchBar.setPlaceholderText(
            'Search...')
        self.searchBar.setSizePolicy(sizePolicy)
        self.searchBar.setContentsMargins(10, 0, 0, 0)
        self.searchBar.setObjectName('searchBar')

        # Sorter
        self.tocBox = FixedComboBox(self)
        self.tocBox.setObjectName('sortingBox')
        self.tocBox.setToolTip('Table of Contents')

        # All of these will be put after the spacer
        # This means that the buttons in the left side of
        # the toolbar have to split up and added here
        self.boxSpacer = self.addWidget(spacer)

        self.tocBoxAction = self.addWidget(self.tocBox)
        self.searchBarAction = self.addWidget(self.searchBar)

    def toggle_font_settings(self):
        if self.fontButton.isChecked():
            self.font_settings_on()
        else:
            self.font_settings_off()

    def font_settings_on(self):
        self.fullscreenButton.setVisible(False)
        self.settingsButton.setVisible(False)

        self.fontBoxAction.setVisible(True)
        self.fontSizeBoxAction.setVisible(True)
        self.fgColorAction.setVisible(True)
        self.bgColorAction.setVisible(True)
        self.lineSpacingUp.setVisible(True)
        self.lineSpacingDown.setVisible(True)
        self.paddingUp.setVisible(True)
        self.paddingDown.setVisible(True)
        self.profileAction.setVisible(True)
        self.fontSeparator1.setVisible(True)
        self.fontSeparator2.setVisible(True)
        self.fontSeparator3.setVisible(True)
        self.fontSeparator3.setVisible(True)
        self.fontSeparator4.setVisible(False)

        self.tocBoxAction.setVisible(False)
        self.searchBarAction.setVisible(False)

    def font_settings_off(self):
        self.fullscreenButton.setVisible(True)
        self.settingsButton.setVisible(True)

        self.fontBoxAction.setVisible(False)
        self.fontSizeBoxAction.setVisible(False)
        self.fgColorAction.setVisible(False)
        self.bgColorAction.setVisible(False)
        self.lineSpacingUp.setVisible(False)
        self.lineSpacingDown.setVisible(False)
        self.paddingUp.setVisible(False)
        self.paddingDown.setVisible(False)
        self.profileAction.setVisible(False)
        self.fontSeparator1.setVisible(False)
        self.fontSeparator2.setVisible(False)
        self.fontSeparator3.setVisible(False)
        self.fontSeparator4.setVisible(False)

        self.tocBoxAction.setVisible(True)
        self.searchBarAction.setVisible(True)


class LibraryToolBar(QtWidgets.QToolBar):
    def __init__(self, parent=None):
        super(LibraryToolBar, self).__init__(parent)

        spacer = QtWidgets.QWidget()
        spacer.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.setMovable(False)
        self.setIconSize(QtCore.QSize(22, 22))
        self.setFloatable(False)
        self.setObjectName("LibraryToolBar")

        # Buttons
        self.addButton = QtWidgets.QAction(
            QtGui.QIcon.fromTheme('add'), 'Add book', self)
        self.deleteButton = QtWidgets.QAction(
            QtGui.QIcon.fromTheme('remove'), 'Delete book', self)
        self.settingsButton = QtWidgets.QAction(
            QtGui.QIcon.fromTheme('settings'), 'Settings', self)

        # Add buttons
        self.addAction(self.addButton)
        self.addAction(self.deleteButton)
        self.addSeparator()
        self.addAction(self.settingsButton)

        # Filter
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        # self.searchBar = QtWidgets.QLineEdit()
        self.searchBar = FixedLineEdit(self)
        self.searchBar.setPlaceholderText(
            'Search for Title, Author, Tags...')
        self.searchBar.setSizePolicy(sizePolicy)
        self.searchBar.setContentsMargins(10, 0, 0, 0)
        self.searchBar.setObjectName('searchBar')

        # Sorter
        sorting_choices = ['Title', 'Author', 'Year']
        self.sortingBox = FixedComboBox(self)
        self.sortingBox.addItems(sorting_choices)
        self.sortingBox.setObjectName('sortingBox')
        self.sortingBox.setSizePolicy(sizePolicy)
        self.sortingBox.setMinimumContentsLength(10)
        self.sortingBox.setToolTip('Sort by')

        # Add widgets
        self.addWidget(spacer)
        self.addWidget(self.sortingBox)
        self.addWidget(self.searchBar)


# Sublassing these widgets out prevents them from resizing
class FixedComboBox(QtWidgets.QComboBox):
    def __init__(self, parent=None):
        super(FixedComboBox, self).__init__(parent)

    def sizeHint(self):
        return QtCore.QSize(400, 22)


class FixedLineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super(FixedLineEdit, self).__init__(parent)

    def sizeHint(self):
        return QtCore.QSize(400, 22)


class FixedPushButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super(FixedPushButton, self).__init__(parent)

    def sizeHint(self):
        return QtCore.QSize(36, 30)


class Tab(QtWidgets.QWidget):
    def __init__(self, metadata, parent=None):
        # TODO
        # A horizontal slider to control flow
        # Keyboard shortcuts
        # Take hint from a position function argument to open the book
        # at a specific page

        # The content display widget is currently a QTextBrowser
        super(Tab, self).__init__(parent)
        self.parent = parent
        self.metadata = metadata  # Save progress data into this dictionary
        # self.setStyleSheet("background-color: black")

        title = self.metadata['title']
        path = self.metadata['path']

        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.contentView = QtWidgets.QTextBrowser(self)
        self.contentView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.contentView.setObjectName("contentView")
        self.contentView.verticalScrollBar().setSingleStep(7)
        self.contentView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.gridLayout.addWidget(self.contentView, 0, 0, 1, 1)
        self.parent.addTab(self, title)
        # self.contentView.setStyleSheet(
        #     "QTextEdit {font-size:20px; padding-left:100; padding-right:100; background-color:black}")


class LibraryDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, parent=None):
        super(LibraryDelegate, self).__init__(parent)

    def paint(self, painter, option, index):
        QtWidgets.QStyledItemDelegate.paint(self, painter, option, index)
        option = option.__class__(option)
        state = index.data(QtCore.Qt.UserRole + 5)
        if state:
            if state == 'deleted':
                read_icon = QtGui.QIcon.fromTheme('vcs-conflicting').pixmap(36)
            if state == 'completed':
                read_icon = QtGui.QIcon.fromTheme('vcs-normal').pixmap(36)
            if state == 'inprogress':
                read_icon = QtGui.QIcon.fromTheme('vcs-locally-modified').pixmap(36)
        else:
            return

        x_draw = option.rect.bottomRight().x() - 30
        y_draw = option.rect.bottomRight().y() - 35
        painter.drawPixmap(x_draw, y_draw, read_icon)
