def read_file(name):
    with open(name, "r",encoding='UTF-8') as f:
        test = f.read()
        f.close()
        return test
def read_filelist(name):
    with open(name, "r",encoding='UTF-8') as f:
        test = f.read()
        f.close()
        return test.split(',')


