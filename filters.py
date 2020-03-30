from compressor.filters import CallbackOutputFilter


class GoogleClosureCompileFilter(CallbackOutputFilter):
    dependencies = ['requests']
    callback = 'google_closure_online_compile_filter.compiler.minify'
