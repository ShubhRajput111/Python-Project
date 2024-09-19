from print_statement import repeat_hello, hello_name


def print_even_up_to_number(input_number):
    list_of_numbers= list(range(1, input_number+1))
    print(list_of_numbers)
    for num in list_of_numbers:
        if num %2 ==0:
            print(num)



if __name__ == "__main__":
    print("hello world")
    repeat_hello(somename="Shubham", m_times=5)
    hello_name("Shubham")

list_of_names = ["Shubham", "Rahul", "Shyam", "Nandey", "Ram"]
for name in list_of_names:
    hello_name(name)


    number_list = [1,2,3,4,5]
    print(number_list)

    for num in number_list:
        print(num)

    print_even_up_to_number(21)
