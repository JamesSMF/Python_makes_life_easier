import re

def do_split(links):
    return re.findall('(https?://\S+)', links)
