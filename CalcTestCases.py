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

def perform_operation(buttons):
    for button in buttons:
        window.child_window(title=button, control_type="Button").click_input()
    window.child_window(title="Equals", control_type="Button").click_input()
    result = window.child_window(auto_id="CalculatorResults", control_type="Text").window_text()
    print(f"Результат: {result}")
    window.child_window(title="Clear", control_type="Button").click_input()

print("Выполнение операции сложения: 1 + 1")
perform_operation(['One', 'Plus', 'One'])

print("Выполнение операции вычитания: 3 - 1")
perform_operation(['Three', 'Minus', 'One'])

print("Выполнение операции умножения: 2 * 2")
perform_operation(['Two', 'Multiply by', 'Two'])

print("Выполнение операции деления: 4 / 2")
perform_operation(['Four', 'Divide by', 'Two'])


print("Выполнение операции извлечения квадратного корня из 9")
window.child_window(title="Nine", control_type="Button").click_input()
window.child_window(title="Square root", control_type="Button").click_input()
window.child_window(title="Equals", control_type="Button").click_input()
sqrt_result = window.child_window(auto_id="CalculatorResults", control_type="Text").window_text()
print(f"Результат квадратного корня: {sqrt_result}")
window.child_window(title="Clear", control_type="Button").click_input()


print("Вычисление процентов: 50% от 100")
window.child_window(title="One", control_type="Button").click_input()
window.child_window(title="Zero", control_type="Button").click_input()
window.child_window(title="Zero", control_type="Button").click_input()
window.child_window(title="Percent", control_type="Button").click_input()
percent_result = window.child_window(auto_id="CalculatorResults", control_type="Text").window_text()
print(f"Результат вычисления процентов: {percent_result}")
window.child_window(title="Clear", control_type="Button").click_input()




print("Проверка цифровых кнопок")
button_titles = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
for i, title in enumerate(button_titles):
    window.child_window(title=title, control_type="Button").click_input()
    result = window.child_window(auto_id="CalculatorResults", control_type="Text").window_text()
    print(f"Кнопка {i}: {result}")
    window.child_window(title="Clear", control_type="Button").click_input()



send_keys('%h'); send_keys('%2')
print("Переключение на режим Scientific.")


def perform_scientific_operation(operation_buttons, expected_result):
    for button in operation_buttons:
        window.child_window(title=button, control_type="Button").click_input()
    window.child_window(title="Equals", control_type="Button").click_input()
    result = window.child_window(auto_id="CalculatorResults", control_type="Text").window_text()
    assert expected_result in result, f"Результат не совпадает: ожидаемый {expected_result}, полученный {result}"
    window.child_window(title="Clear", control_type="Button").click_input()


perform_scientific_operation(["Sin", "One"], "Display is 0.8414709848078965")  # sin(1)
perform_scientific_operation(["Cosine", "One"], "Display is 0.5403023058681398")  # cos(1)
perform_scientific_operation(["Tangent", "One"], "Display is 1.5574077246549023")  # tan(1)


perform_scientific_operation(["Log", "One", "Zero"], "Display is 1")  # log(10)
perform_scientific_operation(["Ln", "E"], "Display is 1")  # ln(e)


perform_scientific_operation(["E", "caret", "Two"], "Display is 7.3890560989306495")  # e^2


perform_scientific_operation(["Five", "n!"], "Display is 120")  # 5!


perform_scientific_operation(["Pi"], "Display is 3.141592653589793")  # π





window.close()
print("Калькулятор закрыт.")
