THE NEXUS'S CODE, AS IT RAN ON 2 OCTOBER 2026

The Nexus is Needpedia's own document server (see inventory.txt,
section 7). It ran on an ordinary Linux desktop.

web/                     the pages; gallery.html is the front page
order-server.py          the small server program behind the admin
                         features, volunteer logins and AI studios
nginx.conf,
nginx-default.conf       the web server's settings
docker-compose.yml,
home-docker-compose.yml  the settings files that start each part
                         (web server, server program, terminal,
                         front door, Cloudflare Tunnel)
activity_monitor.sh      collects needpedia.org's activity numbers
crontab.txt              the schedule that runs it every 5 minutes
the other scripts        keep the folder listings and article
                         index up to date

Every password, key and token was replaced with REPLACE_ME. Make
your own. The list of volunteer accounts (volunteers.json) was
left out; make your own volunteer logins.
