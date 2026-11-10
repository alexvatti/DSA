/* ============================================================
   Sliding Window — Visual Playground
   Every problem is turned into a list of "steps" (snapshots).
   The controller below just walks through that list.
   ============================================================ */

/* ---------- helpers ---------- */
function snap(o) {
  return Object.assign(
    { arr: [], left: null, right: null, win: null, best: null,
      marks: {}, panels: [], msg: '', result: null }, o);
}
const P = (label, items) => ({ label, items });
const W = (l, r) => (l <= r ? [l, r] : null);
const mapItems = (m) => [...m.entries()].map(([k, v]) => `${k}×${v}`);
const text = (a, l, r) => a.slice(l, r + 1).join('');

/* ============================================================
   5. Longest Substring Without Repeating Characters
   ============================================================ */
function stepsLongestSubstring(s) {
  const a = [...s], st = [], seen = new Set();
  let left = 0, best = 0, bestWin = null;
  const panels = () => [P('seen (set)', [...seen]), P('best length', [String(best)])];

  st.push(snap({ arr: a, msg: 'Start: the window is empty. left = 0, best = 0.', panels: panels() }));

  for (let r = 0; r < a.length; r++) {
    const c = a[r];
    if (seen.has(c)) {
      st.push(snap({ arr: a, left, right: r, win: W(left, r - 1), best: bestWin, marks: { [r]: 'new' },
        msg: `right = ${r}: '${c}' is already in the window → duplicate. Shrink from the left.`, panels: panels() }));
      while (seen.has(c)) {
        const out = a[left];
        seen.delete(out);
        left++;
        st.push(snap({ arr: a, left, right: r, win: W(left, r - 1), best: bestWin, marks: { [left - 1]: 'out', [r]: 'new' },
          msg: `Remove '${out}' and move left → ${left}.${seen.has(c) ? ` '${c}' is still inside, keep shrinking.` : ` '${c}' is gone.`}`,
          panels: panels() }));
      }
    }
    seen.add(c);
    const len = r - left + 1;
    const improved = len > best;
    if (improved) { best = len; bestWin = [left, r]; }
    st.push(snap({ arr: a, left, right: r, win: [left, r], best: bestWin, marks: { [r]: 'add' },
      msg: `Add '${c}'. Window "${text(a, left, r)}" has length ${len}.${improved ? ' New best! 🎉' : ''}`,
      panels: panels() }));
  }
  st.push(snap({ arr: a, best: bestWin, panels: panels(), msg: `Done → longest substring length = ${best}.`, result: String(best) }));
  return st;
}

/* ============================================================
   6. Fruits Into Baskets  (longest subarray, at most 2 types)
   ============================================================ */
function stepsFruits(a) {
  const st = [], count = new Map();
  let left = 0, best = 0, bestWin = null;
  const panels = () => [P('baskets (type×count)', mapItems(count)), P('distinct types', [String(count.size)]), P('best', [String(best)])];

  st.push(snap({ arr: a, msg: 'Start: no fruit picked. left = 0, best = 0.', panels: panels() }));

  for (let r = 0; r < a.length; r++) {
    count.set(a[r], (count.get(a[r]) || 0) + 1);
    if (count.size > 2) {
      st.push(snap({ arr: a, left, right: r, win: [left, r], best: bestWin, marks: { [r]: 'new' },
        msg: `right = ${r}: pick fruit ${a[r]} → ${count.size} types, more than 2 baskets. Shrink from the left.`, panels: panels() }));
      while (count.size > 2) {
        const out = a[left];
        count.set(out, count.get(out) - 1);
        if (count.get(out) === 0) count.delete(out);
        left++;
        st.push(snap({ arr: a, left, right: r, win: [left, r], best: bestWin, marks: { [left - 1]: 'out', [r]: 'new' },
          msg: `Drop fruit ${out} and move left → ${left}.${count.size > 2 ? ' Still 3 types, keep shrinking.' : ` Back to ${count.size} types.`}`,
          panels: panels() }));
      }
    }
    const len = r - left + 1;
    const improved = len > best;
    if (improved) { best = len; bestWin = [left, r]; }
    st.push(snap({ arr: a, left, right: r, win: [left, r], best: bestWin, marks: { [r]: 'add' },
      msg: `Window [${a.slice(left, r + 1).join(', ')}] is valid (${count.size} type${count.size > 1 ? 's' : ''}), length ${len}.${improved ? ' New best! 🎉' : ''}`,
      panels: panels() }));
  }
  st.push(snap({ arr: a, best: bestWin, panels: panels(), msg: `Done → you can pick at most ${best} fruits.`, result: String(best) }));
  return st;
}

/* ============================================================
   7. Longest Repeating Character Replacement
   ============================================================ */
function stepsReplacement(s, k) {
  const a = [...s], st = [], count = new Map();
  let left = 0, best = 0, bestWin = null;
  const maxf = () => Math.max(0, ...count.values());
  const panels = (r) => {
    const len = r - left + 1, mf = maxf();
    return [P('letters (count)', mapItems(count)),
            P('len − max freq', [`${len} − ${mf} = ${len - mf}`, `(k = ${k})`]),
            P('best', [String(best)])];
  };

  st.push(snap({ arr: a, msg: `Start: empty window. We may replace at most k = ${k} letters.`, panels: [P('best', ['0'])] }));

  for (let r = 0; r < a.length; r++) {
    count.set(a[r], (count.get(a[r]) || 0) + 1);
    let need = (r - left + 1) - maxf();
    if (need > k) {
      st.push(snap({ arr: a, left, right: r, win: [left, r], best: bestWin, marks: { [r]: 'new' },
        msg: `right = ${r}: add '${a[r]}'. Replacements needed = ${need} > k = ${k} → shrink.`, panels: panels(r) }));
      while (need > k) {
        const out = a[left];
        count.set(out, count.get(out) - 1);
        if (count.get(out) === 0) count.delete(out);
        left++;
        need = (r - left + 1) - maxf();
        st.push(snap({ arr: a, left, right: r, win: [left, r], best: bestWin, marks: { [left - 1]: 'out', [r]: 'new' },
          msg: `Drop '${out}', left → ${left}. Replacements needed = ${need}${need > k ? ` > ${k}, shrink again.` : ` ≤ ${k}, valid.`}`,
          panels: panels(r) }));
      }
    }
    const len = r - left + 1;
    const improved = len > best;
    if (improved) { best = len; bestWin = [left, r]; }
    st.push(snap({ arr: a, left, right: r, win: [left, r], best: bestWin, marks: { [r]: 'add' },
      msg: `Window "${text(a, left, r)}" needs ${len - maxf()} replacement(s) ≤ ${k} → valid, length ${len}.${improved ? ' New best! 🎉' : ''}`,
      panels: panels(r) }));
  }
  st.push(snap({ arr: a, best: bestWin, panels: [P('best', [String(best)])], msg: `Done → longest repeating substring after replacements = ${best}.`, result: String(best) }));
  return st;
}

/* ============================================================
   8. Permutation in String  (FIXED window = len(s1))
   ============================================================ */
function stepsPermutation(s1, s2) {
  const a = [...s2], st = [], k = s1.length;
  const need = new Map(), win = new Map();
  for (const ch of s1) need.set(ch, (need.get(ch) || 0) + 1);
  const same = () => need.size === win.size && [...need].every(([c, n]) => win.get(c) === n);
  const panels = () => [P('need (from s1)', mapItems(need)), P('window counts', mapItems(win)), P('window size', [String(k)])];

  if (k > a.length) {
    st.push(snap({ arr: a, msg: `s1 is longer than s2 → no permutation can fit.`, result: 'False' }));
    return st;
  }
  st.push(snap({ arr: a, msg: `Start: fixed window of size k = ${k} (length of s1).`, panels: panels() }));

  for (let i = 0; i < a.length; i++) {
    win.set(a[i], (win.get(a[i]) || 0) + 1);
    const marks = { [i]: 'add' };
    let note = `Add '${a[i]}'`;
    if (i >= k) {
      const out = a[i - k];
      win.set(out, win.get(out) - 1);
      if (win.get(out) === 0) win.delete(out);
      marks[i - k] = 'out';
      note += `, drop '${out}'`;
    }
    note += '. ';
    const lft = Math.max(0, i - k + 1);
    if (i < k - 1) {
      st.push(snap({ arr: a, left: 0, right: i, win: [0, i], marks, panels: panels(), msg: `i = ${i}: ${note}Window is not full yet.` }));
      continue;
    }
    if (same()) {
      const m = {}; for (let j = lft; j <= i; j++) m[j] = 'match';
      st.push(snap({ arr: a, left: lft, right: i, win: [lft, i], marks: m, panels: panels(),
        msg: `i = ${i}: ${note}Window "${text(a, lft, i)}" counts equal need → permutation found! ✅`, result: 'True' }));
      return st;
    }
    st.push(snap({ arr: a, left: lft, right: i, win: [lft, i], marks, panels: panels(),
      msg: `i = ${i}: ${note}Window "${text(a, lft, i)}" counts differ from need.` }));
  }
  st.push(snap({ arr: a, panels: panels(), msg: 'Reached the end without a match → no permutation.', result: 'False' }));
  return st;
}

/* ============================================================
   9. Minimum Window Substring
   ============================================================ */
function stepsMinWindow(s, t) {
  const a = [...s], st = [];
  const need = new Map(), win = new Map();
  for (const ch of t) need.set(ch, (need.get(ch) || 0) + 1);
  const required = need.size;
  let have = 0, left = 0, bestLen = Infinity, bestStart = 0;
  const bestWin = () => (bestLen === Infinity ? null : [bestStart, bestStart + bestLen - 1]);
  const panels = () => [P('need (from t)', mapItems(need)), P('window counts', mapItems(win)),
    P('have / required', [`${have} / ${required}`]),
    P('best window', [bestLen === Infinity ? 'none yet' : s.slice(bestStart, bestStart + bestLen)])];

  st.push(snap({ arr: a, msg: `Start: need ${required} distinct character(s) satisfied. left = 0.`, panels: panels() }));

  for (let r = 0; r < a.length; r++) {
    const c = a[r];
    win.set(c, (win.get(c) || 0) + 1);
    const met = need.has(c) && win.get(c) === need.get(c);
    if (met) have++;
    st.push(snap({ arr: a, left, right: r, win: [left, r], best: bestWin(), marks: { [r]: 'add' }, panels: panels(),
      msg: `right = ${r}: add '${c}'.${met ? ` Requirement for '${c}' is now met.` : ''} have = ${have}/${required}.${have === required ? ' Window is valid → try to shrink.' : ''}` }));

    while (have === required) {
      const len = r - left + 1;
      const improved = len < bestLen;
      if (improved) { bestLen = len; bestStart = left; }
      const out = a[left];
      st.push(snap({ arr: a, left, right: r, win: [left, r], best: bestWin(), marks: { [left]: 'out' }, panels: panels(),
        msg: `Valid window "${text(a, left, r)}" (length ${len})${improved ? ' → new smallest! 🎉' : ' → not smaller than best'}. Next: remove '${out}'.` }));
      win.set(out, win.get(out) - 1);
      if (win.get(out) === 0) win.delete(out);
      if (need.has(out) && (win.get(out) || 0) < need.get(out)) have--;
      left++;
    }
  }
  const ans = bestLen === Infinity ? '' : s.slice(bestStart, bestStart + bestLen);
  st.push(snap({ arr: a, best: bestWin(), panels: panels(),
    msg: ans ? `Done → smallest window is "${ans}".` : 'Done → no window contains all characters of t.',
    result: ans ? `"${ans}"` : '"" (empty)' }));
  return st;
}

/* ============================================================
   10. Sliding Window Maximum  (fixed window + monotonic deque)
   ============================================================ */
function stepsWindowMax(a, k) {
  const st = [], dq = [], out = [];
  const panels = () => [P('deque (index:value)', dq.map((j) => `${j}:${a[j]}`)), P('output', out.map(String))];

  st.push(snap({ arr: a, msg: `Start: window size k = ${k}. The deque keeps indices with decreasing values.`, panels: panels() }));

  for (let i = 0; i < a.length; i++) {
    const marks = {}, parts = [];
    if (dq.length && dq[0] <= i - k) {
      marks[dq[0]] = 'out';
      parts.push(`Front index ${dq[0]} left the window → pop it.`);
      dq.shift();
    }
    while (dq.length && a[dq[dq.length - 1]] < a[i]) {
      const j = dq.pop();
      marks[j] = 'dup';
      parts.push(`${a[j]} < ${a[i]} → pop ${a[j]} from the back.`);
    }
    dq.push(i);
    marks[i] = 'new';
    parts.push(`Push index ${i}.`);
    if (i >= k - 1) { out.push(a[dq[0]]); parts.push(`Window full → max = ${a[dq[0]]}.`); }
    else parts.push('Window not full yet.');
    const lft = Math.max(0, i - k + 1);
    st.push(snap({ arr: a, left: lft, right: i, win: [lft, i], marks, panels: panels(), msg: `i = ${i}: ${parts.join(' ')}` }));
  }
  st.push(snap({ arr: a, panels: panels(), msg: `Done → maximums: [${out.join(', ')}].`, result: `[${out.join(', ')}]` }));
  return st;
}

/* ============================================================
   0. Contains Duplicate  (hash set, one pass)
   ============================================================ */
function stepsContainsDuplicate(a) {
  const st = [], seen = new Set();
  const panels = () => [P('seen (set)', [...seen].map(String))];

  st.push(snap({ arr: a, msg: 'Start: an empty set. Walk through each number once.', panels: panels() }));

  for (let i = 0; i < a.length; i++) {
    if (seen.has(a[i])) {
      st.push(snap({ arr: a, right: i, marks: { [i]: 'new' }, panels: panels(),
        msg: `i = ${i}: ${a[i]} is already in the set → duplicate found! ✅`, result: 'True' }));
      return st;
    }
    seen.add(a[i]);
    st.push(snap({ arr: a, right: i, marks: { [i]: 'add' }, panels: panels(),
      msg: `i = ${i}: ${a[i]} is new → add it to the set.` }));
  }
  st.push(snap({ arr: a, panels: panels(), msg: 'Walked the whole array with no repeat → all unique.', result: 'False' }));
  return st;
}

/* ============================================================
   1. Contains Duplicate II  (fixed window of size k + set)
   ============================================================ */
function stepsContainsDuplicateII(a, k) {
  const st = [], win = new Set();
  let left = 0;
  const panels = () => [P('window (last k values)', [...win].map(String)), P('k', [String(k)])];

  st.push(snap({ arr: a, msg: `Start: keep a set of at most k = ${k} recent values.`, panels: panels() }));

  for (let r = 0; r < a.length; r++) {
    if (win.has(a[r])) {
      st.push(snap({ arr: a, left, right: r, win: W(left, r), marks: { [r]: 'new' }, panels: panels(),
        msg: `right = ${r}: ${a[r]} is already inside the window → duplicate within distance k! ✅`, result: 'True' }));
      return st;
    }
    win.add(a[r]);
    st.push(snap({ arr: a, left, right: r, win: W(left, r), marks: { [r]: 'add' }, panels: panels(),
      msg: `right = ${r}: ${a[r]} is new → add it to the window.` }));
    if (win.size > k) {
      const out = a[r - k];
      win.delete(out);
      left = r - k + 1;
      st.push(snap({ arr: a, left, right: r, win: W(left, r), marks: { [r - k]: 'out' }, panels: panels(),
        msg: `Window has more than ${k} values → drop ${out} (index ${r - k}) that fell off the left.` }));
    }
  }
  st.push(snap({ arr: a, panels: panels(), msg: 'Reached the end with no nearby duplicate.', result: 'False' }));
  return st;
}

/* ============================================================
   2. Best Time to Buy and Sell Stock  (buy = left, sell = right)
   ============================================================ */
function stepsBuySell(a) {
  const st = [];
  let left = 0, best = 0, bestWin = null;
  const panels = () => [P('buy price (left)', [String(a[left])]), P('max profit', [String(best)])];

  st.push(snap({ arr: a, left: 0, right: 0, marks: { 0: 'add' }, panels: panels(),
    msg: `Start: buy on day 0 at price ${a[0]}. max profit = 0.` }));

  for (let r = 1; r < a.length; r++) {
    if (a[r] < a[left]) {
      left = r;
      st.push(snap({ arr: a, left, right: r, win: W(left, r), best: bestWin, marks: { [r]: 'new' }, panels: panels(),
        msg: `day ${r}: price ${a[r]} is a new low → move the buy day here (left = ${r}).` }));
    } else {
      const profit = a[r] - a[left];
      const improved = profit > best;
      if (improved) { best = profit; bestWin = [left, r]; }
      st.push(snap({ arr: a, left, right: r, win: W(left, r), best: bestWin, marks: { [r]: 'add' }, panels: panels(),
        msg: `day ${r}: sell at ${a[r]}, bought at ${a[left]} → profit ${profit}.${improved ? ' New best! 🎉' : ''}` }));
    }
  }
  st.push(snap({ arr: a, best: bestWin, panels: panels(), msg: `Done → maximum profit = ${best}.`, result: String(best) }));
  return st;
}

/* ============================================================
   3. Majority Element  (Boyer–Moore voting)
   ============================================================ */
function stepsMajority(a) {
  const st = [];
  let candidate = null, count = 0;
  const panels = () => [P('candidate', [candidate === null ? '—' : String(candidate)]), P('count', [String(count)])];

  st.push(snap({ arr: a, msg: 'Start: no candidate yet, count = 0.', panels: panels() }));

  for (let i = 0; i < a.length; i++) {
    let note = '';
    if (count === 0) {
      candidate = a[i];
      note = `count was 0 → adopt ${a[i]} as the new candidate. `;
    }
    if (a[i] === candidate) { count++; note += `${a[i]} matches candidate → count = ${count}.`; }
    else { count--; note += `${a[i]} differs → count = ${count}.`; }
    st.push(snap({ arr: a, right: i, marks: { [i]: a[i] === candidate ? 'add' : 'dup' }, panels: panels(),
      msg: `i = ${i}: ${note}` }));
  }
  st.push(snap({ arr: a, panels: panels(), msg: `Done → the surviving candidate ${candidate} is the majority element.`, result: String(candidate) }));
  return st;
}

/* ============================================================
   4. Most Frequent Even Element  (frequency map + tie-break)
   ============================================================ */
function stepsMostFrequentEven(a) {
  const st = [], count = new Map();
  let bestVal = -1, bestCount = 0;
  const panels = () => [P('even counts (value×count)', mapItems(count)),
    P('best so far', [bestVal === -1 ? 'none' : `${bestVal} (×${bestCount})`])];

  st.push(snap({ arr: a, msg: 'Start: count only the even numbers.', panels: panels() }));

  for (let i = 0; i < a.length; i++) {
    if (a[i] % 2 === 0) {
      count.set(a[i], (count.get(a[i]) || 0) + 1);
      const cnt = count.get(a[i]);
      const better = cnt > bestCount || (cnt === bestCount && a[i] < bestVal);
      if (better) { bestVal = a[i]; bestCount = cnt; }
      st.push(snap({ arr: a, right: i, marks: { [i]: 'add' }, panels: panels(),
        msg: `i = ${i}: ${a[i]} is even → count = ${cnt}.${better ? ` New best (highest count, smallest value) → ${a[i]}.` : ''}` }));
    } else {
      st.push(snap({ arr: a, right: i, marks: { [i]: 'dup' }, panels: panels(),
        msg: `i = ${i}: ${a[i]} is odd → skip it.` }));
    }
  }
  st.push(snap({ arr: a, panels: panels(),
    msg: bestVal === -1 ? 'No even numbers found → answer is -1.' : `Done → most frequent even element = ${bestVal}.`,
    result: String(bestVal) }));
  return st;
}

/* ---------- input readers (validate + build steps) ---------- */
const $ = (id) => document.getElementById(id);

function parseNums(str) {
  const parts = str.split(',').map((x) => x.trim()).filter(Boolean);
  if (!parts.length) throw new Error('Enter at least one number, separated by commas.');
  const nums = parts.map(Number);
  if (nums.some((n) => !Number.isFinite(n))) throw new Error('Use numbers only, separated by commas.');
  if (nums.length > 20) throw new Error('Use 20 numbers or fewer so the stage stays readable.');
  return nums;
}
function parseText(str, name, lowerOnly) {
  let v = str;
  if (lowerOnly) v = v.toLowerCase();
  if (!v.length) throw new Error(`${name} cannot be empty.`);
  if (v.length > 30) throw new Error(`${name}: use 30 characters or fewer.`);
  if (lowerOnly && !/^[a-z]+$/.test(v)) throw new Error(`${name}: use lowercase letters a–z only.`);
  return v;
}

const READERS = {
  cd: () => stepsContainsDuplicate(parseNums($('cd-input').value)),
  cd2: () => {
    const nums = parseNums($('cd2-input').value);
    const k = parseInt($('cd2-k').value, 10);
    if (!(k >= 0)) throw new Error('k must be 0 or more.');
    return stepsContainsDuplicateII(nums, k);
  },
  bs: () => stepsBuySell(parseNums($('bs-input').value)),
  mj: () => stepsMajority(parseNums($('mj-input').value)),
  fe: () => stepsMostFrequentEven(parseNums($('fe-input').value)),
  ls: () => stepsLongestSubstring(parseText($('ls-input').value, 'String')),
  fb: () => stepsFruits(parseNums($('fb-input').value)),
  cr: () => {
    const k = parseInt($('cr-k').value, 10);
    if (!(k >= 0)) throw new Error('k must be 0 or more.');
    return stepsReplacement(parseText($('cr-input').value, 'String'), k);
  },
  pm: () => stepsPermutation(parseText($('pm-s1').value, 's1', true), parseText($('pm-s2').value, 's2', true)),
  mw: () => stepsMinWindow(parseText($('mw-s').value, 's'), parseText($('mw-t').value, 't')),
  sm: () => {
    const nums = parseNums($('sm-input').value);
    const k = parseInt($('sm-k').value, 10);
    if (!(k >= 1 && k <= nums.length)) throw new Error(`k must be between 1 and ${nums.length}.`);
    return stepsWindowMax(nums, k);
  },
};

/* ---------- rendering ---------- */
const esc = (x) => String(x).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const show = (x) => (x === ' ' ? '␣' : esc(x));
const state = {};

function render(id) {
  const v = state[id], s = v.steps[v.idx];
  const inWin = (i) => s.win && i >= s.win[0] && i <= s.win[1];
  const inBest = (i) => s.best && i >= s.best[0] && i <= s.best[1];

  let html = '<div class="cells">';
  s.arr.forEach((ch, i) => {
    const cls = ['cell'];
    if (inWin(i)) cls.push('in-window');
    if (inBest(i)) cls.push('in-best');
    if (s.marks[i]) cls.push('m-' + s.marks[i]);
    let ptr = '';
    if (s.left === i && s.right === i) ptr = 'L R';
    else if (s.left === i) ptr = 'L';
    else if (s.right === i) ptr = 'R';
    const ptrCls = ptr === 'L' ? 'ptr l' : ptr === 'R' ? 'ptr r' : 'ptr lr';
    html += `<div class="cell-wrap"><div class="${cls.join(' ')}">${show(ch)}</div>` +
            `<div class="idx">${i}</div><div class="${ptrCls}">${ptr}</div></div>`;
  });
  html += '</div>';

  html += '<div class="legend"><span class="lg win">window</span><span class="lg best">best</span>' +
          '<span class="lg add">just added</span><span class="lg out">removed</span></div>';

  s.panels.forEach((p) => {
    html += `<div class="state-row"><span class="plabel">${esc(p.label)}</span>` +
      (p.items.length ? p.items.map((it) => `<span class="chip">${esc(it)}</span>`).join('') : '<span class="chip empty">empty</span>') +
      '</div>';
  });
  if (s.result !== null) html += `<div class="result">Result: <strong>${esc(s.result)}</strong></div>`;
  $(id + '-stage').innerHTML = html;

  const log = $(id + '-log');
  log.innerHTML = v.steps.slice(0, v.idx + 1).map((x, i) =>
    `<div class="log-line${i === v.idx ? ' current' : ''}"><span class="step-no">${i}</span>${esc(x.msg)}</div>`).join('');
  log.scrollTop = log.scrollHeight;

  const play = document.querySelector(`[data-action="play"][data-vis="${id}"]`);
  play.textContent = v.timer ? '⏸ Pause' : '▶ Play';
}

function stop(id) {
  const v = state[id];
  if (v && v.timer) { clearInterval(v.timer); v.timer = null; }
}

function load(id) {
  stop(id);
  try {
    state[id] = { steps: READERS[id](), idx: 0, timer: null };
    render(id);
  } catch (e) {
    $(id + '-stage').innerHTML = `<div class="error">⚠️ ${esc(e.message)}</div>`;
    $(id + '-log').innerHTML = '';
  }
}

function act(id, action) {
  if (action === 'load') return load(id);
  const v = state[id];
  if (!v) return;
  const last = v.steps.length - 1;
  if (action === 'next') { stop(id); if (v.idx < last) v.idx++; }
  else if (action === 'prev') { stop(id); if (v.idx > 0) v.idx--; }
  else if (action === 'reset') { stop(id); v.idx = 0; }
  else if (action === 'play') {
    if (v.timer) stop(id);
    else {
      if (v.idx >= last) v.idx = 0;
      v.timer = setInterval(() => {
        if (v.idx < last) { v.idx++; render(id); }
        if (v.idx >= last) { stop(id); }
        render(id);
      }, 900);
    }
  }
  render(id);
}

/* ---------- start-up (browser only) ---------- */
if (typeof document !== 'undefined') {
  document.addEventListener('click', (e) => {
    const b = e.target.closest('[data-action]');
    if (b) act(b.dataset.vis, b.dataset.action);
    const t = e.target.closest('.tab');
    if (t) {
      Object.keys(state).forEach(stop);
      document.querySelectorAll('.tab').forEach((x) => x.classList.toggle('active', x === t));
      document.querySelectorAll('.panel').forEach((p) => p.classList.toggle('active', p.id === 'panel-' + t.dataset.tab));
      Object.keys(state).forEach(render);
    }
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && e.target.matches('.controls input')) {
      const sec = e.target.closest('.panel');
      const btn = sec.querySelector('[data-action="load"]');
      act(btn.dataset.vis, 'load');
    }
  });
  Object.keys(READERS).forEach(load);
}

if (typeof module !== 'undefined') {
  module.exports = { stepsContainsDuplicate, stepsContainsDuplicateII, stepsBuySell, stepsMajority, stepsMostFrequentEven,
    stepsLongestSubstring, stepsFruits, stepsReplacement, stepsPermutation, stepsMinWindow, stepsWindowMax };
}
