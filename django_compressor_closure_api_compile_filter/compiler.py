import requests

URL = 'https://closure-compiler.appspot.com/compile'
COMPILATION_LEVEL = 'SIMPLE_OPTIMIZATIONS'
"""WHITESPACE_ONLY, SIMPLE_OPTIMIZATIONS, ADVANCED_OPTIMIZATIONS"""
OUTPUT_FORMAT = 'json'


class ParseError(Exception):
    def __init__(self, errors):
        self.errors = errors

    def __str__(self):
        return str(self.errors)


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
        raise ParseError(errors)

    data['output_info'] = 'compiled_code'
    response = requests.post(URL, data).json()

    return response['compiledCode']
