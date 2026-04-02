# Python : Tout est Objet — Mutable, Immutable, et Comment Ça Marche

---

## Introduction

Si tu apprends Python, un des concepts les plus fondamentaux à maîtriser est celui-ci : **tout en Python est un objet**. Les entiers, les chaînes de caractères, les listes, les fonctions — tout est objet. Comprendre ce que ça signifie, et surtout comprendre la différence entre les objets **mutables** et **immutables**, te sauvera des heures de débogage douloureux. Dans cet article, je vais te guider à travers tout ce que j'ai appris sur les objets Python : ce qu'ils sont, comment Python les gère en mémoire, et comment ils se comportent quand on les passe à des fonctions.

---

## id() et type()

Chaque objet en Python possède trois choses :
- Une **valeur**
- Un **type**
- Une **identité** (un ID unique en mémoire)

Python nous fournit deux fonctions built-in pour inspecter les objets :

```python
x = 42
print(type(x))   # <class 'int'>
print(id(x))     # ex: 140234567891234
```

`type()` te dit de quel type est l'objet. `id()` retourne l'adresse mémoire de l'objet (dans CPython, l'implémentation de référence). Deux variables avec le même `id()` pointent vers exactement le même objet en mémoire.

```python
a = [1, 2, 3]
b = a
print(id(a) == id(b))  # True — même objet !
```

---

## Les Objets Mutables

Un objet **mutable** peut être modifié **en place** après sa création. L'objet garde la même identité (même `id()`), mais son contenu change.

Les types mutables built-in sont :
- `list`
- `dict`
- `set`
- `bytearray`

```python
lst = [1, 2, 3]
print(id(lst))      # ex: 140234567891234

lst.append(4)
print(lst)          # [1, 2, 3, 4]
print(id(lst))      # 140234567891234 — même objet !
```

C'est là que les **alias** peuvent te piéger. Quand deux variables pointent vers le même objet mutable, modifier l'une affecte l'autre :

```python
a = [1, 2, 3]
b = a            # b est un alias de a

b.append(4)
print(a)         # [1, 2, 3, 4] — a est affecté !
```

Si tu veux une copie indépendante, utilise `.copy()` ou le slicing :

```python
b = a.copy()     # ou : b = a[:]
b.append(99)
print(a)         # [1, 2, 3, 4] — non affecté
```

---

## Les Objets Immutables

Un objet **immutable** ne peut pas être modifié après sa création. Toute opération qui semble le "modifier" crée en réalité un **nouvel objet**.

Les types immutables built-in sont :
- `int`
- `float`
- `str`
- `tuple`
- `bool`
- `bytes`
- `frozenset`

```python
s = "hello"
print(id(s))     # ex: 140234567891234

s = s + " world"
print(id(s))     # différent ! un nouvel objet a été créé
```

```python
x = 42
x += 1
# Cela ne modifie PAS 42 en place.
# Cela crée un nouvel objet 43 et réassigne x à celui-ci.
print(x)         # 43
```

**Optimisation CPython — le cache des entiers :**
CPython met en cache les petits entiers de **-5 à 256**. Cela signifie que toute variable pointant vers `1` pointe vers le même objet :

```python
a = 1
b = 1
print(a is b)    # True — même objet en cache
```

Mais pour les grands entiers :
```python
a = 1000
b = 1000
print(a is b)    # False — deux objets différents
```

---

## Pourquoi C'est Important ? Comment Python Traite Différemment les Objets Mutables et Immutables

La distinction entre mutable et immutable a de vraies conséquences dans ton code.

**Les objets immutables sont sûrs à partager.** Puisqu'ils ne peuvent pas être modifiés, Python peut les réutiliser librement (comme le cache des entiers, ou l'interning des strings). Tu n'auras jamais d'effets de bord inattendus.

**Les objets mutables demandent de la prudence.** Quand tu partages un objet mutable entre plusieurs variables ou entre différents scopes, toute modification est visible depuis toutes les références :

```python
a = [1, 2, 3]
b = a

b[0] = 99
print(a)         # [99, 2, 3] — a est aussi affecté !
```

L'opérateur `+=` se comporte aussi différemment selon la mutabilité :

```python
# List (mutable) : += modifie en place
a = [1, 2, 3]
print(id(a))     # ex: 140234567891234
a += [4]
print(id(a))     # pareil ! modifié en place

# Int (immutable) : += crée un nouvel objet
x = 10
print(id(x))     # ex: 140234567891456
x += 1
print(id(x))     # différent ! nouvel objet créé
```

---

## Comment les Arguments sont Passés aux Fonctions

Python utilise un modèle appelé **"passage par référence d'objet"** (aussi appelé *passage par assignation*). Ce n'est ni du passage par valeur pur, ni du passage par référence pur.

> **La fonction reçoit une copie de la référence** vers l'objet.

Cela a des implications différentes selon que l'objet est mutable ou immutable.

### Avec des objets immutables

```python
def increment(n):
    n += 1        # crée un nouvel objet localement
    print(n)      # 11

x = 10
increment(x)
print(x)          # 10 — inchangé !
```

Puisque `int` est immutable, `n += 1` crée un nouvel objet. La variable locale `n` pointe maintenant vers un nouvel objet, mais `x` dans le scope extérieur est intact.

### Avec des objets mutables

```python
def add_item(lst):
    lst.append(99)   # modifie l'objet en place

a = [1, 2, 3]
add_item(a)
print(a)             # [1, 2, 3, 99] — modifié !
```

Puisque `list` est mutable et que la fonction reçoit une référence vers le **même objet**, les modifications à l'intérieur de la fonction sont visibles à l'extérieur.

### Réassigner un objet mutable à l'intérieur d'une fonction

```python
def replace(lst):
    lst = [9, 9, 9]  # réassigne uniquement la variable LOCALE

a = [1, 2, 3]
replace(a)
print(a)             # [1, 2, 3] — inchangé !
```

Réassigner `lst` à l'intérieur de la fonction change uniquement la référence locale. Cela n'affecte **pas** `a` dans le scope extérieur.

### Tableau récapitulatif

| Type d'objet | Opération dans la fonction | Effet sur l'original |
|---|---|---|
| Immutable | `n += 1` | Aucun effet |
| Mutable | `lst.append(x)` | Modifié |
| Mutable | `lst = [...]` |  Aucun effet (réassignation locale) |

---

## Conclusion

Comprendre comment Python gère les objets en mémoire n'est pas que théorique — cela affecte directement la façon dont tu écris des fonctions, partages des données et débogues un comportement inattendu. Les points clés à retenir :

- Tout en Python est un objet avec un type, une valeur et une identité.
- Utilise `type()` pour vérifier le type, `id()` pour vérifier l'adresse mémoire.
- Utilise `==` pour comparer les valeurs, `is` pour vérifier si deux variables pointent vers le même objet.
- Les objets **mutables** (list, dict, set) peuvent être modifiés en place — fais attention aux alias.
- Les objets **immutables** (int, str, tuple) créent toujours de nouveaux objets lors d'une modification.
- Les fonctions reçoivent une copie de la référence — les objets mutables peuvent être modifiés à l'intérieur des fonctions, les immutables non.

Maîtrise ces concepts et tu écriras un code Python plus propre, plus sûr et plus prévisible.
