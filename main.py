"""Это модуль для демонстрации работы класса ListAnalyzer."""

from list_analyzer import ListAnalyzer

def main():
    """Точка входа в программу."""
    analyzer = ListAnalyzer([1, 2, 3, 4, 5], [6, 7, 8, 9])
    result = analyzer.compare_means()
    print(result)

if __name__ == "__main__":
    main()
