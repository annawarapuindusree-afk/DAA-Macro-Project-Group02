"""
Project 2: Recursion Tree for Merge Sort (array of 8 elements)

1. merge_sort() sorts the array and records every call of the recursion tree.
2. draw_tree() draws that recorded tree, so the picture always matches the algorithm.

Run:  python3 Project2_MergeSortTree.py      (needs: pip install matplotlib)
Output: Visualization/Visualization.png   - recursion tree with call-order and finish-order numbers
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle


# ---------------------------------------------------------------- algorithm
def merge_sort(A, low, high, level=0, tree=None, counter=None):
    """Sorts A[low:high] in place and returns the list of recursion-tree nodes."""
    if tree is None:
        tree = []
    if counter is None:
        counter = [0]
    counter[0] += 1
    call_no = counter[0]                       # order in which this call STARTS
    before = A[low:high]                       # sub-array when the call starts (divide)
    if high - low > 1:                         # base case: 0 or 1 element -> nothing to do
        mid = (low + high) // 2
        merge_sort(A, low, mid, level + 1, tree, counter)     # sort left half
        merge_sort(A, mid, high, level + 1, tree, counter)    # sort right half
        merge(A, low, mid, high)                              # combine the two sorted halves
    tree.append(dict(low=low, high=high, level=level, call=call_no,
                     finish=len(tree) + 1,                    # order in which this call FINISHES
                     before=before, after=A[low:high]))       # sub-array after merging
    return tree


def merge(A, low, mid, high):
    L, R = A[low:mid], A[mid:high]
    i = j = 0
    k = low
    while i < len(L) and j < len(R):           # compare the front elements
        if L[i] <= R[j]:
            A[k] = L[i]; i += 1                # take the smaller one
        else:
            A[k] = R[j]; j += 1
        k += 1
    while i < len(L):                          # copy what is left of L
        A[k] = L[i]; i += 1; k += 1
    while j < len(R):                          # copy what is left of R
        A[k] = R[j]; j += 1; k += 1


# ------------------------------------------------------------ visualization
def draw_tree(tree, arr, filename, numbered=False):
    BG = "#0f172a"
    CW, GAP, CH = 0.74, 0.06, 0.8                      # tile width, gap, height
    Y = lambda level: 8.2 - 2.3 * level                # y position of each level
    fig = plt.figure(figsize=(19.2, 10.8), dpi=100, facecolor=BG)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis("off"); ax.set_xlim(-1.5, 17.5); ax.set_ylim(0, 10.69)

    def row(cx, y, vals, fc, ec):
        x0 = cx - (len(vals) * (CW + GAP) - GAP) / 2
        for i, v in enumerate(vals):
            x = x0 + i * (CW + GAP)
            ax.add_patch(FancyBboxPatch((x, y - CH / 2), CW, CH, boxstyle="round,pad=0,rounding_size=0.09",
                                        fc=fc, ec=ec, lw=2, zorder=2))
            ax.text(x + CW / 2, y, str(v), color="white", fontsize=22,
                    fontweight="bold", ha="center", va="center", zorder=3)

    def badge(x, y, num, color, r=0.26):
        ax.add_patch(Circle((x, y), r, fc=color, ec="white", lw=2, zorder=4))
        if num is not None:
            ax.text(x, y, str(num), color="#0f172a", fontsize=15, fontweight="bold",
                    ha="center", va="center", zorder=5)

    for n in tree:
        lo, hi, lv = n["low"], n["high"], n["level"]
        cx = lo + hi                                   # centre of the node (leaf i is at 2i+1)
        if hi - lo > 1:                                # edges to the two children
            mid = (lo + hi) // 2
            for clo, chi in ((lo, mid), (mid, hi)):
                ax.plot([cx, clo + chi], [Y(lv) - 0.88, Y(lv + 1) + 0.88], color="#475569", lw=3, zorder=0)
        row(cx, Y(lv) + 0.45, n["before"], "#1d4ed8", "#93c5fd")   # blue  = divide
        row(cx, Y(lv) - 0.45, n["after"], "#15803d", "#86efac")    # green = merge
        if numbered:
            xb = cx - (hi - lo) * (CW + GAP) / 2 - 0.42
            badge(xb, Y(lv) + 0.45, n["call"], "#38bdf8")          # call order
            badge(xb, Y(lv) - 0.45, n["finish"], "#4ade80")        # finish order

    for lv in range(4):
        ax.text(-1.3, Y(lv), f"Level {lv}", color="#94a3b8", fontsize=15, va="center")

    if numbered:
        title = f"Step-Numbered Recursion Tree  -  Merge Sort  {arr}"
        legend = [(1.0, "#38bdf8", "Blue number = call order (when each call starts, Divide)", True),
                  (9.6, "#4ade80", "Green number = finish order (when each node is merged)", True)]
        footer = "Top row = sub-array when the call starts (split)     |     Bottom row = sorted result when the call finishes (merge)"
    else:
        title = f"Recursion Tree of Merge Sort  -  {arr}"
        legend = [(1.0, "#1d4ed8", "Top row: sub-array when it is split (DIVIDE, read top-down)", False),
                  (9.6, "#15803d", "Bottom row: sorted result after MERGE (read bottom-up)", False)]
        footer = "8 elements  ->  3 levels of splitting (log2 8 = 3),  n = 8 work per level  ->  O(n log n)"

    ax.text(8, 10.25, title, color="white", fontsize=30, fontweight="bold", ha="center", va="center")
    for lx, color, label, is_circle in legend:
        if is_circle:
            badge(lx + 0.18, 9.65, None, color, r=0.19)
        else:
            ax.add_patch(FancyBboxPatch((lx, 9.47), 0.36, 0.36, boxstyle="round,pad=0,rounding_size=0.06",
                                        fc=color, ec="white", lw=1.5))
        ax.text(lx + 0.55, 9.65, label, color="#e2e8f0", fontsize=15, va="center")
    ax.text(8, 0.22, footer, color="#cbd5e1", fontsize=17, ha="center", va="center")
    fig.savefig(filename, dpi=100, facecolor=BG)
    plt.close(fig)


if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10, 5]
    original = data[:]
    print("Before:", original)
    tree = merge_sort(data, 0, len(data))
    print("After: ", data)
    os.makedirs("Visualization", exist_ok=True)
    draw_tree(tree, original, "Visualization/Visualization.png", numbered=True)
    print("Saved Visualization/Visualization.png")
