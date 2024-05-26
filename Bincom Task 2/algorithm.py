#create a sort algorithm, implement binary search.

def sort_names(names):
    return sorted(names)


name_list = ["Lawal", "Taiwo", "Mubin","Wakil","Fareed","Hussein"]

def binary_search(name_list, target):
    left, right = 0, len(name_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if name_list[mid] == target:
            return mid
        elif name_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


sorted_names = sort_names(name_list)
print("Sorted Names are:", sorted_names)

search_name = "Hussein"
index = binary_search(sorted_names, search_name)
if index != -1:
    print(f"{search_name} found at index {index}")
else:
    print(f"{search_name} not found")


