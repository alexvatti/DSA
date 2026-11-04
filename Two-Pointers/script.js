/* ============================================================
   Two Pointers — Visual Playground  (script.js)
   ------------------------------------------------------------
   Each visualizer builds an array of "frames". A frame is a
   snapshot describing what to highlight + an explanation line.
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
    }, 900);
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
   1. VALID PALINDROME
   ============================================================ */
function buildPalindrome(raw) {
  const s = raw;
  const n = s.length;
  const frames = [];
  let left = 0, right = n - 1;
  const alnum = (c) => /[a-z0-9]/i.test(c);

  frames.push({ left, right, cls: {}, msg: `Start: <span class="lp">left=0</span>, <span class="rp">right=${n - 1}</span>. Compare front vs back.` });

  let ok = true;
  while (left < right) {
    while (left < right && !alnum(s[left])) {
      frames.push({ left, right, cls: { [left]: "skip" }, msg: `'<b>${escapeHtml(s[left])}</b>' at ${left} is not alphanumeric → skip, <span class="lp">left→${left + 1}</span>.` });
      left++;
    }
    while (left < right && !alnum(s[right])) {
      frames.push({ left, right, cls: { [right]: "skip" }, msg: `'<b>${escapeHtml(s[right])}</b>' at ${right} is not alphanumeric → skip, <span class="rp">right→${right - 1}</span>.` });
      right--;
    }
    if (left >= right) break;
    const a = s[left].toLowerCase(), b = s[right].toLowerCase();
    if (a === b) {
      frames.push({ left, right, cls: { [left]: "match", [right]: "match" }, msg: `'<b>${escapeHtml(s[left])}</b>' == '<b>${escapeHtml(s[right])}</b>' ✓ match. Move both inward.` });
      left++; right--;
    } else {
      frames.push({ left, right, cls: { [left]: "mismatch", [right]: "mismatch" }, msg: `'<b>${escapeHtml(s[left])}</b>' ≠ '<b>${escapeHtml(s[right])}</b>' ✗ <span class="num">Not a palindrome!</span>`, done: false });
      ok = false;
      break;
    }
  }
  if (ok) frames.push({ left, right, cls: {}, msg: `Pointers met. <span class="done">✓ It IS a palindrome.</span>`, done: true });

  return { chars: s.split(""), frames };
}

function escapeHtml(c) {
  return c.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/ /g, "␣");
}

function renderPalindrome(data) {
  const stage = document.getElementById("pal-stage");
  const log = document.getElementById("pal-log");
  return (frame) => {
    stage.innerHTML = "";
    data.chars.forEach((c, i) => {
      const cell = el("div", "cell");
      if (frame.cls[i]) cell.classList.add(frame.cls[i]);
      cell.appendChild(el("span", "idx", i));
      cell.appendChild(document.createTextNode(c === " " ? "␣" : c));
      const ptrs = [];
      if (i === frame.left) ptrs.push('<span class="ptr l">▲L</span>');
      if (i === frame.right) ptrs.push('<span class="ptr r">▲R</span>');
      if (ptrs.length) cell.appendChild(el("span", "ptr", ptrs.join(" ")));
      stage.appendChild(cell);
    });
    log.innerHTML = frame.msg;
  };
}

/* ============================================================
   2. TWO SUM SORTED
   ============================================================ */
function buildTwoSum(nums, target) {
  const frames = [];
  let left = 0, right = nums.length - 1;
  frames.push({ left, right, cls: {}, msg: `Target = <span class="num">${target}</span>. Start wide: <span class="lp">left=0</span>, <span class="rp">right=${right}</span>.` });
  let found = false;
  while (left < right) {
    const sum = nums[left] + nums[right];
    if (sum === target) {
      frames.push({ left, right, cls: { [left]: "match", [right]: "match" }, msg: `${nums[left]} + ${nums[right]} = <span class="num">${sum}</span> = target ✓ <span class="done">Found pair [${left + 1}, ${right + 1}] (1-indexed).</span>`, done: true });
      found = true;
      break;
    } else if (sum < target) {
      frames.push({ left, right, cls: {}, msg: `${nums[left]} + ${nums[right]} = <span class="num">${sum}</span> &lt; ${target} → too small, <span class="lp">left→${left + 1}</span>.` });
      left++;
    } else {
      frames.push({ left, right, cls: {}, msg: `${nums[left]} + ${nums[right]} = <span class="num">${sum}</span> &gt; ${target} → too big, <span class="rp">right→${right - 1}</span>.` });
      right--;
    }
  }
  if (!found) frames.push({ left, right, cls: {}, msg: `Pointers met with no match. <span class="num">No valid pair.</span>`, done: true });
  return { nums, frames };
}

function renderCells(stageId, logId, data) {
  const stage = document.getElementById(stageId);
  const log = document.getElementById(logId);
  return (frame) => {
    stage.innerHTML = "";
    data.nums.forEach((v, i) => {
      const cell = el("div", "cell");
      if (frame.cls[i]) cell.classList.add(frame.cls[i]);
      cell.appendChild(el("span", "idx", i));
      cell.appendChild(document.createTextNode(v));
      const ptrs = [];
      if (i === frame.left) ptrs.push('<span class="ptr l">▲L</span>');
      if (i === frame.right) ptrs.push('<span class="ptr r">▲R</span>');
      if (i === frame.fixed) ptrs.push('<span class="ptr i">▲i</span>');
      if (ptrs.length) cell.appendChild(el("span", "ptr", ptrs.join(" ")));
      stage.appendChild(cell);
    });
    log.innerHTML = frame.msg;
  };
}

/* ============================================================
   3. 3SUM
   ============================================================ */
function buildThreeSum(input) {
  const nums = input.slice().sort((a, b) => a - b);
  const frames = [];
  const results = [];
  const n = nums.length;
  frames.push({ i: -1, left: -1, right: -1, cls: {}, results: [], msg: `Sorted: [${nums.join(", ")}]. We'll fix one number and Two-Sum the rest.` });

  for (let i = 0; i < n; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) {
      frames.push({ i, left: -1, right: -1, cls: { [i]: "skip" }, results: results.slice(), msg: `nums[${i}]=${nums[i]} duplicates previous → skip i.` });
      continue;
    }
    if (nums[i] > 0) {
      frames.push({ i, left: -1, right: -1, cls: { [i]: "skip" }, results: results.slice(), msg: `nums[${i}]=${nums[i]} &gt; 0 and sorted → no triplet can sum to 0. Stop.` });
      break;
    }
    let left = i + 1, right = n - 1;
    frames.push({ i, left, right, cls: {}, results: results.slice(), msg: `Fix <span class="num">nums[${i}]=${nums[i]}</span>. Find two that sum to ${-nums[i]}. <span class="lp">left=${left}</span>, <span class="rp">right=${right}</span>.` });
    while (left < right) {
      const s = nums[i] + nums[left] + nums[right];
      if (s === 0) {
        results.push([nums[i], nums[left], nums[right]]);
        frames.push({ i, left, right, cls: { [i]: "fixed", [left]: "match", [right]: "match" }, results: results.slice(), msg: `${nums[i]} + ${nums[left]} + ${nums[right]} = <span class="num">0</span> ✓ <span class="done">Triplet found!</span> Move both inward & skip dups.` });
        left++; right--;
        while (left < right && nums[left] === nums[left - 1]) left++;
        while (left < right && nums[right] === nums[right + 1]) right--;
      } else if (s < 0) {
        frames.push({ i, left, right, cls: { [i]: "fixed" }, results: results.slice(), msg: `${nums[i]} + ${nums[left]} + ${nums[right]} = <span class="num">${s}</span> &lt; 0 → <span class="lp">left→${left + 1}</span>.` });
        left++;
      } else {
        frames.push({ i, left, right, cls: { [i]: "fixed" }, results: results.slice(), msg: `${nums[i]} + ${nums[left]} + ${nums[right]} = <span class="num">${s}</span> &gt; 0 → <span class="rp">right→${right - 1}</span>.` });
        right--;
      }
    }
  }
  frames.push({ i: -1, left: -1, right: -1, cls: {}, results: results.slice(), msg: `<span class="done">Done.</span> Found ${results.length} unique triplet(s).` });
  return { nums, frames };
}

function renderThreeSum(data) {
  const stage = document.getElementById("th-stage");
  const log = document.getElementById("th-log");
  const found = document.getElementById("th-found");
  return (frame) => {
    stage.innerHTML = "";
    data.nums.forEach((v, idx) => {
      const cell = el("div", "cell");
      if (frame.cls[idx]) cell.classList.add(frame.cls[idx]);
      cell.appendChild(el("span", "idx", idx));
      cell.appendChild(document.createTextNode(v));
      const ptrs = [];
      if (idx === frame.i) ptrs.push('<span class="ptr i">▲i</span>');
      if (idx === frame.left) ptrs.push('<span class="ptr l">▲L</span>');
      if (idx === frame.right) ptrs.push('<span class="ptr r">▲R</span>');
      if (ptrs.length) cell.appendChild(el("span", "ptr", ptrs.join(" ")));
      stage.appendChild(cell);
    });
    found.innerHTML = "";
    (frame.results || []).forEach((t) => {
      found.appendChild(el("span", "triplet", `[${t.join(", ")}]`));
    });
    log.innerHTML = frame.msg;
  };
}

/* ============================================================
   4. CONTAINER WITH MOST WATER
   ============================================================ */
function buildContainer(height) {
  const frames = [];
  let left = 0, right = height.length - 1, best = 0, bestL = 0, bestR = 0;
  while (left < right) {
    const width = right - left;
    const h = Math.min(height[left], height[right]);
    const area = width * h;
    let improved = false;
    if (area > best) { best = area; bestL = left; bestR = right; improved = true; }
    const moveLeft = height[left] < height[right];
    frames.push({
      left, right, bestL, bestR, best, area, h, width,
      msg: `width=${width} × min(${height[left]}, ${height[right]})=${h} → area=<span class="num">${area}</span>. ${improved ? '<span class="done">New best!</span> ' : ""}Shorter line is ${moveLeft ? '<span class="lp">left</span>, move left→' + (left + 1) : '<span class="rp">right</span>, move right→' + (right - 1)}.`,
    });
    if (moveLeft) left++; else right--;
  }
  frames.push({ left, right, bestL, bestR, best, area: best, final: true, msg: `<span class="done">Max water = ${best}</span> between lines ${bestL} and ${bestR}.` });
  return { height, frames };
}

function renderBars(stageId, logId, data, opts) {
  const stage = document.getElementById(stageId);
  const log = document.getElementById(logId);
  const maxH = Math.max(...data.height, 1);
  const unit = 230 / maxH; // px per height unit
  return (frame) => {
    stage.innerHTML = "";
    data.height.forEach((v, i) => {
      const wrap = el("div", "bar-wrap");
      const bar = el("div", "bar");
      bar.style.height = (v * unit) + "px";
      if (i === frame.left) bar.classList.add("left");
      if (i === frame.right) bar.classList.add("right");

      // water fill for rain water
      if (opts.water && frame.waterLevels) {
        const w = frame.waterLevels[i] || 0;
        if (w > 0) {
          const wf = el("div", "water-fill");
          wf.style.height = (w * unit) + "px";
          if (frame.activeWater === i) wf.classList.add("active");
          wrap.appendChild(wf);
        }
      }

      wrap.appendChild(el("div", "bar-val", v));
      wrap.appendChild(bar);
      wrap.appendChild(el("div", "bar-label", i));
      const ptrs = [];
      if (i === frame.left) ptrs.push('<span class="ptr l">▲L</span>');
      if (i === frame.right) ptrs.push('<span class="ptr r">▲R</span>');
      if (ptrs.length) wrap.appendChild(el("span", "bar-ptr", ptrs.join(" ")));
      stage.appendChild(wrap);
    });

    // area overlay for container
    if (opts.area && frame.left >= 0 && frame.right >= 0 && frame.left < frame.right) {
      requestAnimationFrame(() => {
        const wraps = stage.querySelectorAll(".bar-wrap");
        const lw = wraps[frame.left], rw = wraps[frame.right];
        if (!lw || !rw) return;
        const sRect = stage.getBoundingClientRect();
        const lRect = lw.getBoundingClientRect();
        const rRect = rw.getBoundingClientRect();
        const ov = el("div", "area-overlay");
        const leftX = lRect.left - sRect.left + stage.scrollLeft;
        const rightX = rRect.right - sRect.left + stage.scrollLeft;
        ov.style.left = leftX + "px";
        ov.style.width = (rightX - leftX) + "px";
        ov.style.height = (frame.h * unit) + "px";
        ov.style.bottom = "54px";
        stage.appendChild(ov);
      });
    }
    log.innerHTML = frame.msg;
  };
}

/* ============================================================
   5. TRAPPING RAIN WATER
   ============================================================ */
function buildRain(height) {
  const frames = [];
  const n = height.length;
  if (n === 0) {
    frames.push({ left: -1, right: -1, waterLevels: [], msg: "Empty input → 0 water." });
    return { height, frames };
  }
  let left = 0, right = n - 1, leftMax = 0, rightMax = 0, water = 0;
  const levels = new Array(n).fill(0);
  frames.push({ left, right, waterLevels: levels.slice(), msg: `Start: <span class="lp">left=0</span>, <span class="rp">right=${n - 1}</span>, leftMax=0, rightMax=0, water=0.` });
  while (left < right) {
    if (height[left] < height[right]) {
      if (height[left] >= leftMax) {
        leftMax = height[left];
        frames.push({ left, right, activeWater: left, waterLevels: levels.slice(), msg: `Left shorter. height[${left}]=${height[left]} ≥ leftMax → new wall, leftMax=${leftMax}. No water here. left→${left + 1}.` });
      } else {
        const add = leftMax - height[left];
        levels[left] = add;
        water += add;
        frames.push({ left, right, activeWater: left, waterLevels: levels.slice(), msg: `Left shorter. Trap leftMax−h = ${leftMax}−${height[left]} = <span class="num">${add}</span> water. Total=<span class="num">${water}</span>. left→${left + 1}.` });
      }
      left++;
    } else {
      if (height[right] >= rightMax) {
        rightMax = height[right];
        frames.push({ left, right, activeWater: right, waterLevels: levels.slice(), msg: `Right shorter/equal. height[${right}]=${height[right]} ≥ rightMax → new wall, rightMax=${rightMax}. No water here. right→${right - 1}.` });
      } else {
        const add = rightMax - height[right];
        levels[right] = add;
        water += add;
        frames.push({ left, right, activeWater: right, waterLevels: levels.slice(), msg: `Right shorter/equal. Trap rightMax−h = ${rightMax}−${height[right]} = <span class="num">${add}</span> water. Total=<span class="num">${water}</span>. right→${right - 1}.` });
      }
      right--;
    }
  }
  frames.push({ left, right, waterLevels: levels.slice(), msg: `<span class="done">Total trapped water = ${water}</span>.` });
  return { height, frames };
}

/* ============================================================
   6. REMOVE DUPLICATES (slow & fast)
   ============================================================ */
function buildDedupe(nums) {
  const frames = [];
  const arr = nums.slice();
  const n = arr.length;
  if (n === 0) {
    frames.push({ slow: -1, fast: -1, arr: [], written: 0, msg: "Empty array → length 0." });
    return { frames };
  }
  let slow = 0;
  frames.push({ slow, fast: -1, arr: arr.slice(), written: 1, msg: `<span class="lp">slow=0</span> (first element always unique). Scan with fast from 1.` });
  for (let fast = 1; fast < n; fast++) {
    if (arr[fast] !== arr[slow]) {
      slow++;
      arr[slow] = arr[fast];
      frames.push({ slow, fast, arr: arr.slice(), written: slow + 1, msg: `arr[${fast}]=${arr[fast]} ≠ arr[slow] → NEW value. slow→${slow}, write it. Unique so far = ${slow + 1}.` });
    } else {
      frames.push({ slow, fast, arr: arr.slice(), written: slow + 1, msg: `arr[${fast}]=${arr[fast]} == arr[slow]=${arr[slow]} → duplicate, skip. <span class="rp">fast</span> moves on.` });
    }
  }
  frames.push({ slow, fast: n, arr: arr.slice(), written: slow + 1, final: true, msg: `<span class="done">Done. New length k = ${slow + 1}</span>. Unique part: [${arr.slice(0, slow + 1).join(", ")}].` });
  return { frames };
}

function renderDedupe(data) {
  const stage = document.getElementById("dd-stage");
  const log = document.getElementById("dd-log");
  return (frame) => {
    stage.innerHTML = "";
    frame.arr.forEach((v, i) => {
      const cell = el("div", "cell");
      if (i < frame.written) cell.classList.add("unique");
      else if (frame.final) cell.classList.add("dropped");
      if (i === frame.slow) cell.classList.add("slow");
      if (i === frame.fast) cell.classList.add("fast");
      cell.appendChild(el("span", "idx", i));
      cell.appendChild(document.createTextNode(v));
      const ptrs = [];
      if (i === frame.slow) ptrs.push('<span class="ptr s">▲slow</span>');
      if (i === frame.fast) ptrs.push('<span class="ptr f">▲fast</span>');
      if (ptrs.length) cell.appendChild(el("span", "ptr", ptrs.join(" ")));
      stage.appendChild(cell);
    });
    log.innerHTML = frame.msg;
  };
}

/* ============================================================
   Loaders — wire inputs to builders + renderers
   ============================================================ */
const Loaders = {
  pal() {
    const raw = document.getElementById("pal-input").value;
    const data = buildPalindrome(raw);
    Engine.init("pal", data.frames, renderPalindrome(data));
  },
  ts() {
    const nums = parseNums(document.getElementById("ts-input").value);
    const target = Number(document.getElementById("ts-target").value);
    const data = buildTwoSum(nums, target);
    Engine.init("ts", data.frames, renderCells("ts-stage", "ts-log", data));
  },
  th() {
    const nums = parseNums(document.getElementById("th-input").value);
    const data = buildThreeSum(nums);
    Engine.init("th", data.frames, renderThreeSum(data));
  },
  cw() {
    const height = parseNums(document.getElementById("cw-input").value);
    const data = buildContainer(height);
    Engine.init("cw", data.frames, renderBars("cw-stage", "cw-log", data, { area: true }));
  },
  rw() {
    const height = parseNums(document.getElementById("rw-input").value);
    const data = buildRain(height);
    Engine.init("rw", data.frames, renderBars("rw-stage", "rw-log", data, { water: true }));
  },
  dd() {
    const nums = parseNums(document.getElementById("dd-input").value);
    const data = buildDedupe(nums);
    Engine.init("dd", data.frames, renderDedupe(data));
  },
};

/* ---------------- Button wiring ---------------- */
document.querySelectorAll("[data-action]").forEach((btn) => {
  btn.addEventListener("click", () => {
    const vis = btn.dataset.vis;
    const action = btn.dataset.action;
    switch (action) {
      case "load": Loaders[vis](); break;
      case "next": Engine.next(vis); break;
      case "prev": Engine.prev(vis); break;
      case "play": Engine.play(vis); break;
      case "reset": Engine.reset(vis); break;
    }
  });
});

/* ---------------- Auto-load all on first paint ---------------- */
window.addEventListener("DOMContentLoaded", () => {
  Object.values(Loaders).forEach((fn) => fn());
});
