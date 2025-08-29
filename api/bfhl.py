
from http.server import BaseHTTPRequestHandler
import json
import re

# ----- Hardcoded user info (as requested) -----
USER_ID = "yash_singhal_19092004"
EMAIL = "singhalyash340@gmail.com"
ROLL = "22BCE0807"

NUMERIC = re.compile(r"^-?\d+$")
ALPHA = re.compile(r"^[A-Za-z]+$")

def _alt_caps_reversed(s: str) -> str:
    r = s[::-1]
    out = []
    for i, ch in enumerate(r):
        out.append(ch.upper() if i % 2 == 0 else ch.lower())
    return "".join(out)

class handler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200, content_type="application/json"):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers(204)

    def do_POST(self):
        try:
            length = int(self.headers.get("content-length", "0"))
            raw = self.rfile.read(length) if length > 0 else b""
            payload = json.loads(raw.decode("utf-8") or "{}")
        except Exception:
            self._set_headers(400)
            self.wfile.write(json.dumps({"is_success": False, "message": "Invalid JSON"}).encode("utf-8"))
            return

        data = payload.get("data")
        if not isinstance(data, list):
            self._set_headers(400)
            self.wfile.write(json.dumps({"is_success": False, "message": "Invalid payload: missing 'data' array"}).encode("utf-8"))
            return

        odd, even, alphabets, specials = [], [], [], []
        total = 0
        letters = []

        for item in data:
            s = "" if item is None else str(item)
            if NUMERIC.match(s):
                try:
                    n = int(s)
                    total += n
                    (even if n % 2 == 0 else odd).append(s)
                except Exception:
                    specials.append(s)
            elif ALPHA.match(s):
                alphabets.append(s.upper())
                letters.append(s)
            else:
                specials.append(s)
                # include embedded letters for concat rule
                letters.append("".join([c for c in s if c.isalpha()]))

        concat_letters = "".join(letters)
        result = {
            "is_success": True,
            "user_id": USER_ID,
            "email": EMAIL,
            "roll_number": ROLL,
            "odd_numbers": odd,
            "even_numbers": even,
            "alphabets": alphabets,
            "special_characters": specials,
            "sum": str(total),
            "concat_string": _alt_caps_reversed(concat_letters),
        }

        self._set_headers(200)
        self.wfile.write(json.dumps(result).encode("utf-8"))
