#!/usr/bin/env python

from brain_games.cli import entering_user_name


def main():
    print('Welcome to the Brain Games!')
    name = entering_user_name()
    return name


if __name__ == '__main__':
    main()
