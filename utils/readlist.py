def readlist(file_path):
        with open(file_path, "r") as file:
            urls = file.read().splitlines() 
            print(urls)
