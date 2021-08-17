from typing import Tuple
import sys
from os import remove as rm, path
from subprocess import run

from mingus.extra import lilypond

def xml2png(string: str) -> Tuple[bool, str]:
    """
    Converts a MusicXML string to an PNG image.
    Returns a tuple `(success: bool, context: str)`.

    If successful, `success` is `True`, and `context` is the path of the rendered image.

    If failed, `success` is `False`, and `context` is the error message.

    Make sure to `sudo apt install lilypond` on your machine,
    and also do `pipenv install` or `pipenv install mingus`.
    """

    if path.isfile('temp.ly'): rm('temp.ly')
    if path.isfile('temp.ly~'): rm('temp.ly~')
    if path.isfile('temp.png'): rm('temp.png')
    if path.isfile('temp-page1.png'): rm('temp-page1.png')
    try:
        p = run(['musicxml2ly', '-', '-o', 'temp.ly'], input=string, encoding='utf-8')
        if p.returncode:
            return (False, 'Failed to run musicxml2ly, log:\n' + p.stdout)
        else:
            with open('temp.ly', 'r') as g:
                success = lilypond.to_png(g.read(), "temp.png")
                pngExists = path.isfile('temp.png')
                pngPageExists = path.isfile('temp-page1.png')
                if (pngExists or pngPageExists) and success:
                    if pngExists:     return (True, 'temp.png')
                    if pngPageExists: return (True, 'temp-page1.png')
                else:
                    return (False, 'Failed to render image.')
    except Exception as inst:
        return (False, 'Failed. Error:' + sys.exc_info()[0])
