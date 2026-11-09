/* ===== helpers ===== */
const $ = (s, r = document) => r.querySelector(s);
const esc = s => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
const nums = (s, what) => {
  const a = s.split(/[,\s]+/).filter(Boolean).map(Number);
  if (!a.length || a.some(x => !Number.isInteger(x))) throw new Error(`${what} must be whole numbers separated by commas.`);
  return a;
};
const isSorted = a => a.every((x, i) => !i || a[i - 1] <= x);
const needSorted = (a, what) => { if (!isSorted(a)) throw new Error(`${what} must be sorted in increasing order.`); };
const T = (...l) => { const o = {}; l.forEach(([i, t, c]) => { if (i >= 0) (o[i] = o[i] || []).push([t, c]); }); return o; };
const ptrs = (lo, mid, hi) => T([lo, "low", "l"], [mid, "mid", "m"], [hi, "high", "h"]);
const R = (label, vals, o = {}) => ({ label, vals, ...o });
const OUT = { lo: 99, hi: -1 };
const mk = () => { const out = []; return [out, (rows, msg) => out.push({ rows, msg })]; };

function highlight(code) {
  return esc(code).replace(
    /(#.*)|('[^']*')|\b(def|while|if|elif|else|return|import|and|or|not|True|False)\b|\b(\d+)\b|\b(len|max|min|sum|float|ceil)\b|(?<=\bdef )(\w+)/g,
    (m, c, s, k, n) => c ? `<span class="cm">${m}</span>` : s ? `<span class="st">${m}</span>` :
      k ? `<span class="kw">${m}</span>` : n ? `<span class="nm">${m}</span>` : `<span class="fn">${m}</span>`);
}

/* ===== step generators ===== */
function classic(a, t, cols) {
  const [out, S] = mk();
  let lo = 0, hi = a.length - 1;
  const lab = cols ? "Matrix read row by row (flattened)" : "nums";
  const at = i => cols ? ` (row ${Math.floor(i / cols)}, col ${i % cols})` : "";
  S([R(lab, a, { lo, hi, cols, tags: ptrs(lo, -1, hi) })], `Search space is everything: low = ${lo}, high = ${hi}. Target is ${t}.`);
  while (lo <= hi) {
    const mid = (lo + hi) >> 1, v = a[mid];
    if (v === t) {
      S([R(lab, a, { lo, hi, cols, hl: { [mid]: "found" }, tags: ptrs(lo, mid, hi) })], `mid = ${mid}${at(mid)}: ${v} equals ${t}. Found!`);
      return out;
    }
    const right = v < t;
    S([R(lab, a, { lo, hi, cols, tags: ptrs(lo, mid, hi) })],
      `mid = (${lo} + ${hi}) // 2 = ${mid}${at(mid)}: ${v} is ${right ? "less" : "greater"} than ${t}, so discard ${right ? `indices ${lo} to ${mid}: low = ${mid + 1}` : `indices ${mid} to ${hi}: high = ${mid - 1}`}.`);
    if (right) lo = mid + 1; else hi = mid - 1;
  }
  S([R(lab, a, { ...OUT, cols })], `low (${lo}) passed high (${hi}): nothing left. ${t} is not there, return ${cols ? "False" : "-1"}.`);
  return out;
}

function koko({ piles, h }) {
  const [out, S] = mk();
  const mx = Math.max(...piles), ks = Array.from({ length: mx }, (_, i) => i + 1);
  let lo = 1, hi = mx;
  const rows = (tags, hl, per) => [
    R("Candidate speeds k (bananas per hour)", ks, { lo: lo - 1, hi: hi - 1, noidx: 1, tags, hl }),
    R("Piles (hours needed at this k)", piles, { tags: per })
  ];
  S(rows(ptrs(lo - 1, -1, hi - 1)), `The answer is a speed between 1 and ${mx} (the biggest pile). Speeds that are fast enough form a block at the right end, so we binary search on k. Limit: ${h} hours.`);
  while (lo < hi) {
    const mid = (lo + hi) >> 1, parts = piles.map(p => Math.ceil(p / mid)), hrs = parts.reduce((x, y) => x + y, 0), ok = hrs <= h;
    S(rows(ptrs(lo - 1, mid - 1, hi - 1), {}, T(...parts.map((x, i) => [i, `${x}h`, "r"]))),
      `k = ${mid}: hours = ${parts.join(" + ")} = ${hrs}. ${ok ? `That fits in ${h}, so ${mid} works. Try slower: high = ${mid} (keep mid).` : `That is over ${h}, too slow: low = ${mid + 1}.`}`);
    if (ok) hi = mid; else lo = mid + 1;
  }
  S(rows(ptrs(lo - 1, -1, hi - 1), { [lo - 1]: "found" }), `low meets high at ${lo}. The minimum eating speed is k = ${lo}.`);
  return out;
}

function findMin(a) {
  const [out, S] = mk();
  let lo = 0, hi = a.length - 1;
  S([R("nums", a, { lo, hi, tags: ptrs(lo, -1, hi) })], `Start with low = 0, high = ${hi}. The array is a sorted one rotated at some point.`);
  while (lo < hi) {
    const mid = (lo + hi) >> 1, big = a[mid] > a[hi];
    S([R("nums", a, { lo, hi, tags: ptrs(lo, mid, hi) })],
      `mid = ${mid}: compare ${a[mid]} with the last value ${a[hi]}. ${big ? `${a[mid]} is bigger, so the drop (the minimum) is to the right of mid: low = ${mid + 1}.` : `${a[mid]} is not bigger, so the right part is sorted and the minimum is at mid or to its left: high = ${mid}. Keep mid.`}`);
    if (big) lo = mid + 1; else hi = mid;
  }
  S([R("nums", a, { lo, hi, hl: { [lo]: "found" }, tags: ptrs(lo, -1, hi) })], `low = high = ${lo}. The minimum is ${a[lo]}.`);
  return out;
}

function searchRot({ a, t }) {
  const [out, S] = mk();
  let lo = 0, hi = a.length - 1;
  S([R("nums", a, { lo, hi, tags: ptrs(lo, -1, hi) })], `Start with low = 0, high = ${hi}. Target is ${t}.`);
  while (lo <= hi) {
    const mid = (lo + hi) >> 1, v = a[mid], left = a[lo] <= v, sr = {};
    for (let i = left ? lo : mid; i <= (left ? mid : hi); i++) sr[i] = "srt";
    if (v === t) {
      S([R("nums", a, { lo, hi, hl: { [mid]: "found" }, tags: ptrs(lo, mid, hi) })], `mid = ${mid}: ${v} equals ${t}. Found!`);
      return out;
    }
    const goLeft = left ? (a[lo] <= t && t < v) : !(v < t && t <= a[hi]);
    const why = left
      ? `The left half (${a[lo]} to ${v}) is sorted. ${t} ${goLeft ? "falls inside it" : "is not inside it"}`
      : `The right half (${v} to ${a[hi]}) is sorted. ${t} ${goLeft ? "is not inside it" : "falls inside it"}`;
    S([R("nums", a, { lo, hi, hl: sr, tags: ptrs(lo, mid, hi) })], `mid = ${mid} (${v}). ${why}, so ${goLeft ? `high = ${mid - 1}` : `low = ${mid + 1}`}. (Green underline = the sorted half.)`);
    if (goLeft) hi = mid - 1; else lo = mid + 1;
  }
  S([R("nums", a, { ...OUT })], `low passed high: ${t} is not in the array, return -1.`);
  return out;
}

function timeKV({ ts, q }) {
  const [out, S] = mk();
  const vals = ts.map((_, i) => "v" + (i + 1));
  let lo = 0, hi = ts.length - 1, res = -1;
  const rows = (o, hl) => [R("Timestamps (sorted)", ts, { lo, hi, ...o, hl }), R("Value stored at that time", vals, { noidx: 1 })];
  S(rows({ tags: ptrs(lo, -1, hi) }, {}), `get(key, ${q}) wants the latest value set at or before time ${q}: the largest timestamp that is <= ${q}.`);
  while (lo <= hi) {
    const mid = (lo + hi) >> 1, ok = ts[mid] <= q;
    S(rows({ tags: T([lo, "low", "l"], [mid, "mid", "m"], [hi, "high", "h"], [res, "best", "r"]) }, res >= 0 ? { [res]: "best" } : {}),
      `mid = ${mid}: timestamp ${ts[mid]} ${ok ? `is <= ${q}, so it is a candidate. Remember index ${mid} and look right for a later one: low = ${mid + 1}.` : `is after ${q}, too late: high = ${mid - 1}.`}`);
    if (ok) { res = mid; lo = mid + 1; } else hi = mid - 1;
  }
  lo = 99; hi = -1;
  S(rows({ tags: T([res, "answer", "r"]) }, res >= 0 ? { [res]: "found" } : {}),
    res >= 0 ? `Done. The best candidate is timestamp ${ts[res]} (index ${res}), so get returns ${vals[res]}.` : `Every timestamp is after ${q}, so get returns an empty string.`);
  return out;
}

function median({ A, B }) {
  const [out, S] = mk();
  let swapped = false;
  if (A.length > B.length) { [A, B] = [B, A]; swapped = true; }
  const m = A.length, n = B.length, half = (m + n + 1) >> 1;
  const f = x => x === -Infinity ? "-inf" : x === Infinity ? "inf" : x;
  S([R("A (the shorter array)", A), R("B", B)],
    `${swapped ? "We swapped the inputs so A is the shorter one. " : ""}Total ${m + n} numbers, so the left half must hold ${half}. We binary search i = how many numbers to take from A (0 to ${m}); then j = ${half} - i come from B.`);
  let lo = 0, hi = m;
  while (lo <= hi) {
    const i = (lo + hi) >> 1, j = half - i;
    const Al = i ? A[i - 1] : -Infinity, Ar = i < m ? A[i] : Infinity, Bl = j ? B[j - 1] : -Infinity, Br = j < n ? B[j] : Infinity;
    const hA = {}, hB = {}, tA = {}, tB = {};
    if (i) { hA[i - 1] = "hl"; tA[i - 1] = [["L", "l"]]; } if (i < m) { hA[i] = "hr"; tA[i] = [["R", "h"]]; }
    if (j) { hB[j - 1] = "hl"; tB[j - 1] = [["L", "l"]]; } if (j < n) { hB[j] = "hr"; tB[j] = [["R", "h"]]; }
    const rows = (a, b) => [R("A (the shorter array)", A, { cut: i, hl: a, tags: tA }), R("B", B, { cut: j, hl: b, tags: tB })];
    const head = `i = ${i} from A, j = ${half} - ${i} = ${j} from B. Check A-left ${f(Al)} <= B-right ${f(Br)} and B-left ${f(Bl)} <= A-right ${f(Ar)}.`;
    if (Al <= Br && Bl <= Ar) {
      S(rows(hA, hB), `${head} Both hold, so this split is correct.`);
      const lm = Math.max(Al, Bl), rm = Math.min(Ar, Br), odd = (m + n) % 2, fa = {}, fb = {};
      (Al >= Bl ? fa : fb)[(Al >= Bl ? i : j) - 1] = "found";
      if (!odd) (Ar <= Br ? fa : fb)[Ar <= Br ? i : j] = "found";
      S([R("A (the shorter array)", A, { cut: i, hl: fa }), R("B", B, { cut: j, hl: fb })],
        odd ? `Total is odd, so the median is the biggest value on the left: ${lm}.` : `Total is even, so the median is the average of ${lm} (biggest on the left) and ${rm} (smallest on the right): ${(lm + rm) / 2}.`);
      return out;
    }
    const tooBig = Al > Br;
    S(rows(hA, hB), `${head} ${tooBig ? `A-left ${Al} is bigger than B-right ${Br}: we took too many from A, so high = ${i - 1}.` : `B-left ${Bl} is bigger than A-right ${Ar}: we took too few from A, so low = ${i + 1}.`}`);
    if (tooBig) hi = i - 1; else lo = i + 1;
  }
  return out;
}

/* ===== problem definitions ===== */
const rotated = a => {
  const drops = a.filter((x, i) => i && a[i - 1] > x).length;
  if (new Set(a).size !== a.length || drops > 1 || (drops === 1 && a[a.length - 1] > a[0]))
    throw new Error("Array must be a sorted array of distinct numbers, rotated once (e.g. 4, 5, 6, 7, 0, 1, 2).");
  return a;
};
const PROBLEMS = [
  {
    id: "bs", tab: "1 · Binary Search", title: "1 · Binary Search", badge: ["📚 Classic on Array", ""],
    lc: ["704", "binary-search"], diff: "easy",
    desc: "Compare the middle element with the target and throw away the half that cannot contain it.",
    steps: ["Set <code>low = 0</code>, <code>high = n-1</code>.", "Look at <code>mid = (low + high) // 2</code>.", "Equal? Done. Too small? <code>low = mid + 1</code>. Too big? <code>high = mid - 1</code>.", "Stop when <code>low &gt; high</code>: the target is not there."],
    code: `def binary_search(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1    # discard the left half
        else:
            high = mid - 1   # discard the right half
    return -1`,
    fields: [["a", "Sorted array", "text", "-1, 0, 3, 5, 9, 12"], ["t", "Target", "number", "9"]],
    run: v => { const a = nums(v.a, "Array"); needSorted(a, "Array"); return classic(a, +v.t); }
  },
  {
    id: "mx", tab: "2 · Search 2D Matrix", title: "2 · Search a 2D Matrix", badge: ["📚 Flatten + Classic", ""],
    lc: ["74", "search-a-2d-matrix"], diff: "medium",
    desc: "Every row is sorted and each row starts after the previous one ends, so the whole matrix is one sorted list in disguise.",
    steps: ["Treat the matrix as a flat array of <code>rows × cols</code> items.", "Run the classic search on indices <code>0 … rows*cols-1</code>.", "Convert <code>mid</code> back: <code>row = mid // cols</code>, <code>col = mid % cols</code>."],
    code: `def search_matrix(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    low, high = 0, rows * cols - 1
    while low <= high:
        mid = (low + high) // 2
        value = matrix[mid // cols][mid % cols]
        if value == target:
            return True
        elif value < target:
            low = mid + 1
        else:
            high = mid - 1
    return False`,
    fields: [["m", "Matrix (rows separated by |)", "text", "1, 3, 5, 7 | 10, 11, 16, 20 | 23, 30, 34, 60"], ["t", "Target", "number", "3"]],
    run: v => {
      const rows = v.m.split(/[|;\n]/).map(r => r.trim()).filter(Boolean).map(r => nums(r, "Matrix"));
      if (rows.some(r => r.length !== rows[0].length)) throw new Error("Every row needs the same number of values.");
      const flat = rows.flat(); needSorted(flat, "Matrix (read row by row)");
      return classic(flat, +v.t, rows[0].length);
    }
  },
  {
    id: "ko", tab: "3 · Koko Bananas", title: "3 · Koko Eating Bananas", badge: ["🎯 On the Answer", "ans"],
    lc: ["875", "koko-eating-bananas"], diff: "medium",
    desc: "Don't search the piles. Search the possible eating speeds. If speed k finishes in time, every faster speed does too, so the check is monotonic.",
    steps: ["Speeds range from <code>1</code> to <code>max(piles)</code>.", "For a speed <code>mid</code>, hours = sum of <code>ceil(pile / mid)</code>.", "Fits in <code>h</code>? Keep it: <code>high = mid</code>. Too slow? <code>low = mid + 1</code>.", "When <code>low == high</code> that is the smallest working speed."],
    code: `import math

def min_eating_speed(piles, h):
    low, high = 1, max(piles)
    while low < high:
        mid = (low + high) // 2
        hours = sum(math.ceil(p / mid) for p in piles)
        if hours <= h:
            high = mid       # mid works, try slower
        else:
            low = mid + 1    # too slow
    return low`,
    fields: [["p", "Piles", "text", "3, 6, 7, 11"], ["h", "Hours (h)", "number", "8"]],
    run: v => {
      const piles = nums(v.p, "Piles"), h = +v.h;
      if (piles.some(x => x < 1)) throw new Error("Each pile needs at least 1 banana.");
      if (!Number.isInteger(h) || h < piles.length) throw new Error(`Hours must be a whole number of at least ${piles.length} (one hour per pile).`);
      return koko({ piles, h });
    }
  },
  {
    id: "fm", tab: "4 · Min in Rotated", title: "4 · Find Minimum in Rotated Sorted Array", badge: ["📚 Sorted-Half Logic", ""],
    lc: ["153", "find-minimum-in-rotated-sorted-array"], diff: "medium",
    desc: "The minimum is the point where the rotation dropped. Comparing mid with the last value tells you which side that drop is on.",
    steps: ["Use <code>low &lt; high</code> (we are finding a boundary).", "If <code>nums[mid] &gt; nums[high]</code>, the drop is on the right: <code>low = mid + 1</code>.", "Otherwise the minimum is at mid or left: <code>high = mid</code>.", "When the pointers meet, <code>nums[low]</code> is the minimum."],
    code: `def find_min(nums):
    low, high = 0, len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] > nums[high]:
            low = mid + 1    # minimum is on the right
        else:
            high = mid       # mid could be the minimum
    return nums[low]`,
    fields: [["a", "Rotated array", "text", "4, 5, 6, 7, 0, 1, 2"]],
    run: v => findMin(rotated(nums(v.a, "Array")))
  },
  {
    id: "sr", tab: "5 · Search Rotated", title: "5 · Search in Rotated Sorted Array", badge: ["📚 Sorted-Half Logic", ""],
    lc: ["33", "search-in-rotated-sorted-array"], diff: "medium",
    desc: "After any split one half is always sorted. Find out which half, check whether the target lies inside it, and keep or drop that half.",
    steps: ["Compute <code>mid</code>. Found it? Return.", "If <code>nums[low] &lt;= nums[mid]</code> the left half is sorted, otherwise the right half is.", "Target inside the sorted half's range? Search that half. Otherwise search the other.", "Repeat until found or <code>low &gt; high</code>."],
    code: `def search(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[low] <= nums[mid]:           # left half is sorted
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:                                # right half is sorted
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1`,
    fields: [["a", "Rotated array", "text", "4, 5, 6, 7, 0, 1, 2"], ["t", "Target", "number", "0"]],
    run: v => searchRot({ a: rotated(nums(v.a, "Array")), t: +v.t })
  },
  {
    id: "tk", tab: "6 · Time Key-Value", title: "6 · Time Based Key-Value Store", badge: ["⏱️ Floor / Upper-Bound", ""],
    lc: ["981", "time-based-key-value-store"], diff: "medium",
    desc: "Timestamps for a key are stored in increasing order. <code>get(key, t)</code> needs the latest one that is at most <code>t</code>, a floor search.",
    steps: ["Binary search the timestamps list.", "If <code>timestamps[mid] &lt;= t</code> it is a candidate: remember it, then look <strong>right</strong> for a later one.", "If it is after <code>t</code>, look left.", "No candidate found? Return an empty string."],
    code: `def get(timestamps, values, t):
    low, high, best = 0, len(timestamps) - 1, -1
    while low <= high:
        mid = (low + high) // 2
        if timestamps[mid] <= t:
            best = mid       # candidate, look for a later one
            low = mid + 1
        else:
            high = mid - 1
    return values[best] if best != -1 else ""`,
    fields: [["a", "Timestamps (sorted)", "text", "1, 4, 6, 9, 12, 15, 20"], ["t", "Query time t", "number", "10"]],
    run: v => { const ts = nums(v.a, "Timestamps"); needSorted(ts, "Timestamps"); return timeKV({ ts, q: +v.t }); }
  },
  {
    id: "md", tab: "7 · Median of Two", title: "7 · Median of Two Sorted Arrays", badge: ["✂️ Partition Search", ""],
    lc: ["4", "median-of-two-sorted-arrays"], diff: "hard",
    desc: "Don't merge. Binary search on how many items the shorter array contributes to the left half. The cut is right when every left value is at most every right value.",
    steps: ["Make <code>A</code> the shorter array, <code>half = (m + n + 1) // 2</code>.", "Pick <code>i</code> items from A and <code>j = half - i</code> from B.", "Valid when <code>A-left &lt;= B-right</code> and <code>B-left &lt;= A-right</code>.", "Too many from A? <code>high = i - 1</code>. Too few? <code>low = i + 1</code>.", "Odd total: max of the lefts. Even total: average of max-left and min-right."],
    code: `def find_median(a, b):
    if len(a) > len(b):
        a, b = b, a
    m, n = len(a), len(b)
    low, high, half = 0, m, (m + n + 1) // 2
    while low <= high:
        i = (low + high) // 2
        j = half - i
        a_left  = a[i - 1] if i > 0 else float('-inf')
        a_right = a[i]     if i < m else float('inf')
        b_left  = b[j - 1] if j > 0 else float('-inf')
        b_right = b[j]     if j < n else float('inf')
        if a_left <= b_right and b_left <= a_right:
            if (m + n) % 2:
                return max(a_left, b_left)
            return (max(a_left, b_left) + min(a_right, b_right)) / 2
        elif a_left > b_right:
            high = i - 1
        else:
            low = i + 1`,
    legend: '<span><i style="background:var(--low)"></i>L = last value of the left side</span><span><i style="background:var(--high)"></i>R = first value of the right side</span><span><i style="background:var(--mid)"></i>amber line = the cut</span><span><i style="background:var(--found)"></i>median value(s)</span>',
    fields: [["A", "Array A (sorted)", "text", "1, 3, 8, 9, 15"], ["B", "Array B (sorted)", "text", "7, 11, 18, 19, 21, 25"]],
    run: v => { const A = nums(v.A, "A"), B = nums(v.B, "B"); needSorted(A, "A"); needSorted(B, "B"); return median({ A, B }); }
  }
];
const LEGEND = '<span><i style="background:var(--low)"></i>low</span><span><i style="background:var(--mid)"></i>mid</span><span><i style="background:var(--high)"></i>high</span><span><i style="background:var(--found)"></i>found / answer</span><span>Faded cells are already ruled out.</span>';

/* ===== build the page ===== */
$("#tabs").innerHTML = PROBLEMS.map((p, i) => `<button class="tab${i ? "" : " active"}" data-tab="${p.id}">${p.tab}</button>`).join("");
$("#panels").innerHTML = PROBLEMS.map((p, i) => `
  <section class="panel card${i ? "" : " active"}" id="panel-${p.id}">
    <h2>${p.title} <span class="badge ${p.badge[1]}">${p.badge[0]}</span></h2>
    <p class="meta">
      <a class="lc-link" href="https://leetcode.com/problems/${p.lc[1]}/" target="_blank" rel="noopener">🔗 LeetCode ${p.lc[0]}</a>
      <span class="diff ${p.diff}">${p.diff[0].toUpperCase() + p.diff.slice(1)}</span>
    </p>
    <p class="desc">${p.desc}</p>
    <ol class="steps">${p.steps.map(s => `<li>${s}</li>`).join("")}</ol>
    <details class="code-block"><summary>Python solution</summary><pre><code>${highlight(p.code)}</code></pre></details>
    <div class="controls">
      ${p.fields.map(([id, label, type, val]) => `<label>${label}:<input type="${type}" id="${p.id}-${id}" value="${val}" /></label>`).join("")}
      <button class="btn primary" data-action="load" data-vis="${p.id}">Load</button>
      <button class="btn" data-action="prev" data-vis="${p.id}">◀ Prev</button>
      <button class="btn" data-action="play" data-vis="${p.id}">▶ Play</button>
      <button class="btn" data-action="next" data-vis="${p.id}">Next ▶</button>
      <button class="btn" data-action="reset" data-vis="${p.id}">⟲ Reset</button>
    </div>
    <div class="stage" id="${p.id}-stage" aria-live="polite"></div>
    <div class="legend">${p.legend || LEGEND}</div>
    <p class="msg" id="${p.id}-msg"></p>
    <p class="counter" id="${p.id}-count"></p>
    <div class="log" id="${p.id}-log"></div>
  </section>`).join("");

/* ===== rendering ===== */
function rowHtml(r) {
  const n = r.vals.length;
  const cells = r.vals.map((v, i) => {
    const tg = (r.tags && r.tags[i]) || [];
    const h = (r.hl && r.hl[i]) || (tg.some(t => t[1] === "m") ? "mid" : "");
    const has = r.lo !== undefined, out = has && (i < r.lo || i > r.hi);
    const cls = ["slot", out ? "out" : has ? "in" : "", h, r.cut === i && i < n ? "cut" : "", r.cut === n && i === n - 1 ? "cutr" : ""].join(" ");
    return `<div class="${cls}"><div class="cell">${v}</div>${r.noidx ? "" : `<div class="idx">${i}</div>`}<div class="ptr">${tg.map(t => `<span class="${t[1]}">${t[0]}</span>`).join("")}</div></div>`;
  }).join("");
  const style = r.cols ? ` style="grid-template-columns:repeat(${r.cols},var(--w))"` : "";
  return `<div class="rowlabel">${r.label}</div><div class="arrwrap"><div class="arr${r.cols ? " g" : ""}"${style}>${cells}</div></div>`;
}

const V = {};   // per-problem state: { steps, cur, timer }
function render(id) {
  const s = V[id], st = s.steps[s.cur];
  $(`#${id}-stage`).innerHTML = st.rows.map(rowHtml).join("");
  $(`#${id}-msg`).textContent = st.msg;
  $(`#${id}-count`).textContent = `Step ${s.cur + 1} of ${s.steps.length}`;
  const log = $(`#${id}-log`);
  log.innerHTML = `<ol>${s.steps.slice(0, s.cur + 1).map((x, i) => `<li class="${i === s.cur ? "cur" : ""}">${x.msg}</li>`).join("")}</ol>`;
  log.scrollTop = log.scrollHeight;
  if (s.cur === s.steps.length - 1) stop(id);
}
function stop(id) {
  const s = V[id]; if (!s) return;
  clearInterval(s.timer); s.timer = null;
  const b = $(`#panel-${id} [data-action="play"]`); if (b) b.textContent = "▶ Play";
}
function load(id) {
  const p = PROBLEMS.find(x => x.id === id);
  stop(id);
  const v = {};
  p.fields.forEach(([f]) => v[f] = $(`#${id}-${f}`).value);
  try {
    const steps = p.run(v);
    V[id] = { steps, cur: 0, timer: null };
    render(id);
  } catch (e) {
    V[id] = { steps: [], cur: 0, timer: null };
    $(`#${id}-stage`).innerHTML = "";
    $(`#${id}-msg`).textContent = "";
    $(`#${id}-count`).textContent = "";
    $(`#${id}-log`).innerHTML = `<p class="err">⚠️ ${e.message}</p>`;
  }
}
function act(id, action) {
  const s = V[id];
  if (action === "load") return load(id);
  if (!s || !s.steps.length) return;
  if (action === "prev") { stop(id); s.cur = Math.max(0, s.cur - 1); render(id); }
  else if (action === "next") { stop(id); s.cur = Math.min(s.steps.length - 1, s.cur + 1); render(id); }
  else if (action === "reset") { stop(id); s.cur = 0; render(id); }
  else if (action === "play") {
    if (s.timer) return stop(id);
    if (s.cur === s.steps.length - 1) { s.cur = 0; render(id); }
    $(`#panel-${id} [data-action="play"]`).textContent = "⏸ Pause";
    s.timer = setInterval(() => { s.cur++; render(id); }, 1200);
  }
}

document.addEventListener("click", e => {
  const b = e.target.closest("[data-action]");
  if (b) return act(b.dataset.vis, b.dataset.action);
  const t = e.target.closest(".tab");
  if (t) {
    PROBLEMS.forEach(p => stop(p.id));
    document.querySelectorAll(".tab").forEach(x => x.classList.toggle("active", x === t));
    document.querySelectorAll(".panel").forEach(x => x.classList.toggle("active", x.id === "panel-" + t.dataset.tab));
  }
});
document.addEventListener("keydown", e => {
  if (e.key === "Enter" && e.target.matches(".controls input")) load(e.target.id.split("-")[0]);
});
PROBLEMS.forEach(p => load(p.id));
