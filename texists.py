import threading
from pathlib import Path

class Texists:
    def __init__(self):
        pass
    def exists(self, p, timeout=1):
        share_result = [False,]
        def check():
            try:
                if Path(p).exists():
                    share_result[0] = True
            except Exception:
                pass
        t = threading.Thread(target=check, daemon=True)
        t.start()
        t.join(timeout)
        return share_result[0]
