# Number-Related DSA — Interview Question Bank

A curated list of number/math problems commonly asked in coding interviews (FAANG, product companies, startups). Grouped by topic with difficulty, pattern, and complexity notes.

---

## Table of Contents

1. [Digit Manipulation](#1-digit-manipulation)
2. [Prime Numbers](#2-prime-numbers)
3. [GCD, LCM & Number Theory](#3-gcd-lcm--number-theory)
4. [Bit Manipulation](#4-bit-manipulation)
5. [Powers, Roots & Logarithms](#5-powers-roots--logarithms)
6. [Fibonacci & Recurrence](#6-fibonacci--recurrence)
7. [Factorial & Combinatorics](#7-factorial--combinatorics)
8. [Palindrome & Special Numbers](#8-palindrome--special-numbers)
9. [Base Conversion](#9-base-conversion)
10. [Modular Arithmetic](#10-modular-arithmetic)
11. [Binary Search on Numbers](#11-binary-search-on-numbers)
12. [Greedy & Number Patterns](#12-greedy--number-patterns)
13. [Classic LeetCode Number Problems](#13-classic-leetcode-number-problems)
14. [Quick Pattern Cheat Sheet](#14-quick-pattern-cheat-sheet)

---

## 1. Digit Manipulation

| # | Problem | Difficulty | Pattern | Time | Space |
|---|---------|------------|---------|------|-------|
| 1 | Reverse an integer (handle overflow) | Easy | Extract digits with `% 10` and `// 10` | O(log n) | O(1) |
| 2 | Count digits in a number | Easy | `while n: n //= 10` or `log10(n)+1` | O(log n) | O(1) |
| 3 | Sum of digits | Easy | Modulo loop | O(log n) | O(1) |
| 4 | Product of digits | Easy | Modulo loop | O(log n) | O(1) |
| 5 | Check if number is palindrome | Easy | Reverse half or convert to string | O(log n) | O(1) |
| 6 | Find nth digit from right / left | Medium | `n // 10^k % 10` | O(log n) | O(1) |
| 7 | Rotate digits of a number | Medium | Split at k, recombine | O(log n) | O(1) |
| 8 | Add two numbers (linked list digits) | Medium | Carry simulation | O(max(m,n)) | O(1) |
| 9 | Plus One (array of digits) | Easy | Carry from right | O(n) | O(1) |
| 10 | Multiply two numbers (string digits) | Medium | Grade-school multiplication | O(m×n) | O(m+n) |
| 11 | Difference of sum of digits at even/odd positions | Easy | Parity index | O(log n) | O(1) |
| 12 | Minimum number by rearranging digits | Medium | Sort digits / counting sort | O(log n) | O(1) |
| 13 | Maximum number by rearranging digits | Medium | Sort descending | O(log n) | O(1) |
| 14 | Remove k digits to get smallest number | Medium | Monotonic stack | O(n) | O(n) |
| 15 | Next greater number with same digits | Medium | Next permutation on digits | O(log n) | O(1) |
| 16 | Add digits until single digit (digital root) | Easy | `n % 9` trick or loop | O(log n) | O(1) |
| 17 | Find numbers with exactly k divisors | Medium | Prime factorization pattern | O(n√n) | O(1) |
| 18 | Extract every kth digit | Easy | Index arithmetic | O(log n) | O(1) |
| 19 | Check if digits are in increasing order | Easy | Single pass on digits | O(log n) | O(1) |
| 20 | Maximum product by splitting digits | Medium | Greedy split into 3s (like integer break) | O(log n) | O(1) |

**Key idea:** Most digit problems use `digit = n % 10` and `n = n // 10` in a loop.

---

## 2. Prime Numbers

| # | Problem | Difficulty | Pattern | Time | Space |
|---|---------|------------|---------|------|-------|
| 1 | Check if a number is prime | Easy | Trial division up to √n | O(√n) | O(1) |
| 2 | Print all primes up to n (Sieve of Eratosthenes) | Medium | Boolean sieve | O(n log log n) | O(n) |
| 3 | Nth prime number | Medium | Sieve or trial with count | O(n log log n) | O(n) |
| 4 | Prime factorization of n | Medium | Divide by 2, then odd i up to √n | O(√n) | O(1) |
| 5 | Count of prime factors (with multiplicity) | Medium | Factorization loop | O(√n) | O(1) |
| 6 | Smallest prime factor (SPF) for 1..n | Medium | Modified sieve | O(n log log n) | O(n) |
| 7 | Count primes in range [l, r] | Medium | Segmented sieve | O(n log log n) | O(√n) |
| 8 | Twin primes / primes gap | Medium | Sieve + scan | O(n log log n) | O(n) |
| 9 | Largest prime factor | Medium | Factorization | O(√n) | O(1) |
| 10 | Check if n can be expressed as sum of two primes (Goldbach) | Medium | Sieve + two-pointer | O(n log log n) | O(n) |
| 11 | Count primes with digit sum = X | Medium | Sieve + digit check | O(n log log n) | O(n) |
| 12 | Prime partitions / prime splitting | Hard | DP + primes | Varies | Varies |

**Key idea:** Sieve for many queries; trial division for single checks.

---

## 3. GCD, LCM & Number Theory

| # | Problem | Difficulty | Pattern | Time | Space |
|---|---------|------------|---------|------|-------|
| 1 | GCD of two numbers (Euclidean algorithm) | Easy | `gcd(a,b) = gcd(b, a%b)` | O(log min(a,b)) | O(1) |
| 2 | LCM of two numbers | Easy | `lcm(a,b) = a*b // gcd(a,b)` | O(log min(a,b)) | O(1) |
| 3 | GCD of an array | Easy | Fold with gcd | O(n log V) | O(1) |
| 4 | LCM of an array | Medium | Fold with lcm | O(n log V) | O(1) |
| 5 | Check if two numbers are coprime | Easy | `gcd(a,b) == 1` | O(log min(a,b)) | O(1) |
| 6 | Euler's totient φ(n) | Medium | Prime factorization formula | O(√n) | O(1) |
| 7 | Count pairs with gcd = 1 | Medium | Totient or brute | O(n log n) | O(n) |
| 8 | Modular exponentiation (a^b % m) | Medium | Binary exponentiation | O(log b) | O(1) |
| 9 | Modular inverse (a⁻¹ mod m, m prime) | Medium | Fermat: `a^(m-2) % m` | O(log m) | O(1) |
| 10 | Extended Euclidean algorithm | Medium | Coefficients for Bezout | O(log min(a,b)) | O(1) |
| 11 | Chinese Remainder Theorem | Hard | Combine congruences | O(k log n) | O(k) |
| 12 | Count divisors of n | Easy | Loop to √n | O(√n) | O(1) |
| 13 | Sum of divisors of n | Medium | Loop to √n, pair factors | O(√n) | O(1) |
| 14 | Check perfect number (sum of divisors = n) | Easy | Divisor sum | O(√n) | O(1) |
| 15 | Check abundant / deficient number | Easy | Compare divisor sum to n | O(√n) | O(1) |
| 16 | Find all divisors of n | Easy | Loop to √n | O(√n) | O(√n) |
| 17 | Smallest number divisible by 1..n (LCM 1..n) | Medium | Sequential LCM | O(n log n) | O(1) |
| 18 | Trailing zeros in n! (count factors of 5) | Easy | `n/5 + n/25 + ...` | O(log n) | O(1) |
| 19 | Count factors of p in n! | Medium | Legendre's formula | O(log n) | O(1) |
| 20 | Check if a divides b | Easy | `b % a == 0` | O(1) | O(1) |

---

## 4. Bit Manipulation

| # | Problem | Difficulty | Pattern | Time | Space |
|---|---------|------------|---------|------|-------|
| 1 | Check if number is power of 2 | Easy | `n > 0 and n & (n-1) == 0` | O(1) | O(1) |
| 2 | Check if power of 4 | Easy | Power of 2 + bit position check | O(1) | O(1) |
| 3 | Count set bits (Hamming weight) | Easy | `n & (n-1)` loop or built-in | O(1)* | O(1) |
| 4 | Number of 1 bits in range [0, n] | Medium | DP on bits / pattern | O(log n) | O(log n) |
| 5 | Single number (every other appears twice) | Easy | XOR all elements | O(n) | O(1) |
| 6 | Single number II (others appear 3 times) | Medium | Bit count mod 3 | O(n) | O(1) |
| 7 | Single number III (two singles) | Medium | XOR split by differing bit | O(n) | O(1) |
| 8 | Missing number (0..n) | Easy | XOR or sum formula | O(n) | O(1) |
| 9 | Reverse bits of 32-bit integer | Easy | Bit by bit | O(1) | O(1) |
| 10 | Get/set/clear ith bit | Easy | Shift + mask | O(1) | O(1) |
| 11 | Toggle ith bit | Easy | XOR with mask | O(1) | O(1) |
| 12 | Find position of only set bit | Easy | `n & (n-1) == 0` → log2 | O(1) | O(1) |
| 13 | Swap two numbers without temp | Easy | XOR swap | O(1) | O(1) |
| 14 | Add two integers without + or - | Medium | XOR + carry loop | O(1)* | O(1) |
| 15 | Divide two integers without * / % | Medium | Bit shifting | O(log n) | O(1) |
| 16 | Subset XOR sum / total sum of subsets | Medium | 2^n enumeration or DP | O(n·2^n) | O(2^n) |
| 17 | Maximum XOR of two numbers in array | Medium | Binary trie | O(n·32) | O(n·32) |
| 18 | Gray code sequence | Medium | `i ^ (i >> 1)` | O(2^n) | O(2^n) |
| 19 | Complement of base 10 integer | Easy | Find mask then XOR | O(log n) | O(1) |
| 20 | Bitwise AND of range [left, right] | Medium | Find common prefix | O(log n) | O(1) |
| 21 | UTF-8 validation (bit patterns) | Medium | Mask checks | O(n) | O(1) |
| 22 | Find duplicate (1..n, array) | Easy | Floyd or mark indices | O(n) | O(1) |
| 23 | Maximum product of word lengths (bitmask) | Medium | Bitmask per word | O(n²) | O(n) |
| 24 | Sum of two integers (LeetCode) | Medium | XOR + carry | O(1)* | O(1) |
| 25 | Minimum flips to make a OR b equal c | Medium | Bit analysis | O(32) | O(1) |

**Key idea:** XOR cancels duplicates; `n & (n-1)` removes lowest set bit.

---

## 5. Powers, Roots & Logarithms

| # | Problem | Difficulty | Pattern | Time | Space |
|---|---------|------------|---------|------|-------|
| 1 | Pow(x, n) — fast exponentiation | Medium | Binary exponentiation | O(log n) | O(1) |
| 2 | Sqrt(x) — integer square root | Easy | Binary search or Newton | O(log n) | O(1) |
| 3 | Nth root of a number | Medium | Binary search on answer | O(log n · precision) | O(1) |
| 4 | Check if number is perfect square | Easy | Binary search or `int(sqrt(n))**2` | O(log n) | O(1) |
| 5 | Check if number is perfect cube | Easy | Binary search | O(log n) | O(1) |
| 6 | Power of 3 / power of 10 check | Easy | Repeated division or log | O(log n) | O(1) |
| 7 | Super pow (a^b mod 1337, b is array) | Medium | Modular exp + digit DP | O(log b) | O(1) |
| 8 | Sqrt decomposition (concept) | Medium | Block size √n | O(√n) per query | O(n) |
| 9 | Count square numbers in range | Easy | `floor(sqrt(r)) - ceil(sqrt(l)) + 1` | O(1) | O(1) |
| 10 | Find peak element (log n variant) | Medium | Binary search | O(log n) | O(1) |

---

## 6. Fibonacci & Recurrence

| # | Problem | Difficulty | Pattern | Time | Space |
|---|---------|------------|---------|------|-------|
| 1 | Nth Fibonacci number | Easy | Iterative / matrix exp | O(n) / O(log n) | O(1) |
| 2 | Fibonacci mod m | Medium | Matrix exponentiation | O(log n) | O(1) |
| 3 | Climbing stairs (1 or 2 steps) | Easy | DP = Fibonacci | O(n) | O(1) |
| 4 | Tribonacci / n-step stairs | Easy | DP generalization | O(n) | O(1) |
| 5 | Min cost climbing stairs | Easy | DP | O(n) | O(1) |
| 6 | Decode ways (1/2 digit mapping) | Medium | DP | O(n) | O(1) |
| 7 | House robber (linear DP) | Medium | DP max non-adjacent | O(n) | O(1) |
| 8 | Integer break (max product) | Medium | Math: break into 3s | O(log n) | O(1) |
| 9 | Nth magical number (multiples of a, b) | Hard | Binary search + inclusion-exclusion | O(log(n·max)) | O(1) |
| 10 | Rabbit pairs (Fibonacci story) | Easy | Fibonacci | O(n) | O(1) |
| 11 | Padovan / other recurrences | Medium | DP with k previous terms | O(n) | O(k) |
| 12 | Find formula for sequence | Medium | Difference table / characteristic eq | Varies | Varies |

---

## 7. Factorial & Combinatorics

| # | Problem | Difficulty | Pattern | Time | Space |
|---|---------|------------|---------|------|-------|
| 1 | Factorial of n | Easy | Loop or recursion | O(n) | O(1) |
| 2 | Trailing zeroes in n! | Easy | Count factors of 5 | O(log n) | O(1) |
| 3 | nCr (binomial coefficient) | Medium | Formula with cancellation | O(r) | O(1) |
| 4 | nPr (permutations) | Easy | `n! / (n-r)!` | O(r) | O(1) |
| 5 | Pascal's triangle row | Medium | nCr iterative | O(n) | O(n) |
| 6 | Unique paths (grid) | Medium | nCr: C(m+n-2, m-1) | O(min(m,n)) | O(1) |
| 7 | Count arrangements / Catalan number | Hard | `C(2n,n)/(n+1)` | O(n) | O(n) |
| 8 | Next permutation | Medium | Lexicographic algorithm | O(n) | O(1) |
| 9 | Previous permutation | Medium | Reverse of next perm logic | O(n) | O(1) |
| 10 | Kth permutation sequence | Hard | Factoradic / Cantor expansion | O(n²) | O(n) |
| 11 | Permutation sequence (1..n) | Hard | Factorial number system | O(n²) | O(n) |
| 12 | Count numbers with k distinct digits | Medium | DP + combinatorics | O(n·k) | O(n·k) |
| 13 | Distribute candies (combinations) | Medium | Stars and bars | O(n) | O(1) |
| 14 | Number of ways to climb / tile | Medium | DP combinatorics | O(n) | O(1) |

---

## 8. Palindrome & Special Numbers

| # | Problem | Difficulty | Pattern | Time | Space |
|---|---------|------------|---------|------|-------|
| 1 | Palindrome number | Easy | Reverse half | O(log n) | O(1) |
| 2 | Armstrong / Narcissistic number | Easy | Sum of digit^power | O(log n) | O(1) |
| 3 | Happy number | Easy | Floyd cycle on digit-square sum | O(log n) | O(1) |
| 4 | Automorphic number | Medium | Check if n² ends with n | O(log n) | O(1) |
| 5 | Neon number (sum of digits of n² = n) | Easy | Digit sum | O(log n) | O(1) |
| 6 | Spy number (sum = product of digits) | Easy | Digit loop | O(log n) | O(1) |
| 7 | Harshad (Niven) number | Easy | Divisible by digit sum | O(log n) | O(1) |
| 8 | Kaprekar number | Medium | n² split sum = n | O(log n) | O(1) |
| 9 | Perfect, abundant, deficient | Easy | Divisor sum | O(√n) | O(1) |
| 10 | Smith number | Medium | Digit sum equals prime factor digit sum | O(√n) | O(1) |
| 11 | Ugly number (2,3,5 factors only) | Medium | Factor division | O(log n) | O(1) |
| 12 | Super ugly number | Medium | Min-heap / DP | O(n log n) | O(n) |
| 13 | Nth ugly number | Medium | Three pointers DP | O(n) | O(n) |
| 14 | Colorful number (product digits unique) | Easy | Hash set on digits | O(log n) | O(1) |
| 15 | Buzz / Fizz patterns | Easy | Modulo conditions | O(n) | O(1) |

---

## 9. Base Conversion

| # | Problem | Difficulty | Pattern | Time | Space |
|---|---------|------------|---------|------|-------|
| 1 | Decimal to binary | Easy | `bin(n)` or loop `% 2` | O(log n) | O(log n) |
| 2 | Binary to decimal | Easy | Horner's method | O(log n) | O(1) |
| 3 | Decimal to any base (2–36) | Medium | Repeated division | O(log n) | O(log n) |
| 4 | Any base to decimal | Medium | Positional sum | O(digits) | O(1) |
| 5 | Convert between arbitrary bases | Medium | Via decimal intermediate | O(n) | O(n) |
| 6 | Fraction to binary representation | Medium | Multiply fractional part | O(precision) | O(1) |
| 7 | Excel sheet column title (1→A, 26→Z) | Easy | 1-indexed base-26 | O(log n) | O(log n) |
| 8 | Excel sheet column number (AB→28) | Easy | Horner base-26 | O(length) | O(1) |
| 9 | Roman to integer | Easy | Left-to-right subtract rule | O(n) | O(1) |
| 10 | Integer to Roman | Medium | Greedy subtract symbols | O(1) | O(1) |
| 11 | Add binary strings | Easy | Carry simulation | O(max(m,n)) | O(1) |
| 12 | Convert negative decimal to 2's complement | Medium | Fixed width bits | O(32) | O(1) |

---

## 10. Modular Arithmetic

| # | Problem | Difficulty | Pattern | Time | Space |
|---|---------|------------|---------|------|-------|
| 1 | (a + b) % m | Easy | `(a%m + b%m) % m` | O(1) | O(1) |
| 2 | (a - b) % m | Easy | Add m before mod | O(1) | O(1) |
| 3 | (a * b) % m | Easy | Cast to avoid overflow | O(1) | O(1) |
| 4 | Fast modular exponentiation | Medium | Binary pow | O(log exp) | O(1) |
| 5 | Modular inverse | Medium | Fermat / extended GCD | O(log m) | O(1) |
| 6 | Factorial mod p | Medium | Loop with mod | O(n) | O(1) |
| 7 | nCr mod p (p prime) | Hard | Fermat factorial + inverse | O(n) | O(n) |
| 8 | Lucas theorem for nCr mod p | Hard | Recursive on p-adic | O(log n) | O(log n) |
| 9 | Count pairs with sum % k = 0 | Medium | Remainder frequency map | O(n) | O(k) |
| 10 | Subarray sum divisible by k | Medium | Prefix mod + hash map | O(n) | O(k) |
| 11 | Random pick with weight | Medium | Prefix sum + binary search | O(n) build | O(n) |
| 12 | Fraction to recurring decimal | Medium | Remainder cycle detection | O(|denom|) | O(|denom|) |

---

## 11. Binary Search on Numbers

| # | Problem | Difficulty | Pattern | Time | Space |
|---|---------|------------|---------|------|-------|
| 1 | Sqrt(x) | Easy | BS on [0, x] | O(log x) | O(1) |
| 2 | Pow(x, n) | Medium | BS exponentiation | O(log n) | O(1) |
| 3 | Find minimum in rotated sorted array | Medium | BS on values | O(log n) | O(1) |
| 4 | Koko eating bananas | Medium | BS on speed (answer space) | O(n log max) | O(1) |
| 5 | Minimum days to make m bouquets | Medium | BS on days | O(n log max) | O(1) |
| 6 | Capacity to ship packages within D days | Medium | BS on capacity | O(n log sum) | O(1) |
| 7 | Split array largest sum | Hard | BS on max sum | O(n log sum) | O(1) |
| 8 | Nth magical number | Hard | BS + inclusion-exclusion | O(log answer) | O(1) |
| 9 | Aggressive cows (max min distance) | Hard | BS on distance | O(n log range) | O(1) |
| 10 | Median of two sorted arrays | Hard | BS on partition | O(log min(m,n)) | O(1) |

---

## 12. Greedy & Number Patterns

| # | Problem | Difficulty | Pattern | Time | Space |
|---|---------|------------|---------|------|-------|
| 1 | Jump game (reach last index) | Medium | Greedy max reach | O(n) | O(1) |
| 2 | Gas station (circuit) | Medium | Total surplus + start | O(n) | O(1) |
| 3 | Candy distribution (ratings) | Hard | Two-pass greedy | O(n) | O(1) |
| 4 | Integer break | Medium | Max product → 3s | O(log n) | O(1) |
| 5 | Monotone increasing digits | Medium | Greedy from right | O(log n) | O(1) |
| 6 | Remove k digits (smallest) | Medium | Stack | O(n) | O(n) |
| 7 | Construct smallest number from DI string | Medium | Greedy stack | O(n) | O(n) |
| 8 | Wiggle subsequence | Medium | Greedy peaks/valleys | O(n) | O(1) |
| 9 | Maximum swap (one swap) | Medium | Greedy digit placement | O(log n) | O(log n) |
| 10 | Break integer into least numbers (DP/greedy) | Medium | Coin change variant | O(n·amount) | O(amount) |

---

## 13. Classic LeetCode Number Problems

Quick reference — problem name, number, difficulty:

| Problem | LC # | Diff | Core technique |
|---------|------|------|----------------|
| Reverse Integer | 7 | Med | Digit extraction, overflow |
| Palindrome Number | 9 | Easy | Reverse half |
| Plus One | 66 | Easy | Carry |
| Sqrt(x) | 69 | Easy | Binary search |
| Climbing Stairs | 70 | Easy | Fibonacci DP |
| Pow(x, n) | 50 | Med | Fast pow |
| Single Number | 136 | Easy | XOR |
| Single Number II | 137 | Med | Bit mod 3 |
| Single Number III | 260 | Med | XOR partition |
| Missing Number | 268 | Easy | XOR / sum |
| Happy Number | 202 | Easy | Cycle detection |
| Count Primes | 204 | Med | Sieve |
| Ugly Number | 263 | Med | Factor check |
| Ugly Number II | 264 | Med | DP three pointers |
| Super Ugly Number | 313 | Med | Heap / DP |
| Integer Break | 343 | Med | Math greedy |
| Sum of Two Integers | 371 | Med | Bit XOR |
| Super Pow | 372 | Med | Mod exp |
| Complement of Base 10 | 1009 | Easy | Bit mask |
| Number of Steps to Reduce to Zero | 1342 | Easy | Bit/count |
| Count Good Triplets | 1534 | Easy | Brute / optimize |
| Decode Ways | 91 | Med | DP |
| Multiply Strings | 43 | Med | Manual multiply |
| Fraction to Recurring Decimal | 166 | Med | Mod cycle |
| Excel Sheet Column Title | 168 | Easy | Base-26 |
| Excel Sheet Column Number | 171 | Easy | Base-26 parse |
| Factorial Trailing Zeroes | 172 | Med | Count 5s |
| Excel Sheet Column (related) | — | — | — |
| Power of Two | 231 | Easy | `n & (n-1)` |
| Power of Three | 326 | Easy | Division loop |
| Power of Four | 342 | Easy | Bit trick |
| Integer Replacement | 397 | Med | Greedy / memo |
| Nth Digit | 400 | Med | Math skip |
| Elimination Game | 390 | Med | Pattern |
| Perfect Squares | 279 | Med | DP / math |
| Add Digits | 258 | Easy | Digital root |
| Add Binary | 67 | Easy | Carry |
| Hamming Distance | 461 | Easy | XOR count |
| Total Hamming Distance | 477 | Med | Bit DP |
| Reverse Bits | 190 | Easy | Bit ops |
| Number of 1 Bits | 191 | Easy | Brian Kernighan |
| Range Bitwise AND | 201 | Med | Common prefix |
| Bitwise AND of Numbers Range | 201 | Med | Shift |
| Maximum Product of Word Lengths | 318 | Med | Bitmask |
| Bulb Switcher | 319 | Med | Perfect squares |
| Find the Duplicate Number | 287 | Med | Floyd cycle |
| Add Two Numbers | 2 | Med | Linked list carry |
| Roman to Integer | 13 | Easy | Map |
| Integer to Roman | 12 | Med | Greedy |
| Valid Number | 65 | Hard | State machine |
| Random Pick with Weight | 528 | Med | Prefix + BS |
| Nth Magical Number | 878 | Hard | BS + inclusion-exclusion |
| Minimum Operations to Reduce to Zero | 2579 | Med | Digit/greedy |

---

## 14. Quick Pattern Cheat Sheet

### Digit extraction
```python
while n:
    digit = n % 10
    n //= 10
```

### Reverse integer (with overflow guard)
```python
rev = 0
while n:
    rev = rev * 10 + n % 10
    n //= 10
```

### GCD (Euclidean)
```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
```

### Fast power
```python
def pow_mod(base, exp, mod):
    result = 1
    while exp:
        if exp & 1:
            result = result * base % mod
        base = base * base % mod
        exp >>= 1
    return result
```

### Sieve of Eratosthenes
```python
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return is_prime
```

### Count trailing zeros in n!
```python
def trailing_zeros(n):
    count = 0
    while n:
        n //= 5
        count += n
    return count
```

### Check power of 2
```python
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0
```

### Digital root (single digit sum)
```python
def digital_root(n):
    return 1 + (n - 1) % 9 if n else 0
```

### XOR single number
```python
def single_number(nums):
    ans = 0
    for x in nums:
        ans ^= x
    return ans
```

---

## Suggested Study Order (Interview Prep)

| Week | Focus | Target count |
|------|-------|--------------|
| 1 | Digits + palindrome + reverse + plus one | 15–20 problems |
| 2 | Primes + GCD/LCM + divisors | 15–20 problems |
| 3 | Bit manipulation (XOR, power of 2, bits) | 15–20 problems |
| 4 | Pow, sqrt, mod arithmetic | 10–15 problems |
| 5 | DP on numbers (Fibonacci, decode, stairs) | 10–15 problems |
| 6 | Mixed / LeetCode classics + timed mocks | 20+ problems |

---

## Tips for Interviews

1. **Clarify overflow** — Ask if 32-bit bounds apply (`2^31 - 1`).
2. **Avoid floats** — Use integer math for sqrt/pow when possible.
3. **Modular arithmetic** — Mention when results can be huge (nCr, pow).
4. **Edge cases** — `n = 0`, negative numbers, single digit, max int.
5. **State complexity** — Most digit problems are O(log n); sieve is O(n log log n).
6. **Don't jump to strings** — Interviewers prefer math/bit solutions when asked for O(1) space.

---

*Use this with `number_related_DSA.ipynb` for hands-on Python practice. Add solutions problem-by-problem as you solve them.*
