#!/usr/bin/env python

from __future__ import print_function, division, absolute_import

import io, os, re, sys

headers_content = []
if 'headers' in os.environ.keys():
	headers = os.environ["headers"].split (' ')
elif len(sys.argv) > 2:
	headers = sys.argv[1:] # with Meson we pass headers as command line args
else:
	headers = []

for h in headers:
	if h.endswith (".h"):
		with io.open (h, encoding='utf-8') as f: headers_content.append (f.read ())

result = """EXPORTS
%s
LIBRARY lib%s-0.dll""" % (
	"\n".join (sorted (re.findall (r"^hb_\w+(?= \()", "\n".join (headers_content), re.M))),
	sys.argv[1].replace ('src/', '').replace ('.def', '')
)

with open (sys.argv[1], "w") as f: f.write (result)
