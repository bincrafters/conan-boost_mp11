#!/usr/bin/env python

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostMp11Conan(base.BoostBaseConan):
    name = "boost_mp11"
    url = "https://github.com/bincrafters/conan-boost_mp11"
    lib_short_names = ["mp11"]
    header_only_libs = ["mp11"]
    b2_requires = [
        "boost_config",
    ]


