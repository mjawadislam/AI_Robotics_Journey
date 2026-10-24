# AI & Robotics Journey - Day 1

### 1. Python Basics
* **`print()` Function:** Used to display output on the screen.
  *(Computer se baat bulwane ya screen par result dikhane ke liye).*
* **Comments (`#`):** Lines ignored by Python interpreter, used for documentation.
  *(Computer is line ko ignore kar deta hai, yeh sirf hamare samajhne ke liye hai).*
* **Variables:** Named containers used to store data values in memory.
  *(Data save karne wale dabbe, jaise `naam = "Muhammad Jawad"`).*
* **Shortcuts:** `Ctrl + /` to toggle comments easily.

## Day 2: Data Types, Hierarchy & Type Casting

### Core Data Types
- **str (String):** Text wrapped in quotes (e.g., `"Jawad"`).
  - *Roman Urdu:* Har text jo quotes ke andar ho.
- **int (Integer):** Whole numbers without decimals (e.g., `20`).
  - *Roman Urdu:* Poora number, jismein koi point/ashariya na ho.
- **float (Floating Point):** Real numbers with decimal points (e.g., `25.5`).
  - *Roman Urdu:* Ashariya ya point wala number.
- **bool (Boolean):** Binary evaluation states (`True` or `False`).
  - *Roman Urdu:* Sirf do faislay: Sach (`True`) ya Jhooth (`False`).

---

### Type Conversion & Hierarchy Rules
1. **Implicit Conversion (Safe Promotion):**
   - Operations between `int` and `float` automatically promote to `float` to prevent precision loss.
   - *Roman Urdu:* Agar integer aur float ko aapas mein calculate karein (maslan `50.0 + 200`), to Python data loss bachane ke liye jawab hamesha `float` banayega (`250.0`).
2. **Strict Incompatibility:**
   - Incompatible families (such as `str` and numeric types) throw a `TypeError` if concatenated directly.
   - *Roman Urdu:* Text aur Number do alag khandan hain, yeh bina convert kiye direct jama nahi ho sakte.
3. **Explicit Type Casting:**
   - `int("50")` -> Converts string into numeric integer `50`.
   - `float("50")` -> Converts string into floating point `50.0`.
   - `input()` returns a string by default; mathematical operations require explicit casting (e.g., `float(input())`).
   - *Roman Urdu:* Apne haath se type badalna. Terminal ka `input()` hamesha text/string lata hai, isliye hisaab ke liye pehle `int()` ya `float()` lagana zaroori hai.

---

### Modern Output Formatting (f-strings)
- Formatted string literals allow direct variable interpolation using `{variable_name}` without manual concatenation.
- *Roman Urdu:* Quotes ke shuru mein `f` lagao aur text ke darmiyan `{variable}` likh do. Python khud value wahan print kar deta hai, bina kisi plus ya comma ke maslay ke.

---

### Conditional Logic (Decision Making)
- `if`: Primary condition check. Evaluates truthiness before running indented block.
  - *Roman Urdu:* Pehla faisla. Agar yeh shart sach hai to andar ka code chalega.
- `elif` (Else If): Secondary sequential condition evaluated only if preceding checks fail.
  - *Roman Urdu:* Agar pehli shart ghalat ho jaye, to doosri shart check karta hai.
- `else`: Catch-all fallback executed when none of the conditions evaluate to `True`.
  - *Roman Urdu:* Jab koi shart sach na nikle, to aakhir mein yeh code chalta hai.
- Indentation (4 spaces) is strictly enforced by Python syntax to define code scope.

## Day 3: Collections (Lists) & Iteration (Loops)

### Python Lists (`list`)
- Ordered, mutable collections defined with square brackets `[]`.
- **Zero-Based Indexing:** Accessing elements begins at `0` (`list[0]`), while negative indexing accesses elements from the end (`list[-1]`).
- **Length (`len()`):** Returns the total count of elements inside a collection (e.g., `len(budgets)`).
- **Dynamic Insertion:**
  - `.append(value)`: Adds an item to the end of the list.
  - `.insert(index, value)`: Inserts an item at a specific target position (`index, value`).
- *Roman Urdu:* 
  - List ek tokri hai jismein multiple values tarteeb se rakhte hain (`[]`).
  - Computer ginti `0` se shuru karta hai, aur `-1` ka matlab sab se aakhri cheez.
  - `len()` list ke andar total items ki ginti batata hai.
  - `.append()` hamesha aakhir mein jorta hai; `.insert()` apni marzi ke number/index par naya item bitha deta hai.

---

### Iteration with `for` Loops
- Automates repetitive actions across iterable collections.
- **Loop Variable:** Temporarily holds the current item being processed during each cycle.
- **Scope & Indentation:** Block execution relies on a strict 4-space indentation following the `:` token. Without indentation, code executes outside loop scope.
- *Roman Urdu (Toffee Tokri Rule):*
  - `budgets` toffee ki tokri hai aur `b` (ya `single_budget`) aapka haath hai jo ek waqt mein sirf ek toffee uthata hai.
  - Har toffee par calculation (sticker) lagti hai aur computer agle item par chala jata hai jab tak tokri khali na ho jaye.
  - Loop ke andar chalne wali lines ko `Tab` (4 spaces) aage dhakelna lazmi hai, warna computer unhe loop ka hissa nahi manta.