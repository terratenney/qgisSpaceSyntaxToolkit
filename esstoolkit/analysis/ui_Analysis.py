# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_Analysis.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_AnalysisDialog(object):
    def setupUi(self, AnalysisDialog):
        AnalysisDialog.setObjectName(_fromUtf8("AnalysisDialog"))
        AnalysisDialog.resize(390, 550)
        AnalysisDialog.setMinimumSize(QtCore.QSize(390, 550))
        AnalysisDialog.setToolTip(_fromUtf8(""))
        self.analysisLayout = QtGui.QWidget()
        self.analysisLayout.setObjectName(_fromUtf8("analysisLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.analysisLayout)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.analysisDataLayout = QtGui.QHBoxLayout()
        self.analysisDataLayout.setObjectName(_fromUtf8("analysisDataLayout"))
        self.analysisDataLabel = QtGui.QLabel(self.analysisLayout)
        self.analysisDataLabel.setObjectName(_fromUtf8("analysisDataLabel"))
        self.analysisDataLayout.addWidget(self.analysisDataLabel)
        self.analysisDataEdit = QtGui.QLineEdit(self.analysisLayout)
        self.analysisDataEdit.setAcceptDrops(False)
        self.analysisDataEdit.setFrame(False)
        self.analysisDataEdit.setReadOnly(True)
        self.analysisDataEdit.setObjectName(_fromUtf8("analysisDataEdit"))
        self.analysisDataLayout.addWidget(self.analysisDataEdit)
        self.analysisDataButton = QtGui.QPushButton(self.analysisLayout)
        self.analysisDataButton.setObjectName(_fromUtf8("analysisDataButton"))
        self.analysisDataLayout.addWidget(self.analysisDataButton)
        self.verticalLayout_2.addLayout(self.analysisDataLayout)
        self.analysisLayersTabs = QtGui.QTabWidget(self.analysisLayout)
        self.analysisLayersTabs.setEnabled(True)
        self.analysisLayersTabs.setObjectName(_fromUtf8("analysisLayersTabs"))
        self.analysisMapTab = QtGui.QWidget()
        self.analysisMapTab.setObjectName(_fromUtf8("analysisMapTab"))
        self.gridLayout = QtGui.QGridLayout(self.analysisMapTab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.analysisMapLabel = QtGui.QLabel(self.analysisMapTab)
        self.analysisMapLabel.setObjectName(_fromUtf8("analysisMapLabel"))
        self.gridLayout.addWidget(self.analysisMapLabel, 0, 0, 1, 1)
        self.analysisMapCombo = QtGui.QComboBox(self.analysisMapTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.analysisMapCombo.sizePolicy().hasHeightForWidth())
        self.analysisMapCombo.setSizePolicy(sizePolicy)
        self.analysisMapCombo.setObjectName(_fromUtf8("analysisMapCombo"))
        self.gridLayout.addWidget(self.analysisMapCombo, 0, 1, 1, 1)
        self.analysisMapSegmentCheck = QtGui.QCheckBox(self.analysisMapTab)
        self.analysisMapSegmentCheck.setObjectName(_fromUtf8("analysisMapSegmentCheck"))
        self.gridLayout.addWidget(self.analysisMapSegmentCheck, 1, 0, 1, 2)
        self.gridLayout.setColumnStretch(1, 1)
        self.analysisLayersTabs.addTab(self.analysisMapTab, _fromUtf8(""))
        self.analysisUnlinksTab = QtGui.QWidget()
        self.analysisUnlinksTab.setObjectName(_fromUtf8("analysisUnlinksTab"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.analysisUnlinksTab)
        self.horizontalLayout_4.setContentsMargins(12, -1, 12, 12)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.analysisUnlinksLabel = QtGui.QLabel(self.analysisUnlinksTab)
        self.analysisUnlinksLabel.setObjectName(_fromUtf8("analysisUnlinksLabel"))
        self.horizontalLayout_4.addWidget(self.analysisUnlinksLabel)
        self.analysisUnlinksCombo = QtGui.QComboBox(self.analysisUnlinksTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.analysisUnlinksCombo.sizePolicy().hasHeightForWidth())
        self.analysisUnlinksCombo.setSizePolicy(sizePolicy)
        self.analysisUnlinksCombo.setObjectName(_fromUtf8("analysisUnlinksCombo"))
        self.horizontalLayout_4.addWidget(self.analysisUnlinksCombo)
        self.horizontalLayout_4.setStretch(1, 3)
        self.analysisLayersTabs.addTab(self.analysisUnlinksTab, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.analysisLayersTabs)
        self.axialAnalysisTabs = QtGui.QTabWidget(self.analysisLayout)
        self.axialAnalysisTabs.setObjectName(_fromUtf8("axialAnalysisTabs"))
        self.axialEditTab = QtGui.QWidget()
        self.axialEditTab.setObjectName(_fromUtf8("axialEditTab"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.axialEditTab)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.axialEditLayout = QtGui.QGridLayout()
        self.axialEditLayout.setObjectName(_fromUtf8("axialEditLayout"))
        self.axialVerifyButton = QtGui.QPushButton(self.axialEditTab)
        self.axialVerifyButton.setDefault(False)
        self.axialVerifyButton.setObjectName(_fromUtf8("axialVerifyButton"))
        self.axialEditLayout.addWidget(self.axialVerifyButton, 0, 0, 1, 1)
        self.axialVerifyProgressBar = QtGui.QProgressBar(self.axialEditTab)
        self.axialVerifyProgressBar.setProperty("value", 24)
        self.axialVerifyProgressBar.setObjectName(_fromUtf8("axialVerifyProgressBar"))
        self.axialEditLayout.addWidget(self.axialVerifyProgressBar, 0, 1, 1, 1)
        self.axialVerifyCancelButton = QtGui.QPushButton(self.axialEditTab)
        self.axialVerifyCancelButton.setObjectName(_fromUtf8("axialVerifyCancelButton"))
        self.axialEditLayout.addWidget(self.axialVerifyCancelButton, 0, 2, 1, 1)
        self.axialUpdateButton = QtGui.QPushButton(self.axialEditTab)
        self.axialUpdateButton.setObjectName(_fromUtf8("axialUpdateButton"))
        self.axialEditLayout.addWidget(self.axialUpdateButton, 1, 0, 1, 1)
        self.axialReportFilterCombo = QtGui.QComboBox(self.axialEditTab)
        self.axialReportFilterCombo.setObjectName(_fromUtf8("axialReportFilterCombo"))
        self.axialEditLayout.addWidget(self.axialReportFilterCombo, 1, 1, 1, 1)
        self.axialVerifySettingsButton = QtGui.QPushButton(self.axialEditTab)
        self.axialVerifySettingsButton.setObjectName(_fromUtf8("axialVerifySettingsButton"))
        self.axialEditLayout.addWidget(self.axialVerifySettingsButton, 1, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.axialEditLayout)
        self.axialReportList = QtGui.QTableWidget(self.axialEditTab)
        self.axialReportList.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.axialReportList.setProperty("showDropIndicator", False)
        self.axialReportList.setDragDropOverwriteMode(False)
        self.axialReportList.setAlternatingRowColors(False)
        self.axialReportList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.axialReportList.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.axialReportList.setShowGrid(False)
        self.axialReportList.setWordWrap(False)
        self.axialReportList.setColumnCount(2)
        self.axialReportList.setObjectName(_fromUtf8("axialReportList"))
        self.axialReportList.setRowCount(0)
        self.axialReportList.horizontalHeader().setStretchLastSection(True)
        self.axialReportList.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.axialReportList)
        self.axialAnalysisTabs.addTab(self.axialEditTab, _fromUtf8(""))
        self.axialDepthmapTab = QtGui.QWidget()
        self.axialDepthmapTab.setObjectName(_fromUtf8("axialDepthmapTab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.axialDepthmapTab)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 10)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.axialDepthmapAnalysisLayout = QtGui.QHBoxLayout()
        self.axialDepthmapAnalysisLayout.setObjectName(_fromUtf8("axialDepthmapAnalysisLayout"))
        self.axialDepthmapAxialRadio = QtGui.QRadioButton(self.axialDepthmapTab)
        self.axialDepthmapAxialRadio.setChecked(True)
        self.axialDepthmapAxialRadio.setObjectName(_fromUtf8("axialDepthmapAxialRadio"))
        self.axialDepthmapAnalysisLayout.addWidget(self.axialDepthmapAxialRadio)
        self.axialDepthmapSegmentRadio = QtGui.QRadioButton(self.axialDepthmapTab)
        self.axialDepthmapSegmentRadio.setObjectName(_fromUtf8("axialDepthmapSegmentRadio"))
        self.axialDepthmapAnalysisLayout.addWidget(self.axialDepthmapSegmentRadio)
        self.axialDepthmapSettingsButton = QtGui.QPushButton(self.axialDepthmapTab)
        self.axialDepthmapSettingsButton.setObjectName(_fromUtf8("axialDepthmapSettingsButton"))
        self.axialDepthmapAnalysisLayout.addWidget(self.axialDepthmapSettingsButton)
        self.verticalLayout.addLayout(self.axialDepthmapAnalysisLayout)
        self.axialDepthmapSettingsLayout = QtGui.QGridLayout()
        self.axialDepthmapSettingsLayout.setObjectName(_fromUtf8("axialDepthmapSettingsLayout"))
        self.axialDepthmapRadiusLabel = QtGui.QLabel(self.axialDepthmapTab)
        self.axialDepthmapRadiusLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.axialDepthmapRadiusLabel.setObjectName(_fromUtf8("axialDepthmapRadiusLabel"))
        self.axialDepthmapSettingsLayout.addWidget(self.axialDepthmapRadiusLabel, 0, 0, 1, 1)
        self.axialDepthmapRadiusText = QtGui.QLineEdit(self.axialDepthmapTab)
        self.axialDepthmapRadiusText.setObjectName(_fromUtf8("axialDepthmapRadiusText"))
        self.axialDepthmapSettingsLayout.addWidget(self.axialDepthmapRadiusText, 0, 1, 1, 1)
        self.axialDepthmapWeightCheck = QtGui.QCheckBox(self.axialDepthmapTab)
        self.axialDepthmapWeightCheck.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.axialDepthmapWeightCheck.setObjectName(_fromUtf8("axialDepthmapWeightCheck"))
        self.axialDepthmapSettingsLayout.addWidget(self.axialDepthmapWeightCheck, 1, 0, 1, 1)
        self.axialDepthmapWeightCombo = QtGui.QComboBox(self.axialDepthmapTab)
        self.axialDepthmapWeightCombo.setObjectName(_fromUtf8("axialDepthmapWeightCombo"))
        self.axialDepthmapSettingsLayout.addWidget(self.axialDepthmapWeightCombo, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.axialDepthmapSettingsLayout)
        self.axialDepthmapOuputLayout = QtGui.QGridLayout()
        self.axialDepthmapOuputLayout.setObjectName(_fromUtf8("axialDepthmapOuputLayout"))
        self.axialDepthmapOutputLabel = QtGui.QLabel(self.axialDepthmapTab)
        self.axialDepthmapOutputLabel.setObjectName(_fromUtf8("axialDepthmapOutputLabel"))
        self.axialDepthmapOuputLayout.addWidget(self.axialDepthmapOutputLabel, 0, 0, 1, 1)
        self.axialDepthmapOutputText = QtGui.QLineEdit(self.axialDepthmapTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axialDepthmapOutputText.sizePolicy().hasHeightForWidth())
        self.axialDepthmapOutputText.setSizePolicy(sizePolicy)
        self.axialDepthmapOutputText.setObjectName(_fromUtf8("axialDepthmapOutputText"))
        self.axialDepthmapOuputLayout.addWidget(self.axialDepthmapOutputText, 0, 1, 1, 2)
        self.axialDepthmapCalculateButton = QtGui.QPushButton(self.axialDepthmapTab)
        self.axialDepthmapCalculateButton.setObjectName(_fromUtf8("axialDepthmapCalculateButton"))
        self.axialDepthmapOuputLayout.addWidget(self.axialDepthmapCalculateButton, 1, 0, 1, 1)
        self.axialDepthmapProgressBar = QtGui.QProgressBar(self.axialDepthmapTab)
        self.axialDepthmapProgressBar.setProperty("value", 24)
        self.axialDepthmapProgressBar.setObjectName(_fromUtf8("axialDepthmapProgressBar"))
        self.axialDepthmapOuputLayout.addWidget(self.axialDepthmapProgressBar, 1, 1, 1, 1)
        self.axialDepthmapCancelButton = QtGui.QPushButton(self.axialDepthmapTab)
        self.axialDepthmapCancelButton.setObjectName(_fromUtf8("axialDepthmapCancelButton"))
        self.axialDepthmapOuputLayout.addWidget(self.axialDepthmapCancelButton, 1, 2, 1, 1)
        self.axialDepthmapOuputLayout.setColumnMinimumWidth(1, 1)
        self.axialDepthmapOuputLayout.setColumnStretch(1, 1)
        self.verticalLayout.addLayout(self.axialDepthmapOuputLayout)
        self.axialDepthmapReportList = QtGui.QPlainTextEdit(self.axialDepthmapTab)
        self.axialDepthmapReportList.setObjectName(_fromUtf8("axialDepthmapReportList"))
        self.verticalLayout.addWidget(self.axialDepthmapReportList)
        self.axialDepthmapDownload = QtGui.QLabel(self.axialDepthmapTab)
        self.axialDepthmapDownload.setAlignment(QtCore.Qt.AlignCenter)
        self.axialDepthmapDownload.setOpenExternalLinks(True)
        self.axialDepthmapDownload.setObjectName(_fromUtf8("axialDepthmapDownload"))
        self.verticalLayout.addWidget(self.axialDepthmapDownload)
        self.verticalLayout.setStretch(3, 1)
        self.axialAnalysisTabs.addTab(self.axialDepthmapTab, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.axialAnalysisTabs)
        self.verticalLayout_2.setStretch(2, 5)
        AnalysisDialog.setWidget(self.analysisLayout)

        self.retranslateUi(AnalysisDialog)
        self.analysisLayersTabs.setCurrentIndex(0)
        self.axialAnalysisTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AnalysisDialog)

    def retranslateUi(self, AnalysisDialog):
        AnalysisDialog.setWindowTitle(_translate("AnalysisDialog", "Graph Analysis", None))
        self.analysisDataLabel.setText(_translate("AnalysisDialog", "Data store", None))
        self.analysisDataEdit.setText(_translate("AnalysisDialog", "specify for storing analysis results", None))
        self.analysisDataEdit.setPlaceholderText(_translate("AnalysisDialog", "specify for storing analysis results", None))
        self.analysisDataButton.setText(_translate("AnalysisDialog", "...", None))
        self.analysisMapLabel.setText(_translate("AnalysisDialog", "Layer", None))
        self.analysisMapSegmentCheck.setText(_translate("AnalysisDialog", "Segment map or road centre line", None))
        self.analysisLayersTabs.setTabText(self.analysisLayersTabs.indexOf(self.analysisMapTab), _translate("AnalysisDialog", "Map", None))
        self.analysisUnlinksLabel.setText(_translate("AnalysisDialog", "Layer", None))
        self.analysisLayersTabs.setTabText(self.analysisLayersTabs.indexOf(self.analysisUnlinksTab), _translate("AnalysisDialog", "Unlinks", None))
        self.axialVerifyButton.setText(_translate("AnalysisDialog", "Verify", None))
        self.axialVerifyCancelButton.setText(_translate("AnalysisDialog", "Cancel", None))
        self.axialUpdateButton.setText(_translate("AnalysisDialog", "Update IDs", None))
        self.axialVerifySettingsButton.setText(_translate("AnalysisDialog", "Settings", None))
        self.axialReportList.setSortingEnabled(True)
        self.axialAnalysisTabs.setTabText(self.axialAnalysisTabs.indexOf(self.axialEditTab), _translate("AnalysisDialog", "Verify layer", None))
        self.axialDepthmapAxialRadio.setText(_translate("AnalysisDialog", "Axial", None))
        self.axialDepthmapSegmentRadio.setText(_translate("AnalysisDialog", "Segment", None))
        self.axialDepthmapSettingsButton.setText(_translate("AnalysisDialog", "Settings", None))
        self.axialDepthmapRadiusLabel.setText(_translate("AnalysisDialog", "Radius:", None))
        self.axialDepthmapRadiusText.setText(_translate("AnalysisDialog", "2,4,n", None))
        self.axialDepthmapWeightCheck.setText(_translate("AnalysisDialog", "Weight:", None))
        self.axialDepthmapOutputLabel.setText(_translate("AnalysisDialog", "Output table:", None))
        self.axialDepthmapCalculateButton.setText(_translate("AnalysisDialog", "Calculate", None))
        self.axialDepthmapCancelButton.setText(_translate("AnalysisDialog", "Cancel", None))
        self.axialDepthmapDownload.setToolTip(_translate("AnalysisDialog", "https://varoudis.github.io/depthmapX/", None))
        self.axialDepthmapDownload.setText(_translate("AnalysisDialog", "<qt><a href=\"http://archtech.gr/varoudis/depthmapX/?dir=depthmapXnet\"><span style=\" text-decoration: underline; color:#0000ff;\">Download depthmapXnet...</a></qt>", None))
        self.axialAnalysisTabs.setTabText(self.axialAnalysisTabs.indexOf(self.axialDepthmapTab), _translate("AnalysisDialog", "depthmapX remote", None))

import resources_rc
