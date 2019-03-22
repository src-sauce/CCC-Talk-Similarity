"""
getData.py
"""


import os
import json
import pysrt
import requests
from bs4 import BeautifulSoup


__author__ = "info@dotarmin.info"
# Git at https://github.com/src-sauce


ignore = ['../', 'LICENSE_CC-BY-4.0.txt']



def get_urls(start_url, save_dir):

    def get_links_in(so):
        return [link['href'] for link in so.find_all('a') if link.text not in ignore]

    soup = BeautifulSoup(requests.get(start_url).text, 'html.parser')
    links = get_links_in(soup)
    paths = ['%s%s' % (start_url, link) for link in links]
    path_structure = {}
    for path in paths:
        soup2 = BeautifulSoup(requests.get(path).text, 'html.parser')
        links2 = get_links_in(soup2)
        paths2 = ['%s%s' % (path, link) for link in links2]
        path_structure[path] = paths2
    # print(path_structure)
    save_name = '%spath_structure.json' % save_dir
    with open(save_name, 'w') as f:
        f.write(json.dumps(path_structure))
    return path_structure


def request_parse(urls):
    return [
        " ".join([ p.text for p in BeautifulSoup(requests.get(url).text, 'html.parser').find_all('p') ])
        for url in open(urls, 'r').read().split('\n')
    ]


def save_hierarchy(hierarchy, path):
    for key in hierarchy:
        dir_key = key.split('/')[-2]
        if not os.path.exists(path):
            print(f'Created dir {path}')
            os.mkdir(path)
        if dir_key not in os.listdir(path):
            print(f'Created dir {path}')
            os.mkdir('%s%s' % (path, dir_key))
        local_dir = '%s%s' % (path, dir_key)
        for link in hierarchy[key]:
            print(f'Fetching file from {link} from {key}')
            soup = BeautifulSoup(requests.get(link).text, 'html.parser')
            fname = link.split('/')[-1]
            # if fname[-4:] != '.srt': fname += '.srt'
            # print(fname)
            with open('%s/%s' % (local_dir, fname), 'w') as f:
                f.write(soup.text)
                f.close()



class SRTs:
    def __init__(self, configs, _nd=0):
        self.srts_dir = configs['SUBTITLES']
        self.srt_objects = self.loadSrts(n_dirs=_nd)
        self.raw_texts = self.loadRawTexts()

    def loadSrts(self, n_dirs=0):
        srt_objects = {}
        dirs = [f for f in os.listdir(self.srts_dir) if not os.path.isfile(f)]
        if n_dirs == 0: n_dirs = len(dirs)
        for i in range(n_dirs):
            directory = dirs[i]
            for file in [fi for fi in os.listdir('%s%s/' % (self.srts_dir, directory)) if fi.split('.')[-1] == 'srt']:
                srt_objects[file] = pysrt.open('%s%s/%s' % (self.srts_dir, directory, file))
        # print('Availble files %s' % len(srt_objects))
        return srt_objects

    def loadRawTexts(self):
        texts = {}
        for file in self.srt_objects.keys():
            texts[file] = ""
            for fragment in self.srt_objects[file]:
                texts[file] += fragment.text.replace('\n', ' ') + ' '
        return texts



if __name__ == "__main__":
    configs = json.load(open('config.json', 'r'))
    urls = get_urls(configs['URL'], configs['OUTPUT'])
    struct = json.load(open('path_structure.json', 'r'))
    save_hierarchy(struct, configs['SUBTITLES'])
    srt_object = SRTs(configs, _nd=0)
    print("Ok, i'm done")

