import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QPushButton,
    QComboBox, QSpinBox, QMessageBox
)

class RestaurantApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ресторан: Заказ блюда")

        # Меню с блюдами и ценами
        self.menu = {
            "Пицца": 500,
            "Бургер": 300,
            "Паста": 450,
            "Салат": 250
            bfdsvhkbf
        }

        # Создание элементов интерфейса
        self.layout = QVBoxLayout()

        self.label = QLabel("Выберите блюдо:")
        self.layout.addWidget(self.label)

        self.combo = QComboBox()
        self.combo.addItems(self.menu.keys())
        self.layout.addWidget(self.combo)

        self.qty_label = QLabel("Количество:")
        self.layout.addWidget(self.qty_label)

        self.spin_box = QSpinBox()
        self.spin_box.setRange(1, 10)
        self.layout.addWidget(self.spin_box)

        self.order_button = QPushButton("Заказать")
        self.order_button.clicked.connect(self.process_order)
        self.layout.addWidget(self.order_button)

        self.setLayout(self.layout)

    def process_order(self):
        dish = self.combo.currentText()
        qty = self.spin_box.value()
        price = self.menu[dish] * qty
        QMessageBox.information(self, "Заказ оформлен",
                                f"Вы заказали {qty} x {dish}\nИтого: {price} руб.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = RestaurantApp()
    window.resize(300, 200)
    window.show()
    sys.exit(app.exec())
