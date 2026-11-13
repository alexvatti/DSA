/* ============================================================
   Stack — Visual Playground
   Every problem is turned into a list of "steps" (snapshots).
   The controller below just walks through that list.
   ============================================================ */

/* ---------- helpers ---------- */
function snap(o) {
  return Object.assign(
    { arr: [], labels: null, mode: 'cells', i: null, win: null, best: null,
      marks: {}, stack: [], ghost: null, panels: [], msg: '', result: null }, o);
}
const P = (label, items) => ({ label, items });
const item = (t, s) => ({ t: String(t), s: s === undefined ? '' : String(s) });

/* ============================================================
   1. Valid Parentheses
   ============================================================ */
function stepsValid(str) {
  const a = [...str], st = [], stack = [];
  const pairs = { ')': '(', ']': '[', '}': '{' };
  const view = () => stack.map((x) => item(x.ch, 'idx ' + x.idx));
  const panels = () => [P('stack size', [String(stack.length)])];
  const base = (o) => snap(Object.assign({ arr: a, stack: view(), panels: panels() }, o));

  st.push(base({ msg: 'Start: empty stack. Push every opener, pop when a closer arrives.' }));
  for (let i = 0; i < a.length; i++) {
    const c = a[i];
    if (!pairs[c]) {
      stack.push({ ch: c, idx: i });
      st.push(base({ i, marks: { [i]: 'add' }, msg: `'${c}' is an opener → push it.` }));
      continue;
    }
    if (!stack.length) {
      st.push(base({ i, marks: { [i]: 'dup' }, result: 'False',
        msg: `'${c}' is a closer but the stack is empty → nothing to match → invalid.` }));
      return st;
    }
    const top = stack[stack.length - 1];
    if (top.ch !== pairs[c]) {
      st.push(base({ i, marks: { [i]: 'dup', [top.idx]: 'dup' }, result: 'False',
        msg: `'${c}' needs '${pairs[c]}' but the top is '${top.ch}' → wrong type or order → invalid.` }));
      return st;
    }
    stack.pop();
    st.push(base({ i, marks: { [i]: 'match', [top.idx]: 'match' }, ghost: item(top.ch, 'idx ' + top.idx),
      msg: `'${c}' matches the top '${top.ch}' → pop.` }));
  }
  const ok = stack.length === 0;
  st.push(base({ result: ok ? 'True' : 'False',
    msg: ok ? 'Stack is empty → every opener was matched.' : `${stack.length} opener(s) still on the stack → unmatched → invalid.` }));
  return st;
}

/* ============================================================
   2. Min Stack  (stack of (value, min so far) pairs)
   ============================================================ */
function stepsMinStack(ops) {
  const labels = ops.map((o) => (o.op === 'push' ? `push(${o.v})` : `${o.op}()`));
  const st = [], stack = [], out = [];
  const view = () => stack.map((x) => item(x.v, 'min ' + x.m));
  const panels = () => [
    P('current min', [stack.length ? String(stack[stack.length - 1].m) : '—']),
    P('outputs', out.map(String))];
  const base = (o) => snap(Object.assign({ arr: labels, mode: 'wide', stack: view(), panels: panels() }, o));

  st.push(base({ msg: 'Start: empty stack. Each entry will be a pair (value, min so far).' }));
  ops.forEach((o, i) => {
    let msg, ghost = null, mark = 'add';
    if (o.op === 'push') {
      const prev = stack.length ? stack[stack.length - 1].m : null;
      const m = prev === null ? o.v : Math.min(o.v, prev);
      stack.push({ v: o.v, m });
      msg = prev === null
        ? `push ${o.v}: first element, so min = ${o.v}. Store (${o.v}, ${m}).`
        : `push ${o.v}: min(${o.v}, ${prev}) = ${m}. Store (${o.v}, ${m}).`;
    } else if (o.op === 'pop') {
      const x = stack.pop();
      ghost = item(x.v, 'min ' + x.m); mark = 'out';
      msg = `pop: remove (${x.v}, ${x.m}). The min of what remains is already stored below.`;
    } else if (o.op === 'top') {
      const x = stack[stack.length - 1];
      out.push(x.v); mark = 'match';
      msg = `top → ${x.v} (the value of the top pair).`;
    } else {
      const x = stack[stack.length - 1];
      out.push(x.m); mark = 'match';
      msg = `getMin → ${x.m} (read the min stored in the top pair, no scanning).`;
    }
    st.push(base({ i, marks: { [i]: mark }, ghost, msg }));
  });
  st.push(base({ msg: 'Done. Every operation took O(1).', result: out.length ? out.join(', ') : '(no outputs)' }));
  return st;
}

/* ============================================================
   3. Daily Temperatures  (monotonic decreasing stack of indices)
   ============================================================ */
function stepsDaily(a) {
  const st = [], stack = [], ans = a.map(() => null);
  const view = () => stack.map((j) => item(a[j] + '°', 'idx ' + j));
  const panels = () => [P('answer so far', ans.map((x) => (x === null ? '?' : String(x))))];
  const base = (o) => snap(Object.assign({ arr: a, stack: view(), panels: panels() }, o));

  st.push(base({ msg: 'Start: empty stack. It will hold indices of days still waiting for a warmer day.' }));
  for (let i = 0; i < a.length; i++) {
    let popped = false;
    while (stack.length && a[i] > a[stack[stack.length - 1]]) {
      const j = stack.pop();
      ans[j] = i - j; popped = true;
      st.push(base({ i, marks: { [j]: 'match', [i]: 'new' }, ghost: item(a[j] + '°', 'idx ' + j),
        msg: `${a[i]}° > ${a[j]}° (day ${j}) → day ${j} waited ${i - j} day(s). Pop it.` }));
    }
    stack.push(i);
    st.push(base({ i, marks: { [i]: 'add' },
      msg: `Push day ${i} (${a[i]}°).${popped ? '' : ' Nobody on the stack was colder, so nothing to resolve.'} It now waits for a warmer day.` }));
  }
  stack.forEach((j) => { ans[j] = 0; });
  st.push(base({ result: '[' + ans.join(', ') + ']',
    msg: stack.length ? `Days still on the stack never saw a warmer day → they stay 0.` : 'Stack is empty → every day found a warmer day.' }));
  return st;
}

/* ============================================================
   4. Car Fleet  (sort by position, stack of arrival times)
   ============================================================ */
function stepsCarFleet(target, pos, spd) {
  const cars = pos.map((p, i) => ({ p, s: spd[i] })).sort((x, y) => y.p - x.p);
  const fmt = (x) => String(Number(x.toFixed(2)));
  const times = cars.map((c) => (target - c.p) / c.s);
  const arr = times.map(fmt), labels = cars.map((c) => 'p' + c.p);
  const st = [], stack = [];
  const view = () => stack.map((t, k) => item(fmt(t), 'fleet ' + (k + 1)));
  const panels = () => [P('target', [String(target)]), P('fleets so far', [String(stack.length)])];
  const base = (o) => snap(Object.assign({ arr, labels, stack: view(), panels: panels() }, o));

  st.push(base({ msg: 'Start: cars sorted from closest to the target to farthest. Each cell shows time = (target − position) / speed.' }));
  times.forEach((t, i) => {
    const top = stack.length ? stack[stack.length - 1] : null;
    if (top === null || t > top) {
      stack.push(t);
      st.push(base({ i, marks: { [i]: 'add' },
        msg: `Car at ${cars[i].p} (speed ${cars[i].s}): time ${fmt(t)}${top === null ? ', nobody ahead' : ` > ${fmt(top)}`} → cannot catch the fleet ahead → new fleet.` }));
    } else {
      st.push(base({ i, marks: { [i]: 'dup' },
        msg: `Car at ${cars[i].p} (speed ${cars[i].s}): time ${fmt(t)} ≤ ${fmt(top)} → it catches up and joins the fleet ahead. No push.` }));
    }
  });
  st.push(base({ result: String(stack.length), msg: `Done → ${stack.length} fleet(s) reach the target.` }));
  return st;
}

/* ============================================================
   5. Largest Rectangle in Histogram  (monotonic increasing stack)
   ============================================================ */
function stepsHistogram(h) {
  const n = h.length, st = [], stack = [];
  let best = 0, bestWin = null;
  const view = () => stack.map((x) => item('h=' + x.h, 'start ' + x.s));
  const panels = () => [P('best area', [String(best)])];
  const base = (o) => snap(Object.assign({ arr: h, mode: 'bars', best: bestWin, stack: view(), panels: panels() }, o));

  st.push(base({ msg: 'Start: empty stack of (start, height). Bars on it can still extend to the right.' }));
  for (let i = 0; i < n; i++) {
    let start = i;
    while (stack.length && stack[stack.length - 1].h > h[i]) {
      const x = stack.pop();
      const area = x.h * (i - x.s), improved = area > best;
      if (improved) { best = area; bestWin = [x.s, i - 1]; }
      start = x.s;
      st.push(base({ i, win: [x.s, i - 1], marks: { [i]: 'new' }, ghost: item('h=' + x.h, 'start ' + x.s),
        msg: `h[${i}] = ${h[i]} < ${x.h} → that bar can't extend further. Width ${i} − ${x.s} = ${i - x.s}, area ${x.h}×${i - x.s} = ${area}.${improved ? ' New best! 🎉' : ''} Pop; the new bar will start at ${x.s}.` }));
    }
    stack.push({ s: start, h: h[i] });
    st.push(base({ i, marks: { [i]: 'add' },
      msg: `Push (start ${start}, h=${h[i]}).${start < i ? ` It inherits start ${start}: it can stretch back over the taller bars it popped.` : ''}` }));
  }
  while (stack.length) {
    const x = stack.pop();
    const area = x.h * (n - x.s), improved = area > best;
    if (improved) { best = area; bestWin = [x.s, n - 1]; }
    st.push(base({ win: [x.s, n - 1], ghost: item('h=' + x.h, 'start ' + x.s),
      msg: `End of array: bar h=${x.h} extends to the end. Width ${n} − ${x.s} = ${n - x.s}, area = ${area}.${improved ? ' New best! 🎉' : ''}` }));
  }
  st.push(base({ result: String(best), msg: `Done → largest rectangle area = ${best}.` }));
  return st;
}

/* ---------- input readers (validate + build steps) ---------- */
const $ = (id) => document.getElementById(id);

function parseNums(str, opts) {
  const o = Object.assign({ max: 20, int: false, min: -Infinity }, opts);
  const parts = str.split(',').map((x) => x.trim()).filter(Boolean);
  if (!parts.length) throw new Error('Enter at least one number, separated by commas.');
  const nums = parts.map(Number);
  if (nums.some((n) => !Number.isFinite(n))) throw new Error('Use numbers only, separated by commas.');
  if (o.int && nums.some((n) => !Number.isInteger(n))) throw new Error('Use whole numbers only.');
  if (nums.some((n) => n < o.min)) throw new Error(`Numbers must be ${o.min} or more.`);
  if (nums.length > o.max) throw new Error(`Use ${o.max} numbers or fewer so the stage stays readable.`);
  return nums;
}
function parseBrackets(str) {
  const v = str.replace(/\s+/g, '');
  if (!v.length) throw new Error('String cannot be empty.');
  if (v.length > 24) throw new Error('Use 24 characters or fewer.');
  if (!/^[()[\]{}]+$/.test(v)) throw new Error('Use only the characters ( ) [ ] { }');
  return v;
}
function parseOps(str) {
  const parts = str.split(',').map((x) => x.trim()).filter(Boolean);
  if (!parts.length) throw new Error('Enter at least one operation.');
  if (parts.length > 16) throw new Error('Use 16 operations or fewer.');
  let size = 0;
  return parts.map((p, n) => {
    let m;
    if ((m = /^push\s*\(?\s*(-?\d+)\s*\)?$/i.exec(p))) { size++; return { op: 'push', v: Number(m[1]) }; }
    const k = p.replace(/[()\s]/g, '').toLowerCase();
    const op = { pop: 'pop', top: 'top', getmin: 'getMin' }[k];
    if (!op) throw new Error(`Operation #${n + 1} ("${p}") is not valid. Use: push 5, pop, top, getMin.`);
    if (!size) throw new Error(`Operation #${n + 1} (${op}) runs on an empty stack.`);
    if (op === 'pop') size--;
    return { op };
  });
}

const READERS = {
  vp: () => stepsValid(parseBrackets($('vp-input').value)),
  ms: () => stepsMinStack(parseOps($('ms-input').value)),
  dt: () => stepsDaily(parseNums($('dt-input').value, { int: true })),
  cf: () => {
    const target = Number($('cf-target').value);
    const pos = parseNums($('cf-pos').value, { max: 12, min: 0 });
    const spd = parseNums($('cf-spd').value, { max: 12 });
    if (!(target > 0)) throw new Error('Target must be greater than 0.');
    if (pos.length !== spd.length) throw new Error('Positions and speeds must have the same length.');
    if (new Set(pos).size !== pos.length) throw new Error('Positions must be distinct.');
    if (pos.some((p) => p >= target)) throw new Error('Every position must be less than the target.');
    if (spd.some((s) => s <= 0)) throw new Error('Speeds must be greater than 0.');
    return stepsCarFleet(target, pos, spd);
  },
  lr: () => stepsHistogram(parseNums($('lr-input').value, { max: 14, int: true, min: 0 })),
};

/* ---------- rendering ---------- */
const esc = (x) => String(x).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const state = {};

function render(id) {
  const v = state[id], s = v.steps[v.idx];
  const inWin = (i) => s.win && i >= s.win[0] && i <= s.win[1];
  const inBest = (i) => s.best && i >= s.best[0] && i <= s.best[1];
  const bars = s.mode === 'bars';
  const max = Math.max(1, ...s.arr.map(Number));

  let html = `<div class="${bars ? 'bars' : 'cells' + (s.mode === 'wide' ? ' wide' : '')}">`;
  s.arr.forEach((val, i) => {
    const cls = [bars ? 'bar' : 'cell'];
    if (inWin(i)) cls.push('in-window');
    if (inBest(i)) cls.push('in-best');
    if (s.marks[i]) cls.push('m-' + s.marks[i]);
    const style = bars ? ` style="height:${Math.round(26 + (Number(val) / max) * 110)}px"` : '';
    const lbl = s.labels ? s.labels[i] : i;
    html += `<div class="${bars ? 'bar-wrap' : 'cell-wrap'}"><div class="${cls.join(' ')}"${style}>${esc(val)}</div>` +
            `<div class="idx">${esc(lbl)}</div><div class="ptr r">${s.i === i ? 'i' : ''}</div></div>`;
  });
  html += '</div>';

  html += '<div class="legend"><span class="lg add">pushed / just added</span><span class="lg cur">current</span>' +
          '<span class="lg match">resolved / matched</span><span class="lg dup">rejected / merged</span>' +
          (s.win || s.best ? '<span class="lg win">span</span><span class="lg best">best</span>' : '') + '</div>';

  html += '<div class="stack-area"><div class="stack-col"><div class="stack-head">▼ TOP OF STACK</div>';
  if (s.ghost) html += `<div class="sitem ghost"><b>${esc(s.ghost.t)}</b><small>${esc(s.ghost.s)} · popped</small></div>`;
  if (!s.stack.length) html += '<div class="sempty">empty</div>';
  for (let k = s.stack.length - 1; k >= 0; k--) {
    const x = s.stack[k];
    html += `<div class="sitem${k === s.stack.length - 1 ? ' top' : ''}"><b>${esc(x.t)}</b><small>${esc(x.s)}</small></div>`;
  }
  html += '<div class="sbase"></div></div></div>';

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
  module.exports = { stepsValid, stepsMinStack, stepsDaily, stepsCarFleet, stepsHistogram, parseOps };
}
