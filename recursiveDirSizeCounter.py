import os



def disk_usage(path):
    total = os.path.getsize(path)
    if(os.path.isdir(path) == False):
        return False
    else:
        for sub_dir in os.listdir(path):
            file = sub_dir
            child_path = os.path.join(path, file)
            total+=disk_usage(child_path)
    print(str(total))


def main():
    path = input("Enter a directory path: ")
    disk_usage(path)


if __name__ == "__main__":
    main()
