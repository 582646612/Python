def read_file(name):
    with open(name, "r",encoding='UTF-8') as f:
        test = f.read()
        f.close()
        return test