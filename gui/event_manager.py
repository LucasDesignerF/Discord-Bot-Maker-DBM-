from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel

class EventManager(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("Gerenciador de Eventos")
        self.layout.addWidget(self.label)

        self.event_input = QTextEdit()
        self.layout.addWidget(self.event_input)

        self.save_button = QPushButton("Salvar Evento")
        self.layout.addWidget(self.save_button)