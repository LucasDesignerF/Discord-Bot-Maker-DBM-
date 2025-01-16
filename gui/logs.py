from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit

class LogPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.logs = QTextEdit()
        self.logs.setReadOnly(True)
        self.layout.addWidget(self.logs)