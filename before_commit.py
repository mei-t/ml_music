#!/usr/bin/env python
import json
import codecs

with codecs.open("music-playground.edit.ipynb", "r", "utf-8") as input:
    with codecs.open("music-playground.ipynb", "w", "utf-8") as output:
        loaded = json.load(input)
        json.dump(loaded, output, separators=(',', ':'), ensure_ascii=False, indent=1)
