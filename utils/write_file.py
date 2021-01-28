import os


def write_file(path, *args):
    if path is not None:
        path = 'data/'
    if not os.path.exists(path):
        os.makedirs(path)
    samples_file = open(path + '/write_file.txt', 'a', encoding='utf8')

    for i in args:
        samples_file.write('{}\n'.format(i))
    samples_file.close()
