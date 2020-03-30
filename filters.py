from compressor.filters import CallbackOutputFilter


class ClosureAPICompileFilter(CallbackOutputFilter):
    dependencies = ['requests']
    callback = 'compiler.minify'
