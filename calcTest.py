import time
from subprocess import Popen
from pywinauto import Desktop
from pywinauto.keyboard import send_keys


Popen('calc.exe', shell=True)
window = Desktop(backend="uia").Calculator
window.wait('visible')
print("Калькулятор запущен.")


send_keys('%h'); send_keys('%1')
print("Переключение на режим Standard.")


window.child_window(title="Three", control_type="Button").click_input()
print("Выбрано число: 3")
window.child_window(title="Multiply by", control_type="Button").click_input()
print("Выбрана операция: умножение")
window.child_window(title="One", control_type="Button").click_input()
print("Выбрано число: 1")
window.child_window(title="Equals", control_type="Button").click_input()
print("Выполнена операция: 3 x 1")


send_keys('%h'); send_keys('%C')
window.child_window(title="Five", control_type="Button").click_input()
print("Число 5 добавлено в память.")


send_keys('%h'); send_keys('%2')  
time.sleep(1)
try:
    window.child_window(title="Four", control_type="Button").click_input()
    window.child_window(title="Eight", control_type="Button").click_input()
    window.child_window(title="Sin", control_type="Button").click_input()  
    print("Выполнен расчет синуса для числа 48.")
except Exception as e:
    print(f"Ошибка при попытке использовать синус: {e}")


send_keys('%h'); send_keys('%1')
window.child_window(title="One", control_type="Button").click_input()
window.child_window(title="Plus", control_type="Button").click_input()
window.child_window(title="One", control_type="Button").click_input()
window.child_window(title="Equals", control_type="Button").click_input()
print("Выполнено сложение: 1 + 1")


window.close()
print("Калькулятор закрыт.")
