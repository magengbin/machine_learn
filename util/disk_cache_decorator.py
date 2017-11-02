import functools
import os
import pickle
from ensure_directory import ensure_directory


def disk_cache(basename, directory, method=False):
    """
    Function decorator for caching pickleable return values on disk. Uses a
    hash computed from the function arguments for invalidation. If 'method',
    skip the first argument, usually being self or cls. The cache filepath is
    'directory/basename-hash.pickle'.
    """
    directory = os.path.expanduser(directory)
    ensure_directory(directory)

    def wrapper(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            key = (tuple(args), tuple(kwargs.items()))
            # Don't use self or cls for the invalidation hash.
            if method and key:
                key = key[1:]
            filename = '{}-{}.pickle'.format(basename, hash(key))
            print(filename)
            filepath = os.path.join(directory, filename)
            print(filepath)
            if os.path.isfile(filepath):
                with open(filepath, 'rb') as handle:
                    return pickle.load(handle)
            result = func(*args, **kwargs)
            with open(filepath, 'wb') as handle:
                pickle.dump(result, handle)
            return result
        return wrapped

    return wrapper


if __name__ == '__main__':
    directory = os.path.abspath('./tmp/dataset/')
    if not os.path.exists(directory):
        os.mkdir(directory)

    @disk_cache('dataset', directory)
    def get_dataset(one_hot=True):
        # dataset = Dataset('http://example.com/dataset.bz2')
        # dataset = Tokenize(dataset)
        # if one_hot:
        #    dataset = OneHotEncoding(dataset)
        # return dataset
        return True
    get_dataset()

