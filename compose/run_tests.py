from socket import gethostbyname
from sys import stdout, argv

from requests import get
from time import sleep


def test():
    sleep(10)
    stdout.write('\n\nRunning tests\n\n')
    request_url = f"http://{gethostbyname('localhost')}:5000"

    for _ in range(10):
        stdout.write(get(url=request_url).content.decode(encoding='UTF-8'))
        sleep(1)

    stdout.write('Completed Tests.\n\nShutting down container.\n\n\n')


if __name__ == '__main__':
    if len(argv) == 2 and argv[1] == 'RUN_TEST':
        test()
    else:
        exit('This is a test script to make GET calls to the flask app spun by docker.\n'
             'Do not run this file manually.\n'
             'Run `bash docker-compose.sh` on a command-line instead.')
