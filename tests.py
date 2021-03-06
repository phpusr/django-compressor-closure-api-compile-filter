import unittest

from django_compressor_closure_api_compile_filter import compiler

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


class TestClosureApiCompiler(unittest.TestCase):

    def test_minify_bad(self):
        with self.assertRaises(compiler.ParseError) as cm:
            compiler.minify(ERROR_JS_CODE)

        errors = cm.exception.errors
        self.assertTrue(len(errors), 1)
        self.assertTrue(errors[0]['type'], 'JSC_PARSE_ERROR')

    def test_minify_good(self):
        minify_code = compiler.minify(GOOD_JS_CODE)
        self.assertTrue(minify_code, 'function hello(){console.log()};')


class TestJoinApiCompiler(unittest.TestCase):

    def test_join(self):
        code = compiler.join(GOOD_JS_CODE)
        self.assertTrue(code, GOOD_JS_CODE)
