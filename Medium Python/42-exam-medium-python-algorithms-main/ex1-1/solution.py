# old version
# def sort_list_of_lists(lst: list[list[int]]) -> list[list[int]]:
#     return [sorted(x) for x in lst]

# def sort_list_of_lists(lst: list[list[int]]) -> list[list[int]]:
#     sorted_list = []
#     for inner in lst:              # take each inner list
#         sorted_list.append(sorted(inner))   # sort it, add to sorted_list
#     return sorted_list

# def sort_list_of_lists(lst: list[list[int]]) -> list[list[int]]:
#     for inner in lst:              # take each inner list
#         inner = inner.sort()
#     return lst

def sort_list_of_lists(lst: list[list[int]]) -> list[list[int]]:
    for list in lst:
        list = list.sort()
    return lst


print(sort_list_of_lists([[3, 1, 2], [6, 5, 4], [9, 8, 7]]))