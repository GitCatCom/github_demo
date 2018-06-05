import time

def simple_func():
    for _ in range(1, 10):
        print('*'*_)

if __name__ == '__main__':
    print("HelloGithub.")
    print("The current date is {}.".format(time.asctime()))
    simple_func()