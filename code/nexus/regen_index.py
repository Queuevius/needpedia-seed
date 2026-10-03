#!/usr/bin/env python3
"""Rebuild folder indexes (index.html + index.txt), the root
articles-index.txt pointer Adele uses, and llms.txt.
Run after adding or removing any article/botskill:
    python3 /home/clearcrow/Needpedia_Nexus/regen_index.py
"""
import os, re, html, datetime

ROOT = '/home/clearcrow/Needpedia_Nexus'
BASE = 'https://nexus.needpedia.org'
FOLDERS = {
    'articles':  'Long-form articles, core facts, glossary, use cases, episodes',
    'botskills': 'Behaviour guides for the Needpedia AI assistants',
}
# Documents listed even though they live outside the folders above.
# Added at Nexus session N44, 28 September 2026. To list another one,
# add a line: (folder whose list it joins, title, web address).
EXTRAS = [
    ('botskills', 'BOTSKILL: WORKING WITH TONY',
     f'{BASE}/working-with-tony.html'),
]
TODAY = datetime.date.today().isoformat()

def title_of(path):
    s = open(path, encoding='utf-8', errors='ignore').read(30000)
    for pat in (r'<title>(.*?)</title>', r'<h1[^>]*>(.*?)</h1>'):
        m = re.search(pat, s, re.S | re.I)
        if m:
            t = re.sub(r'<[^>]+>', ' ', m.group(1))
            t = re.sub(r'\s+', ' ', html.unescape(t)).strip()
            if t:
                return t[:120]
    return os.path.basename(path)[:-5].replace('-', ' ').capitalize()

def collect(folder):
    d = os.path.join(ROOT, folder)
    out = []
    for fn in sorted(os.listdir(d)):
        if fn.endswith('.html') and fn != 'index.html':
            out.append((title_of(os.path.join(d, fn)), f'{BASE}/{folder}/{fn}'))
    out += [(t, u) for f, t, u in EXTRAS if f == folder]
    return sorted(out, key=lambda x: x[0].lower())

def write_txt(items, folder, path):
    L = [f'Needpedia Nexus - {folder} index',
         f'Rebuilt {TODAY} - {len(items)} documents',
         f'Description: {FOLDERS[folder]}', '',
         'Every document below is a plain public page. Fetch any URL directly.', '']
    L += [f'{t}\n{u}\n' for t, u in items]
    L += [f'Nexus front door: {BASE}/start.html',
          f'Full nexus listing: {BASE}/llms.txt']
    open(path, 'w', encoding='utf-8').write('\n'.join(L) + '\n')

def write_html(items, folder):
    rows = '\n'.join(
        f'<li><a href="{u}">{html.escape(t)}</a></li>' for t, u in items)
    doc = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Needpedia Nexus - {folder} index</title>
<style>
 body{{background:#0a0a0a;color:#e8e8e8;font-family:'IBM Plex Sans',system-ui,sans-serif;
   max-width:820px;margin:0 auto;padding:48px 24px;line-height:1.6}}
 h1{{font-size:1.5rem;font-weight:500;margin-bottom:.25rem}}
 p.meta{{color:#888;font-size:.9rem;margin-bottom:2rem}}
 ul{{list-style:none;padding:0}}
 li{{padding:.45rem 0;border-bottom:1px solid #2a2a2a}}
 a{{color:#c8ff00;text-decoration:none}} a:hover{{text-decoration:underline}}
 footer{{margin-top:3rem;color:#888;font-size:.85rem;border-top:1px solid #2a2a2a;padding-top:1rem}}
</style></head><body>
<h1>Needpedia Nexus &mdash; {folder}</h1>
<p class="meta">{FOLDERS[folder]}<br>{len(items)} documents &middot; rebuilt {TODAY}</p>
<ul>
{rows}
</ul>
<footer>Nexus front door: <a href="{BASE}/start.html">start.html</a> &middot;
Full listing for AI readers: <a href="{BASE}/llms.txt">llms.txt</a> &middot;
Main site: <a href="https://www.needpedia.org">needpedia.org</a></footer>
</body></html>
'''
    open(os.path.join(ROOT, folder, 'index.html'), 'w', encoding='utf-8').write(doc)

def write_llms(counts):
    L = ['# Needpedia Nexus', '',
         'Public document collection for Needpedia, an open-source nonprofit civic',
         'collaboration platform (needpedia.org). Everything listed here is a plain',
         'public page and may be fetched directly.', '',
         f'Rebuilt {TODAY}', '',
         '## Start here', f'{BASE}/start.html', '  Front door: what Needpedia is, how to get involved, contact addresses.', '',
         '## Collections']
    for f, desc in FOLDERS.items():
        L += [f'{BASE}/{f}/index.html', f'  {desc} ({counts[f]} documents).',
              f'{BASE}/{f}/index.txt', '  Same listing, plain text.', '']
    L += ['## Working with Tony, and the thread system',
          f'{BASE}/working-with-tony.html',
          "  How any AI works with Tony Brasher, Needpedia's founder, and where every",
          '  project thread keeps its prompt accomplice and its public updates posts.', '']
    L += ['## Nonprofit records (public by intent)',
          f'{BASE}/Articles/Nonprofit%20Documents%20for%20Needpedia/',
          '  Articles of incorporation, bylaws, board members, conflict-of-interest policy.', '',
          '## Elsewhere',
          'https://www.needpedia.org  - the live platform',
          'https://github.com/Queuevius/Needpedia/wiki  - developer wiki', '',
          '## Contact',
          'Info@Needpedia.org - general', 'Needpedia@gmail.com - general',
          'VC@Needpedia.org - volunteer coordination']
    open(os.path.join(ROOT, 'llms.txt'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')

counts = {}
for folder in FOLDERS:
    items = collect(folder)
    counts[folder] = len(items)
    write_html(items, folder)
    write_txt(items, folder, os.path.join(ROOT, folder, 'index.txt'))
    if folder == 'articles':
        write_txt(items, folder, os.path.join(ROOT, 'articles-index.txt'))
    print(f'{folder}: {len(items)} documents')
write_llms(counts)
print('llms.txt written')
