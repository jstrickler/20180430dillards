#!/usr/bin/env python

import shutil

shutil.make_archive('DATAFILES', 'zip', 'DATA')

shutil.make_archive('DATAFILES', 'tar', 'DATA')

shutil.make_archive('DATAFILES', 'gztar', 'DATA')
