from srtfix.srtfix import main
from pathlib import Path

src = [str(f) for f in Path('srtfix').glob('*.py')]
dist = list(Path('dist').glob('*'))


def task_test():
    return {
        'actions': ['pytest -v'],
        'file_dep': src,
    }


def task_build():
    return {
        'actions': [
            'python setup.py sdist bdist_wheel'
        ],
        'file_dep': src,
    }


def task_local_install():
    return {
        'actions': ['python setup.py install'],
        'file_dep': dist,
    }


def task_upload_test():
    with open('VERSION') as f:
        version = f.read()

    whl = f'dist/srtfix-{version}-py3-none-any.whl'
    return {
        'actions': [
            f'python -m twine upload --repository testpypi {whl}'
        ],
        'file_dep': [whl],
        'verbosity': 2,
    }
