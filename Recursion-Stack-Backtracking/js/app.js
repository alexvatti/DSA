/* Shared page engine: reads window.PROBLEM (made by the build script from real sys.settrace runs of the real code) */
(function () {
  const P = window.PROBLEM, $ = (s, r = document) => r.querySelector(s);
  const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  const hl = line => esc(line).replace(/(#.*$)|("[^"]*")|\b(def|class|while|if|elif|else|return|is|not|and|or|None|True|False|for|in|break)\b|\b(\d+)\b|(?<=def )(\w+)/g,
    (m, c, s, k, n, f) => c ? `<span class="cm">${c}</span>` : s ? `<span class="st">${s}</span>` : k ? `<span class="kw">${k}</span>` : n ? `<span class="nm">${n}</span>` : `<span class="fn">${f}</span>`);
  const M = [
    { icon: '🔁', name: 'Loop', sub: 'for / while', stack: false },
    { icon: '🔂', name: 'Recursion', sub: 'function calls itself', stack: false },
    { icon: '📚', name: 'Recursion + own Stack', sub: 'push down, pop up', stack: true },
    { icon: '🧭', name: 'Own Stack + Backtracking', sub: '(state, go / back)', stack: true }
  ];
  const S = { inp: 0, m: 0, step: [0, 0, 0, 0], timer: null };
  const link = (l, u, c) => `<a class="chip ${c}" href="${u}" target="_blank" rel="noopener">${esc(l)}</a>`;

  $('#app').innerHTML = `
    <div class="topbar"><a href="../index.html">← All problems</a><a href="../index.html#stack">📦 Our Stack (base code)</a><span class="spacer"></span>
      ${P.prev ? `<a href="${P.prev}.html">← ${esc(P.prevTitle)}</a>` : ''}${P.next ? `<a href="${P.next}.html">${esc(P.nextTitle)} →</a>` : ''}</div>
    <h1>${P.id} · ${esc(P.title)}</h1>
    <div class="chips"><span class="chip lv">${esc(P.diff)}</span><span class="chip">${esc(P.tag)}</span>
      ${P.lc.map(x => link('🔗 ' + x[0], x[1], 'lc')).join('')}</div>
    <section class="card"><h2>📝 Problem</h2><p>${esc(P.statement)}</p><pre class="ex">${esc(P.examples.join('\n'))}</pre></section>
    <section class="card"><div class="inputs"><b>Try it with:</b><span id="inputs"></span><span class="dim">(the page replays a real run of the real code)</span></div></section>
    <nav class="tabs" id="tabs"></nav>
    <section class="card" id="method"></section>
    <section class="card"><h2>⚖️ The 4 ways side by side</h2>
      <table class="cmp"><tr><th>Method</th><th>Extra memory</th><th>Weak spot</th></tr>
      <tr><td>🔁 Loop</td><td>O(1) variables</td><td>awkward for tree-shaped problems (subsets, permutations)</td></tr>
      <tr><td>🔂 Recursion</td><td>Python's call stack, O(depth)</td><td>RecursionError at depth ≈ 1000</td></tr>
      <tr><td>📚 Recursion + own stack</td><td>our Stack, O(depth)</td><td>more code than recursion</td></tr>
      <tr><td>🧭 Own stack + backtracking</td><td>our Stack, O(depth)</td><td>most code — but no depth limit, and it is the template for every LeetCode backtracking problem</td></tr></table>
      <p class="idea" style="margin-top:12px">💡 <b>Takeaway:</b> ${esc(P.takeaway)}</p>
      ${P.related.length ? `<p><b>🚀 Next on LeetCode:</b> ${P.related.map(x => link(x[0], x[1], 'lc')).join(' ')}</p>` : ''}</section>`;

  $('#inputs').innerHTML = P.methods[0].runs.map((r, i) => `<button class="ibtn" data-i="${i}">${esc(r.label)}</button>`).join(' ');
  $('#tabs').innerHTML = M.map((m, i) => `<button class="tab" data-m="${i}">${m.icon} ${i + 1} · ${m.name}<small>${m.sub}</small></button>`).join('');
  $('#inputs').onclick = e => { const b = e.target.closest('[data-i]'); if (b) { stop(); S.inp = +b.dataset.i; S.step = [0, 0, 0, 0]; render(); } };
  $('#tabs').onclick = e => { const b = e.target.closest('[data-m]'); if (b) { stop(); S.m = +b.dataset.m; render(); } };

  function stop() { if (S.timer) { clearInterval(S.timer); S.timer = null; const b = $('#play'); if (b) b.textContent = '▶ Play'; } }
  const run = () => P.methods[S.m].runs[S.inp];

  function render() {
    document.querySelectorAll('.ibtn').forEach(b => b.classList.toggle('active', +b.dataset.i === S.inp));
    document.querySelectorAll('.tab').forEach(b => b.classList.toggle('active', +b.dataset.m === S.m));
    const m = P.methods[S.m], mm = M[S.m], n = run().frames.length;
    $('#method').innerHTML = `
      <div class="idea">${mm.icon} <b>${mm.name}.</b> ${esc(m.idea)}</div>
      ${mm.stack ? `<div class="need">📦 This method uses <b>our own Stack</b> — refer to the <a href="../index.html#stack">base code</a> (<code>push</code>, <code>pop</code>, <code>is_empty</code>).</div>` : ''}
      <div class="controls"><button class="btn" id="prev">◀ Prev</button><button class="btn primary" id="play">▶ Play</button><button class="btn" id="next">Next ▶</button><button class="btn" id="reset">⟲ Reset</button>
        <input type="range" id="sl" min="0" max="${n - 1}" value="0"><span class="cnt" id="cnt"></span></div>
      <div class="work">
        <div class="code" id="code">${m.code.split('\n').map((l, i) => `<div class="cl"><span class="ln">${i + 1}</span><span class="tx">${hl(l) || ' '}</span></div>`).join('')}</div>
        <div>
          <div class="panel"><h3>▶ Next line to run</h3><div class="now" id="now"></div><div class="ops" id="ops"></div></div>
          <div class="panel"><h3>Variables</h3><div id="vars"></div></div>
          <div class="panel"><h3>${S.m === 1 ? 'Python call stack (recursion)' : 'Call stack'}</h3><div id="calls"></div></div>
          <div class="panel"><h3>Our own Stack</h3><div id="stks"></div></div>
          <div id="res"></div>
        </div></div>
      <div class="panel" style="margin-top:10px"><h3>Step log</h3><div class="log" id="log"></div></div>`;
    $('#prev').onclick = () => go(-1); $('#next').onclick = () => go(1); $('#reset').onclick = () => { stop(); S.step[S.m] = 0; update(); };
    $('#sl').oninput = e => { stop(); S.step[S.m] = +e.target.value; update(); };
    $('#play').onclick = () => {
      if (S.timer) return stop();
      if (S.step[S.m] >= n - 1) S.step[S.m] = 0;
      $('#play').textContent = '⏸ Pause';
      S.timer = setInterval(() => { if (S.step[S.m] < n - 1) { S.step[S.m]++; update(); } else stop(); }, 750);
      update();
    };
    update();
  }
  function go(d) { stop(); const n = run().frames.length; S.step[S.m] = Math.max(0, Math.min(n - 1, S.step[S.m] + d)); update(); }

  function update() {
    const r = run(), F = r.frames, i = S.step[S.m], f = F[i], pv = F[i - 1];
    document.querySelectorAll('#code .cl').forEach((el, k) => el.classList.toggle('cur', k + 1 === f.l));
    $('#sl').value = i; $('#cnt').textContent = `Step ${i + 1} / ${F.length}`;
    $('#now').textContent = f.n;
    $('#ops').innerHTML = f.o.map(o => `<span class="op ${o.startsWith('push') ? 'push' : 'pop'}">${o.startsWith('push') ? '↓' : '↑'} ${esc(o)}</span>`).join('');
    const ents = Object.entries(f.v);
    $('#vars').innerHTML = ents.length ? `<table class="vars">${ents.map(([k, v]) => `<tr class="${pv && pv.v[k] !== v ? 'chg' : ''}"><td>${esc(k)}</td><td>${esc(v)}</td></tr>`).join('')}</table>` : '<span class="dim">(none yet)</span>';
    $('#calls').innerHTML = S.m === 1
      ? [...f.c].reverse().map((c, k) => `<div class="item call ${k === 0 ? 'top' : ''}">${esc(c)}</div>`).join('')
      : '<span class="dim">Only one function runs, so there is no call stack to watch.</span>';
    $('#stks').innerHTML = M[S.m].stack
      ? `<div class="stks">${f.s.map(([nm, items]) => `<div class="stk"><h4>${esc(nm)}</h4>${items.length ? [...items].reverse().map((x, k) => `<div class="item ${k === 0 ? 'top' : ''}">${esc(x)}</div>`).join('') : '<span class="dim">(empty)</span>'}</div>`).join('') || '<span class="dim">(not created yet)</span>'}</div>`
      : '<span class="dim">This method does not use our own Stack.</span>';
    $('#res').innerHTML = i === F.length - 1 ? `<div class="res">✅ Result = ${esc(r.result)}</div>` : '';
    const from = Math.max(0, i - 7);
    $('#log').innerHTML = F.slice(from, i + 1).map((x, k) => `<div class="${from + k === i ? 'cur' : ''}">${from + k + 1}. ${esc(x.n)}${x.o.length ? '   [' + esc(x.o.join(', ')) + ']' : ''}</div>`).join('');
  }
  document.addEventListener('keydown', e => { if (e.key === 'ArrowRight') go(1); if (e.key === 'ArrowLeft') go(-1); });
  render();
})();
