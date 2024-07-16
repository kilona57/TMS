nums = [2, 3, 12, 5, 17, 29]

TARGET = 29


def search_two_nums_sum(nums_lst: list, target: int) -> float:
    number_dict = {}

    for i, numbers in enumerate(nums_lst):
        difference = target - numbers
        if difference in number_dict:
            return [number_dict[difference], i]
        number_dict[numbers] = i

    return []


print(search_two_nums_sum(nums, TARGET))
