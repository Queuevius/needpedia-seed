#!/usr/bin/env python3
"""Append an entry to DEVLOG.md.  Usage:
     python3 devlog_append.py entry.txt
     echo "text" | python3 devlog_append.py
"""
import sys
DEVLOG = '/home/clearcrow/Needpedia_Nexus/DEVLOG.md'
text = open(sys.argv[1], encoding='utf-8').read() if len(sys.argv) > 1 else sys.stdin.read()
if not text.strip():
    sys.exit('empty entry - nothing appended')
with open(DEVLOG, 'a', encoding='utf-8') as f:
    f.write('\n' + text.rstrip() + '\n')
print('DEVLOG appended,', len(text.strip().splitlines()), 'lines')
