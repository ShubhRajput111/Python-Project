
def is_prime(number):
    list_of_number_from_2_to_nminusone = list(range(2, number))
    print(f"List of numbers' = {list_of_number_from_2_to_nminusone}")
    for num in list_of_number_from_2_to_nminusone:
        if number % num ==0:
            return False
        return True

if __name__=="__main__":
    print("This is a file for testing prime number")

    input_numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
    for num in input_numbers:
        if is_prime(num):
            print(f" input num is {num} It is prime")
        else:
            print(f" input num is {num}. It is not a prime")
