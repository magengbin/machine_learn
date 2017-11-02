import os
import shutil
import errno
from ensure_directory import ensure_directory
from lxml import etree
from urllib.request import urlopen


def download(url, directory, filename=None):
    """
    Download a file and return its filename on the local file system. If the
    file is already there, it will not be downloaded again. The filename is
    derived from the url if not provided. Return the filepath.
    """
    if not filename:
        _, filename = os.path.split(url)
    directory = os.path.expanduser(directory)
    ensure_directory(directory)
    filepath = os.path.join(directory, filename)
    if os.path.isfile(filepath):
        return filepath
    print('Download', filepath)
    with urlopen(url) as response, open(filepath, 'wb') as file_:
        shutil.copyfileobj(response, file_)
    return filepath


if __name__ == '__main__':
    url = 'https://update.futu5.com/conn_all_ip_list.txt'
    directory = os.path.abspath('./tmp/')
    if not os.path.exists(directory):
        os.mkdir(directory)
    download(url=url, directory=directory)
