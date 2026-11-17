// firebase-init.js
// Config firebase-config.js içinde (gitignore'da). Örnek: firebase-config.example.js

// Modüler değil, "compat" SDK kullanıyoruz — build aracı olmadan <script> tag'iyle
// çalışsın diye. Basit statik siteler için en az sürtünmeli yol bu.
firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const db = firebase.firestore();

// Her ziyaretçiye görünmez, anonim bir kimlik ver. Bu sayede Firestore
// güvenlik kuralları "bu istek gerçekten bu odanın oyuncusundan mı geliyor"
// diye request.auth.uid ile kontrol edebiliyor.
function ensureSignedIn() {
  return new Promise((resolve, reject) => {
    auth.onAuthStateChanged(user => {
      if (user) { resolve(user); return; }
      auth.signInAnonymously().catch(reject);
    });
  });
}
