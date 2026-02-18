1 expliquer Expliquer HTTP vs HTTPS
HTTP et HTTPS sont des protocoles de communication web.

HTTP : 
- Données non sécurisées (en clair)
- N'importe qui peut les lire
- Port 80

HTTPS :
- Données chiffrées avec SSL/TLS
- Sécurisé contre les espions
- Port 443
- Utilisé pour les sites sensibles (banques, e-commerce)

La différence principale : HTTPS protège vos données avec du chiffrement.


Aspects de Sécurité
Que protège HTTPS ?

Confidentialité : Les données sont illisibles pour les espions
Intégrité : Les données ne peuvent pas être modifiées sans détection
Authentification : Vérifie que vous communiquez avec le bon serveur


2. Structure des Requêtes et Réponses HTTP
Structure d'une Requête HTTP
┌─────────────────────────────────────────────────────────────────┐
│                     REQUÊTE HTTP                                │
├─────────────────────────────────────────────────────────────────┤
│ 1. LIGNE DE REQUÊTE (Request Line)                             │
│    GET /api/users HTTP/1.1                                      │
│    └─┬─┘ └────┬────┘ └───┬───┘                                │
│      │        │           └─ Version HTTP                       │
│      │        └─ Chemin (path)                                  │
│      └─ Méthode HTTP                                            │
├─────────────────────────────────────────────────────────────────┤
│ 2. EN-TÊTES (Headers)                                           │
│    Host: api.example.com                                        │
│    User-Agent: Mozilla/5.0 (Windows NT 10.0)                   │
│    Accept: application/json                                     │
│    Accept-Language: fr-FR,fr;q=0.9                             │
│    Content-Type: application/json                               │
│    Authorization: Bearer eyJhbGciOiJIUzI1NiIs...               │
│    Cookie: session_id=abc123                                    │
├─────────────────────────────────────────────────────────────────┤
│ 3. LIGNE VIDE (obligatoire)                                     │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│ 4. CORPS (Body) - Optionnel, uniquement pour POST/PUT/PATCH    │
│    {                                                            │
│      "nom": "Alice",                                            │
│      "email": "alice@example.com"                               │
│    }                                                            │
└─────────────────────────────────────────────────────────────────┘
Structure d'une Réponse HTTP
┌─────────────────────────────────────────────────────────────────┐
│                     RÉPONSE HTTP                                │
├─────────────────────────────────────────────────────────────────┤
│ 1. LIGNE DE STATUT (Status Line)                               │
│    HTTP/1.1 200 OK                                              │
│    └───┬───┘ └┬┘ └┬┘                                          │
│        │      │   └─ Phrase de statut                          │
│        │      └─ Code de statut                                │
│        └─ Version HTTP                                          │
├─────────────────────────────────────────────────────────────────┤
│ 2. EN-TÊTES (Headers)                                           │
│    Date: Wed, 18 Feb 2026 10:00:00 GMT                         │
│    Server: nginx/1.18.0                                         │
│    Content-Type: application/json; charset=utf-8                │
│    Content-Length: 348                                          │
│    Connection: keep-alive                                       │
│    Cache-Control: no-cache                                      │
│    Set-Cookie: session_id=xyz789; HttpOnly; Secure             │
│    Access-Control-Allow-Origin: *                               │
├─────────────────────────────────────────────────────────────────┤
│ 3. LIGNE VIDE (obligatoire)                                     │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│ 4. CORPS (Body) - Les données retournées                       │
│    {                                                            │
│      "status": "success",                                       │
│      "data": {                                                  │
│        "id": 1,                                                 │
│        "nom": "Alice",                                          │
│        "email": "alice@example.com"                             │
│      }                                                          │
│    }                                                            │
└─────────────────────────────────────────────────────────────────┘

3. Méthodes HTTP Communes
Les 5 Méthodes Principales

4. PATCH - Modifier partiellement une ressource
Description : Modifie SEULEMENT certains champs de la ressource
Cas d'utilisation :

Changer juste l'email d'un utilisateur
Mettre à jour le statut d'une commande

Exemples :
httpPATCH /api/users/5
Body: {
  "email": "newemail@example.com"
}
→ Change SEULEMENT l'email
Réponse typique : 200 OK

5. DELETE - Supprimer une ressource
Description : Supprime la ressource spécifiée
Cas d'utilisation :

Supprimer un compte utilisateur
Retirer un produit du panier

Exemples :
httpDELETE /api/users/5
→ Supprime l'utilisateur 5
Réponse typique : 204 No Content ou 200 OK


Liste A-Méthodes HTTP
1. GET
   Description : Récupère des données
   Cas d'usage : Afficher une page web, récupérer une liste d'utilisateurs
   Exemple : GET /api/users → retourne tous les utilisateurs

2. POST
   Description : Crée de nouvelles données
   Cas d'usage : Créer un compte utilisateur, publier un commentaire
   Exemple : POST /api/users avec {"nom":"Bob"} → crée l'utilisateur Bob

3. PUT
   Description : Remplace complètement une ressource
   Cas d'usage : Mettre à jour tout un profil utilisateur
   Exemple : PUT /api/users/5 → remplace toutes les infos de l'utilisateur 5

4. DELETE
   Description : Supprime une ressource
   Cas d'usage : Supprimer un compte, retirer un produit
   Exemple : DELETE /api/users/5 → supprime l'utilisateur 5

5. PATCH - Modifier partiellement une ressource
Description : Modifie SEULEMENT certains champs de la ressource
Cas d'utilisation :

Changer juste l'email d'un utilisateur
Mettre à jour le statut d'une commande

Exemples :
PATCH /api/users/5
Body: {
  "email": "newemail@example.com"
}
→ Change SEULEMENT l'email



Liste B - Codes de Status
Les Codes les Plus Importants
Catégorie 2xx - Succès 
200 OK
1. 200 OK
   Description : Requête réussie
   Scénario : Vous demandez une liste d'utilisateurs et le serveur vous la renvoie

2. 201 Created
   Description : Ressource créée avec succès
   Scénario : Vous créez un nouveau compte et il est enregistré

3. 404 Not Found
   Description : Ressource non trouvée
   Scénario : Vous tapez une URL qui n'existe pas (page introuvable)

4. 400 Bad Request
   Description : Requête invalide
   Scénario : Vous envoyez du JSON mal formaté au serveur

5. 500 Internal Server Error
   Description : Erreur du serveur
   Scénario : Bug dans le code du serveur, base de données plantée



