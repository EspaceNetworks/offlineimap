#!/usr/bin/env python

# $Id: setup.py,v 1.1 2002/06/21 18:10:49 jgoerzen Exp $

# IMAP synchronization
# Module: installer
# COPYRIGHT #
# Copyright (C) 2002 - 2006 John Goerzen
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

import os
#from distutils.core import setup, Command
# Always prefer setuptools over distutils
from setuptools import setup, find_packages, Command
import offlineimap
import logging
from test.OLItest import TextTestRunner, TestLoader, OLITestLib

# To use a consistent encoding
from codecs import open

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.


class TestCommand(Command):
    """runs the OLI testsuite"""
    description = """Runs the test suite. In order to execute only a single
        test, you could also issue e.g. 'python -m unittest
        test.tests.test_01_basic.TestBasicFunctions.test_01_olistartup' on the
        command line."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        logging.basicConfig(format='%(message)s')
        # set credentials and OfflineImap command to be executed:
        OLITestLib(cred_file='./test/credentials.conf', cmd='./offlineimap.py')
        suite = TestLoader().discover('./test/tests')
        #TODO: failfast does not seem to exist in python2.6?
        TextTestRunner(verbosity=2,failfast=True).run(suite)

pkgs=find_packages(exclude=['contrib.*', 'docs.*', 'tests.*', 'test.*', 'test', 'tests'])
#print("%s"% repr(pkgs))

setup(name = "offlineimap",
      version = offlineimap.__version__,
      description = offlineimap.__description__,
      long_description=long_description, # Optional
      author = offlineimap.__author__,
      author_email = offlineimap.__author_email__,
      maintainer = offlineimap.__maintainer__,
      maintainer_email = offlineimap.__maintainer_email__,
      url = offlineimap.__homepage__,

      scripts = ['bin/offlineimap'],
      license = offlineimap.__copyright__ + \
                ", Licensed under the GPL version 2",
      cmdclass = { 'test': TestCommand},

    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

	'Environment :: Console',
	'Environment :: No Input/Output (Daemon)',

        # Indicate who your project is intended for
        'Intended Audience :: Information Technology',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: System Administrators',

	'Natural Language :: English',

	'Operating System :: POSIX :: Linux',
	'Operating System :: POSIX :: BSD',
	'Operating System :: POSIX',
	'Operating System :: Microsoft :: Windows',
	'Operating System :: MacOS :: MacOS X',

        'Topic :: Communications :: Email',
	'Topic :: Communications :: Email Clients (MUA)',
        'Topic :: Communications :: Email :: Post-Office :: IMAP',

        # Pick your license as you wish
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    # This field adds keywords for your project which will appear on the
    # project page. What does your project relate to?
    #
    # Note that this is a string of words separated by whitespace, not a list.
    keywords=['IMAP', 'sync', 'email', 'Gmail', 'Maildir', 'kerberos', 'TLS', 'SSL', 'GSSAPI', 'offline', 'python', 'emails', 'mutt', 'notmuch', 'synchronize', 'maildir', 'mailboxes'], # Optional

    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    #packages = ['offlineimap', 'offlineimap.folder',
    #            'offlineimap.repository', 'offlineimap.ui',
    #            'offlineimap.utils'],
    packages=pkgs,  # Required

    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['six'],  # Optional

    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example:
    #
    #   $ pip install sampleproject[dev]
    #
    # Similar to `install_requires` above, these must be valid existing
    # projects.
    extras_require={  # Optional
        'dev': ['check-manifest'],
        'tests': ['coverage','pytest','pytest-cov','coverage','codecov','gssapi'],
        'kerberos': ['gssapi'],
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.
    #
    # If using Python 2.6 or earlier, then these have to be included in
    # MANIFEST.in as well.
    #package_data={  # Optional
    #    'sample': ['package_data.dat'],
    #},

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    #
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    #data_files=[('my_data', ['data/data_file'])],  # Optional

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    #entry_points={  # Optional
    #    'console_scripts': [
    #        'sample=sample:main',
    #    ],
    #},

    # List additional URLs that are relevant to your project as a dict.
    #
    # This field corresponds to the "Project-URL" metadata fields:
    # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    #
    # Examples listed include a pattern for specifying where the package tracks
    # issues, where the source is hosted, where to say thanks to the package
    # maintainers, and where to support the project financially. The key is
    # what's used to render the link text on PyPI.
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/OfflineIMAP/offlineimap/issues',
        'Funding': 'https://opencollective.com/offlineimap#backer',
        'Say Thanks!': 'http://saythanks.io/to/offlineimap',
        'Source': 'https://github.com/OfflineIMAP/offlineimap',
    },

)

