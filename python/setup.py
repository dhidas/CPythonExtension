from distutils.core import setup, Extension

module1 = Extension('AddTwo',
                    include_dirs = ['include'],
                    sources = ['src/AddTwo.cc',
                               'src/_AddTwo.cc',
                               ])

setup (name = 'AddTwo',
       version = '0.1',
       description = 'This is a test package',
       author = 'Dean Andrew Hidas',
       author_email = 'dhidas@bnl.gov',
       url = 'https://ya.right.there.is.a.url.for.this.software.net',
       long_description = '''At the moment there is not a long description for this''',
       ext_modules = [module1])
