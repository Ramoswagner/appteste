import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QLineEdit, QListWidget,
    QListWidgetItem
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lista de Tarefas — Teste Nuitka")
        self.setMinimumSize(420, 500)
        self._build()

    def _build(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(16)

        title = QLabel("📝 Minhas Tarefas")
        title.setFont(QFont("Segoe UI", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        row = QHBoxLayout()
        self._input = QLineEdit()
        self._input.setPlaceholderText("Nova tarefa...")
        self._input.setFixedHeight(36)
        self._input.returnPressed.connect(self._add)
        row.addWidget(self._input)

        add_btn = QPushButton("Adicionar")
        add_btn.setFixedHeight(36)
        add_btn.clicked.connect(self._add)
        row.addWidget(add_btn)
        layout.addLayout(row)

        self._list = QListWidget()
        self._list.setAlternatingRowColors(True)
        layout.addWidget(self._list)

        del_btn = QPushButton("🗑  Remover Selecionada")
        del_btn.setFixedHeight(36)
        del_btn.clicked.connect(self._remove)
        layout.addWidget(del_btn)

        self._status = QLabel("Nenhuma tarefa ainda.")
        self._status.setAlignment(Qt.AlignCenter)
        self._status.setStyleSheet("color: gray; font-size: 12px;")
        layout.addWidget(self._status)

    def _add(self):
        text = self._input.text().strip()
        if not text:
            return
        item = QListWidgetItem(f"  {text}")
        item.setCheckState(Qt.Unchecked)
        self._list.addItem(item)
        self._input.clear()
        self._update_status()

    def _remove(self):
        row = self._list.currentRow()
        if row >= 0:
            self._list.takeItem(row)
        self._update_status()

    def _update_status(self):
        total = self._list.count()
        self._status.setText(
            f"{total} tarefa{'s' if total != 1 else ''}" if total else "Nenhuma tarefa ainda."
        )


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    w = MainWindow()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
