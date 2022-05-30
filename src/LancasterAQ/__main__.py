import argparse
from importlib.metadata import metadata


def main():
    info = metadata('LancasterAQ')
    parser = argparse.ArgumentParser(prog=info['Name'])
    parser.add_argument('--version', '-V', action='version', version=f'%(prog)s {info["version"]}')
    args = parser.parse_args()


if __name__ == '__main__':
    main()
