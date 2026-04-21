#!/usr/bin/env python3
"""
HKMA Stablecoin News Monitor
Check for updates on HKMA stablecoin issuer regulation page
"""

import urllib.request
import json
import re
from datetime import datetime

URL = "https://www.hkma.gov.hk/eng/key-functions/international-financial-centre/stablecoin-issuers/"
REGISTER_URL = "https://www.hkma.gov.hk/eng/regulatory-resources/registers/register-of-licensed-stablecoin-issuers/"
PRESSEES_URL = "https://www.hkma.gov.hk/eng/news-and-media/press-releases/"
STATE_FILE = "/home/hermesagentsrv/workspace/obsidian-vault/.hkma_stablecoin_state.json"

def fetch_page(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return resp.read().decode("utf-8")

def extract_press_releases(html):
    """Extract press release dates and titles"""
    pattern = r'<li[^>]*>(\d{2}\s\w{3}\s\d{4})\s*<a[^>]*>([^<]+)</a>'
    matches = re.findall(pattern, html)
    return [(date.strip(), title.strip()) for date, title in matches[:20]]

def extract_last_revision(html):
    """Extract last revision date"""
    match = re.search(r'Last revision date\s*:\s*(\d{1,2}\s+\w+\s+\d{4})', html)
    return match.group(1) if match else None

def load_state():
    try:
        with open(STATE_FILE) as f:
            return json.load(f)
    except:
        return {"last_press_releases": [], "last_revision": None}

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)

def main():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] Checking HKMA Stablecoin updates...")
    
    html = fetch_page(URL)
    register_html = fetch_page(REGISTER_URL)
    
    press_releases = extract_press_releases(register_html)
    last_revision = extract_last_revision(register_html)
    
    state = load_state()
    
    new_releases = []
    for pr in press_releases:
        if pr not in state["last_press_releases"]:
            new_releases.append(pr)
    
    changes = []
    
    if new_releases:
        changes.append(f"🆕 NEW PRESS RELEASES ({len(new_releases)}):")
        for date, title in new_releases:
            changes.append(f"   - {date}: {title}")
        state["last_press_releases"] = press_releases
    
    if last_revision and last_revision != state.get("last_revision"):
        changes.append(f"📝 Register revision updated: {last_revision}")
        state["last_revision"] = last_revision
    
    save_state(state)
    
    if changes:
        print("\n".join(changes))
        return "\n".join(changes)
    else:
        print("No new updates found.")
        return None

if __name__ == "__main__":
    result = main()
    if result:
        print(f"\n--- UPDATE DETECTED ---")
