import requests
import re
import sys

handles = [
    "@UOLEsporte", "@FootureFC", "@ESPNBrasil", "@TNTSportsBR", "@jozanovalis",
    "@SudacaBrasil", "@dwkickoff", "@CazeTV", "@NossoFutebol", "@CanalGOAT",
    "@FabrizioRomano", "@SkySportsFootball", "@ESPNFC", "@LaLiga", "@seriea",
    "@premierleague", "@bundesliga", "@TyCSports", "@ESPNArgentina",
    "@CBSSportsGolazo", "@tudn_usa", "@SPL", "@SSCSports", "@JLEAGUEInternational",
    "@KLEAGUE", "@jovempanesportes", "@getv", "@walacevborges", "@CanaldoVSR",
    "@BrunoFormiga", "@canaldojorgeiggor", "@MarceloBechler1", "@FredCaldeira",
    "@TatiMantovani", "@claraalbuquerque", "@arthurquezada", "@daznwomensfootball"
]

def get_channel_id(handle):
    url = f"https://www.youtube.com/{handle}"
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}
        r = requests.get(url, headers=headers, timeout=15)
        if r.status_code == 200:
            match = re.search(r'UC[a-zA-Z0-9_-]{22}', r.text)
            if match:
                return match.group(0)
    except Exception as e:
        pass
    return None

results = {}
for h in handles:
    cid = get_channel_id(h)
    results[h] = cid
    print(f"{h}: {cid}")

import json
with open("yt_mapping.json", "w") as f:
    json.dump(results, f, indent=2)
