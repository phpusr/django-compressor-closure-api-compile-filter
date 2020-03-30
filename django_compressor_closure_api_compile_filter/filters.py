from compressor.filters import CallbackOutputFilter


class ClosureAPICompileFilter(CallbackOutputFilter):
    dependencies = ['requests']
    callback = 'django_compressor_closure_api_compile_filter.compiler.minify'
