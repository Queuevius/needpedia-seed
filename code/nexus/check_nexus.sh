#!/bin/bash
cd /home/clearcrow/Needpedia_Nexus
echo "== MUST BE 404 =="
for p in /HANDOFF_next_session.txt /order-server.py /docker-compose.yml /volunteers.json /kb/ /config/ /.git/config; do
  printf "%-30s %s\n" "$p" "$(curl -s -o /dev/null -w '%{http_code}' "https://nexus.needpedia.org$p")"
done
echo "== MUST BE 200 =="
for p in / /start.html /llms.txt /articles-index.txt /articles/index.html /botskills/index.html; do
  printf "%-30s %s\n" "$p" "$(curl -s -o /dev/null -w '%{http_code}' "https://nexus.needpedia.org$p")"
done
echo "== TERMINAL (want 401) =="
curl -s -o /dev/null -w '%{http_code}\n' https://nexus.needpedia.org/terminal/
echo "== ARTICLES LINKED (want 23+) =="
grep -c '<li><a' articles/index.html
echo "== WATCHER (2=ok, 4=duplicate, 0=dead) =="
pgrep -f watch-articles.sh | wc -l
echo "== GIT (blank = clean) =="
git status --porcelain | head -3
echo "== DEVLOG LINES (rotate past 800) =="
wc -l < DEVLOG.md
