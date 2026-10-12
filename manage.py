from modules.app import app
from modules.window import main_window

if __name__ == "__main__":
    main_window.show()  # Менеджер даёт команду: "Покажи окно"
    app.exec()          # Менеджер запускает цикл PyQt6
