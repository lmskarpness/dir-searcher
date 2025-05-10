import os
import re

class FileSearcher:

    def search(self, directories, target):
        results = []
        
        for directory in directories:
            for root, _, files in os.walk(directory):
                for file in files:
                    if re.search(target, file):
                        results.append(root + '/' + file)
        return results