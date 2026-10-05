# Merge Sort – Recursion Tree

![Recursion tree for Merge Sort](Visualization/Visualization.png)

---

## **1. The Question**

Sort this list from smallest to largest:

`[38, 27, 43, 3, 9, 82, 10, 5]`

---

## **2. The Solution**

Use **Merge Sort**. It first cuts the list into smaller and smaller pieces, and then joins the pieces back together in sorted order.

- **Divide:** cut the list in half again and again until each piece has only 1 number.
- **Merge:** join two sorted pieces into one bigger sorted piece, and repeat until one list remains.

A piece with 1 number is already sorted, so that is where we stop cutting.

**Reading the picture:** blue boxes show a piece before it is split, and green boxes show the same piece after it is sorted. The blue circle shows the order of splitting, and the green circle shows the order of finishing.

---

## **3. The Algorithm (Pseudocode)**

The algorithm has two parts: **MERGE-SORT** does the dividing, and **MERGE** joins two sorted pieces.

```
MERGE-SORT(A, low, high)
    if high - low <= 1              // 0 or 1 element: already sorted
        return                      // base case, stop dividing
    mid = (low + high) / 2          // find the middle
    MERGE-SORT(A, low, mid)         // sort the left half
    MERGE-SORT(A, mid, high)        // sort the right half
    MERGE(A, low, mid, high)        // join the two sorted halves


MERGE(A, low, mid, high)
    L = copy of A[low .. mid)       // left sorted piece
    R = copy of A[mid .. high)      // right sorted piece
    i = 0, j = 0, k = low
    while i < length(L) and j < length(R)
        if L[i] <= R[j]             // compare the front numbers
            A[k] = L[i];  i = i + 1 // take the smaller one
        else
            A[k] = R[j];  j = j + 1
        k = k + 1
    while i < length(L)             // right list is empty:
        A[k] = L[i];  i = i + 1;  k = k + 1     // copy the rest of L
    while j < length(R)             // left list is empty:
        A[k] = R[j];  j = j + 1;  k = k + 1     // copy the rest of R
```

**In simple words:** MERGE-SORT keeps cutting the list at the middle until a piece has 1 number, and then MERGE joins the pieces back in sorted order. To sort our list, we start with `MERGE-SORT(A, 0, 8)`.

**Link to the steps below:** the two `MERGE-SORT` calls inside the algorithm are the *Divide* steps (Steps 1–7), and each `MERGE` call is one *Merge* step (Steps 8–14).

---

## **4. The Process (Step by Step)**

### **Part A – Divide (cut into halves)**

**Step 1:** Take the full list `[38, 27, 43, 3, 9, 82, 10, 5]` and cut it exactly in the middle. This gives two pieces, `[38, 27, 43, 3]` and `[9, 82, 10, 5]`.

**Step 2:** Go to the left piece `[38, 27, 43, 3]` first and cut it in the middle again. This gives `[38, 27]` and `[43, 3]`.

**Step 3:** Take `[38, 27]` and cut it into two single numbers. This gives `[38]` and `[27]`, and both are already sorted.

**Step 4:** Take `[43, 3]` and cut it into two single numbers. This gives `[43]` and `[3]`, and now the whole left side is divided.

**Step 5:** Move to the right piece `[9, 82, 10, 5]` and cut it in the middle. This gives `[9, 82]` and `[10, 5]`.

**Step 6:** Take `[9, 82]` and cut it into single numbers. This gives `[9]` and `[82]`, which need no more cutting.

**Step 7:** Take `[10, 5]` and cut it into single numbers. This gives `[10]` and `[5]`, and now every piece has 1 number, so dividing is finished.

### **Part B – Merge the left side**

**Step 8:** Merge `[38]` and `[27]` by comparing their numbers. Since 27 is smaller than 38, 27 goes first, and the result is `[27, 38]`.

**Step 9:** Merge `[43]` and `[3]` in the same way. Since 3 is smaller than 43, 3 goes first, and the result is `[3, 43]`.

**Step 10:** Merge `[27, 38]` and `[3, 43]` by always comparing the first number of each list and taking the smaller one.
- Compare 27 and 3 → take **3**
- Compare 27 and 43 → take **27**
- Compare 38 and 43 → take **38**
- Left list is empty → add **43**

The left side is now fully sorted: `[3, 27, 38, 43]`.

### **Part C – Merge the right side**

**Step 11:** Merge `[9]` and `[82]` by comparing them. Since 9 is smaller than 82, 9 goes first, and the result is `[9, 82]`.

**Step 12:** Merge `[10]` and `[5]` in the same way. Since 5 is smaller than 10, 5 goes first, and the result is `[5, 10]`.

**Step 13:** Merge `[9, 82]` and `[5, 10]` by comparing the first numbers of both lists again and again.
- Compare 9 and 5 → take **5**
- Compare 9 and 10 → take **9**
- Compare 82 and 10 → take **10**
- Right list is empty → add **82**

The right side is now fully sorted: `[5, 9, 10, 82]`.

### **Part D – Final merge**

**Step 14:** Merge the two sorted halves `[3, 27, 38, 43]` and `[5, 9, 10, 82]` into one list. Compare the first numbers of both halves each time and take the smaller one.
- Compare 3 and 5 → take **3**
- Compare 27 and 5 → take **5**
- Compare 27 and 9 → take **9**
- Compare 27 and 10 → take **10**
- Compare 27 and 82 → take **27**
- Compare 38 and 82 → take **38**
- Compare 43 and 82 → take **43**
- Left list is empty → add **82**

---

## **5. The Result**

**Sorted list:** `[3, 5, 9, 10, 27, 38, 43, 82]`

**Time taken:** the list is halved 3 times (8 → 4 → 2 → 1), and each level looks at all 8 numbers once. So the work is about 8 × 3 = 24 steps, which is written as **O(n log n)**.
