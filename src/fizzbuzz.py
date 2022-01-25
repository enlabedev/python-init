class fizzbuzz:
    def __init__(self) -> None:
        self.nums: list = []

    def multiple(self, min_number: int, max_number: int, multiple_list: dict) -> list:
        for number in range(min_number, max_number + 1):
            text_to_validate = ""
            for key, multiple in multiple_list.items():
                if number % key == 0:
                    text_to_validate += multiple
            if text_to_validate == "":
                text_to_validate = number
            self.nums.append(text_to_validate)
        return self.nums
