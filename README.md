# Forma Hafızası

Futbol bilgi oyunu (3-2-1 tarzı). Ekranda iki takım çıkar; ikisinde de forma giymiş ortak bir oyuncuyu bulmaya çalışırsın.

## Modlar
- **Tek kişilik:** Rastgele iki takım, ortak oyuncuyu tahmin et. Bilemezsen pas geç.
- **Düello (`/duello`):** Arkadaşınla ya da hızlı eşleşmeyle oyna. Sırayla birer takım seçilir, ikiniz de ortak oyuncuyu bulmaya çalışırsınız; önce bilen puanı alır. Klasik mod: 5 round, 30 sn takım seçimi, 30 sn tahmin.

## Teknoloji
- Statik site (HTML/JS), Firebase Hosting
- Firestore + anonim Auth (düello odaları)
- Veri: `public/data/*.json`, Transfermarkt (Kaggle açık veri seti) kaynaklı, `export_to_json.py` ile üretilir. Kısa süreli/kiralık bazı transferler eksik olabilir.

## Kurulum
1. Firebase projesi oluştur, Firestore ve Anonymous Auth'u aç.
2. `cp public/js/firebase-config.example.js public/js/firebase-config.js` ve değerleri doldur.
3. `firebase deploy` (hosting + firestore rules).

Yerel test: `python3 -m http.server -d public`
