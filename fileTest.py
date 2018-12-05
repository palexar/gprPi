

def main():
    f = open("scan1.txt", "w+")
    print("opened file")
    for i in range(10):
        f.write("This is line %d\r\n" % (i+1))

    f.close()

if __name__== "__main__":
    main()
