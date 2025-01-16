from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QTabWidget, QTextEdit, QPushButton, QLineEdit, QLabel, QMessageBox
)
from gui.command_editor import CommandEditor
from gui.event_manager import EventManager
from gui.logs import LogPanel
from core.bot_manager import BotManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Discord Bot Maker")
        self.setGeometry(100, 100, 1200, 800)

        # Layout principal
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Abas
        self.tabs = QTabWidget()
        self.layout.addWidget(self.tabs)

        # Dashboard
        self.dashboard = QWidget()
        self.dashboard_layout = QVBoxLayout()
        self.dashboard.setLayout(self.dashboard_layout)

        # Token Input
        self.token_label = QLabel("Token do Bot:")
        self.dashboard_layout.addWidget(self.token_label)
        self.token_input = QLineEdit()
        self.dashboard_layout.addWidget(self.token_input)

        # Start/Stop Buttons
        self.start_button = QPushButton("Iniciar Bot")
        self.start_button.clicked.connect(self.start_bot)
        self.dashboard_layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Parar Bot")
        self.stop_button.clicked.connect(self.stop_bot)
        self.stop_button.setEnabled(False)
        self.dashboard_layout.addWidget(self.stop_button)

        # Adicionar abas
        self.tabs.addTab(self.dashboard, "Dashboard")
        self.tabs.addTab(CommandEditor(), "Editor de Comandos")
        self.tabs.addTab(EventManager(), "Gerenciador de Eventos")
        self.tabs.addTab(LogPanel(), "Logs")

        # Bot Manager
        self.bot_manager = None

    def start_bot(self):
        token = self.token_input.text().strip()
        if not token:
            QMessageBox.warning(self, "Erro", "Insira um token válido!")
            return

        self.bot_manager = BotManager(token)
        try:
            self.bot_manager.start_bot()
            self.start_button.setEnabled(False)
            self.stop_button.setEnabled(True)
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Falha ao iniciar o bot: {e}")

    def stop_bot(self):
        if self.bot_manager:
            self.bot_manager.stop_bot()
            self.start_button.setEnabled(True)
            self.stop_button.setEnabled(False)