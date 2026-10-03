import os

ROOT = "/home/clearcrow/Needpedia_Nexus"
SKIP = {"config", "kb", "master_uploads", "volunteer-logs", "cloudflared",
        "nginx", "__check__", ".git"}

def walk(rel):
    full = os.path.join(ROOT, rel) if rel else ROOT
    names = sorted(os.listdir(full))
    lines = []
    for n in names:
        if n.startswith(".") or n.startswith("_") or n in SKIP:
            continue
        if n in ("index.txt", "index.html"):
            continue
        path = os.path.join(full, n)
        href = "/" + (rel + "/" if rel else "") + n
        if os.path.isdir(path):
            lines.append(href + "/")
            walk((rel + "/" if rel else "") + n)
        else:
            lines.append(href)
    if rel:
        out = os.path.join(full, "index.txt")
        if os.path.exists(out) and rel in ("articles", "botskills"):
            print("left alone:", rel)
            return
        open(out, "w", encoding="utf-8").write("\n".join(lines) + "\n")
        print("wrote", len(lines), "entries ->", rel + "/index.txt")

for d in sorted(os.listdir(ROOT)):
    if os.path.isdir(os.path.join(ROOT, d)) and d not in SKIP and not d.startswith("."):
        walk(d)
