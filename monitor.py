#!/usr/bin/env python3
import json, sys, time, urllib.request
from pathlib import Path

def check(url):
    started=time.time()
    try:
        with urllib.request.urlopen(url, timeout=10) as r:
            return {'url':url,'status':r.status,'latency_ms':round((time.time()-started)*1000,2)}
    except Exception as e:
        return {'url':url,'status':'error','error':str(e)}
if __name__=='__main__':
    targets=json.loads(Path(sys.argv[1]).read_text()) if len(sys.argv)>1 else []
    print(json.dumps([check(u) for u in targets], indent=2))
