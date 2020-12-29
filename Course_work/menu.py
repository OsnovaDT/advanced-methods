import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

# Импорт дизайна приложения
from menu_ui import Ui_menu_window
# Импорт окон с методами Эйлера и Рунге-Кутта
from euler import main as euler_main
from runge_kutt import main as runge_kutt_main


# Задание стиля элементам окна
STYLESHEET = """
*{
    background:#FFF;
    font-family: "Webdings";
    border-radius: 10px;
}

#euler_btn{
    border: 2px solid;
}

#runge_kutt_btn{
    border: 2px solid;
}
"""


class MenuWindow(QMainWindow, Ui_menu_window):
    """Класс меню для выбора метода вычисления дифура"""

    def __init__(self):
        """Конструктор класса MenuWindow"""

        # Обращение к классу QMainWindow для дополнения текщего класса
        super().__init__()

        # Подключение дизайна
        self.setupUi(self)

        # Установка стиля у элементов окна
        self.setStyleSheet(STYLESHEET)

        # Задание методов для работы кнопок.
        # По нажатию на кнопки, открываются соответствующие окна.
        self.euler_btn.clicked.connect(lambda: euler_main())
        self.runge_kutt_btn.clicked.connect(lambda: runge_kutt_main())


def main():
    """Основная функция

    Создание приложения и его окна.
    Ожидание выхода из приложения.

    """

    # Создание приложения
    application = QApplication(sys.argv)

    # Создание и отображение окна приложения
    menu_window = MenuWindow()
    menu_window.show()

    # Обработка событий приложения, после оконачния которой,
    # происходит прекращение работы всей программы
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
