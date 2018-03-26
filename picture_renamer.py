#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import os
import re


def get_creation_date(file):
    stats = os.stat(file)
    return datetime.datetime.fromtimestamp(stats.st_ctime).strftime('%Y-%m-%d')

def get_pictures(path):
    pics = [file for file in os.listdir(path) if file.endswith(".png")]
    return pics

def main():
    pngs = get_pictures(".")
    for png in pngs:
        m = re.search("-- \d{4}-\d{2}-\d{2}.png", png)
        if not m:
            date = get_creation_date(png)
            if re.search("[(]\d*[)]", png):
                png_new = png.rsplit(")", 1)[0] + ") -- {}".format(date) + ".png"
            else:
                png_new = png.rsplit(".", 1)[0] + " -- {}".format(date) + ".png"
            os.rename(png, png_new)


if __name__ == "__main__":
    main()
