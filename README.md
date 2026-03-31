# holbertonschool-higher_level_programming
exercise foun

# Guide complet — JavaScript DOM Manipulation

## Sommaire

1. [Les bases du DOM](#1-les-bases-du-dom)
2. [Sélectionner des éléments](#2-sélectionner-des-éléments)
3. [Modifier le style](#3-modifier-le-style)
4. [Modifier le contenu](#4-modifier-le-contenu)
5. [Modifier le DOM](#5-modifier-le-dom)
6. [Les événements](#6-les-événements)
7. [Les requêtes réseau](#7-les-requêtes-réseau)
8. [Récapitulatif des exercices](#8-récapitulatif-des-exercices)
9. [Règles semistandard](#9-règles-semistandard)

---

## 1. Les bases du DOM

Le DOM (Document Object Model) est la représentation de la page HTML sous forme d'objets JavaScript. Il permet de lire et modifier la page sans la recharger.

```
document
└── html
    ├── head
    └── body
        ├── header
        ├── div
        └── footer
```

Le point d'entrée est toujours `document`.

---

## 2. Sélectionner des éléments

### Par balise
```js
document.querySelector('header');       // 1er header trouvé
document.querySelectorAll('li');        // tous les li
```

### Par ID (unique sur la page)
```js
document.querySelector('#monId');
document.getElementById('monId');
```

### Par classe (plusieurs éléments)
```js
document.querySelector('.maClasse');    // le 1er
document.querySelectorAll('.maClasse'); // tous
```

### Tableau récapitulatif

| Sélecteur | Syntaxe | Retourne |
|---|---|---|
| Balise | `'header'` | 1 élément |
| ID | `'#red_header'` | 1 élément |
| Classe | `'.my_list'` | 1 ou plusieurs |

---

## 3. Modifier le style

### Directement via `.style`
```js
document.querySelector('header').style.color = '#FF0000';
document.querySelector('header').style.backgroundColor = 'blue';
```

### Via les classes CSS (meilleure pratique)
```js
const el = document.querySelector('header');

el.classList.add('red');          // ajoute la classe
el.classList.remove('red');       // supprime la classe
el.classList.toggle('red');       // ajoute si absente, supprime si présente
el.classList.contains('red');     // retourne true/false
el.classList.replace('red', 'green'); // remplace une classe par une autre
```

---

## 4. Modifier le contenu

```js
const el = document.querySelector('header');

// Lire
console.log(el.textContent); // texte brut
console.log(el.innerHTML);   // texte + HTML

// Modifier
el.textContent = 'New Header!!!';          // texte brut
el.innerHTML = '<strong>Gras</strong>';    // avec HTML
```

---

## 5. Modifier le DOM

```js
// Créer un élément
const li = document.createElement('li');
li.textContent = 'Item';

// Ajouter à la fin d'un élément parent
document.querySelector('.my_list').appendChild(li);

// Supprimer un élément
document.querySelector('#monElement').remove();
```

---

## 6. Les événements

### Événement utilisateur (clic, frappe...)
```js
document.querySelector('#btn').addEventListener('click', function () {
  // code exécuté au clic
});
```

### Événement DOM (chargement de la page)
```js
// Indispensable quand le script est dans le <head>
document.addEventListener('DOMContentLoaded', function () {
  // le DOM est prêt, on peut accéder aux éléments
});
```

### Différence clé

| Type | Déclenché par | Exemple |
|---|---|---|
| Événement DOM | Le navigateur | `DOMContentLoaded` |
| Événement utilisateur | L'utilisateur | `click`, `input`, `mouseover` |

---

## 7. Les requêtes réseau

### Fetch API (méthode moderne)
```js
fetch('https://api.example.com/data')
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    document.querySelector('#result').textContent = data.name;
  });
```

### XMLHttpRequest (ancienne méthode)
```js
const xhr = new XMLHttpRequest();
xhr.open('GET', 'https://api.example.com/data');
xhr.onload = function () {
  const data = JSON.parse(xhr.responseText);
  console.log(data);
};
xhr.send();
```

> Toujours préférer **Fetch** pour les nouveaux projets.

---

## 8. Récapitulatif des exercices

### 0-script.js — Changer la couleur du header
```js
document.querySelector('header').style.color = '#FF0000';
```
Concept : sélection par balise + modification de style.

---

### 1-script.js — Changer la couleur au clic
```js
document.querySelector('#red_header').addEventListener('click', function () {
  document.querySelector('header').style.color = '#FF0000';
});
```
Concept : événement utilisateur `click`.

---

### 2-script.js — Ajouter une classe au clic
```js
document.querySelector('#red_header').addEventListener('click', function () {
  document.querySelector('header').classList.add('red');
});
```
Concept : `classList.add()` — meilleure pratique que modifier `style` directement.

---

### 3-script.js — Basculer entre deux classes
```js
document.querySelector('#toggle_header').addEventListener('click', function () {
  const header = document.querySelector('header');
  if (header.classList.contains('red')) {
    header.classList.replace('red', 'green');
  } else {
    header.classList.replace('green', 'red');
  }
});
```
Concept : `classList.contains()` + `classList.replace()` — toujours une classe, jamais les deux.

---

### 4-script.js — Ajouter un élément à une liste
```js
document.querySelector('#add_item').addEventListener('click', function () {
  const li = document.createElement('li');
  li.textContent = 'Item';
  document.querySelector('.my_list').appendChild(li);
});
```
Concept : `createElement()` + `appendChild()`.

---

### 5-script.js — Mettre à jour le contenu d'un élément
```js
document.querySelector('#update_header').addEventListener('click', function () {
  document.querySelector('header').textContent = 'New Header!!!';
});
```
Concept : `textContent` pour modifier le texte.

---

### 6-script.js — Fetch d'un personnage Star Wars
```js
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    document.querySelector('#character').textContent = data.name;
  });
```
Concept : Fetch API + affichage d'une donnée JSON.

---

### 7-script.js — Fetch et liste de films Star Wars
```js
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    data.results.forEach(function (movie) {
      const li = document.createElement('li');
      li.textContent = movie.title;
      document.querySelector('#list_movies').appendChild(li);
    });
  });
```
Concept : Fetch + boucle `forEach` + création dynamique d'éléments.

---

### 8-script.js — Fetch depuis le `<head>`
```js
document.addEventListener('DOMContentLoaded', function () {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      document.querySelector('#hello').textContent = data.hello;
    });
});
```
Concept : `DOMContentLoaded` — obligatoire quand le script est dans le `<head>` car le DOM n'est pas encore chargé.

---

## 9. Règles semistandard

| Règle | Correct | Incorrect |
|---|---|---|
| Pas de `var` | `const` / `let` | `var` |
| Espace avant `function ()` | `function ()` | `function()` |
| Espace avant `{` | `function () {` | `function () {` |
| Indentation 2 espaces | `  code` | `    code` |
| Point-virgule obligatoire | `console.log('a');` | `console.log('a')` |
| Newline à la fin du fichier | ✅ | ❌ |

### Corriger automatiquement
```bash
semistandard --fix monFichier.js
semistandard monFichier.js  # vérifier (aucune sortie = OK)
```
