class Subfoo:
    def hello(self):
        print("hello subfoo")

def main():
    foo = Subfoo()
    foo.hello()

if __name__ == '__main__':
    main()