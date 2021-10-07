## @file
## @brief meta: eBook firmware proto

from metaL import *

p = Project(
    title='''eBook firmware proto''',
    about='''
* pure embedded Linux (Buildroot)
* hardware supported:
  * x86 PC
  * Raspberry Pi
''') \
    | Buildroot()

p.sync()
