from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True, 'includes': ["email.mime.multipart","email.mime.text"] }},
    windows = [{'script': "PassRevealetor.pyw"}],
    zipfile = None,
)
