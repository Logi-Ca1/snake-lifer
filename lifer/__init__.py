from snake.scale import FileType, scale


NAME = "lifer"
VERSION = "1.0"

AUTHOR = "Calvin Cho"
AUTHOR_EMAIL = "calvin.cho@countercept.com"

DESCRIPTION = "a module to run lifer on lnk files"

LICENSE = "https://github.com/countercept/snake-scales/blob/master/LICENSE"

URL = "https://github.com/countercept/snake-scales"


__scale__ = scale(
    name=NAME,
    description=DESCRIPTION,
    version=VERSION,
    author=AUTHOR,
    supports=[
        FileType.FILE
    ],
)
