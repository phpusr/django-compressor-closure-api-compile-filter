#!/usr/bin/env python3

import requests
# src: https://developers.google.com/closure/compiler/?csw=1
# online: https://closure-compiler.appspot.com/home
# compilation_level: WHITESPACE_ONLY, SIMPLE_OPTIMIZATIONS, ADVANCED_OPTIMIZATIONS
# API reference: https://developers.google.com/closure/compiler/docs/api-ref
import sys

URL = 'https://closure-compiler.appspot.com/compile'
COMPILATION_LEVEL = 'SIMPLE_OPTIMIZATIONS'
"""WHITESPACE_ONLY, SIMPLE_OPTIMIZATIONS, ADVANCED_OPTIMIZATIONS"""
OUTPUT_FORMAT = 'json'


class ParseError(Exception):
    def __init__(self, errors):
        self.errors = errors


def minify(text):
    data = dict(
        js_code=text,
        compilation_level=COMPILATION_LEVEL,
        output_format=OUTPUT_FORMAT,
        output_info='errors'
    )
    response = requests.post(URL, data).json()
    errors = response.get('errors')
    if errors:
        raise ParseError(errors=errors)

    data['output_info'] = 'compiled_code'
    response = requests.post(URL, data).json()

    return response['compiledCode']


def main(argv):
    js_code = ''

    if argv:
        for file_path in argv:
            with open(file_path) as file:
                js_code += file.read()
    elif sys.stdin:
        for line in sys.stdin:
            js_code += line

    print(minify(js_code))


if __name__ == '__main__':
    main(sys.argv[1:])
