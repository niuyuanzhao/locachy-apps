#!/usr/bin/env python3
"""Check this repository as a LOCachy system takes it, with that system's own
helper (never a copy of it here):
  python3 -I tools/check.py PATH/TO/locachy/src/link/locachy_apps.py
It says OK and how many presets there are, or why the system would refuse
the whole catalog (the first thing it finds)."""
import os
import subprocess
import sys

if len(sys.argv) != 2 or not os.path.isfile(sys.argv[1]):
    sys.exit(__doc__)
here = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.exit(subprocess.run([sys.executable, "-I", sys.argv[1], "validate", here]).returncode)
