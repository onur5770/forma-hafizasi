"""
export_to_json.py
Eski akış: scrape -> pandas -> CSV -> phpMyAdmin'e SQL import
Yeni akış:  scrape -> pandas -> bu script -> public/data/*.json -> firebase deploy

Girdi olarak player_rows bekleniyor: (player_name, team_id, team_name) üçlüleri.
Kendi scraping/pandas kodunun ürettiği DataFrame'i buraya uyarlaman yeterli.
"""

import json
from itertools import combinations
from collections import defaultdict
from build_league_map import LEAGUE_MAP  # {team_id: "Türkiye"/"İngiltere"/... } — yeni takım eklersen oraya bir satır ekle, buradan otomatik okunur

# ÖRNEK veri — kendi gerçek verinle değiştir
player_rows = [
    ("Wesley Sneijder", "gs", "Galatasaray"),
    ("Wesley Sneijder", "inter", "Inter"),
    ("Wesley Sneijder", "real", "Real Madrid"),
    ("Didier Drogba", "gs", "Galatasaray"),
    ("Didier Drogba", "chelsea", "Chelsea"),
]

teams_seen = {}
teams_by_player = defaultdict(dict)  # player_name -> {team_id: team_name}

for name, team_id, team_name in player_rows:
    teams_seen[team_id] = team_name
    teams_by_player[name][team_id] = team_name

# ---- teams.json ----
teams_json = [
    {"id": tid, "name": tname, "league": LEAGUE_MAP.get(tid, "Diğer")}
    for tid, tname in teams_seen.items()
]

# ---- players.json (autocomplete için sadece isim listesi yeterli) ----
players_json = sorted(teams_by_player.keys())

# ---- team_pairs.json (asıl soru bankası) ----
pair_map = {}
for player_name, teams in teams_by_player.items():
    items = sorted(teams.items())  # [(team_id, team_name), ...]
    for (id_a, name_a), (id_b, name_b) in combinations(items, 2):
        key = (id_a, id_b)
        if key not in pair_map:
            pair_map[key] = {
                "team1_id": id_a, "team1_name": name_a,
                "team2_id": id_b, "team2_name": name_b,
                "team1_league": LEAGUE_MAP.get(id_a, "Diğer"),
                "team2_league": LEAGUE_MAP.get(id_b, "Diğer"),
                "answers": []
            }
        pair_map[key]["answers"].append(player_name)

team_pairs_json = list(pair_map.values())

# ---- Dosyaları yaz ----
with open("public/data/teams.json", "w", encoding="utf-8") as f:
    json.dump(teams_json, f, ensure_ascii=False, indent=2)

with open("public/data/players.json", "w", encoding="utf-8") as f:
    json.dump(players_json, f, ensure_ascii=False, indent=2)

with open("public/data/team_pairs.json", "w", encoding="utf-8") as f:
    json.dump(team_pairs_json, f, ensure_ascii=False, indent=2)

print(f"{len(teams_json)} takım, {len(players_json)} oyuncu, {len(team_pairs_json)} takım çifti yazıldı.")
unmapped = [t["name"] for t in teams_json if t["league"] == "Diğer"]
if unmapped:
    print(f"UYARI: {len(unmapped)} takımın lig bilgisi build_league_map.py içinde yok, 'Diğer' olarak işaretlendi:")
    for name in unmapped:
        print("  -", name)
print("Şimdi: firebase deploy --only hosting")
