#!/usr/bin/env python
import os

def print_file(fn):
    with open(fn) as f:
        for line in f.readlines():
            print(line.strip().replace("<p>", "<p>\n").replace("</p>", "\n</p>"))

def fix_url(s):
    return s.lower().replace(".", '').replace("?", '').replace("'", '').replace(')', '').replace(' (', '_').replace(',', '').replace('; ', '_').replace(':  ', '_').replace(': ', '_').replace(' ', '-')

breadcrumbs = []
with open('template') as f:
    for line in f:
        line = line.strip()
        print(line)
        if line.startswith('### '):
            while len(breadcrumbs) > 2:
                breadcrumbs.pop()
            breadcrumbs.append(line[4:])
            location = '/'.join([fix_url(x) for x in breadcrumbs])
            files = os.listdir('www.chesstactics.org/' + location)
            fns = sorted([(fn, fn.replace('.html', '').split('_')[-1]) for fn in files], key=lambda x: x[1])
            for fn in fns:
                full_fn = 'www.chesstactics.org/' + location + '/' + fn[0]
                os.system(r"""grep "mobile figure" %s | perl -nle 'm:src=".*/([^/"]*.gif)".*>(\w+ to move):; print "\n![](www.chesstactics.org/gfx/figures/$1)\n\n<span style=\"text-align: center\">$2</span>\n"' > /tmp/a""" % full_fn)
                print_file('/tmp/a')
                os.system(r"""awk "/tactics text-->/ { a=1; } /\/div/ { a=0; } { if (a) print }" %s > /tmp/a""" % full_fn)
                print_file('/tmp/a')
                print("----------------------------")
        elif line.startswith('## '):
            while len(breadcrumbs) > 1:
                breadcrumbs.pop()
            breadcrumbs.append(line[3:])
        elif line.startswith('# '):
            breadcrumbs.clear()
            breadcrumbs.append(line[2:])
