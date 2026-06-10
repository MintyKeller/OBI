# 💡 Tips e Truques para OBI

## 1️⃣ Leitura e Saída Eficiente

### Python
```python
# Rápido
a, b = map(int, input().split())

# Múltiplas linhas
for _ in range(n):
    x = int(input())
```

### Java
```java
Scanner sc = new Scanner(System.in);
int a = sc.nextInt();
String linha = sc.nextLine();
```

### C++
```cpp
int a, b;
cin >> a >> b;  // Rápido
// Para entrada muito grande:
ios_base::sync_with_stdio(false);
cin.tie(NULL);
```

### JavaScript
```javascript
const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');
```

---

## 2️⃣ Estruturas de Dados Essenciais

| Operação | Python | Java | C++ | JavaScript |
|----------|--------|------|-----|------------|
| Array | `list` | `ArrayList` | `vector` | `Array` |
| Fila | `deque` | `Queue` | `queue` | `Array` (com índices) |
| Pilha | `deque` | `Stack` | `stack` | `Array` |
| Mapa | `dict` | `HashMap` | `map` | `Object` / `Map` |
| Conjunto | `set` | `HashSet` | `set` | `Set` |

---

## 3️⃣ Algoritmos Clássicos para OBI

### Ordenação
- **Bubble Sort**: O(n²) - muito lento, evite!
- **Merge Sort**: O(n log n) - confiável
- **Quick Sort**: O(n log n) em média
- **Counting Sort**: O(n + k) - para valores limitados

### Busca
- **Busca Linear**: O(n) - simples
- **Busca Binária**: O(log n) - para arrays ordenados

### Dinâmica
- **Fibonacci**: DP clássica
- **Knapsack**: Problema da mochila
- **Moedas**: Mínimo de moedas

### Greedy
- **Seleção de Atividades**: Ordene e escolha
- **Cédulas**: Use a maior nota possível

---

## 4️⃣ Dicas de Implementação

✅ **Sempre:**
- Teste com os exemplos fornecidos
- Verifique edge cases (valores negativos, zero, muito grandes)
- Use tipos de dados adequados (int vs long long em C++)

❌ **Evite:**
- Recursão muito profunda (pode dar stack overflow)
- Arrays muito grandes em memória (use estruturas eficientes)
- Operações O(n²) quando o limite é n = 100,000

---

## 5️⃣ Complexidade de Tempo Aceitável

| Limite | Operações OK |
|--------|-------------|
| n ≤ 10 | O(n!) |
| n ≤ 20 | O(2^n) |
| n ≤ 100 | O(n³) |
| n ≤ 1,000 | O(n² log n) |
| n ≤ 100,000 | O(n log n) |
| n ≤ 1,000,000 | O(n) |

---

## 6️⃣ Debugando Erros Comuns

🔴 **Time Limit Exceeded (TLE)**
- Seu algoritmo é muito lento
- Verifique complexidade
- Use estruturas mais eficientes

🔴 **Wrong Answer (WA)**
- Saída incorreta
- Teste com mais exemplos
- Verifique edge cases

🔴 **Runtime Error**
- Acesso a índice fora dos limites
- Divisão por zero
- Estouro de stack

---

## 7️⃣ Atalhos Úteis

### Python
```python
# Ler N linhas de números
arr = [list(map(int, input().split())) for _ in range(n)]

# Encontrar máximo/mínimo
print(max(lista))
print(min(lista))

# Ordenar
lista.sort()
lista.sort(reverse=True)

# Contar frequências
from collections import Counter
freq = Counter(lista)
```

### Java
```java
// Arrays.sort()
Arrays.sort(arr);

// Collections.sort()
Collections.sort(list);

// HashMap
Map<Integer, Integer> map = new HashMap<>();
map.put(key, value);
```

### C++
```cpp
// Sort
sort(arr, arr + n);
sort(v.begin(), v.end());

// Reverse
reverse(v.begin(), v.end());

// Encontrar
find(v.begin(), v.end(), valor);
```

---

**Boa sorte! 🏆**
