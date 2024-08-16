

print('hello world')

myname = "Shubham"
print(f"Hello {myname}! How are you?")


def hello_name(somename):
    print(f'Hello {somename}! This is a function.')


def repeat_hello(somename, m_times):
    for i in range (m_times):
        print(f'Hello there {somename}! This is print statement number: {i+1}')


if __name__ == "__main__":
    hello_name("class")
    hello_name("Shubham")


    repeat_hello(somename="Shubham", m_times=5)


