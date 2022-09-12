''' Write a program to create seperate functions for each with local variable
name and each local variable should represent the respective name from each place '''

def sc(name="hd"):
    print(f"My Name in School is {name}")
    wk()
def cn(name="sd"):
    print(f"My Name in College is {name}")
def wk(name="hh"):
    print(f"My Name at Work Place is {name}")
    cn()
sc()