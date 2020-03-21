import os


def get_images_names(dir):
    for i in os.listdir(dir):
        if '.' in i and i.split('.')[-1] in ['jpg', 'png']:
            yield i


if __name__ == '__main__':
    for i in get_images_names('static/img'):
        print(i)
