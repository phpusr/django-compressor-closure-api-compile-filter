import unittest

import compiler

ERROR_JS_CODE = '''
fun hello() {
    conso.log()
}
'''

GOOD_JS_CODE = '''
function hello() {
    console.log('hello')
}
'''


class TestCompiler(unittest.TestCase):

    def test_minify(self):
        with self.assertRaises(compiler.ParseError) as cm:
            compiler.minify(ERROR_JS_CODE)

        errors = cm.exception.errors
        self.assertTrue(len(errors), 1)
        self.assertTrue(errors[0]['type'], 'JSC_PARSE_ERROR')

    def test_minify_good(self):
        minify_code = compiler.minify(GOOD_JS_CODE)
        self.assertTrue(minify_code, 'function hello(){console.log()};')
