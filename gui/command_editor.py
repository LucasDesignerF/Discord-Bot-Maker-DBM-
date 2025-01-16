from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel

class CommandEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("Editor de Comandos")
        self.layout.addWidget(self.label)

        self.command_input = QTextEdit()
        self.layout.addWidget(self.command_input)

        self.save_button = QPushButton("Salvar Comando")
        self.layout.addWidget(self.save_button)