import os, inspect
from os.path import join, abspath, pardir
import re
import numpy
import pdb
from cv2 import imread, imwrite

class ImageManager:

    @staticmethod
    def _get_file_dir():
        return os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) # script directory

    def find_child_dirs(self, dir_path):
        child_dir_paths = []

        for dirname, dirnames, filenames in os.walk(dir_path):
            # print path to all subdirectories first.
            for subdirname in dirnames:
                child_dir_paths.append(os.path.join(dirname, subdirname))
        return child_dir_paths

    def files_from_dir_paths(self, dir_paths):
        fpaths = []
        for leaf_dir_path in dir_paths:
            for fname in os.listdir(leaf_dir_path):
                if len(re.findall(r'.*JPG', fname)) != 0:
                    fpaths.append(join(leaf_dir_path, fname))
        return fpaths

    def __init__(self):
        filedir = self._get_file_dir()
        image_root_dir = join(abspath(join(filedir, pardir)), 'images')
        self.dir_paths = self.find_child_dirs(image_root_dir)
        self.image_paths = self.files_from_dir_paths(self.dir_paths)

    def get_all_image_paths(self):
        return self.image_paths

    def get_all_images(self):
        return [imread(image_path) for image_path in self.get_all_image_paths()]

    def get_image_path(self, seedn=1):
        """
        Chooses a pseudo random image for a unit test.
        Pseudorandom in order to select the same image every time.
        :param seedn:
        :return:
        """
        lenImages = len(self.image_paths)
        numpy.random.seed(seedn)
        i = numpy.ceil(lenImages * numpy.random.random())
        return self.image_paths[int(i)]

    def get_image(self, seedn=1):
        return imread(self.get_image_path(seedn))

    def get_image_paths(self, n, seedn=1):
        """
        Get a set of size n using seed seedn.
        Designed for repeatable unit tests.

        :param n: number of images you need
        :param seed: Seed in order to make tests repeatable
        :return:
        """
        lenImages = len(self.image_paths)
        numpy.random.seed(seedn)
        indices = numpy.ceil(lenImages * numpy.random.random_sample((n,)))
        return [self.image_paths[int(i)] for i in indices]

    def get_images(self, n, seedn=1):
        return [imread(image_path) for image_path in self.get_image_paths(n, seedn)]

    def get_specific_image(self, name):
        potential_matches = []
        for path in self.get_all_image_paths():
            print name
            print path
            if len(re.findall(name, path)) > 0:
                potential_matches.append(path)
        pdb.set_trace()
        if len(potential_matches) != 1:
            raise Exception("Must use a string which uniquely matches image")


    def get_random_image_paths(self, n):
        """
        Truly random image section for integration tests, performance observation
        :param n:
        :return:
        """
        lenImages = len(self.image_paths)
        indices = numpy.ceil(lenImages * numpy.random.random_sample((n,)))
        return [self.image_paths[int(i)] for i in indices]

    def get_random_images(self, n):
        return [imread(image_path) for image_path in self.get_random_image_paths(n)]

    def writetmp(self, img):
        imwrite(self._get_file_dir() + '/../out/tmp.jpg', img)

    def write_n(self, n, img):
        imwrite(self._get_file_dir() + '/../out/%d.jpg' % n, img)


IM = ImageManager()
