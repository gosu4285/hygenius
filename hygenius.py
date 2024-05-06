import os
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QDialog,
    QVBoxLayout,
    QTextBrowser,
)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

from element_info import element_info


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class ElementDialog(QDialog):
    def __init__(self, element_info, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"{element_info['number']}. {element_info['name']} Information")
        self.setWindowFlags(self.windowFlags() ^ Qt.WindowContextHelpButtonHint)
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        # label = QLabel(element_info['description'])
        # label = QLabel()
        # label.setWordWrap(True)
        # layout.addWidget(label)

        browser = QTextBrowser()
        browser.setOpenExternalLinks(True)
        browser.append(element_info['description'])
        for url_link in element_info['link_url']:
            browser.append(f"<a href={url_link}>{url_link}</a>")
        layout.addWidget(browser)

        '''
        button = QPushButton("설명창 닫기")
        button.clicked.connect(self.accept)
        layout.addWidget(button)
        '''

        self.setLayout(layout)

    def position_dialog(self, parent, click_pos):
        parent_rect = parent.geometry()
        dialog_rect = self.geometry()

        x = parent_rect.x() + click_pos.x()
        y = parent_rect.y() + click_pos.y()

        screen_geometry = QApplication.desktop().availableGeometry()
        x = min(x, screen_geometry.width() - dialog_rect.width())
        y = min(y, screen_geometry.height() - dialog_rect.height())

        self.move(x, y)


class PeriodicTable(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('하이지니어스 원소주기율표 설명 프로그램')
        self.setGeometry(100, 100, 1814, 905)

        icon = QIcon(resource_path('hynix_icon.ico'))
        self.setWindowIcon(icon)

        label = QLabel(self)
        pixmap = QPixmap(resource_path('periodic_table.jpg'))
        label.setPixmap(pixmap)

        self.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            pos = event.pos()
            for element, data in element_info.items():
                print(f'element: {element}')
                if data["rect"].contains(pos):
                    dialog = ElementDialog(element_info[element], self)
                    dialog.position_dialog(self, pos)
                    dialog.exec_()
                    break


if __name__ == '__main__':
    app = QApplication(sys.argv)
    periodic_table = PeriodicTable()
    sys.exit(app.exec_())
