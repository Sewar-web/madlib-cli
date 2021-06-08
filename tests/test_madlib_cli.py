from madlib_cli import __version__
from madlib_cli.madlib import read_template ,parse_template,merg


def test_version():
    assert __version__ == '0.1.0'


def test_read_it():
    actu=read_template('text/template.txt')
    aspp='the path is invalid'
    assert actu != aspp
def test_prse_it():
        assert parse_template('text/template.txt')== r"\{(.*?)\}"
def merg_it():
            ac1='text/template.txt'
            ac2=r"\{(.*?)\}"
            assert merg(ac1 and ac2)== True



