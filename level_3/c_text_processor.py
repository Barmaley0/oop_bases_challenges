"""
У нас есть класс TextProcessor, который содержит в себе методы для работы с текстом.

Задания:
    1. Создайте класс AdvancedTextProcessor, который будет наследником TextProcessor.
    2. Переопределите метод summarize у класса AdvancedTextProcessor таким образом, чтобы он возвращал еще и количество слов в тексте.
       Например: Total text length: 67, total number of words in the text: 10
    3. Создайте экземпляры каждого из двух классов и у каждого экземпляра вызовите все возможные методы.
"""


class TextProcessor:
    def __init__(self, text):
        self.text = text

    def to_upper(self):
        return self.text.upper()

    def summarize(self):
        return f'Total text length: {len(self.text)}'


class AdvancedTextProcessor(TextProcessor):
    def __init__(self, text):
        super().__init__(text)

    def summarize(self):
        return f"{super().summarize()} total number of words in text: {len(self.text.split())}"


if __name__ == '__main__':
    text_processor = TextProcessor(
        "Программист не стал заморачиваться и назвал детей новый сын1 и новый сын2."
    )

    advanced_text_processor = AdvancedTextProcessor(
        "Программист не стал заморачиваться и назвал детей новый сын1 и новый сын2."
    )

    print("TextProcessor methods:")
    print(f"Uppercase text: {text_processor.to_upper()}")
    print(f"Summarize text: {text_processor.summarize()}")
    print()

    print("AdvancedTextProcessor methods")
    print(f"Uppercase text: {advanced_text_processor.to_upper()}")
    print(f"Summarize text: {advanced_text_processor.summarize()}")
