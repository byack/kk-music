# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'music_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_kk_music(object):
    def setupUi(self, kk_music):
        kk_music.setObjectName("kk_music")
        kk_music.resize(1200, 650)
        kk_music.setMinimumSize(QtCore.QSize(1200, 650))
        kk_music.setMaximumSize(QtCore.QSize(1200, 650))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ico/kk-music.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        kk_music.setWindowIcon(icon)
        kk_music.setToolTip("")
        self.line = QtWidgets.QFrame(kk_music)
        self.line.setGeometry(QtCore.QRect(250, 0, 20, 651))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayoutWidget = QtWidgets.QWidget(kk_music)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(280, 70, 641, 511))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.grid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.grid.setObjectName("grid")
        self.title1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.title1.setMaximumSize(QtCore.QSize(140, 60))
        self.title1.setStyleSheet("color: rgb(42, 201, 123);")
        self.title1.setText("")
        self.title1.setFlat(True)
        self.title1.setObjectName("title1")
        self.grid.addWidget(self.title1, 1, 1, 1, 1)
        self.title5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.title5.setMaximumSize(QtCore.QSize(140, 60))
        self.title5.setStyleSheet("color: rgb(42, 201, 123);")
        self.title5.setText("")
        self.title5.setFlat(True)
        self.title5.setObjectName("title5")
        self.grid.addWidget(self.title5, 3, 1, 1, 1)
        self.img7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.img7.setMaximumSize(QtCore.QSize(140, 140))
        self.img7.setText("")
        self.img7.setScaledContents(True)
        self.img7.setObjectName("img7")
        self.grid.addWidget(self.img7, 2, 3, 1, 1)
        self.img4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.img4.setMaximumSize(QtCore.QSize(140, 140))
        self.img4.setText("")
        self.img4.setScaledContents(True)
        self.img4.setObjectName("img4")
        self.grid.addWidget(self.img4, 2, 0, 1, 1)
        self.img1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.img1.setMaximumSize(QtCore.QSize(140, 140))
        self.img1.setText("")
        self.img1.setScaledContents(True)
        self.img1.setObjectName("img1")
        self.grid.addWidget(self.img1, 0, 1, 1, 1)
        self.title6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.title6.setMaximumSize(QtCore.QSize(140, 60))
        self.title6.setStyleSheet("color: rgb(42, 201, 123);")
        self.title6.setText("")
        self.title6.setFlat(True)
        self.title6.setObjectName("title6")
        self.grid.addWidget(self.title6, 3, 2, 1, 1)
        self.img2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.img2.setMaximumSize(QtCore.QSize(140, 140))
        self.img2.setText("")
        self.img2.setScaledContents(True)
        self.img2.setObjectName("img2")
        self.grid.addWidget(self.img2, 0, 2, 1, 1)
        self.img0 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.img0.setMaximumSize(QtCore.QSize(140, 140))
        self.img0.setText("")
        self.img0.setScaledContents(True)
        self.img0.setObjectName("img0")
        self.grid.addWidget(self.img0, 0, 0, 1, 1)
        self.title0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.title0.setMaximumSize(QtCore.QSize(140, 60))
        self.title0.setStyleSheet("color: rgb(42, 201, 123);")
        self.title0.setText("")
        self.title0.setFlat(True)
        self.title0.setObjectName("title0")
        self.grid.addWidget(self.title0, 1, 0, 1, 1)
        self.img5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.img5.setMaximumSize(QtCore.QSize(140, 140))
        self.img5.setText("")
        self.img5.setScaledContents(True)
        self.img5.setObjectName("img5")
        self.grid.addWidget(self.img5, 2, 1, 1, 1)
        self.title4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.title4.setMaximumSize(QtCore.QSize(140, 60))
        self.title4.setStyleSheet("color: rgb(42, 201, 123);")
        self.title4.setText("")
        self.title4.setFlat(True)
        self.title4.setObjectName("title4")
        self.grid.addWidget(self.title4, 3, 0, 1, 1)
        self.img3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.img3.setMaximumSize(QtCore.QSize(140, 140))
        self.img3.setText("")
        self.img3.setScaledContents(True)
        self.img3.setObjectName("img3")
        self.grid.addWidget(self.img3, 0, 3, 1, 1)
        self.title2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.title2.setMaximumSize(QtCore.QSize(140, 60))
        self.title2.setStyleSheet("color: rgb(42, 201, 123);")
        self.title2.setText("")
        self.title2.setFlat(True)
        self.title2.setObjectName("title2")
        self.grid.addWidget(self.title2, 1, 2, 1, 1)
        self.title7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.title7.setMaximumSize(QtCore.QSize(140, 60))
        self.title7.setStyleSheet("color: rgb(42, 201, 123);")
        self.title7.setText("")
        self.title7.setFlat(True)
        self.title7.setObjectName("title7")
        self.grid.addWidget(self.title7, 3, 3, 1, 1)
        self.title3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.title3.setMaximumSize(QtCore.QSize(140, 60))
        self.title3.setStyleSheet("color: rgb(42, 201, 123);")
        self.title3.setText("")
        self.title3.setFlat(True)
        self.title3.setObjectName("title3")
        self.grid.addWidget(self.title3, 1, 3, 1, 1)
        self.img6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.img6.setMaximumSize(QtCore.QSize(140, 140))
        self.img6.setText("")
        self.img6.setScaledContents(True)
        self.img6.setObjectName("img6")
        self.grid.addWidget(self.img6, 2, 2, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(kk_music)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(280, 590, 641, 51))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.gridLayoutWidget_2)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.time_ico = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.time_ico.setText("")
        self.time_ico.setPixmap(QtGui.QPixmap("ico/music.png"))
        self.time_ico.setObjectName("time_ico")
        self.horizontalLayout_3.addWidget(self.time_ico)
        self.time_pre = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.time_pre.setObjectName("time_pre")
        self.horizontalLayout_3.addWidget(self.time_pre)
        self.time_line = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.time_line.setMinimumSize(QtCore.QSize(380, 0))
        self.time_line.setMaximumSize(QtCore.QSize(380, 16777215))
        self.time_line.setPageStep(0)
        self.time_line.setOrientation(QtCore.Qt.Horizontal)
        self.time_line.setObjectName("time_line")
        self.horizontalLayout_3.addWidget(self.time_line)
        self.time_next = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.time_next.setObjectName("time_next")
        self.horizontalLayout_3.addWidget(self.time_next)
        self.volume = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.volume.setText("")
        self.volume.setPixmap(QtGui.QPixmap("ico/center_volume.png"))
        self.volume.setObjectName("volume")
        self.horizontalLayout_3.addWidget(self.volume)
        self.volume_line = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.volume_line.setPageStep(0)
        self.volume_line.setProperty("value", 50)
        self.volume_line.setOrientation(QtCore.Qt.Horizontal)
        self.volume_line.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.volume_line.setTickInterval(0)
        self.volume_line.setObjectName("volume_line")
        self.horizontalLayout_3.addWidget(self.volume_line)
        self.downloads = QtWidgets.QPushButton(kk_music)
        self.downloads.setGeometry(QtCore.QRect(1030, 590, 48, 48))
        self.downloads.setMinimumSize(QtCore.QSize(48, 48))
        self.downloads.setMaximumSize(QtCore.QSize(48, 48))
        self.downloads.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ico/downloads.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.downloads.setIcon(icon1)
        self.downloads.setIconSize(QtCore.QSize(48, 48))
        self.downloads.setFlat(True)
        self.downloads.setObjectName("downloads")
        self.localhost = QtWidgets.QPushButton(kk_music)
        self.localhost.setGeometry(QtCore.QRect(1090, 590, 48, 48))
        self.localhost.setMinimumSize(QtCore.QSize(48, 48))
        self.localhost.setMaximumSize(QtCore.QSize(48, 48))
        self.localhost.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ico/open_folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.localhost.setIcon(icon2)
        self.localhost.setIconSize(QtCore.QSize(48, 48))
        self.localhost.setFlat(True)
        self.localhost.setObjectName("localhost")
        self.logo = QtWidgets.QLabel(kk_music)
        self.logo.setGeometry(QtCore.QRect(0, 10, 250, 100))
        self.logo.setMinimumSize(QtCore.QSize(250, 100))
        self.logo.setMaximumSize(QtCore.QSize(250, 100))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("ico/logo.png"))
        self.logo.setObjectName("logo")
        self.myplaylist = QtWidgets.QLabel(kk_music)
        self.myplaylist.setGeometry(QtCore.QRect(0, 110, 81, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.myplaylist.setFont(font)
        self.myplaylist.setObjectName("myplaylist")
        self.new_playlist = QtWidgets.QPushButton(kk_music)
        self.new_playlist.setGeometry(QtCore.QRect(90, 120, 24, 24))
        self.new_playlist.setMinimumSize(QtCore.QSize(24, 24))
        self.new_playlist.setMaximumSize(QtCore.QSize(24, 24))
        self.new_playlist.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ico/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_playlist.setIcon(icon3)
        self.new_playlist.setIconSize(QtCore.QSize(24, 24))
        self.new_playlist.setFlat(True)
        self.new_playlist.setObjectName("new_playlist")
        self.delete_playlist = QtWidgets.QPushButton(kk_music)
        self.delete_playlist.setGeometry(QtCore.QRect(120, 120, 24, 24))
        self.delete_playlist.setMinimumSize(QtCore.QSize(24, 24))
        self.delete_playlist.setMaximumSize(QtCore.QSize(24, 24))
        self.delete_playlist.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ico/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_playlist.setIcon(icon4)
        self.delete_playlist.setIconSize(QtCore.QSize(24, 24))
        self.delete_playlist.setFlat(True)
        self.delete_playlist.setObjectName("delete_playlist")
        self.add_to_playlist = QtWidgets.QPushButton(kk_music)
        self.add_to_playlist.setGeometry(QtCore.QRect(970, 590, 48, 48))
        self.add_to_playlist.setMinimumSize(QtCore.QSize(48, 48))
        self.add_to_playlist.setMaximumSize(QtCore.QSize(48, 48))
        self.add_to_playlist.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("ico/add_to_list.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_to_playlist.setIcon(icon5)
        self.add_to_playlist.setIconSize(QtCore.QSize(48, 48))
        self.add_to_playlist.setFlat(True)
        self.add_to_playlist.setObjectName("add_to_playlist")
        self.layoutWidget = QtWidgets.QWidget(kk_music)
        self.layoutWidget.setGeometry(QtCore.QRect(280, 0, 581, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(15)
        font.setItalic(True)
        self.search.setFont(font)
        self.search.setObjectName("search")
        self.horizontalLayout.addWidget(self.search)
        self.search_edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.search_edit.setBaseSize(QtCore.QSize(0, 0))
        self.search_edit.setInputMask("")
        self.search_edit.setText("")
        self.search_edit.setObjectName("search_edit")
        self.horizontalLayout.addWidget(self.search_edit)
        self.src_choose = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.src_choose.setFont(font)
        self.src_choose.setObjectName("src_choose")
        self.src_choose.addItem("")
        self.src_choose.addItem("")
        self.horizontalLayout.addWidget(self.src_choose)
        self.listview = QtWidgets.QListWidget(kk_music)
        self.listview.setGeometry(QtCore.QRect(930, 30, 270, 550))
        self.listview.setMinimumSize(QtCore.QSize(270, 550))
        self.listview.setMaximumSize(QtCore.QSize(270, 550))
        self.listview.setObjectName("listview")
        self.listview_lable = QtWidgets.QLabel(kk_music)
        self.listview_lable.setGeometry(QtCore.QRect(930, 10, 81, 21))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(15)
        self.listview_lable.setFont(font)
        self.listview_lable.setObjectName("listview_lable")
        self.myplaylist_list = QtWidgets.QListWidget(kk_music)
        self.myplaylist_list.setGeometry(QtCore.QRect(0, 150, 260, 401))
        self.myplaylist_list.setObjectName("myplaylist_list")
        self.disc_title = QtWidgets.QLabel(kk_music)
        self.disc_title.setGeometry(QtCore.QRect(4, 628, 251, 20))
        self.disc_title.setMinimumSize(QtCore.QSize(251, 20))
        self.disc_title.setMaximumSize(QtCore.QSize(251, 20))
        self.disc_title.setText("")
        self.disc_title.setObjectName("disc_title")
        self.disc = QtWidgets.QLabel(kk_music)
        self.disc.setEnabled(True)
        self.disc.setGeometry(QtCore.QRect(0, 560, 64, 64))
        self.disc.setMinimumSize(QtCore.QSize(64, 64))
        self.disc.setMaximumSize(QtCore.QSize(64, 64))
        self.disc.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.disc.setText("")
        self.disc.setPixmap(QtGui.QPixmap("ico/disc.png"))
        self.disc.setObjectName("disc")
        self.music_pre = QtWidgets.QPushButton(kk_music)
        self.music_pre.setGeometry(QtCore.QRect(80, 570, 48, 48))
        self.music_pre.setMinimumSize(QtCore.QSize(48, 48))
        self.music_pre.setMaximumSize(QtCore.QSize(48, 48))
        self.music_pre.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("ico/on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.music_pre.setIcon(icon6)
        self.music_pre.setIconSize(QtCore.QSize(48, 48))
        self.music_pre.setFlat(True)
        self.music_pre.setObjectName("music_pre")
        self.music_start_stop = QtWidgets.QPushButton(kk_music)
        self.music_start_stop.setGeometry(QtCore.QRect(140, 570, 48, 48))
        self.music_start_stop.setMinimumSize(QtCore.QSize(48, 48))
        self.music_start_stop.setMaximumSize(QtCore.QSize(48, 48))
        self.music_start_stop.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("ico/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.music_start_stop.setIcon(icon7)
        self.music_start_stop.setIconSize(QtCore.QSize(48, 48))
        self.music_start_stop.setFlat(True)
        self.music_start_stop.setObjectName("music_start_stop")
        self.music_next = QtWidgets.QPushButton(kk_music)
        self.music_next.setGeometry(QtCore.QRect(200, 570, 48, 48))
        self.music_next.setMinimumSize(QtCore.QSize(48, 48))
        self.music_next.setMaximumSize(QtCore.QSize(48, 48))
        self.music_next.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("ico/de.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.music_next.setIcon(icon8)
        self.music_next.setIconSize(QtCore.QSize(48, 48))
        self.music_next.setFlat(True)
        self.music_next.setObjectName("music_next")
        self.message_label = QtWidgets.QLabel(kk_music)
        self.message_label.setGeometry(QtCore.QRect(1020, 9, 171, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.message_label.setFont(font)
        self.message_label.setStyleSheet("color:rgb(255, 0, 0)")
        self.message_label.setText("")
        self.message_label.setObjectName("message_label")
        self.song_modle = QtWidgets.QPushButton(kk_music)
        self.song_modle.setGeometry(QtCore.QRect(930, 600, 30, 30))
        self.song_modle.setMinimumSize(QtCore.QSize(30, 30))
        self.song_modle.setMaximumSize(QtCore.QSize(30, 30))
        self.song_modle.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("ico/cycle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.song_modle.setIcon(icon9)
        self.song_modle.setIconSize(QtCore.QSize(30, 30))
        self.song_modle.setFlat(True)
        self.song_modle.setObjectName("song_modle")

        self.retranslateUi(kk_music)
        QtCore.QMetaObject.connectSlotsByName(kk_music)

    def retranslateUi(self, kk_music):
        _translate = QtCore.QCoreApplication.translate
        kk_music.setWindowTitle(_translate("kk_music", "KK-Music"))
        self.title1.setToolTip(_translate("kk_music", "单击"))
        self.title5.setToolTip(_translate("kk_music", "单击"))
        self.img7.setToolTip(_translate("kk_music", "点击下方标题"))
        self.img4.setToolTip(_translate("kk_music", "点击下方标题"))
        self.img1.setToolTip(_translate("kk_music", "点击下方标题"))
        self.title6.setToolTip(_translate("kk_music", "单击"))
        self.img2.setToolTip(_translate("kk_music", "点击下方标题"))
        self.img0.setToolTip(_translate("kk_music", "点击下方标题"))
        self.title0.setToolTip(_translate("kk_music", "单击"))
        self.img5.setToolTip(_translate("kk_music", "点击下方标题"))
        self.title4.setToolTip(_translate("kk_music", "单击"))
        self.img3.setToolTip(_translate("kk_music", "点击下方标题"))
        self.title2.setToolTip(_translate("kk_music", "单击"))
        self.title7.setToolTip(_translate("kk_music", "单击"))
        self.title3.setToolTip(_translate("kk_music", "单击"))
        self.img6.setToolTip(_translate("kk_music", "点击下方标题"))
        self.time_pre.setText(_translate("kk_music", "00:00"))
        self.time_next.setText(_translate("kk_music", "00:00"))
        self.downloads.setToolTip(_translate("kk_music", "下载当前播放歌曲"))
        self.localhost.setToolTip(_translate("kk_music", "导入本地音乐"))
        self.myplaylist.setText(_translate("kk_music", "我的歌单"))
        self.new_playlist.setToolTip(_translate("kk_music", "添加歌单"))
        self.delete_playlist.setToolTip(_translate("kk_music", "删除歌单"))
        self.add_to_playlist.setToolTip(_translate("kk_music", "将当前歌曲添加到歌单中"))
        self.search.setToolTip(_translate("kk_music", "在搜索框中搜索"))
        self.search.setText(_translate("kk_music", "搜索"))
        self.search_edit.setPlaceholderText(_translate("kk_music", "搜索单曲、歌单、歌手"))
        self.src_choose.setToolTip(_translate("kk_music", "选择音乐源"))
        self.src_choose.setItemText(0, _translate("kk_music", "网易云"))
        self.src_choose.setItemText(1, _translate("kk_music", "QQ音乐"))
        self.listview_lable.setText(_translate("kk_music", "歌单列表"))
        self.music_pre.setToolTip(_translate("kk_music", "上一首"))
        self.music_start_stop.setToolTip(_translate("kk_music", "播放/暂停"))
        self.music_next.setToolTip(_translate("kk_music", "下一首"))
        self.song_modle.setToolTip(_translate("kk_music", "列表循环"))
