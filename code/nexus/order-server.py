import http.server, json, os, urllib.parse, hashlib, datetime, base64, urllib.request, secrets, time, shutil, zipfile, io
BASE   = '/data'
PASS = 'REPLACE_ME'
PORT   = 8181
DEVLOG      = '/data/DEVLOG.md'
UPLOAD_ROOT = '/home/clearcrow/Needpedia_Nexus/master_uploads'
HOME_ROOT   = '/home/clearcrow'
DRIVE_CAP   = 0.80
OR_KEY        = 'REPLACE_ME'

# --- N39c: web research tools (server-side; model decides when to search)
WEB_SYS = {
    'role': 'system',
    'content': ('You have web search, a web page reader, and a clock '
                'available as tools. Use them for anything time-sensitive, '
                'for facts you are not certain of, and whenever you are '
                'asked to research something. Do not search for casual '
                'conversation or questions about yourself. Cite sources as '
                'markdown links.')
}
WEB_TOOLS = [
    {'type': 'openrouter:web_search',
     'parameters': {'engine': 'parallel', 'mode': 'turbo',
                    'max_results': 5, 'max_uses': 3,
                    'max_total_results': 10}},
    {'type': 'openrouter:web_fetch'},
    {'type': 'openrouter:datetime'},
]
# --- end N39c
VOL_KEY = 'REPLACE_ME'

ADMIN_CONVS   = '/home/clearcrow/admin-convs'
ACTIVITY_JSON = '/home/clearcrow/Nexus_private/data/activity.json'
CAPTURE_TOKEN = 'REPLACE_ME'
# In-memory admin tokens: token -> expiry timestamp
_admin_tokens = {}
def hash_pw(pw):
    return hashlib.sha256(pw.encode()).hexdigest()
def load_volunteers():
    path = os.path.join(BASE, 'volunteers.json')
    try:
        with open(path) as f:
            return json.load(f)
    except:
        return []
def issue_token():
    tok = secrets.token_hex(32)
    _admin_tokens[tok] = time.time() + 86400  # 24 hours
    return tok
def valid_token(tok):
    if not tok or tok not in _admin_tokens:
        return False
    if time.time() > _admin_tokens[tok]:
        del _admin_tokens[tok]
        return False
    return True
STORAGE_CAP = 5 * 1024 * 1024 * 1024
def dir_size(path):
    total = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            try:
                total += os.path.getsize(os.path.join(dirpath, f))
            except:
                pass
    return total
class Handler(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, X-Admin-Token')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.end_headers()
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path   = parsed.path
        params = urllib.parse.parse_qs(parsed.query)
        if path == '/admin-devlog':
            self._handle_devlog_get(params)
        elif path == '/admin-browse':
            self._handle_admin_browse(params)
        elif path == '/admin-file':
            self._handle_admin_file(params)
        elif path == '/admin-convs':
            self._handle_admin_convs_get(params)
        elif path == '/admin-conv':
            self._handle_admin_conv_get(params)
        elif path == '/admin-activity':
            self._handle_admin_activity(params)
        elif path == '/volunteer-convs':
            self._handle_volunteer_convs_get(params)
        elif path == '/volunteer-conv':
            self._handle_volunteer_conv_get(params)
        else:
            self.send_response(404)
            self.end_headers()
    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path   = parsed.path
        length = int(self.headers.get('Content-Length', 0))
        if path == '/folder-upload':
            raw = self.rfile.read(length)
            self._handle_folder_upload(raw, parsed.query)
            return
        body   = json.loads(self.rfile.read(length))

        if path == '/save-order':
            self._handle_save_order(body)
        elif path == '/volunteer-auth':
            self._handle_auth(body)
        elif path == '/volunteer-log':
            self._handle_log(body)
        elif path == '/save-text':
            self._handle_save_text(body)
        elif path == '/save-image':
            self._handle_save_image(body)
        elif path == '/admin-auth':
            self._handle_admin_auth(body)
        elif path == '/admin-ops':
            self._handle_admin_ops(body)
        elif path == '/admin-delete':
            self._handle_admin_delete(body)
        elif path == '/admin-chat-proxy':
            self._handle_admin_chat_proxy(body)
        elif path == '/volunteer-chat-proxy':
            self._handle_volunteer_chat_proxy(body)
        elif path == '/admin-convs':
            self._handle_admin_convs_post(body)
        elif path == '/admin-import':
            self._handle_admin_import(body)
        elif path == '/admin-conv-delete':
            self._handle_admin_conv_delete(body)
        elif path == '/admin-conv-rename':
            self._handle_admin_conv_rename(body)
        elif path == '/capture':
            self._handle_capture(body)
        else:
            self.send_response(404)
            self.end_headers()
    def _handle_admin_auth(self, body):
        pw = body.get('password', '')
        if pw == PASS:
            tok = issue_token()
            self.send_response(200)
            self._cors()
            self.end_headers()
            self.wfile.write(json.dumps({'success': True, 'token': tok}).encode())
        else:
            self.send_response(401)
            self._cors()
            self.end_headers()
            self.wfile.write(json.dumps({'success': False, 'error': 'Invalid password'}).encode())

    def _handle_devlog_get(self, params):
        tok = self.headers.get('X-Admin-Token', '')
        pw  = params.get('password', [''])[0]
        if not valid_token(tok) and pw != PASS:
            self.send_response(403)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(b'Unauthorized')
            return
        try:
            with open(DEVLOG, 'r') as f:
                content = f.read().encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(content)
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(str(e).encode())

    def _handle_admin_activity(self, params):
        tok = self.headers.get('X-Admin-Token', '')
        if not valid_token(tok):
            self.send_response(403); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"Unauthorized"}')
            return
        try:
            with open(ACTIVITY_JSON, 'rb') as f:
                data = f.read()
            self.send_response(200); self._cors()
            self.send_header('Cache-Control', 'no-store')
            self.end_headers()
            self.wfile.write(data)
        except FileNotFoundError:
            self.send_response(404); self._cors(); self.end_headers()
            self.wfile.write(b'{"ok":false,"error":"no data yet"}')
        except Exception as e:
            self.send_response(500); self._cors(); self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode())

    def _handle_admin_ops(self, body):
        tok = self.headers.get('X-Admin-Token', '')
        if not valid_token(tok):
            self.send_response(401)
            self._cors()
            self.end_headers()
            self.wfile.write(b'{"error":"Unauthorized"}')
            return
        action = body.get('action', '')
        self.send_response(200)
        self._cors()
        self.end_headers()
        self.wfile.write(json.dumps({'result': f'Ops not yet wired up (action: {action}). Coming in a future session.'}).encode())

    def _handle_admin_delete(self, body):
        tok = self.headers.get('X-Admin-Token', '')
        if not valid_token(tok):
            self.send_response(401); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"Unauthorized"}')
            return
        target    = body.get('path', '')
        real_path = os.path.realpath(target)
        if not real_path.startswith(os.path.realpath(HOME_ROOT)):
            self.send_response(403); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"Path not allowed"}')
            return
        if real_path == os.path.realpath(HOME_ROOT) or real_path == os.path.realpath(UPLOAD_ROOT):
            self.send_response(403); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"Cannot delete root folders"}')
            return
        try:
            if os.path.isdir(real_path):
                shutil.rmtree(real_path)
            elif os.path.isfile(real_path):
                os.remove(real_path)
            else:
                self.send_response(404); self._cors(); self.end_headers()
                self.wfile.write(b'{"error":"Not found"}')
                return
            self.send_response(200); self._cors(); self.end_headers()
            self.wfile.write(json.dumps({'ok': True, 'deleted': real_path}).encode())
        except Exception as e:
            self.send_response(500); self._cors(); self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode())

    def _handle_folder_upload(self, raw, query_string):
        tok = self.headers.get('X-Admin-Token', '')
        if not valid_token(tok):
            self.send_response(401); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"Unauthorized"}')
            return
        params      = urllib.parse.parse_qs(query_string)
        target      = params.get('path', [UPLOAD_ROOT])[0]
        real_target = os.path.realpath(target)
        if not real_target.startswith(os.path.realpath(HOME_ROOT)):
            self.send_response(403); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"Path not allowed"}')
            return
        usage = shutil.disk_usage('/')
        if len(raw) > 0 and (usage.used + len(raw)) / usage.total > DRIVE_CAP:
            self.send_response(507); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"Drive cap reached"}')
            return
        try:
            os.makedirs(real_target, exist_ok=True)
            extracted = []
            with zipfile.ZipFile(io.BytesIO(raw)) as zf:
                for member in zf.namelist():
                    member_clean = os.path.normpath(member)
                    if member_clean.startswith('..'):
                        continue
                    dest = os.path.realpath(os.path.join(real_target, member_clean))
                    if not dest.startswith(real_target):
                        continue
                    zf.extract(member, real_target)
                    if not member.endswith('/'):
                        extracted.append(member)
            self.send_response(200); self._cors(); self.end_headers()
            self.wfile.write(json.dumps({'ok': True, 'files': extracted, 'count': len(extracted), 'target': real_target}).encode())
        except Exception as e:
            self.send_response(500); self._cors(); self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode())

    def _handle_admin_browse(self, params):
        tok = self.headers.get('X-Admin-Token', '')
        if not valid_token(tok):
            self.send_response(403); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"Unauthorized"}')
            return
        browse_path = params.get('path', [UPLOAD_ROOT])[0]
        real_path   = os.path.realpath(browse_path)
        if not real_path.startswith(os.path.realpath(HOME_ROOT)):
            self.send_response(403); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"Path not allowed"}')
            return
        if not os.path.isdir(real_path):
            self.send_response(404); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"Not a directory"}')
            return
        entries = []
        try:
            for name in sorted(os.listdir(real_path)):
                full = os.path.join(real_path, name)
                try:
                    stat = os.stat(full)
                    entries.append({
                        'name':     name,
                        'type':     'dir' if os.path.isdir(full) else 'file',
                        'size':     stat.st_size,
                        'modified': datetime.datetime.utcfromtimestamp(stat.st_mtime).isoformat() + 'Z',
                        'path':     full
                    })
                except Exception:
                    pass
        except Exception as e:
            self.send_response(500); self._cors(); self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode())
            return
        parent = str(os.path.dirname(real_path))
        self.send_response(200); self._cors(); self.end_headers()
        self.wfile.write(json.dumps({'path': real_path, 'parent': parent, 'entries': entries}).encode())

    def _handle_admin_file(self, params):
        tok = self.headers.get('X-Admin-Token', '')
        if not valid_token(tok):
            self.send_response(403); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"Unauthorized"}')
            return
        file_path = params.get('path', [''])[0]
        real_path = os.path.realpath(file_path)
        if not real_path.startswith(os.path.realpath(HOME_ROOT)):
            self.send_response(403); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"Path not allowed"}')
            return
        if not os.path.isfile(real_path):
            self.send_response(404); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"Not found"}')
            return
        try:
            with open(real_path, 'rb') as fh:
                data = fh.read()
            filename = os.path.basename(real_path)
            self.send_response(200)
            self.send_header('Content-Type', 'application/octet-stream')
            self.send_header('Content-Disposition', 'attachment; filename="' + filename + '"')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type, X-Admin-Token')
            self.send_header('Content-Length', str(len(data)))
            self.end_headers()
            self.wfile.write(data)
        except Exception as e:
            self.send_response(500); self._cors(); self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode())

    def _handle_save_order(self, body):
        if body.get('password') != PASS:
            self.send_response(403)
            self._cors()
            self.end_headers()
            self.wfile.write(b'{"error":"bad password"}')
            return
        folder = body.get('folder', '').strip('/').replace('..', '')
        order  = body.get('order', [])
        target = os.path.join(BASE, folder, '_order.json')
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, 'w') as f:
            json.dump(order, f)
        self.send_response(200)
        self._cors()
        self.end_headers()
        self.wfile.write(b'{"ok":true}')

    def _handle_auth(self, body):
        username   = body.get('username', '').strip()
        password   = body.get('password', '')
        volunteers = load_volunteers()
        hashed     = hash_pw(password)
        match = next((v for v in volunteers if v['username'] == username and v['password_hash'] == hashed), None)
        if match:
            self.send_response(200)
            self._cors()
            self.end_headers()
            self.wfile.write(json.dumps({'ok': True, 'username': username}).encode())
        else:
            self.send_response(403)
            self._cors()
            self.end_headers()
            self.wfile.write(b'{"error":"invalid credentials"}')

    def _handle_save_image(self, body):
        username   = body.get('username', '').strip().replace('..', '').replace('/', '')
        session_id = body.get('session_id', '').strip().replace('..', '').replace('/', '').replace(' ', '_')
        if not username or not session_id:
            self.send_response(400); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"missing username or session_id"}')
            return

        log_root = os.path.join(BASE, 'volunteer-logs')
        if dir_size(log_root) > STORAGE_CAP:
            self.send_response(507); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"storage cap reached"}')
            return

        sess_dir = os.path.join(log_root, username, 'image-sessions')
        os.makedirs(sess_dir, exist_ok=True)

        now   = datetime.datetime.utcnow().isoformat() + 'Z'
        entry = {
            'timestamp': now,
            'model':     body.get('model', ''),
            'prompt':    body.get('prompt', ''),
            'img_url':   body.get('img_url', '')
        }

        img_url      = entry.get('img_url', '')
        img_filename = None
        img_index    = len([f for f in os.listdir(sess_dir) if f.startswith(session_id) and f.endswith('.png')]) + 1
        img_filename = session_id + '_' + str(img_index).zfill(2) + '.png'
        img_path     = os.path.join(sess_dir, img_filename)
        try:
            if img_url.startswith('data:image'):
                header, b64data = img_url.split(',', 1)
                img_bytes = base64.b64decode(b64data)
                with open(img_path, 'wb') as f:
                    f.write(img_bytes)
            elif img_url.startswith('http'):
                req       = urllib.request.urlopen(img_url, timeout=30)
                img_bytes = req.read()
                with open(img_path, 'wb') as f:
                    f.write(img_bytes)
            else:
                img_filename = None
        except Exception:
            img_filename = None

        if img_filename:
            entry['local_file'] = img_filename
        entry.pop('img_url', None)

        sess_file = os.path.join(sess_dir, session_id + '.json')
        session   = []
        if os.path.exists(sess_file):
            try:
                with open(sess_file) as f:
                    session = json.load(f)
            except:
                session = []
        session.append(entry)
        with open(sess_file, 'w') as f:
            json.dump(session, f, indent=2)

        index_file = os.path.join(log_root, username, 'index.json')
        index      = []
        if os.path.exists(index_file):
            try:
                with open(index_file) as f:
                    index = json.load(f)
            except:
                index = []
        existing = next((x for x in index if x.get('session_id') == session_id), None)
        if existing:
            existing['last_updated'] = now
            existing['image_count']  = len(session)
        else:
            index.insert(0, {
                'type':         'image',
                'session_id':   session_id,
                'title':        body.get('prompt', '')[:60],
                'started_at':   now,
                'last_updated': now,
                'image_count':  1
            })
        with open(index_file, 'w') as f:
            json.dump(index, f, indent=2)

        self.send_response(200); self._cors(); self.end_headers()
        self.wfile.write(b'{"ok":true}')

    def _handle_save_text(self, body):
        username = body.get('username', '').strip().replace('..', '').replace('/', '')
        convo_id = body.get('convo_id', '').strip().replace('..', '').replace('/', '').replace(' ', '_')
        if not username or not convo_id:
            self.send_response(400); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"missing username or convo_id"}')
            return

        log_root   = os.path.join(BASE, 'volunteer-logs')
        total_size = dir_size(log_root)
        if total_size > STORAGE_CAP:
            self.send_response(507); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"storage cap reached"}')
            return

        convo_dir  = os.path.join(log_root, username, 'convos')
        os.makedirs(convo_dir, exist_ok=True)

        convo_file = os.path.join(convo_dir, convo_id + '.jsonl')
        now        = datetime.datetime.utcnow().isoformat() + 'Z'
        entry      = {
            'timestamp': now,
            'model':     body.get('model', ''),
            'user_msg':  body.get('user_msg', ''),
            'reply':     body.get('reply', '')
        }
        with open(convo_file, 'a') as f:
            f.write(json.dumps(entry) + '\n')

        index_file = os.path.join(log_root, username, 'index.json')
        index      = []
        if os.path.exists(index_file):
            try:
                with open(index_file) as f:
                    index = json.load(f)
            except:
                index = []
        existing = next((x for x in index if x.get('convo_id') == convo_id), None)
        if existing:
            existing['last_updated'] = now
            existing['title']        = body.get('title', existing.get('title', 'Untitled'))
        else:
            index.insert(0, {
                'convo_id':    convo_id,
                'title':       body.get('title', 'Untitled'),
                'started_at':  now,
                'last_updated': now
            })
        with open(index_file, 'w') as f:
            json.dump(index, f, indent=2)

        self.send_response(200); self._cors(); self.end_headers()
        self.wfile.write(b'{"ok":true}')

    def _handle_log(self, body):
        username = body.get('username', '').strip().replace('..', '').replace('/', '')
        if not username:
            self.send_response(400); self.end_headers(); return
        entry              = body.get('entry', {})
        entry['timestamp'] = datetime.datetime.utcnow().isoformat() + 'Z'
        log_path           = os.path.join(BASE, 'volunteer-logs', username + '.json')
        logs               = []
        if os.path.exists(log_path):
            try:
                with open(log_path) as f:
                    logs = json.load(f)
            except:
                logs = []
        logs.append(entry)
        with open(log_path, 'w') as f:
            json.dump(logs, f, indent=2)
        self.send_response(200)
        self._cors()
        self.end_headers()
        self.wfile.write(b'{"ok":true}')

    def _handle_admin_chat_proxy(self, body):
        tok = self.headers.get('X-Admin-Token', '')
        if not valid_token(tok):
            self.send_response(401); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"Unauthorized"}'); return
        payload = json.dumps({
            'model':    body.get('model', 'deepseek/deepseek-v4-pro-0813'),
            'messages': (([WEB_SYS] + body.get('messages', []))
                         if body.get('web') else body.get('messages', [])),
            **({'tools': WEB_TOOLS, 'max_tool_calls': 6}
               if body.get('web') else {})
        }).encode()
        req = urllib.request.Request(
            'https://openrouter.ai/api/v1/chat/completions',
            data=payload,
            headers={
                'Content-Type':  'application/json',
                'Authorization': 'Bearer ' + OR_KEY,
                'HTTP-Referer':  'https://nexus.needpedia.org',
                'X-Title':       'Needpedia Admin Chat',
            }
        )
        try:
            resp = urllib.request.urlopen(req, timeout=120)
            self.send_response(200); self._cors(); self.end_headers()
            self.wfile.write(resp.read())
        except urllib.error.HTTPError as e:
            self.send_response(e.code); self._cors(); self.end_headers()
            self.wfile.write(e.read())
        except Exception as e:
            self.send_response(500); self._cors(); self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode())

    def _handle_volunteer_chat_proxy(self, body):
        payload = json.dumps({
            'model':    body.get('model', 'qwen/qwen3-235b-a22b-2507'),
            'messages': (([WEB_SYS] + body.get('messages', []))
                         if body.get('web') else body.get('messages', [])),
            **({'tools': WEB_TOOLS, 'max_tool_calls': 6}
               if body.get('web') else {}),
            'stream': True
        }).encode()
        req = urllib.request.Request(
            'https://openrouter.ai/api/v1/chat/completions',
            data=payload,
            headers={
                'Content-Type':  'application/json',
                'Authorization': 'Bearer ' + VOL_KEY,
                'HTTP-Referer':  'https://nexus.needpedia.org',
                'X-Title':       'Needpedia Volunteer Text Studio',
            }
        )
        try:
            resp = urllib.request.urlopen(req, timeout=300)
        except urllib.error.HTTPError as e:
            self.send_response(e.code); self._cors(); self.end_headers()
            self.wfile.write(e.read())
            return
        except Exception as e:
            self.send_response(500); self._cors(); self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode())
            return
        self.send_response(200); self._cors()
        self.send_header('Content-Type', 'text/event-stream')
        self.send_header('Cache-Control', 'no-cache')
        self.send_header('X-Accel-Buffering', 'no')
        self.end_headers()
        try:
            for line in resp:
                self.wfile.write(line)
                self.wfile.flush()
        except Exception as e:
            try:
                msg = json.dumps({'error': {'message': str(e)}})
                self.wfile.write(('data: ' + msg + '\n\n').encode())
                self.wfile.flush()
            except Exception:
                pass

    def _handle_admin_convs_get(self, params):
        tok = self.headers.get('X-Admin-Token', '')
        if not valid_token(tok):
            self.send_response(403); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"Unauthorized"}'); return
        os.makedirs(ADMIN_CONVS, exist_ok=True)
        idx = os.path.join(ADMIN_CONVS, 'index.json')
        data = []
        if os.path.exists(idx):
            try:
                with open(idx) as f: data = json.load(f)
            except: pass
        self.send_response(200); self._cors(); self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def _handle_admin_conv_get(self, params):
        tok = self.headers.get('X-Admin-Token', '')
        if not valid_token(tok):
            self.send_response(403); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"Unauthorized"}'); return
        cid = params.get('id', [''])[0].replace('..', '').replace('/', '')
        if not cid:
            self.send_response(400); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"Missing id"}'); return
        p = os.path.join(ADMIN_CONVS, cid + '.json')
        if not os.path.exists(p):
            self.send_response(404); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"Not found"}'); return
        with open(p) as f: raw = f.read()
        self.send_response(200); self._cors(); self.end_headers()
        self.wfile.write(raw.encode())

    def _handle_admin_convs_post(self, body):
        tok = self.headers.get('X-Admin-Token', '')
        if not valid_token(tok):
            self.send_response(401); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"Unauthorized"}'); return
        conv = body.get('conversation', {})
        cid  = conv.get('id', '').replace('..', '').replace('/', '').replace(' ', '_')
        if not cid:
            self.send_response(400); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"Missing conversation.id"}'); return
        os.makedirs(ADMIN_CONVS, exist_ok=True)
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        conv['updated_at'] = now
        if 'created_at' not in conv: conv['created_at'] = now
        with open(os.path.join(ADMIN_CONVS, cid + '.json'), 'w') as f:
            json.dump(conv, f, indent=2)
        idx = os.path.join(ADMIN_CONVS, 'index.json')
        index = []
        if os.path.exists(idx):
            try:
                with open(idx) as f: index = json.load(f)
            except: pass
        entry = next((x for x in index if x.get('id') == cid), None)
        if entry:
            entry.update({'title': conv.get('title', 'Untitled'),
                          'model': conv.get('model', ''), 'updated_at': now})
        else:
            index.insert(0, {'id': cid, 'title': conv.get('title', 'Untitled'),
                             'model': conv.get('model', ''),
                             'created_at': now, 'updated_at': now})
        with open(idx, 'w') as f: json.dump(index, f, indent=2)
        self.send_response(200); self._cors(); self.end_headers()
        self.wfile.write(b'{"ok":true}')

    def _handle_volunteer_convs_get(self, params):
        user = params.get('user', [''])[0].strip().replace('..', '').replace('/', '')
        if not user:
            self.send_response(400); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"Missing user"}'); return
        idx  = os.path.join(BASE, 'volunteer-logs', user, 'index.json')
        data = []
        if os.path.exists(idx):
            try:
                with open(idx) as f: data = json.load(f)
            except: pass
        data = [x for x in data if x.get('convo_id')]
        self.send_response(200); self._cors(); self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def _handle_volunteer_conv_get(self, params):
        user = params.get('user', [''])[0].strip().replace('..', '').replace('/', '')
        cid  = params.get('id',   [''])[0].strip().replace('..', '').replace('/', '')
        if not user or not cid:
            self.send_response(400); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"Missing user or id"}'); return
        p = os.path.join(BASE, 'volunteer-logs', user, 'convos', cid + '.jsonl')
        if not os.path.exists(p):
            self.send_response(404); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"Not found"}'); return
        msgs = []
        with open(p) as f:
            for line in f:
                line = line.strip()
                if not line: continue
                try: e = json.loads(line)
                except: continue
                if e.get('user_msg'):
                    msgs.append({'role': 'user', 'content': e.get('user_msg', '')})
                if e.get('reply'):
                    msgs.append({'role': 'assistant', 'content': e.get('reply', '')})
        self.send_response(200); self._cors(); self.end_headers()
        self.wfile.write(json.dumps({'convo_id': cid, 'messages': msgs}).encode())

    def _handle_capture(self, body):
        tok = self.headers.get('X-Capture-Token', '')
        if tok != CAPTURE_TOKEN:
            self.send_response(401); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"Unauthorized"}'); return
        claude_id = str(body.get('claude_id', '')).replace('..', '').replace('/', '')
        if not claude_id:
            self.send_response(400); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"Missing claude_id"}'); return
        cid = 'cap' + claude_id
        incoming_msgs = body.get('messages', [])
        title = body.get('title', 'Untitled')
        os.makedirs(ADMIN_CONVS, exist_ok=True)
        path = os.path.join(ADMIN_CONVS, cid + '.json')
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        if os.path.exists(path):
            try:
                with open(path) as f: conv = json.load(f)
            except:
                conv = {}
        else:
            conv = {}
        stored_msgs = conv.get('messages', [])
        existing_keys = set((m.get('role',''), m.get('content','')) for m in stored_msgs)
        merged = list(stored_msgs)
        for m in incoming_msgs:
            key = (m.get('role',''), m.get('content',''))
            if key not in existing_keys:
                merged.append(m)
                existing_keys.add(key)
        conv['id'] = cid
        conv['title'] = title
        conv['model'] = 'deepseek/deepseek-v4-pro-0813'
        conv['messages'] = merged
        conv['updated_at'] = now
        if 'created_at' not in conv:
            conv['created_at'] = now
        with open(path, 'w') as f:
            json.dump(conv, f, indent=2)
        idx = os.path.join(ADMIN_CONVS, 'index.json')
        index = []
        if os.path.exists(idx):
            try:
                with open(idx) as f: index = json.load(f)
            except: pass
        entry = next((x for x in index if x.get('id') == cid), None)
        if entry:
            entry.update({'title': title, 'model': 'deepseek/deepseek-v4-pro-0813', 'updated_at': now})
        else:
            index.insert(0, {'id': cid, 'title': title, 'model': 'deepseek/deepseek-v4-pro-0813',
                              'created_at': now, 'updated_at': now})
        with open(idx, 'w') as f: json.dump(index, f, indent=2)
        self.send_response(200); self._cors(); self.end_headers()
        self.wfile.write(b'{"ok":true}')

    def _handle_admin_conv_delete(self, body):
        tok = self.headers.get('X-Admin-Token', '')
        if not valid_token(tok):
            self.send_response(401); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"Unauthorized"}'); return
        cid = body.get('id', '').replace('..', '').replace('/', '')
        if not cid:
            self.send_response(400); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"Missing id"}'); return
        p = os.path.join(ADMIN_CONVS, cid + '.json')
        if os.path.exists(p):
            os.remove(p)
        idx = os.path.join(ADMIN_CONVS, 'index.json')
        index = []
        if os.path.exists(idx):
            try:
                with open(idx) as f: index = json.load(f)
            except: pass
        index = [x for x in index if x.get('id') != cid]
        with open(idx, 'w') as f: json.dump(index, f, indent=2)
        self.send_response(200); self._cors(); self.end_headers()
        self.wfile.write(b'{"success":true}')

    def _handle_admin_conv_rename(self, body):
        tok = self.headers.get('X-Admin-Token', '')
        if not valid_token(tok):
            self.send_response(401); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"Unauthorized"}'); return
        cid = body.get('id', '').replace('..', '').replace('/', '')
        title = (body.get('title') or '').strip()
        if not cid or not title:
            self.send_response(400); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"Missing id or title"}'); return
        p = os.path.join(ADMIN_CONVS, cid + '.json')
        if os.path.exists(p):
            try:
                with open(p) as f: conv = json.load(f)
                conv['title'] = title
                with open(p, 'w') as f: json.dump(conv, f, indent=2)
            except: pass
        idx = os.path.join(ADMIN_CONVS, 'index.json')
        index = []
        if os.path.exists(idx):
            try:
                with open(idx) as f: index = json.load(f)
            except: pass
        for x in index:
            if x.get('id') == cid:
                x['title'] = title
        with open(idx, 'w') as f: json.dump(index, f, indent=2)
        self.send_response(200); self._cors(); self.end_headers()
        self.wfile.write(b'{"success":true}')

    def _handle_admin_import(self, body):
        tok = self.headers.get('X-Admin-Token', '')
        if not valid_token(tok):
            self.send_response(401); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"Unauthorized"}'); return
        raw   = body.get('raw', '')
        title = body.get('title', '').strip()
        if not raw.strip():
            self.send_response(400); self._cors(); self.end_headers()
            self.wfile.write(b'{"error":"Empty paste"}'); return
        import re as _re
        # Strip known claude.ai UI artifacts line-by-line
        junk = {'show more','pasted','copy','retry','edit','share'}
        raw_lines = []
        prev = None
        for ln in raw.split('\n'):
            s = ln.strip()
            if s.lower() in junk:
                continue
            if s and s == prev:  # drop consecutive duplicate lines
                continue
            raw_lines.append(ln)
            if s:
                prev = s
        cleaned = '\n'.join(raw_lines)
        # Look for explicit turn markers at line start
        marker = _re.compile(r'^\s*(ME|YOU|USER|HUMAN|AI|ASSISTANT|CLAUDE)\s*:',
                             _re.IGNORECASE)
        user_words = {'me','you','user','human'}
        messages = []
        has_markers = any(marker.match(l) for l in cleaned.split('\n'))
        if has_markers:
            cur_role = 'user'
            cur_buf = []
            for line in cleaned.split('\n'):
                m = marker.match(line)
                if m:
                    if cur_buf:
                        messages.append({'role': cur_role,
                                         'content': '\n'.join(cur_buf).strip()})
                        cur_buf = []
                    tag = m.group(1).lower()
                    cur_role = 'user' if tag in user_words else 'assistant'
                    rest = line[m.end():].strip()
                    if rest:
                        cur_buf.append(rest)
                else:
                    cur_buf.append(line)
            if cur_buf:
                messages.append({'role': cur_role,
                                 'content': '\n'.join(cur_buf).strip()})
        else:
            # Fallback: blank-line blocks, alternating (imperfect)
            blocks = [b.strip() for b in cleaned.split('\n\n') if b.strip()]
            role = 'user'
            for b in blocks:
                messages.append({'role': role, 'content': b})
                role = 'assistant' if role == 'user' else 'user'
        messages = [m for m in messages if m['content']]
        if not messages:
            messages = [{'role': 'user', 'content': raw.strip()}]
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        cid = 'adm_' + str(int(time.time())) + '_' + secrets.token_hex(3)
        conv = {
            'id':         cid,
            'title':      title or (messages[0]['content'][:55] if messages else 'Imported'),
            'model':      'imported',
            'messages':   messages,
            'created_at': now,
            'updated_at': now
        }
        os.makedirs(ADMIN_CONVS, exist_ok=True)
        with open(os.path.join(ADMIN_CONVS, cid + '.json'), 'w') as f:
            json.dump(conv, f, indent=2)
        idx = os.path.join(ADMIN_CONVS, 'index.json')
        index = []
        if os.path.exists(idx):
            try:
                with open(idx) as f: index = json.load(f)
            except: pass
        index.insert(0, {'id': cid, 'title': conv['title'],
                         'model': 'imported', 'created_at': now, 'updated_at': now})
        with open(idx, 'w') as f: json.dump(index, f, indent=2)
        self.send_response(200); self._cors(); self.end_headers()
        self.wfile.write(json.dumps({'ok': True, 'id': cid,
                         'message_count': len(messages)}).encode())

    def _cors(self):
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, X-Admin-Token')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')


if __name__ == '__main__':
    print(f'Order server on :{PORT}')
    http.server.ThreadingHTTPServer(('', PORT), Handler).serve_forever()
