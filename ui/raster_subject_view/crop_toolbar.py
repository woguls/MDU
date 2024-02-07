from PyQt6.QtWidgets import QToolBar, QVBoxLayout, QLineEdit, QPushButton
import qtawesome as qta

class CroptToolbar():

    def __init__(self,parent):
        self.commit_icon = qta.icon('mdi6.check-circle')
        self.cancel_icon = qta.icon('mdi.cancel')
        self.parent = parent

    def show(self):
        self.parent.toolbar.clear()

        width_edit = QLineEdit(self.parent)
        height_edit = QLineEdit(self.parent)

        self.parent.toolbar.addWidget(width_edit)
        self.parent.toolbar.addWidget(height_edit)   
