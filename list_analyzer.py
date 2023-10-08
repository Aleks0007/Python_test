"""Модуль для анализа и сравнения средних значений двух списков."""

class ListAnalyzer:
    """Класс для анализа и сравнения средних значений двух списков."""

    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def calculate_mean(self, lst):
        """Вычисляет среднее значение списка."""
        return sum(lst) / len(lst) if lst else 0

    def compare_means(self):
        """Сравнивает средние значения двух списков и возвращает результат сравнения."""
        mean1 = self.calculate_mean(self.list1)
        mean2 = self.calculate_mean(self.list2)

        if mean1 > mean2:
            return "Первый список имеет большее среднее значение"
        if mean1 < mean2:
            return "Второй список имеет большее среднее значение"
        return "Средние значения равны"
 