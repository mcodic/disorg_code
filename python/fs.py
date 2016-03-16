"""
all about files and filenames
"""

_all_ = ["rext"]

def rext(text):
    """
    remove extensions from list items
    """
    if ("." in text[-5:]):
        a = list(text)
        a.reverse()
        toList = "".join(a)
        dotPos = len(text) - toList.find(".")
        return text[:dotPos]
    else: return text