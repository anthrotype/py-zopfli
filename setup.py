#!/usr/bin/env python
"""
pyzopfli
======

Python bindings to zopfli
"""

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import sys


class custom_build_ext(build_ext):

    def build_extensions(self):
        if sys.platform == "win32":
            from distutils.msvccompiler import MSVCCompiler
            if isinstance(self.compiler, MSVCCompiler):
                # disable Language Extensions not compatible with ANSI C
                for ext in self.extensions:
                    ext.extra_compile_args.append("/Za")
        build_ext.build_extensions(self)


setup(
    name='zopfli',
    version='0.0.8',
    author='Adam DePrince',
    author_email='adeprince@nypublicradio.org',
    maintainer="Cosimo Lupo",
    maintainer_email="cosimo.lupo@daltonmaag.com",
    description='Zopfli module for python',
    long_description=__doc__,
    ext_modules=[
        Extension('zopfli.zopfli',
            sources=[
                'zopfli/src/zopfli/blocksplitter.c',
                'zopfli/src/zopfli/cache.c',
                'zopfli/src/zopfli/deflate.c',
                'zopfli/src/zopfli/gzip_container.c',
                'zopfli/src/zopfli/squeeze.c',
                'zopfli/src/zopfli/hash.c',
                'zopfli/src/zopfli/katajainen.c',
                'zopfli/src/zopfli/lz77.c',
                'zopfli/src/zopfli/tree.c',
                'zopfli/src/zopfli/util.c',
                'zopfli/src/zopfli/zlib_container.c',
                'src/zopflimodule.c',
            ],
        )
    ],
    package_dir={"": "src"},
    packages=["zopfli"],
    zip_safe=False,
    license='ASL',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: System :: Archiving :: Compression',
        ],
    url="https://github.com/anthrotype/py-zopfli",
    test_suite="tests",
    cmdclass={
        "build_ext": custom_build_ext,
    },
)
