# Forma Hafızası

Futbol formalarından takım/oyuncu tahmin oyunu. Tek kişilik mod ve gerçek zamanlı **düello** modu (`/duello`) içerir.

## Teknoloji
- Statik site (HTML/JS), Firebase Hosting
- Firestore + anonim Auth (düello odaları)
- Veri: `public/data/*.json` (`export_to_json.py` ile üretilir)

## Kurulum
1. Firebase projesi oluştur, Firestore ve Anonymous Auth'u aç.
2. `cp public/js/firebase-config.example.js public/js/firebase-config.js` ve değerleri doldur.
3. `firebase deploy` (hosting + firestore rules).

Yerel test: `firebase emulators:start` veya `python3 -m http.server -d public`.
