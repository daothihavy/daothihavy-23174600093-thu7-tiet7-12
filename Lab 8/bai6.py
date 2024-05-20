### Bai 6
## Viết một chương trình có thể lọc các số lẻ trong một danh sách bằng cách sử dụng hàm filter.
def is_odd(num):
    return num % 2 != 0

def filter_odd_numbers(numbers):
    odd_numbers = filter(is_odd, numbers)
    return list(odd_numbers)
#VD
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = filter_odd_numbers(number_list)

print("Các số lẻ trong danh sách là:", odd_numbers)


## Viết một chương trình có thể lọc các số chẵn trong một danh sách bằng cách  sử dụng hàm filter.
def is_even(num):
    return num % 2 == 0

def filter_even_numbers(numbers):
    even_numbers = filter(is_even, numbers)
    return list(even_numbers)
#VD
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_even_numbers(number_list)

print("Các số chẵn trong danh sách là:", even_numbers)



## Viết một chương trình sử dụng hàm map() để tạo ra một danh sách trong đó các phần tử là lập phương của các phần tử trong danh sách ban đầu.
def cube(x):
    return x ** 3
def map_to_cube(numbers):
    cubes = map(cube, numbers)
    return list(cubes)
#VD
number_list = [1, 2, 3, 4, 5]

cubed_numbers = map_to_cube(number_list)
print("Danh sách các lập phương của các phần tử trong danh sách ban đầu là:", cubed_numbers)



## Viết một chương trình sử dụng hàm map() và filter() để tạo ra một danh sách trong đó các phần tử là lập phương của các số chẵn trong một danh sách đã 
def is_even(num):
    return num % 2 == 0

def cube(x):
    return x ** 3

def map_and_filter_to_cube_even(numbers):
    even_numbers = filter(is_even, numbers)
    cubed_even_numbers = map(cube, even_numbers)
    return list(cubed_even_numbers)
#VD
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cubed_even_numbers = map_and_filter_to_cube_even(number_list)

print("Danh sách các lập phương của các số chẵn trong danh sách ban đầu là:", cubed_even_numbers)



## Viết một chương trình sử dụng hàm map() và filter() để tạo ra một danh sách trong đó các phần tử là bình phương của các số lẻ trong một danh sách đã cho
def is_odd(num):
    return num % 2 != 0

def square(x):
    return x ** 2

def map_and_filter_to_square_odd(numbers):
    odd_numbers = filter(is_odd, numbers)
    squared_odd_numbers = map(square, odd_numbers)
    return list(squared_odd_numbers)
#VD
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_odd_numbers = map_and_filter_to_square_odd(number_list)

print("Danh sách các bình phương của các số lẻ trong danh sách ban đầu là:", squared_odd_numbers)
