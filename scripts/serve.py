#!/usr/bin/env python3

import sys
import argparse
import subprocess
import livereload


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--python', default='python3')
    parser.add_argument('--pelican', default='pelican')
    parser.add_argument('-i', '--input', default='content')
    parser.add_argument('-o', '--output', default='output')
    parser.add_argument('-s', '--settings', default='pelicanconf.py')
    parser.add_argument('-p', '--port', default='8000')
    args = parser.parse_args()

    watcher = server = None

    try:
        # Rebuild static files
        watcher = subprocess.Popen([
            args.pelican,
            '--autoreload',
            '--output', args.output,
            '--settings', args.settings,
            args.input,
        ])

        # Serve static files
        server = subprocess.Popen([
            args.python, '-m', 'pelican.server', args.port,
        ], cwd=args.output)

        # Live reload
        live = livereload.Server()
        live.watch('content', delay=2)
        live.watch('theme', delay=2)
        live.serve(port=35729)

    except KeyboardInterrupt:
        pass

    finally:
        if watcher and watcher.pid:
            watcher.terminate()

        if server and server.pid:
            server.terminate()


if __name__ == '__main__':
    assert sys.version_info >= (3,), "Python 3.0 version required."
    main()
