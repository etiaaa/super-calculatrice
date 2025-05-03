# Plan de test

## calculate/operators.py
- ✅ addition, substraction, multiplication, division
- 🧪 Cas normaux et limites (ex: division par 0, erreurs de syntaxe)
- ➕ Ajouts : modulo, puissance

## calculate/view.py
- ❌ Mock de `input()` et `print()` requis
- 🧪 Tests des fonctions statiques

## calculate/controller.py
- 🔁 `_is_input_valid`, `_is_quit`, `_operations`
- 🎭 Utilisation de pytest-mock
