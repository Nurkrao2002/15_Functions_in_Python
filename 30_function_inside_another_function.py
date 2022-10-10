def display(st):
    def message():
        return 'How are you? '
    m=message()+st
    return m
n=input("Enter your Name:")
s=display(n)
print(s)