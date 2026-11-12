/* ============================================================
   Hashing — Visual Playground  (script.js)
   ------------------------------------------------------------
   Each visualizer builds an array of "frames". A frame is a
   snapshot: which cells to highlight, what the hash map / set
   looks like right now, and an explanation line.
   A tiny engine renders frames and supports prev/next/play/reset.
   ============================================================ */

"use strict";

/* ---------------- Tab switching ---------------- */
document.getElementById("tabs").addEventListener("click", (e) => {
  const btn = e.target.closest(".tab");
  if (!btn) return;
  document.querySelectorAll(".tab").forEach((t) => t.classList.remove("active"));
  document.querySelectorAll(".panel").forEach((p) => p.classList.remove("active"));
  btn.classList.add("active");
  document.getElementById("panel-" + btn.dataset.tab).classList.add("active");
});

/* ---------------- Helpers ---------------- */
function parseNums(str) {
  return str
    .split(",")
    .map((x) => x.trim())
    .filter((x) => x !== "")
    .map(Number)
    .filter((n) => !Number.isNaN(n));
}

function el(tag, cls, html) {
  const n = document.createElement(tag);
  if (cls) n.className = cls;
  if (html !== undefined) n.innerHTML = html;
  return n;
}

function esc(c) {
  return String(c).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

/* ============================================================
   Generic engine: stores frames per visualizer and renders them
   ============================================================ */
const Engine = {
  state: {}, // vis -> { frames, idx, timer, render }

  init(vis, frames, renderFn) {
    this.stop(vis);
    this.state[vis] = { frames, idx: 0, timer: null, render: renderFn };
    this.show(vis, 0);
  },

  show(vis, idx) {
    const s = this.state[vis];
    if (!s) return;
    s.idx = Math.max(0, Math.min(idx, s.frames.length - 1));
    s.render(s.frames[s.idx], s.idx, s.frames.length);
  },

  next(vis) {
    const s = this.state[vis];
    if (!s) return;
    if (s.idx >= s.frames.length - 1) { this.stop(vis); return; }
    this.show(vis, s.idx + 1);
  },

  prev(vis) {
    const s = this.state[vis];
    if (!s) return;
    this.show(vis, s.idx - 1);
  },

  play(vis) {
    const s = this.state[vis];
    if (!s) return;
    this.stop(vis);
    s.timer = setInterval(() => {
      if (s.idx >= s.frames.length - 1) { this.stop(vis); return; }
      this.next(vis);
    }, 1000);
  },

  stop(vis) {
    const s = this.state[vis];
    if (s && s.timer) { clearInterval(s.timer); s.timer = null; }
  },

  reset(vis) {
    this.stop(vis);
    this.show(vis, 0);
  },
};

/* ============================================================
   Shared renderer: rows of cells + one or more hash maps/sets
   frame = {
     rows:  [ { label?, cells: [ {t, cls?, ptr?} ] } ],
     maps:  [ { title, entries: [ {k, v?, cls?} ] } ],
     msg:   "html"
   }
   ============================================================ */
function cellsOf(arr, cls = {}, ptr = {}) {
  return arr.map((t, i) => ({ t, cls: cls[i], ptr: ptr[i] }));
}

function renderGeneric(stageId, mapsId, logId) {
  const stage = document.getElementById(stageId);
  const maps = document.getElementById(mapsId);
  const log = document.getElementById(logId);
  return (frame) => {
    // ---- cell rows ----
    stage.innerHTML = "";
    const multi = frame.rows.length > 1;
    stage.classList.toggle("multi", multi);
    frame.rows.forEach((row) => {
      const holder = multi ? el("div", "cell-row") : stage;
      if (row.label) holder.appendChild(el("div", "row-label", row.label));
      row.cells.forEach((c, i) => {
        const cell = el("div", "cell");
        if (c.cls) cell.classList.add(c.cls);
        cell.appendChild(el("span", "idx", i));
        cell.appendChild(document.createTextNode(c.t));
        if (c.ptr) cell.appendChild(el("span", "ptr c", c.ptr));
        holder.appendChild(cell);
      });
      if (multi) stage.appendChild(holder);
    });
    // ---- hash maps / sets ----
    maps.innerHTML = "";
    frame.maps.forEach((m) => {
      const box = el("div", "map-box");
      box.appendChild(el("div", "map-title", esc(m.title)));
      const list = el("div", "map-entries");
      if (!m.entries.length) list.appendChild(el("span", "map-empty", "(empty)"));
      m.entries.forEach((e) => {
        const chip = el("span", "entry" + (e.cls ? " " + e.cls : ""));
        chip.innerHTML = e.v === undefined
          ? esc(e.k)
          : `${esc(e.k)}<span class="arrow">→</span><span class="val">${esc(e.v)}</span>`;
        list.appendChild(chip);
      });
      box.appendChild(list);
      maps.appendChild(box);
    });
    log.innerHTML = frame.msg;
  };
}

/* ============================================================
   1. TWO SUM  (map: value -> index)
   ============================================================ */
function buildTwoSum(nums, target) {
  const frames = [];
  const seen = new Map();
  const snap = (hl, cls) => [...seen].map(([k, v]) => ({ k, v, cls: k === hl ? cls : undefined }));
  const mk = (cls, ptr, entries, msg, title = "seen  { value → index }") => ({
    rows: [{ cells: cellsOf(nums, cls, ptr) }],
    maps: [{ title, entries }],
    msg,
  });

  frames.push(mk({}, {}, [], `Target = <span class="num">${target}</span>. <span class="lp">seen</span> starts empty. For each x we look up <b>need = target − x</b>.`));

  for (let i = 0; i < nums.length; i++) {
    const x = nums[i], need = target - x;
    if (seen.has(need)) {
      const j = seen.get(need);
      frames.push(mk({ [i]: "match", [j]: "match" }, { [i]: "▲x", [j]: "▲need" }, snap(need, "hit"),
        `x=${x}, need = ${target}−${x} = <span class="num">${need}</span> → <b>found in map</b> at index ${j} ✓ <span class="done">Answer [${j}, ${i}].</span>`));
      return { frames };
    }
    seen.set(x, i);
    frames.push(mk({ [i]: "cur" }, { [i]: "▲x" }, snap(x, "new"),
      `x=${x}, need = ${target}−${x} = <span class="num">${need}</span> → not in map. Store <span class="lp">${x} → ${i}</span>.`));
  }
  frames.push(mk({}, {}, snap(), `Finished with no pair. <span class="num">No solution.</span>`));
  return { frames };
}

/* ============================================================
   2. VALID ANAGRAM  (map: char -> count)
   ============================================================ */
function buildAnagram(s, t) {
  const frames = [];
  const A = s.split(""), B = t.split("");
  const count = new Map();
  const snap = (hl, cls) => [...count].map(([k, v]) => ({ k, v, cls: k === hl ? cls : undefined }));
  const mk = (ca, pa, cb, pb, entries, msg) => ({
    rows: [
      { label: "s", cells: cellsOf(A, ca, pa) },
      { label: "t", cells: cellsOf(B, cb, pb) },
    ],
    maps: [{ title: "count  { char → how many }", entries }],
    msg,
  });
  const dash = (c) => (c === " " ? "␣" : esc(c));

  if (A.length !== B.length) {
    frames.push(mk({}, {}, {}, {}, [], `Lengths differ (${A.length} vs ${B.length}) → <span class="num">not an anagram</span>.`));
    return { frames };
  }
  frames.push(mk({}, {}, {}, {}, [], `Same length ✓. Pass 1: <b>count</b> every char of <code>s</code>. Pass 2: <b>spend</b> counts with <code>t</code>.`));

  for (let i = 0; i < A.length; i++) {
    count.set(A[i], (count.get(A[i]) || 0) + 1);
    frames.push(mk({ [i]: "cur" }, { [i]: "▲" }, {}, {}, snap(A[i], "new"),
      `Pass 1: '<b>${dash(A[i])}</b>' → count = <span class="num">${count.get(A[i])}</span>.`));
  }
  for (let i = 0; i < B.length; i++) {
    const c = B[i];
    if (!count.get(c)) {
      frames.push(mk({}, {}, { [i]: "mismatch" }, { [i]: "▲" }, snap(c, "miss").concat(count.has(c) ? [] : [{ k: c, v: 0, cls: "miss" }]),
        `Pass 2: '<b>${dash(c)}</b>' has count 0 (or is missing) → <span class="num">✗ not an anagram</span>.`));
      return { frames };
    }
    count.set(c, count.get(c) - 1);
    frames.push(mk({}, {}, { [i]: "cur" }, { [i]: "▲" }, snap(c, "hit"),
      `Pass 2: '<b>${dash(c)}</b>' available → spend one. count = <span class="num">${count.get(c)}</span>.`));
  }
  frames.push(mk({}, {}, Object.fromEntries(B.map((_, i) => [i, "match"])), {}, snap(),
    `All of <code>t</code> was paid for by <code>s</code>. <span class="done">✓ It IS an anagram.</span>`));
  return { frames };
}

/* ============================================================
   3. VALID SUDOKU  (sets per row / col / box)
   ============================================================ */
const SUDOKU_PRESETS = {
  valid: [
    "53..7....", "6..195...", ".98....6.",
    "8...6...3", "4..8.3..1", "7...2...6",
    ".6....28.", "...419..5", "....8..79",
  ],
  invalid: [
    "83..7....", "6..195...", ".98....6.",
    "8...6...3", "4..8.3..1", "7...2...6",
    ".6....28.", "...419..5", "....8..79",
  ],
};

function buildSudoku(rowsStr) {
  const board = rowsStr.map((r) => r.split(""));
  const rows = [...Array(9)].map(() => new Set());
  const cols = [...Array(9)].map(() => new Set());
  const boxes = [...Array(9)].map(() => new Set());
  const done = new Set();
  const frames = [];
  const fmt = (set, hl, cls) => [...set].sort().map((k) => ({ k, cls: k === hl ? cls : undefined }));
  const mk = (cur, clash, r, c, b, hl, hlCls, msg) => ({
    board, cur, clash, done: new Set(done),
    maps: [
      { title: r === null ? "row set" : `rows[${r}]`, entries: r === null ? [] : fmt(rows[r], hl, hlCls) },
      { title: c === null ? "col set" : `cols[${c}]`, entries: c === null ? [] : fmt(cols[c], hl, hlCls) },
      { title: b === null ? "box set" : `boxes[${b}]`, entries: b === null ? [] : fmt(boxes[b], hl, hlCls) },
    ],
    msg,
  });

  frames.push(mk(null, null, null, null, null, null, null,
    `One set per <b>row</b>, <b>column</b> and <b>3×3 box</b>. Scan cells left→right, top→bottom. Box id = <code>(r//3)*3 + c//3</code>.`));

  for (let r = 0; r < 9; r++) {
    for (let c = 0; c < 9; c++) {
      const v = board[r][c];
      if (v === ".") continue;
      const b = Math.floor(r / 3) * 3 + Math.floor(c / 3);
      let where = null, clashAt = null;
      if (rows[r].has(v)) where = "row";
      else if (cols[c].has(v)) where = "column";
      else if (boxes[b].has(v)) where = "box";
      if (where) {
        // find the earlier cell holding the same digit in that group
        for (const key of done) {
          const [rr, cc] = key.split(",").map(Number);
          if (board[rr][cc] !== v) continue;
          const bb = Math.floor(rr / 3) * 3 + Math.floor(cc / 3);
          if ((where === "row" && rr === r) || (where === "column" && cc === c) || (where === "box" && bb === b)) { clashAt = [rr, cc]; break; }
        }
        frames.push(mk([r, c], clashAt, r, c, b, v, "miss",
          `(${r},${c}) = <b>${v}</b> → already in this <span class="num">${where}</span> set ✗ <span class="num">Invalid Sudoku!</span>`));
        return { frames };
      }
      rows[r].add(v); cols[c].add(v); boxes[b].add(v);
      done.add(r + "," + c);
      frames.push(mk([r, c], null, r, c, b, v, "new",
        `(${r},${c}) = <b>${v}</b> → not in row ${r}, col ${c} or box ${b}. Add to all three sets.`));
    }
  }
  frames.push(mk(null, null, null, null, null, null, null, `All filled cells checked, no duplicates. <span class="done">✓ Valid Sudoku.</span>`));
  return { frames };
}

function renderSudoku() {
  const stage = document.getElementById("sd-stage");
  const maps = document.getElementById("sd-maps");
  const log = document.getElementById("sd-log");
  return (frame) => {
    stage.innerHTML = "";
    const grid = el("div", "sudoku");
    for (let r = 0; r < 9; r++) {
      for (let c = 0; c < 9; c++) {
        const v = frame.board[r][c];
        const cell = el("div", "sd-cell", v === "." ? "" : v);
        if (c % 3 === 2 && c !== 8) cell.classList.add("bx-r");
        if (r % 3 === 2 && r !== 8) cell.classList.add("bx-b");
        if (frame.cur) {
          const [cr, cc] = frame.cur;
          const sameBox = Math.floor(cr / 3) === Math.floor(r / 3) && Math.floor(cc / 3) === Math.floor(c / 3);
          if (r === cr || c === cc || sameBox) cell.classList.add("peer");
        }
        if (frame.done.has(r + "," + c)) cell.classList.add("done");
        if (frame.cur && frame.cur[0] === r && frame.cur[1] === c) cell.classList.add(frame.clash || frame.msg.includes("Invalid") ? "clash" : "cur");
        if (frame.clash && frame.clash[0] === r && frame.clash[1] === c) cell.classList.add("clash");
        grid.appendChild(cell);
      }
    }
    stage.appendChild(grid);
    maps.innerHTML = "";
    frame.maps.forEach((m) => {
      const box = el("div", "map-box");
      box.appendChild(el("div", "map-title", esc(m.title)));
      const list = el("div", "map-entries");
      if (!m.entries.length) list.appendChild(el("span", "map-empty", "(empty)"));
      m.entries.forEach((e) => list.appendChild(el("span", "entry" + (e.cls ? " " + e.cls : ""), esc(e.k))));
      box.appendChild(list);
      maps.appendChild(box);
    });
    log.innerHTML = frame.msg;
  };
}

/* ============================================================
   4. LONGEST CONSECUTIVE SEQUENCE  (set)
   ============================================================ */
function buildLongest(nums) {
  const frames = [];
  const set = [...new Set(nums)];
  const has = new Set(set);
  const chips = (cls = {}) => set.map((k) => ({ k, cls: cls[k] }));
  const mk = (cls, chipCls, msg, title = "num_set  { unique values }") => ({
    rows: [{ cells: cellsOf(set, cls) }],
    maps: [{ title, entries: chips(chipCls) }],
    msg,
  });
  if (!set.length) {
    frames.push(mk({}, {}, "Empty input → longest = 0."));
    return { frames };
  }
  let best = 0;
  frames.push(mk({}, {}, `Put everything in a <b>set</b> (duplicates vanish). For each x: if <code>x−1</code> exists, x is mid-run → skip; else x <b>starts</b> a run.`));

  set.forEach((x, i) => {
    if (has.has(x - 1)) {
      frames.push(mk({ [i]: "skip" }, { [x - 1]: "hit" },
        `x=${x}: <span class="num">${x - 1}</span> is in the set → ${x} is in the middle of a run. <b>Skip</b>.`));
      return;
    }
    frames.push(mk({ [i]: "cur" }, { [x]: "new" }, `x=${x}: ${x - 1} is NOT in the set → <span class="lp">${x} starts a run</span>. Count upward.`));
    let len = 1;
    const run = { [x]: "hit" };
    while (has.has(x + len)) {
      run[x + len] = "hit";
      len++;
      frames.push(mk({ [i]: "cur" }, { ...run }, `${x + len - 1} exists → run length = <span class="num">${len}</span>.`));
    }
    best = Math.max(best, len);
    frames.push(mk({ [i]: "cur" }, { ...run }, `${x + len} not in set → run ends. Length <span class="num">${len}</span>. Best so far = <span class="num">${best}</span>.`));
  });
  frames.push(mk({}, {}, `<span class="done">Longest consecutive sequence = ${best}</span>.`));
  return { frames };
}

/* ============================================================
   5. SUBARRAY SUM EQUALS K  (map: prefix -> count)
   ============================================================ */
function buildSubarray(nums, k) {
  const frames = [];
  const freq = new Map([[0, 1]]);
  const snap = (hl, cls) => [...freq].map(([key, v]) => ({ k: key, v, cls: key === hl ? cls : undefined }));
  const mk = (cls, ptr, entries, msg) => ({
    rows: [{ cells: cellsOf(nums, cls, ptr) }],
    maps: [{ title: "freq  { prefix_sum → times seen }", entries }],
    msg,
  });
  let prefix = 0, count = 0;
  frames.push(mk({}, {}, snap(0, "new"), `k = <span class="num">${k}</span>. <code>freq = {0: 1}</code> (the empty prefix). At each i look up <b>prefix − k</b>.`));

  for (let i = 0; i < nums.length; i++) {
    prefix += nums[i];
    const need = prefix - k;
    const found = freq.get(need) || 0;
    count += found;
    const cls = {};
    for (let j = 0; j <= i; j++) cls[j] = "unique";
    cls[i] = found ? "match" : "cur";
    const entriesBefore = snap(found ? need : undefined, "hit");
    frames.push(mk(cls, { [i]: "▲i" }, entriesBefore,
      `prefix = <span class="num">${prefix}</span>, need = ${prefix} − ${k} = <span class="num">${need}</span> → seen <b>${found}</b>× → ` +
      (found ? `<span class="done">+${found} subarray(s)</span>` : `+0`) + `. count = <span class="num">${count}</span>.`));
    freq.set(prefix, (freq.get(prefix) || 0) + 1);
    frames.push(mk(cls, { [i]: "▲i" }, snap(prefix, "new"), `Record prefix <span class="lp">${prefix}</span> → ${freq.get(prefix)} in <code>freq</code>.`));
  }
  frames.push(mk({}, {}, snap(), `<span class="done">Total subarrays with sum ${k} = ${count}</span>.`));
  return { frames };
}

/* ============================================================
   Loaders — wire inputs to builders + renderers
   ============================================================ */
const Loaders = {
  ts() {
    const nums = parseNums(document.getElementById("ts-input").value);
    const target = Number(document.getElementById("ts-target").value);
    Engine.init("ts", buildTwoSum(nums, target).frames, renderGeneric("ts-stage", "ts-maps", "ts-log"));
  },
  an() {
    const s = document.getElementById("an-s").value;
    const t = document.getElementById("an-t").value;
    Engine.init("an", buildAnagram(s, t).frames, renderGeneric("an-stage", "an-maps", "an-log"));
  },
  sd() {
    const key = document.getElementById("sd-preset").value;
    Engine.init("sd", buildSudoku(SUDOKU_PRESETS[key]).frames, renderSudoku());
  },
  lc() {
    const nums = parseNums(document.getElementById("lc-input").value);
    Engine.init("lc", buildLongest(nums).frames, renderGeneric("lc-stage", "lc-maps", "lc-log"));
  },
  sk() {
    const nums = parseNums(document.getElementById("sk-input").value);
    const k = Number(document.getElementById("sk-k").value);
    Engine.init("sk", buildSubarray(nums, k).frames, renderGeneric("sk-stage", "sk-maps", "sk-log"));
  },
};

/* ---------------- Button wiring ---------------- */
document.querySelectorAll("[data-action]").forEach((btn) => {
  btn.addEventListener("click", () => {
    const vis = btn.dataset.vis;
    switch (btn.dataset.action) {
      case "load": Loaders[vis](); break;
      case "next": Engine.next(vis); break;
      case "prev": Engine.prev(vis); break;
      case "play": Engine.play(vis); break;
      case "reset": Engine.reset(vis); break;
    }
  });
});

document.getElementById("sd-preset").addEventListener("change", () => Loaders.sd());

/* ---------------- Auto-load all on first paint ---------------- */
window.addEventListener("DOMContentLoaded", () => {
  Object.values(Loaders).forEach((fn) => fn());
});
