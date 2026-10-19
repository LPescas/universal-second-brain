/**
 * Second Brain Dashboard — app.js
 * Architecture: Cloud-ready data layer with local fetch fallback
 * Future: Replace DATA_CONFIG.mode = 'local' with 'cloud' to switch to API
 */

'use strict';

// ============================================================
// CONFIGURATION — Cloud-ready switch point
// ============================================================
const DATA_CONFIG = {
  mode: 'local',  // 'local' | 'cloud'
  cloudBaseUrl: 'https://your-second-brain-api.com/api',  // future cloud URL
  localPaths: {
    healthReport:   '../scripts/health_report.json',
    metricsExport:  '../scripts/metrics_export.json',
    masterIndex:    '../MASTER_INDEX.yaml',   // text fetch only
    learningLog:    '../learning_log.md',      // text fetch only
    reposData:      'repos_data.json',
    graphData:      'graph_data.json',
    projectsGraphData: 'projects_graph_data.json',
  },
};

// Static project data derived from MASTER_INDEX (fallback + enriched)
const STATIC_PROJECTS = [
  {
    id: 'rpa',
    name: 'UNIQ RPA',
    path: 'C:/Projetos/RPA',
    status: 'active',
    tech: ['python', 'flask', 'selenium', 'sqlite', 'html', 'js'],
    modules: 6,
    description: 'Suite de automacao corporativa para Clinica UNIQ',
    context_file: 'projects/rpa_context.md',
  },
  {
    id: 'wrpe_recorder',
    name: 'WRPE Recorder',
    path: 'C:/Projetos/WRPE_Recorder',
    status: 'active',
    tech: ['python', 'playwright', 'selenium', 'sqlite', 'chrome-extension'],
    modules: 1,
    description: 'Gravacao e reproducao de interacoes web de alta fidelidade',
    context_file: 'projects/wrpe_recorder_context.md',
  },
  {
    id: 'ecosistema global',
    name: 'Second Brain (Ecossistema)',
    path: 'C:/Users/USER/.second_brain',
    status: 'active',
    tech: ['markdown', 'yaml', 'python', 'powershell', 'html', 'js', 'css'],
    modules: 12,
    description: 'Sistema central de memória, regras e governança para a IA (AG Kit)',
    context_file: 'MASTER_INDEX.yaml',
  },
];

// Static knowledge domains
const STATIC_KNOWLEDGE = [
  { id: 'rpa_architecture', name: 'RPA Architecture & Automação UNIQ', icon: '🤖', category: 'Robótica & Automação Web', triggers: ['rpa', 'automation', 'selenium', 'driver', 'orchestrator'], file: 'knowledge/rpa_architecture.md', rules_count: 7 },
  { id: 'frontend_patterns', name: 'Frontend Patterns & Design System', icon: '🎨', category: 'Interface do Usuário & UX', triggers: ['html', 'css', 'js', 'react', 'next', 'ui', 'design'], file: 'knowledge/frontend_patterns.md', rules_count: 5 },
  { id: 'python_patterns', name: 'Python Patterns & Clean Code', icon: '🐍', category: 'Engenharia de Software', triggers: ['python', 'flask', 'fastapi', 'async', 'typing'], file: 'knowledge/python_patterns.md', rules_count: 4 },
  { id: 'governance', name: 'Governança Zero Trust & AG Kit', icon: '🛡️', category: 'Governança & Segurança', triggers: ['governance', 'zero-trust', 'compliance', 'audit', 'documentation'], file: 'knowledge/governance.md', rules_count: 4 },
  { id: 'devops_infra', name: 'DevOps, Deploy & Servidores Locais', icon: '⚡', category: 'Infraestrutura & Deploy', triggers: ['deploy', 'docker', 'ci', 'server', 'infra'], file: 'knowledge/devops_infra.md', rules_count: 3 },
  { id: 'user_preferences', name: 'Preferências & Memória do Usuário', icon: '🧠', category: 'Memória Central da Máquina', triggers: ['preferencias', 'usuario', 'perfil', 'memoria', 'estilo'], file: '.agents/memory/user-preferences.md', rules_count: 5 },
];

// ============================================================
// DATA LAYER — fetch with local/cloud abstraction
// ============================================================

async function fetchLocal(relativePath) {
  try {
    const res = await fetch(relativePath + '?t=' + Date.now());
    if (!res.ok) return null;
    const ct = res.headers.get('content-type') || '';
    if (ct.includes('json')) return await res.json();
    return await res.text();
  } catch {
    return null;
  }
}

async function fetchData(key) {
  if (DATA_CONFIG.mode === 'cloud') {
    try {
      const res = await fetch(`${DATA_CONFIG.cloudBaseUrl}/${key}`);
      return res.ok ? res.json() : null;
    } catch {
      return null;
    }
  }
  return fetchLocal(DATA_CONFIG.localPaths[key] || null);
}

async function loadHealthReport() {
  return await fetchData('healthReport');
}

async function loadMetricsExport() {
  return await fetchData('metricsExport');
}

// ============================================================
// DEMO DATA — shown when real data not available (first run)
// ============================================================

function getDemoMetrics() {
  return {
    generated_at: new Date().toISOString(),
    all_time: {
      total_interactions: 0,
      sb_usage_rate: 0,
      total_files_read: 0,
      total_files_avoided: 0,
      total_tokens_saved: 0,
      total_sb_updates: 0,
      avg_files_per_interaction: 0,
      efficiency_ratio: 0,
    },
    last_7_days: { total_interactions: 0, total_tokens_saved: 0, total_files_avoided: 0 },
    last_30_days: { total_interactions: 0, total_tokens_saved: 0 },
    by_project: [],
    timeline_30d: Array.from({ length: 30 }, (_, i) => ({
      date: new Date(Date.now() - (29 - i) * 86400000).toISOString().slice(0, 10),
      tokens_saved: 0,
    })),
    recent_entries: [],
  };
}

function getDemoHealth() {
  return {
    timestamp: new Date().toISOString(),
    status: 'OK',
    files: [
      { file: 'MASTER_INDEX.yaml', exists: true, size_bytes: 3100 },
      { file: 'global_rules.md', exists: true, size_bytes: 4200 },
      { file: 'behavioral_patterns.yaml', exists: true, size_bytes: 2676 },
      { file: 'active_behavior_rules.yaml', exists: true, size_bytes: 5200 },
      { file: 'learning_log.md', exists: true, size_bytes: 2908 },
    ],
    master_index: { ok: true, lines: 163, limit: 300 },
    learning_log: { ok: true, lines: 66, size_kb: 2.8, pending_entries: 1, needs_consolidation: false },
    project_contexts: [
      { project: 'rpa', age_days: 0, stale: false, size_bytes: 4800 },
      { project: 'wrpe_recorder', age_days: 0, stale: false, size_bytes: 2200 },
      { project: 'automationtest_122844', age_days: 0, stale: false, size_bytes: 1200 },
    ],
    issues: [],
  };
}

// ============================================================
// FORMATTING HELPERS
// ============================================================

function formatNumber(n) {
  if (n == null || isNaN(n)) return '—';
  if (n >= 1000000) return (n / 1000000).toFixed(1) + 'M';
  if (n >= 1000) return (n / 1000).toFixed(1) + 'K';
  return String(Math.round(n));
}

function formatDate(iso) {
  if (!iso) return '—';
  try {
    const d = new Date(iso);
    return d.toLocaleDateString('pt-BR', { day: '2-digit', month: '2-digit', year: '2-digit' }) +
           ' ' + d.toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' });
  } catch { return iso; }
}

function pct(n) {
  return n != null ? `${Math.round(n)}%` : '—';
}

// ============================================================
// TIMELINE CHART — canvas sparkline
// ============================================================

function drawTimeline(canvasId, data) {
  const canvas = document.getElementById(canvasId);
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  const dpr = window.devicePixelRatio || 1;
  const rect = canvas.getBoundingClientRect();

  canvas.width  = rect.width * dpr;
  canvas.height = 140 * dpr;
  ctx.scale(dpr, dpr);

  const W = rect.width;
  const H = 140;
  const PAD = { top: 10, right: 10, bottom: 24, left: 40 };
  const innerW = W - PAD.left - PAD.right;
  const innerH = H - PAD.top - PAD.bottom;

  const values = data.map(d => d.tokens_saved || 0);
  const maxVal = Math.max(...values, 1);
  const minVal = 0;

  // Clear
  ctx.clearRect(0, 0, W, H);

  // Grid lines
  ctx.strokeStyle = 'rgba(255,255,255,0.04)';
  ctx.lineWidth = 1;
  [0.25, 0.5, 0.75, 1].forEach(frac => {
    const y = PAD.top + innerH * (1 - frac);
    ctx.beginPath();
    ctx.moveTo(PAD.left, y);
    ctx.lineTo(PAD.left + innerW, y);
    ctx.stroke();
  });

  // Y axis labels
  ctx.fillStyle = 'rgba(148,163,184,0.6)';
  ctx.font = '10px Inter';
  ctx.textAlign = 'right';
  [0, 0.5, 1].forEach(frac => {
    const y = PAD.top + innerH * (1 - frac) + 3;
    const label = formatNumber(Math.round(maxVal * frac));
    ctx.fillText(label, PAD.left - 6, y);
  });

  // X axis labels (every 5 days)
  ctx.textAlign = 'center';
  data.forEach((d, i) => {
    if (i % 5 === 0 || i === data.length - 1) {
      const x = PAD.left + (i / (data.length - 1)) * innerW;
      const y = H - 6;
      ctx.fillText(d.date.slice(5), x, y);
    }
  });

  if (values.every(v => v === 0)) {
    // No data state
    ctx.fillStyle = 'rgba(148,163,184,0.3)';
    ctx.font = '13px Inter';
    ctx.textAlign = 'center';
    ctx.fillText('Sem dados ainda — aguardando primeiras interacoes', W / 2, H / 2);
    return;
  }

  // Gradient fill
  const gradient = ctx.createLinearGradient(0, PAD.top, 0, PAD.top + innerH);
  gradient.addColorStop(0, 'rgba(59,130,246,0.3)');
  gradient.addColorStop(1, 'rgba(59,130,246,0.02)');

  ctx.beginPath();
  data.forEach((d, i) => {
    const x = PAD.left + (i / (data.length - 1)) * innerW;
    const y = PAD.top + innerH * (1 - (d.tokens_saved - minVal) / (maxVal - minVal));
    if (i === 0) ctx.moveTo(x, y);
    else ctx.lineTo(x, y);
  });

  // Close for fill
  const lastX = PAD.left + innerW;
  const baseY = PAD.top + innerH;
  ctx.lineTo(lastX, baseY);
  ctx.lineTo(PAD.left, baseY);
  ctx.closePath();
  ctx.fillStyle = gradient;
  ctx.fill();

  // Line
  ctx.beginPath();
  ctx.strokeStyle = '#3b82f6';
  ctx.lineWidth = 2;
  ctx.lineJoin = 'round';
  data.forEach((d, i) => {
    const x = PAD.left + (i / (data.length - 1)) * innerW;
    const y = PAD.top + innerH * (1 - (d.tokens_saved - minVal) / (maxVal - minVal));
    if (i === 0) ctx.moveTo(x, y);
    else ctx.lineTo(x, y);
  });
  ctx.stroke();

  // Dots on data points (only where > 0)
  data.forEach((d, i) => {
    if (d.tokens_saved > 0) {
      const x = PAD.left + (i / (data.length - 1)) * innerW;
      const y = PAD.top + innerH * (1 - (d.tokens_saved - minVal) / (maxVal - minVal));
      ctx.beginPath();
      ctx.arc(x, y, 3, 0, Math.PI * 2);
      ctx.fillStyle = '#60a5fa';
      ctx.fill();
      ctx.strokeStyle = '#0d1220';
      ctx.lineWidth = 1.5;
      ctx.stroke();
    }
  });
}

// ============================================================
// SECTION RENDERERS
// ============================================================

function renderDashboard(metrics, health) {
  if (typeof metrics === 'string') { metrics = {}; }
  const at = metrics.all_time || {};
  const ba = metrics.before_after || {};
  const baWith = ba.with_sb || {};
  const baWithout = ba.without_sb || {};

  // KPIs
  const set = function(id, val) {
    var el = document.getElementById(id);
    if (el) el.textContent = val;
  };

  // Tokens Today
  let tokensToday = 0;
  const todayStr = new Date().toISOString().slice(0, 10);
  if (metrics.daily_timeline && metrics.daily_timeline.length > 0) {
    const todayEntry = metrics.daily_timeline.find(d => d.date === todayStr);
    tokensToday = todayEntry ? todayEntry.total_tokens : metrics.daily_timeline[metrics.daily_timeline.length - 1].total_tokens;
  }
  set('val-tokens-today', formatNumber(tokensToday));

  set('val-interactions', formatNumber(at.total_interactions));
  set('val-tokens', formatNumber(at.avg_tokens_per_session));
  set('val-duration', (at.avg_duration_per_session || 0) + ' min');
  set('val-efficiency', formatNumber(at.efficiency_tokens_per_minute) + ' /min');

  // System Census KPI
  if (metrics.system_census) {
    const c = metrics.system_census;
    set('val-census', `${c.skills_count} Skills / ${c.repos_count} Repos`);
  } else {
    set('val-census', '47 Skills / 25 Repos');
  }

  // Total spent badge
  set('total-spent-badge', formatNumber(at.total_tokens_spent) + ' tokens total');

  // Before vs After (dynamic from backend calculation)
  set('before-tokens', formatNumber(baWithout.avg_tokens || 0));
  set('before-files', formatNumber(baWithout.avg_files || 0));
  set('before-duration', (baWithout.avg_duration || 0) + ' min');
  set('after-tokens', formatNumber(baWith.avg_tokens || 0));
  set('after-files', formatNumber(baWith.avg_files || 0));
  set('after-duration', (baWith.avg_duration || 0) + ' min');

  // Dynamic Timeline mode (Daily vs Session)
  window.updateTimelineDisplay = function(mode) {
    if (mode) currentTimelineMode = mode;
    const dailyBtn = document.getElementById('toggle-timeline-daily');
    const sessionBtn = document.getElementById('toggle-timeline-session');
    const titleEl = document.getElementById('timeline-chart-title');

    if (currentTimelineMode === 'daily') {
      if (dailyBtn) dailyBtn.classList.add('active');
      if (sessionBtn) sessionBtn.classList.remove('active');
      if (titleEl) titleEl.textContent = 'Tokens Utilizados por Dia (Real)';
      if (metrics.daily_timeline && metrics.daily_timeline.length > 0) {
        const dailyData = metrics.daily_timeline.map(d => ({
          date: d.date.slice(5),
          tokens_saved: d.total_tokens
        }));
        requestAnimationFrame(() => drawTimeline('timeline-canvas', dailyData));
      }
    } else {
      if (dailyBtn) dailyBtn.classList.remove('active');
      if (sessionBtn) sessionBtn.classList.add('active');
      if (titleEl) titleEl.textContent = 'Tokens Gastos por Sessão (Últimas 30)';
      if (metrics.session_timeline && metrics.session_timeline.length > 0) {
        const sessionData = metrics.session_timeline.map(s => ({
          date: '#' + s.session + ' ' + s.date.slice(5),
          tokens_saved: s.tokens_spent
        }));
        requestAnimationFrame(() => drawTimeline('timeline-canvas', sessionData));
      }
    }
  };

  updateTimelineDisplay(currentTimelineMode || 'daily');

  // Project bars (tokens spent, not saved)
  var barsEl = document.getElementById('project-bars');
  if (barsEl && metrics.by_project && metrics.by_project.length > 0) {
    var maxTokens = Math.max.apply(null, metrics.by_project.map(function(p) { return p.total_tokens_spent; }).concat([1]));
    barsEl.innerHTML = metrics.by_project.map(function(p) {
      return '<div class="project-bar-item">' +
        '<div class="project-bar-header">' +
        '<span class="project-bar-name">' + p.project + '</span>' +
        '<span class="project-bar-value">' + formatNumber(p.total_tokens_spent) + ' tkn</span>' +
        '</div>' +
        '<div class="project-bar-track">' +
        '<div class="project-bar-fill" style="width: ' + (p.total_tokens_spent / maxTokens * 100).toFixed(1) + '%"></div>' +
        '</div>' +
        '</div>';
    }).join('');
  } else {
    if (barsEl) barsEl.innerHTML = '<div class="empty-state">Sem interacoes por projeto ainda</div>';
  }
}

function renderProjects(metrics) {
  var grid = document.getElementById('projects-grid');
  if (!grid) return;

  var byProject = {};
  if (metrics && metrics.by_project) {
    metrics.by_project.forEach(function(p) { byProject[(p.project || '').toLowerCase()] = p; });
  }

  grid.innerHTML = STATIC_PROJECTS.map(function(proj) {
    var stats = byProject[proj.id.toLowerCase()] || {};
    return '<div class="project-card">' +
      '<div class="project-card-header">' +
      '<div>' +
      '<div class="project-name">' + proj.name + '</div>' +
      '<div class="project-path">' + proj.path + '</div>' +
      '</div>' +
      '<span class="status-badge status-' + proj.status + '">' + (proj.status === 'active' ? 'Ativo' : 'Pendente') + '</span>' +
      '</div>' +
      '<div class="project-tech">' +
      proj.tech.map(function(t) { return '<span class="tech-tag">' + t + '</span>'; }).join('') +
      '</div>' +
      '<div style="font-size:12px; color: var(--text-muted);">' + proj.description + '</div>' +
      '<div class="project-stats">' +
      '<div class="project-stat">' +
      '<div class="project-stat-value">' + formatNumber(stats.total_interactions || 0) + '</div>' +
      '<div class="project-stat-label">Interacoes</div>' +
      '</div>' +
      '<div class="project-stat">' +
      '<div class="project-stat-value">' + formatNumber(stats.total_tokens_spent || 0) + '</div>' +
      '<div class="project-stat-label">Tokens Gastos</div>' +
      '</div>' +
      '<div class="project-stat">' +
      '<div class="project-stat-value">' + formatNumber(stats.efficiency_tokens_per_minute || 0) + '</div>' +
      '<div class="project-stat-label">Eficiencia (tkn/min)</div>' +
      '</div>' +
      '<div class="project-stat">' +
      '<div class="project-stat-value">' + formatNumber(stats.total_files_read || 0) + '</div>' +
      '<div class="project-stat-label">Arq. Analisados</div>' +
      '</div>' +
      '</div>' +
      '</div>';
  }).join('');
}

function renderHistory(metrics) {
  var tbody = document.getElementById('history-tbody');
  if (!tbody) return;

  var entries = metrics && metrics.recent_entries ? [].concat(metrics.recent_entries).reverse() : [];

  if (entries.length === 0) {
    tbody.innerHTML = '<tr><td colspan="7" class="loading-cell">Sem interacoes registradas ainda. O Second Brain atualizara automaticamente.</td></tr>';
    return;
  }

  tbody.innerHTML = entries.map(function(e) {
    return '<tr>' +
      '<td>' + formatDate(e.timestamp) + '</td>' +
      '<td>' + (e.project || '—') + '</td>' +
      '<td style="max-width:200px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">' + (e.task_description || '—') + '</td>' +
      '<td>' + formatNumber(e.tokens_spent) + '</td>' +
      '<td>' + (e.files_read != null ? e.files_read : '—') + '</td>' +
      '<td>' + (e.duration_minutes != null ? e.duration_minutes : '—') + '</td>' +
      '<td>' + (e.sb_updates != null ? e.sb_updates : '—') + '</td>' +
      '</tr>';
  }).join('');
}

function renderHealth(health) {
  const grid = document.getElementById('health-grid');
  const issuesPanel = document.getElementById('issues-panel');
  if (!grid) return;

  const cards = [];

  // Core files
  if (health.files) {
    health.files.forEach(f => {
      const ok = f.exists && f.size_bytes > 0;
      cards.push({
        name: f.file,
        detail: f.exists ? `${(f.size_bytes / 1024).toFixed(1)} KB` : 'FALTANDO',
        status: ok ? 'ok' : 'error',
        statusText: ok ? 'OK' : 'ERRO',
      });
    });
  }

  // MASTER_INDEX
  if (health.master_index) {
    const mi = health.master_index;
    cards.push({
      name: 'MASTER_INDEX size',
      detail: `${mi.lines} linhas (limite: ${mi.limit})`,
      status: mi.ok ? 'ok' : 'warning',
      statusText: mi.ok ? 'OK' : 'ATENCAO',
    });
  }

  // Learning Log
  if (health.learning_log) {
    const ll = health.learning_log;
    cards.push({
      name: 'Learning Log',
      detail: `${ll.lines} linhas, ${ll.size_kb} KB, ${ll.pending_entries} pendentes`,
      status: ll.needs_consolidation ? 'warning' : 'ok',
      statusText: ll.needs_consolidation ? 'CONSOLIDAR' : 'OK',
    });
  }

  // Project contexts
  if (health.project_contexts) {
    health.project_contexts.forEach(ctx => {
      cards.push({
        name: `Contexto: ${ctx.project}`,
        detail: `${ctx.age_days} dias de idade, ${(ctx.size_bytes / 1024).toFixed(1)} KB`,
        status: ctx.stale ? 'warning' : 'ok',
        statusText: ctx.stale ? 'DESATUALIZADO' : 'OK',
      });
    });
  }

  grid.innerHTML = cards.map(c => `
    <div class="health-card ${c.status}">
      <div class="health-card-name">${c.name}</div>
      <div class="health-card-detail">${c.detail}</div>
      <div class="health-status-text text-${c.status}">${c.statusText}</div>
    </div>
  `).join('');

  // Issues
  if (issuesPanel) {
    const issues = health.issues || [];
    if (issues.length === 0) {
      issuesPanel.innerHTML = `<div style="color:var(--green-400); font-size:13px; padding:8px 0;">Todos os sistemas nominais.</div>`;
    } else {
      issuesPanel.innerHTML = issues.map(i => `<div class="issue-item">${i}</div>`).join('');
    }
  }

  // Sidebar health indicator
  const dot = document.getElementById('health-dot');
  const statusText = document.getElementById('health-status-text');
  const status = health.status || 'OK';
  if (dot) {
    dot.className = 'health-dot' + (status === 'OK' ? '' : status === 'ISSUES' ? ' warning' : ' error');
  }
  if (statusText) {
    statusText.textContent = status === 'OK' ? 'Nominal' : `${(health.issues || []).length} problema(s)`;
  }
}

function renderKnowledge() {
  const grid = document.getElementById('knowledge-grid');
  if (!grid) return;

  grid.innerHTML = STATIC_KNOWLEDGE.map(k => `
    <div class="knowledge-card" onclick="openKnowledgeModal('${k.id}')">
      <div class="knowledge-card-header">
        <div class="knowledge-card-icon-title">
          <span class="knowledge-card-icon">${k.icon}</span>
          <div>
            <div class="knowledge-card-title">${k.name}</div>
            <span class="knowledge-card-badge">${k.category}</span>
          </div>
        </div>
      </div>
      <div class="knowledge-card-triggers">
        ${k.triggers.map(t => `<span class="trigger-tag">${t}</span>`).join('')}
      </div>
      <div class="knowledge-card-stats">
        <span>${k.rules_count} regras registradas</span>
        <span class="knowledge-card-cta">Inspecionar Área &amp; Regras &rarr;</span>
      </div>
    </div>
  `).join('');
}

window.openKnowledgeModal = async function(domainId) {
  const modal = document.getElementById('knowledge-details-modal');
  if (!modal) return;

  // Set default loading state
  document.getElementById('kmodal-title').textContent = 'Carregando detalhes...';
  document.getElementById('kmodal-rules-list').innerHTML = '<li>Carregando regras...</li>';
  document.getElementById('kmodal-preferences-grid').innerHTML = '<div>Carregando preferências...</div>';
  document.getElementById('kmodal-evolution-list').innerHTML = '<div>Carregando histórico...</div>';
  document.getElementById('kmodal-raw-content').textContent = 'Carregando...';
  modal.style.display = 'flex';

  try {
    const res = await fetch(`/api/knowledge/details?domain=${encodeURIComponent(domainId)}`);
    const data = await res.json();
    if (!data.ok) throw new Error(data.error || 'Erro ao carregar dados');

    document.getElementById('kmodal-icon').textContent = data.icon || '📚';
    document.getElementById('kmodal-title').textContent = data.title || domainId;
    document.getElementById('kmodal-category').textContent = data.category || 'Conhecimento';
    document.getElementById('kmodal-file-path').textContent = data.file || '';

    // Rules tab
    const rulesList = document.getElementById('kmodal-rules-list');
    if (rulesList && data.rules) {
      rulesList.innerHTML = data.rules.map(r => `<li>${r}</li>`).join('');
    }

    // Preferences tab
    const prefGrid = document.getElementById('kmodal-preferences-grid');
    if (prefGrid && data.user_preferences) {
      const p = data.user_preferences;
      const prefItems = [
        { label: 'Linguagem Principal', val: p.linguagem_preferida || 'Python / JavaScript' },
        { label: 'Estilo de Explicação', val: p.estilo_explicacao || 'pt-BR sênior, direto ao ponto' },
        { label: 'Padrão de Código', val: p.estilo_codigo || 'Clean Code em inglês, tipado' },
        { label: 'Práticas Proibidas', val: p.praticas_proibidas || 'Sem prints soltos, sem dados expostos' },
        { label: 'Projetos da Máquina', val: p.projetos_alvo || 'RPA UNIQ, WRPE, Second Brain' },
      ];
      prefGrid.innerHTML = prefItems.map(item => `
        <div class="kmodal-pref-card">
          <div class="kmodal-pref-label">${item.label}</div>
          <div class="kmodal-pref-val">${item.val}</div>
        </div>
      `).join('');
    }

    // Evolution tab
    const evoList = document.getElementById('kmodal-evolution-list');
    if (evoList && data.auto_evolution) {
      evoList.innerHTML = data.auto_evolution.map(e => `
        <div class="kmodal-evo-item">
          <span class="kmodal-evo-date">${e.data || 'Auto'}</span>
          <span class="kmodal-evo-event">${e.evento}</span>
        </div>
      `).join('');
    }

    // Raw markdown tab
    const rawContent = document.getElementById('kmodal-raw-content');
    if (rawContent) {
      rawContent.textContent = data.markdown_content || '';
    }

  } catch (err) {
    document.getElementById('kmodal-title').textContent = 'Erro ao carregar detalhes';
    document.getElementById('kmodal-rules-list').innerHTML = `<li>Erro: ${err.message}</li>`;
  }
};

function initKnowledgeModalTabs() {
  const modal = document.getElementById('knowledge-details-modal');
  const closeBtn = document.getElementById('kmodal-close-btn');

  if (closeBtn && modal) {
    closeBtn.addEventListener('click', () => {
      modal.style.display = 'none';
    });
    modal.addEventListener('click', (e) => {
      if (e.target === modal) modal.style.display = 'none';
    });
  }

  document.querySelectorAll('.kmodal-tab').forEach(tab => {
    tab.addEventListener('click', () => {
      const targetTab = tab.getAttribute('data-tab');
      document.querySelectorAll('.kmodal-tab').forEach(t => t.classList.remove('active'));
      document.querySelectorAll('.kmodal-tab-content').forEach(c => c.classList.remove('active'));
      tab.classList.add('active');
      const targetContent = document.getElementById(`kmodal-tab-${targetTab}`);
      if (targetContent) targetContent.classList.add('active');
    });
  });
}

// ============================================================
// NAVIGATION
// ============================================================

const SECTION_TITLES = {
  dashboard: 'Dashboard Executivo',
  projects: 'Projetos da Máquina',
  health: 'Saúde e Integridade',
  knowledge: 'Base de Conhecimento & Preferências',
  repos: 'Hub Universal de Repositórios Especializados',
  graphs: 'Grafo de Conhecimento Visual',
  aurelio: 'Aurélio AI — Jarvis Desktop',
};

function activateSection(id) {
  document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));

  const section = document.getElementById(`section-${id}`);
  const navItem = document.querySelector(`.nav-item[data-section="${id}"]`);

  if (section) section.classList.add('active');
  if (navItem) navItem.classList.add('active');

  const titleEl = document.getElementById('section-title');
  if (titleEl) titleEl.textContent = SECTION_TITLES[id] || id;
}

// ============================================================
// HISTORY FILTER
// ============================================================

// Keep reference to latest metrics for the filter function
let currentMetricsForFilter = null;

function filterHistory() {
  const search = document.getElementById('history-search');
  const period = document.getElementById('history-period');
  const q = (search ? search.value : '').toLowerCase();
  const days = period ? parseInt(period.value) : 30;
  const cutoff = isNaN(days) ? null : new Date(Date.now() - days * 86400000);

  let entries = currentMetricsForFilter && currentMetricsForFilter.recent_entries ? [...currentMetricsForFilter.recent_entries].reverse() : [];
  if (cutoff) {
    entries = entries.filter(e => new Date(e.timestamp) > cutoff);
  }
  if (q) {
    entries = entries.filter(e =>
      (e.project || '').toLowerCase().includes(q) ||
      (e.task_description || '').toLowerCase().includes(q)
    );
  }

  const tbody = document.getElementById('history-tbody');
  if (!tbody) return;
  if (entries.length === 0) {
    tbody.innerHTML = `<tr><td colspan="8" class="loading-cell">Nenhuma entrada encontrada.</td></tr>`;
    return;
  }
  tbody.innerHTML = entries.map(e => `
    <tr>
      <td>${formatDate(e.timestamp)}</td>
      <td>${e.project || '—'}</td>
      <td style="max-width:200px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">${e.task_description || '—'}</td>
      <td>${e.sb_consulted ? '<span class="sb-badge-yes">SIM</span>' : '<span class="sb-badge-no">NAO</span>'}</td>
      <td>${e.files_read != null ? e.files_read : '—'}</td>
      <td>${e.files_avoided != null ? e.files_avoided : '—'}</td>
      <td>${formatNumber(e.tokens_saved_estimate)}</td>
      <td>${e.sb_updates != null ? e.sb_updates : '—'}</td>
    </tr>
  `).join('');
}

// ============================================================
// HUB DE 25 REPOSITÓRIOS — ENGINE & INTERFACE
// ============================================================

let allReposData = [];
let currentCategoryFilter = 'all';

async function loadAndRenderRepos() {
  const grid = document.getElementById('repos-grid');
  if (!grid) return;
  try {
    const res = await fetch('repos_data.json');
    if (!res.ok) throw new Error("Falha ao carregar repos_data.json");
    allReposData = await res.json();
    filterAndRenderRepos();
  } catch (err) {
    grid.innerHTML = `<div class="loading-state">Erro ao carregar dados do Hub: ${err.message}</div>`;
  }
}

function filterAndRenderRepos() {
  const grid = document.getElementById('repos-grid');
  if (!grid) return;
  const searchInput = document.getElementById('repos-search');
  const query = (searchInput ? searchInput.value : '').toLowerCase().trim();

  let filtered = allReposData.filter(r => {
    const matchCat = currentCategoryFilter === 'all' || r.category === currentCategoryFilter;
    const matchQuery = !query ||
      r.name.toLowerCase().includes(query) ||
      r.category_label.toLowerCase().includes(query) ||
      r.description.toLowerCase().includes(query);
    return matchCat && matchQuery;
  });

  if (filtered.length === 0) {
    grid.innerHTML = `<div class="loading-state" style="grid-column: 1/-1;">Nenhuma ferramenta encontrada com os filtros atuais.</div>`;
    return;
  }

  grid.innerHTML = filtered.map(r => {
    const badgeClass = r.status === 'OK' ? 'repo-badge' : 'repo-badge cold';
    const commitDate = r.last_commit_date || '19/10/2026 às 15:30';
    const gitVer = r.git_version || r.last_commit || 'v2.0';
    return `
      <div class="repo-card" data-repo="${r.name}">
        <div class="repo-card-top">
          <div class="repo-title">${r.name}</div>
          <span class="${badgeClass}">${r.status}</span>
        </div>
        <div class="repo-category-tag" style="color: ${r.color || '#38bdf8'}">${r.category_label}</div>
        <div class="repo-desc">${r.description}</div>
        <div class="repo-card-meta-row">
          <div class="repo-commit-date-badge">📅 <strong>Último Commit:</strong> ${commitDate}</div>
          <div class="repo-version-pill">🏷️ <strong>Versão:</strong> ${gitVer}</div>
        </div>
        <div class="repo-footer">
          <button class="repo-guide-btn" onclick="openAiGuideModal('${r.name}')">Ver AI_GUIDE.md</button>
        </div>
      </div>
    `;
  }).join('');
}

window.openAiGuideModal = function(repoName) {
  const repo = allReposData.find(r => r.name === repoName);
  if (!repo) return;
  const modal = document.getElementById('ai-guide-modal');
  const title = document.getElementById('modal-repo-title');
  const body = document.getElementById('modal-guide-content');
  if (modal && title && body) {
    title.textContent = `📖 AI_GUIDE.md — ${repo.name} (${repo.category_label})`;
    body.textContent = repo.ai_guide || "Nenhum guia encontrado para esta ferramenta.";
    modal.style.display = 'flex';
  }
};

function initAddRepoHandler() {
  const addBtn = document.getElementById('add-repo-btn');
  const urlInput = document.getElementById('new-repo-url');
  const catSelect = document.getElementById('new-repo-category');
  const descInput = document.getElementById('new-repo-desc');
  const feedback = document.getElementById('add-repo-feedback');

  if (!addBtn || !urlInput) return;

  addBtn.addEventListener('click', async () => {
    const url = urlInput.value.trim();
    if (!url) {
      showFeedback('Por favor, cole a URL completa do repositório GitHub (ex: https://github.com/usuario/repo).', 'error');
      return;
    }

    if (!url.toLowerCase().includes('github.com')) {
      showFeedback('URL inválida. O link deve ser de um repositório GitHub válido.', 'error');
      return;
    }

    const category = catSelect.value === 'auto' ? '' : catSelect.value;
    const description = descInput ? descInput.value.trim() : '';

    addBtn.disabled = true;
    showFeedback('⏳ Clonando repositório com Cold Snapshot, gerando AI_GUIDE.md e registrando commit...', 'loading');

    try {
      const res = await fetch('/api/repos/add', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url, category, description })
      });
      const data = await res.json();

      if (!res.ok || !data.ok) {
        throw new Error(data.error || 'Erro ao processar repositório.');
      }

      showFeedback(`✅ ${data.message || 'Repositório adicionado com sucesso!'} (${data.last_commit_date}, ${data.git_version})`, 'success');
      urlInput.value = '';
      if (descInput) descInput.value = '';

      // Recarrega lista de repositórios do Hub
      await loadAndRenderRepos();

      setTimeout(() => {
        if (feedback) feedback.style.display = 'none';
      }, 7000);
    } catch (err) {
      showFeedback(`❌ Erro: ${err.message}`, 'error');
    } finally {
      addBtn.disabled = false;
    }
  });

  function showFeedback(msg, type) {
    if (!feedback) return;
    feedback.className = `add-repo-feedback ${type}`;
    feedback.textContent = msg;
    feedback.style.display = 'block';
  }
}

// ============================================================
// GRAFO DE CONHECIMENTO INTERATIVO (CANVAS 60FPS)
// ============================================================

let isGraphInitialized = false;

let currentGraphView = 'hub'; // 'hub' | 'projects'
let currentTimelineMode = 'daily'; // 'daily' | 'session'

async function initKnowledgeGraph(viewType) {
  if (viewType) currentGraphView = viewType;
  const canvas = document.getElementById('graph-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const detailsCard = document.getElementById('graph-details-card');

  function resizeCanvas() {
    const rect = canvas.parentElement.getBoundingClientRect();
    canvas.width = rect.width;
    canvas.height = rect.height;
  }
  resizeCanvas();

  const dataFile = currentGraphView === 'projects' ? 'projects_graph_data.json' : 'graph_data.json';
  let graphData = null;
  try {
    const res = await fetch(dataFile);
    if (!res.ok) throw new Error("Falha ao ler " + dataFile);
    graphData = await res.json();
  } catch (e) {
    console.error("Erro no graph_data:", e);
    return;
  }

  const legendContainer = document.getElementById('graph-legend-container');
  if (legendContainer) {
    if (currentGraphView === 'projects') {
      legendContainer.innerHTML = `
        <span class="legend-item"><span class="legend-dot" style="background:#38bdf8"></span>Estação/Root</span>
        <span class="legend-item"><span class="legend-dot" style="background:#10b981"></span>Projetos</span>
        <span class="legend-item"><span class="legend-dot" style="background:#34d399"></span>Módulos / Backend</span>
        <span class="legend-item"><span class="legend-dot" style="background:#f59e0b"></span>Bancos SQLite</span>
        <span class="legend-item"><span class="legend-dot" style="background:#6366f1"></span>Frontend</span>
        <span class="legend-item"><span class="legend-dot" style="background:#ef4444"></span>Regras / Guardião</span>
      `;
    } else {
      legendContainer.innerHTML = `
        <span class="legend-item"><span class="legend-dot" style="background:#38bdf8"></span>Core</span>
        <span class="legend-item"><span class="legend-dot" style="background:#06b6d4"></span>Categorias</span>
        <span class="legend-item"><span class="legend-dot" style="background:#3b82f6"></span>25 Repositórios</span>
        <span class="legend-item"><span class="legend-dot" style="background:#10b981"></span>Projetos</span>
      `;
    }
  }

  const nodes = graphData.nodes || [];
  const links = graphData.links || [];
  const centerX = canvas.width / 2;
  const centerY = canvas.height / 2;

  nodes.forEach((n, i) => {
    const angle = (i / nodes.length) * Math.PI * 2;
    let dist = 220;
    if (n.type === 'core' || n.type === 'root') dist = 0;
    else if (n.type === 'project' || n.type === 'category') dist = 140;
    else if (n.type === 'database') dist = 200;
    else if (n.type === 'submodule' || n.type === 'module') dist = 260;
    else dist = 290;

    n.x = centerX + Math.cos(angle) * dist + (Math.random() - 0.5) * 40;
    n.y = centerY + Math.sin(angle) * dist + (Math.random() - 0.5) * 40;
    n.vx = 0;
    n.vy = 0;
  });

  const nodeMap = new Map(nodes.map(n => [n.id, n]));
  const parsedLinks = links.map(l => ({
    source: nodeMap.get(l.source),
    target: nodeMap.get(l.target),
    value: l.value || 1,
    dashed: l.dashed || false
  })).filter(l => l.source && l.target);

  let isPhysicsRunning = true;
  let hoveredNode = null;
  let selectedNode = null;
  let draggedNode = null;

  function tick() {
    if (isPhysicsRunning) {
      for (let i = 0; i < nodes.length; i++) {
        for (let j = i + 1; j < nodes.length; j++) {
          const a = nodes[i];
          const b = nodes[j];
          let dx = b.x - a.x;
          let dy = b.y - a.y;
          let dist = Math.sqrt(dx * dx + dy * dy) || 1;
          if (dist < 320) {
            let force = (320 - dist) / (dist * 22);
            a.vx -= (dx / dist) * force;
            a.vy -= (dy / dist) * force;
            b.vx += (dx / dist) * force;
            b.vy += (dy / dist) * force;
          }
        }
      }

      for (const link of parsedLinks) {
        let dx = link.target.x - link.source.x;
        let dy = link.target.y - link.source.y;
        let dist = Math.sqrt(dx * dx + dy * dy) || 1;
        let targetDist = link.source.type === 'core' ? 150 : 110;
        let force = (dist - targetDist) * 0.035;
        link.source.vx += (dx / dist) * force;
        link.source.vy += (dy / dist) * force;
        link.target.vx -= (dx / dist) * force;
        link.target.vy -= (dy / dist) * force;
      }

      for (const n of nodes) {
        n.vx += (centerX - n.x) * 0.002;
        n.vy += (centerY - n.y) * 0.002;
        n.vx *= 0.88;
        n.vy *= 0.88;
        if (n !== draggedNode) {
          n.x += n.vx;
          n.y += n.vy;
        }
      }
    }

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw links
    for (const link of parsedLinks) {
      ctx.beginPath();
      ctx.moveTo(link.source.x, link.source.y);
      ctx.lineTo(link.target.x, link.target.y);
      ctx.strokeStyle = link.dashed ? 'rgba(59, 130, 246, 0.35)' : 'rgba(255, 255, 255, 0.12)';
      ctx.lineWidth = link.source === hoveredNode || link.target === hoveredNode ? 2.5 : 1;
      if (link.dashed) {
        ctx.setLineDash([4, 4]);
      } else {
        ctx.setLineDash([]);
      }
      ctx.stroke();
    }
    ctx.setLineDash([]);

    // Draw nodes
    for (const n of nodes) {
      const isHover = n === hoveredNode || n === selectedNode;
      const radius = isHover ? n.radius + 3 : n.radius;

      if (isHover || n.type === 'core') {
        ctx.shadowColor = n.color || '#38bdf8';
        ctx.shadowBlur = isHover ? 20 : 10;
      } else {
        ctx.shadowBlur = 0;
      }

      ctx.beginPath();
      ctx.arc(n.x, n.y, radius, 0, Math.PI * 2);
      ctx.fillStyle = n.color || '#3b82f6';
      ctx.fill();
      ctx.shadowBlur = 0;

      ctx.strokeStyle = isHover ? '#fff' : 'rgba(255,255,255,0.2)';
      ctx.lineWidth = isHover ? 2.5 : 1;
      ctx.stroke();

      ctx.fillStyle = isHover ? '#fff' : 'rgba(241, 245, 249, 0.85)';
      ctx.font = `${isHover ? 'bold ' : ''}${n.type === 'core' ? '12px' : '10px'} Inter, sans-serif`;
      ctx.textAlign = 'center';
      ctx.fillText(n.label, n.x, n.y + radius + 14);
    }

    requestAnimationFrame(tick);
  }

  requestAnimationFrame(tick);

  function getCanvasCoords(e) {
    const rect = canvas.getBoundingClientRect();
    return {
      x: e.clientX - rect.left,
      y: e.clientY - rect.top
    };
  }

  function findNode(coords) {
    for (let i = nodes.length - 1; i >= 0; i--) {
      const n = nodes[i];
      const dx = coords.x - n.x;
      const dy = coords.y - n.y;
      if (dx * dx + dy * dy <= (n.radius + 6) * (n.radius + 6)) {
        return n;
      }
    }
    return null;
  }

  canvas.addEventListener('mousemove', (e) => {
    const coords = getCanvasCoords(e);
    if (draggedNode) {
      draggedNode.x = coords.x;
      draggedNode.y = coords.y;
      draggedNode.vx = 0;
      draggedNode.vy = 0;
      return;
    }
    hoveredNode = findNode(coords);
    canvas.style.cursor = hoveredNode ? 'pointer' : 'default';
  });

  canvas.addEventListener('mousedown', (e) => {
    const coords = getCanvasCoords(e);
    const node = findNode(coords);
    if (node) {
      draggedNode = node;
      selectedNode = node;
      showNodeDetails(node, parsedLinks);
    }
  });

  window.addEventListener('mouseup', () => {
    draggedNode = null;
  });

  const resetBtn = document.getElementById('graph-reset-btn');
  if (resetBtn) {
    resetBtn.addEventListener('click', () => {
      nodes.forEach((n, i) => {
        const angle = (i / nodes.length) * Math.PI * 2;
        const dist = n.type === 'core' ? 0 : n.type === 'category' ? 140 : n.type === 'project' ? 220 : 280;
        n.x = centerX + Math.cos(angle) * dist;
        n.y = centerY + Math.sin(angle) * dist;
        n.vx = 0;
        n.vy = 0;
      });
    });
  }

  const togglePhysicsBtn = document.getElementById('graph-toggle-physics');
  if (togglePhysicsBtn) {
    togglePhysicsBtn.addEventListener('click', () => {
      isPhysicsRunning = !isPhysicsRunning;
      togglePhysicsBtn.textContent = isPhysicsRunning ? 'Pausar Física' : 'Retomar Física';
    });
  }

  function showNodeDetails(node, allLinks) {
    if (!detailsCard) return;
    const connectedLinks = allLinks.filter(l => l.source === node || l.target === node);
    const related = connectedLinks.map(l => (l.source === node ? l.target : l.source));

    const typeBadge = (node.type || 'NÓ').toUpperCase();
    const linksHtml = related.map(r => `
      <div class="inspector-link-item" onclick="inspectByName('${r.label}')" style="cursor:pointer;">
        <span class="legend-dot" style="background:${r.color || '#3b82f6'}"></span>
        <span>${r.label}</span>
      </div>
    `).join('');

    let metaHtml = '';
    if (node.path) {
      metaHtml += `
        <div class="inspector-meta-row" style="margin-top:0.6rem; font-size:0.75rem; background:rgba(15,23,42,0.6); padding:6px 10px; border-radius:6px; border:1px solid rgba(255,255,255,0.08); font-family:monospace; color:#38bdf8; word-break:break-all;">
          📂 <strong>Caminho:</strong> ${node.path}
        </div>
      `;
    }
    if (node.entry_point) {
      metaHtml += `
        <div class="inspector-meta-row" style="margin-top:0.4rem; font-size:0.75rem; color:#94a3b8; font-family:monospace;">
          ⚡ <strong>Entry Point:</strong> ${node.entry_point}
        </div>
      `;
    }
    if (node.web_page) {
      metaHtml += `
        <div class="inspector-meta-row" style="margin-top:0.4rem; font-size:0.75rem; color:#a78bfa;">
          🌐 <strong>Página / Interface:</strong> ${node.web_page}
        </div>
      `;
    }
    if (node.tech && Array.isArray(node.tech) && node.tech.length > 0) {
      metaHtml += `
        <div class="inspector-section-label" style="margin-top:0.8rem;">Stack Tecnológica</div>
        <div style="display:flex; flex-wrap:wrap; gap:4px; margin-top:4px;">
          ${node.tech.map(t => `<span style="font-size:0.7rem; background:rgba(59,130,246,0.15); color:#60a5fa; border:1px solid rgba(59,130,246,0.3); padding:2px 8px; border-radius:12px;">${t}</span>`).join('')}
        </div>
      `;
    }
    if (node.protected_files && Array.isArray(node.protected_files) && node.protected_files.length > 0) {
      metaHtml += `
        <div class="inspector-section-label" style="margin-top:0.8rem; color:#f87171;">⚠️ Arquivos Intocáveis / Protegidos</div>
        <div style="font-size:0.72rem; color:#fca5a5; font-family:monospace; background:rgba(239,68,68,0.1); padding:6px 8px; border-radius:6px; border:1px solid rgba(239,68,68,0.2); margin-top:4px;">
          ${node.protected_files.join('<br>')}
        </div>
      `;
    }
    if (node.rules) {
      metaHtml += `
        <div class="inspector-section-label" style="margin-top:0.8rem;">Regras & Governança</div>
        <div style="font-size:0.75rem; color:#cbd5e1; background:rgba(255,255,255,0.03); padding:6px 8px; border-radius:6px; margin-top:4px;">
          ${node.rules}
        </div>
      `;
    }

    let extraAction = '';
    if (node.type === 'repository') {
      extraAction = `<button class="repo-guide-btn" style="width:100%; margin-top:1rem; padding:0.6rem;" onclick="openAiGuideModal('${node.label}')">Abrir Manual AI_GUIDE.md</button>`;
    }

    const descText = node.description || node.desc || 'Nó de relacionamento e topologia da máquina.';

    detailsCard.innerHTML = `
      <div class="node-inspector-title">${node.label}</div>
      <div class="node-inspector-type" style="color:${node.color || '#38bdf8'}">${typeBadge}</div>
      <div class="node-inspector-desc">${descText}</div>
      ${metaHtml}
      <div class="inspector-section-label" style="margin-top:0.8rem;">Conexões Diretas (${related.length})</div>
      <div class="inspector-links-list">
        ${linksHtml}
      </div>
      ${extraAction}
    `;
  }

  window.inspectByName = function(label) {
    const target = nodes.find(n => n.label === label);
    if (target) {
      selectedNode = target;
      showNodeDetails(target, parsedLinks);
    }
  };
}

// ============================================================
// MAIN INIT
// ============================================================

let isEventsBound = false;

async function init() {
  try {
    // Update last-update label
    const lastUpdateEl = document.getElementById('last-update');
    if (lastUpdateEl) lastUpdateEl.textContent = `Atualizado: ${formatDate(new Date().toISOString())}`;

    // Fetch data
    let [health, metricsExport] = await Promise.all([loadHealthReport(), loadMetricsExport()]);

    if (typeof health === 'string') {
        try { health = JSON.parse(health); } catch(e) { health = null; }
    }
    if (typeof metricsExport === 'string') {
        try { metricsExport = JSON.parse(metricsExport); } catch(e) { metricsExport = null; }
    }

    // Fallback to demo data if files not available (first run)
    if (!health) health = getDemoHealth();
    if (!metricsExport) metricsExport = getDemoMetrics();

    currentMetricsForFilter = metricsExport;

    // Render all sections
    renderDashboard(metricsExport, health);
    renderProjects(metricsExport);
    renderHistory(metricsExport);
    renderHealth(health);
    renderKnowledge();
    renderEvolution(metricsExport, health);
    await loadAndRenderRepos();
    if (!isGraphInitialized) {
      initKnowledgeGraph();
      isGraphInitialized = true;
    }

    // Apply filter based on current search values
    filterHistory();

    // Setup event listeners only once
    if (!isEventsBound) {
      document.querySelectorAll('.nav-item').forEach(item => {
        item.addEventListener('click', (e) => {
          e.preventDefault();
          const section = item.getAttribute('data-section');
          if (section) activateSection(section);
        });
      });

      // Category pills filter
      document.querySelectorAll('#repos-categories-filter .cat-pill').forEach(pill => {
        pill.addEventListener('click', () => {
          document.querySelectorAll('#repos-categories-filter .cat-pill').forEach(p => p.classList.remove('active'));
          pill.classList.add('active');
          currentCategoryFilter = pill.getAttribute('data-cat') || 'all';
          filterAndRenderRepos();
        });
      });

      const reposSearch = document.getElementById('repos-search');
      if (reposSearch) {
        reposSearch.addEventListener('input', filterAndRenderRepos);
      }

      // Modal close handlers
      const modal = document.getElementById('ai-guide-modal');
      const closeBtn = document.getElementById('modal-close-btn');
      if (closeBtn && modal) {
        closeBtn.addEventListener('click', () => {
          modal.style.display = 'none';
        });
        modal.addEventListener('click', (e) => {
          if (e.target === modal) modal.style.display = 'none';
        });
      }

      const refreshBtn = document.getElementById('refresh-btn');
      if (refreshBtn) {
        refreshBtn.addEventListener('click', async () => {
          refreshBtn.style.opacity = '0.5';
          refreshBtn.style.pointerEvents = 'none';
          await init();
          refreshBtn.style.opacity = '';
          refreshBtn.style.pointerEvents = '';
        });
      }

      const search = document.getElementById('history-search');
      const period = document.getElementById('history-period');
      if (search) search.addEventListener('input', filterHistory);
      if (period) period.addEventListener('change', filterHistory);

      window.addEventListener('resize', () => {
        if (currentMetricsForFilter && currentMetricsForFilter.timeline_30d) {
          requestAnimationFrame(() => drawTimeline('timeline-canvas', currentMetricsForFilter.timeline_30d));
        }
      });

      // Timeline mode switcher (Por Dia vs Por Sessão)
      const dailyBtn = document.getElementById('toggle-timeline-daily');
      const sessionBtn = document.getElementById('toggle-timeline-session');
      if (dailyBtn && sessionBtn) {
        dailyBtn.addEventListener('click', () => {
          dailyBtn.classList.add('active');
          sessionBtn.classList.remove('active');
          currentTimelineMode = 'daily';
          const chartTitle = document.getElementById('timeline-chart-title');
          if (chartTitle) chartTitle.textContent = 'Tokens Utilizados por Dia (Real)';
          if (window.updateTimelineDisplay) window.updateTimelineDisplay('daily');
        });
        sessionBtn.addEventListener('click', () => {
          sessionBtn.classList.add('active');
          dailyBtn.classList.remove('active');
          currentTimelineMode = 'session';
          const chartTitle = document.getElementById('timeline-chart-title');
          if (chartTitle) chartTitle.textContent = 'Tokens por Sessão (Últimos 30 Pedidos)';
          if (window.updateTimelineDisplay) window.updateTimelineDisplay('session');
        });
      }

      // Graph view switcher (Hub Ferramentas vs Projetos da Máquina)
      const hubBtn = document.getElementById('graph-view-hub');
      const projBtn = document.getElementById('graph-view-projects');
      if (hubBtn && projBtn) {
        hubBtn.addEventListener('click', () => {
          hubBtn.classList.add('active');
          projBtn.classList.remove('active');
          initKnowledgeGraph('hub');
        });
        projBtn.addEventListener('click', () => {
          projBtn.classList.add('active');
          hubBtn.classList.remove('active');
          initKnowledgeGraph('projects');
        });
      }

      isEventsBound = true;
      initKnowledgeModalTabs();
      initAddRepoHandler();
    }
  } catch (err) {
    console.error(err);
    const lastUpdateEl = document.getElementById('last-update');
    if (lastUpdateEl) {
      lastUpdateEl.textContent = "Erro: " + err.message;
      lastUpdateEl.style.color = "red";
    }
    const sbVersion = document.getElementById('sb-version');
    if (sbVersion) sbVersion.textContent = "Erro JS!";
  }
}

document.addEventListener('DOMContentLoaded', init);


// ============================================================
// AURELIO AI CHAT INTEGRATION (OLLAMA & SECOND BRAIN)
// ============================================================

let currentAurelioMode = 'restrito';

async function checkOllamaStatus() {
  const dot = document.getElementById('ollama-status-dot');
  const text = document.getElementById('ollama-status-text');
  const select = document.getElementById('aurelio-model-select');
  if (!dot || !text) return;

  try {
    const res = await fetch('/api/aurelio/status');
    if (!res.ok) throw new Error('HTTP ' + res.status);
    const data = await res.json();
    if (data.online) {
      dot.className = 'ollama-status-dot online';
      text.textContent = 'Ollama: Online (' + (data.modelo_atual || 'pronto') + ')';
      if (select && data.modelo_atual) {
        select.value = data.modelo_atual;
      }
    } else {
      dot.className = 'ollama-status-dot offline';
      text.textContent = 'Ollama: Offline (Inicie o serviço)';
    }
  } catch (err) {
    dot.className = 'ollama-status-dot offline';
    text.textContent = 'Ollama: Indisponível (Sem servidor)';
  }
}

function initAurelioChat() {
  const chatInput = document.getElementById('chat-input');
  const chatSend = document.getElementById('chat-send');
  const chatHistory = document.getElementById('chat-history');
  const modelSelect = document.getElementById('aurelio-model-select');
  const modeBtn = document.getElementById('aurelio-mode-btn');
  const clearBtn = document.getElementById('aurelio-clear-btn');
  const personaSelect = document.getElementById('aurelio-persona-select');

  if (!chatInput || !chatSend) return;

  const PERSONA_INFO = {
    aurelio_master: {
      name: "Aurélio Master (Arquiteto Global)",
      skills: "@clean-code + @architecture + @governance",
      greeting: "Olá. Eu sou o Aurélio Master, assistente de arquitetura e orquestrador global conectado a toda a memória da sua máquina (RPA UNIQ, WRPE e Second Brain)."
    },
    frontend_specialist: {
      name: "Frontend Specialist (Design & UI)",
      skills: "@frontend-design + @design-spec + @clean-code",
      greeting: "Olá. Sou o Especialista de Frontend & UI/UX. Estou pronto para criar interfaces modernas, dark mode premium e livres de qualquer clichê visual."
    },
    rpa_specialist: {
      name: "RPA Specialist (Selenium & UNIQ Way)",
      skills: "@rpa_governance + @systematic-debugging",
      greeting: "Olá. Sou o Especialista de RPA. Minha mente está carregada com as diretrizes da Clínica UNIQ, as 6 pastas obrigatórias e os arquivos intocáveis."
    },
    zero_trust_guardian: {
      name: "Zero Trust Guardian (Governança)",
      skills: "@rpa_governance + @architecture",
      greeting: "Atenção. Sou o Guardião Zero Trust. Monitoro a conformidade estrutural, a documentação obrigatória e a integridade de banco de dados."
    },
    devops_engineer: {
      name: "DevOps Engineer (Deploy & Infra)",
      skills: "@architecture + @clean-code + @devops-infra",
      greeting: "Pronto. Sou o Engenheiro de DevOps. Gerencio processos em background, portas de rede, Git e clonagem com proteção Cold Snapshot."
    },
    systematic_debugger: {
      name: "Systematic Debugger (Causa Raiz 4-Fases)",
      skills: "@systematic-debugging + @testing-patterns",
      greeting: "Pronto para investigar. Sou o Debugger Sistemático. Vou isolar causas-raiz em 4 fases e validar empiricamente antes de propor correções."
    },
    explorer_intel: {
      name: "Explorer & Intel (Mapeamento de Projetos)",
      skills: "@architecture + @clean-code",
      greeting: "Olá. Sou o Explorer. Conheço toda a topologia dos seus projetos locais (RPA, WRPE_Recorder, SecondBrain_Aurelio, AutomationTest)."
    },
    project_planner: {
      name: "Project Planner (Planejamento Socrático)",
      skills: "@plan-writing + @brainstorming",
      greeting: "Olá. Sou o Planejador de Projetos. Decomponho demandas complexas em fases rastreáveis sem escrever código prematuro."
    }
  };

  function updateMindBanner(personaKey) {
    const p = PERSONA_INFO[personaKey] || PERSONA_INFO.aurelio_master;
    const personaNameEl = document.getElementById('mind-persona-name');
    const personaSkillsEl = document.getElementById('mind-skills-text');
    if (personaNameEl) personaNameEl.textContent = p.name;
    if (personaSkillsEl) personaSkillsEl.textContent = p.skills;
  }

  if (personaSelect) {
    updateMindBanner(personaSelect.value);
    personaSelect.addEventListener('change', () => {
      const p = PERSONA_INFO[personaSelect.value] || PERSONA_INFO.aurelio_master;
      updateMindBanner(personaSelect.value);
      addMessage(`**[PERSONA ATIVADA: ${p.name}]**\n${p.greeting}\n\n**[HABILIDADES ATIVAS NA MENTE]**\n${p.skills}`, 'assistant');
    });
  }

  // Poll status initially and periodically
  checkOllamaStatus();
  setInterval(checkOllamaStatus, 15000);

  // Model switch
  if (modelSelect) {
    modelSelect.addEventListener('change', async () => {
      const chosenModel = modelSelect.value;
      try {
        const res = await fetch('/api/aurelio/model', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({ modelo: chosenModel })
        });
        const data = await res.json();
        if (data.status === 'ok') {
          const text = document.getElementById('ollama-status-text');
          if (text) text.textContent = 'Ollama: Online (' + chosenModel + ')';
        }
      } catch (e) {
        console.warn('Não foi possível alterar modelo via API:', e);
      }
    });
  }

  // Mode button toggle
  if (modeBtn) {
    modeBtn.addEventListener('click', () => {
      if (currentAurelioMode === 'restrito') {
        currentAurelioMode = 'expandido';
        modeBtn.setAttribute('data-mode', 'expandido');
        modeBtn.textContent = 'Modo: Expandido (Geral)';
      } else {
        currentAurelioMode = 'restrito';
        modeBtn.setAttribute('data-mode', 'restrito');
        modeBtn.textContent = 'Modo: Restrito (Second Brain)';
      }
    });
  }

  // Clear button
  if (clearBtn && chatHistory) {
    clearBtn.addEventListener('click', () => {
      const curPersona = personaSelect ? personaSelect.value : 'aurelio_master';
      const p = PERSONA_INFO[curPersona] || PERSONA_INFO.aurelio_master;
      chatHistory.innerHTML = `
        <div class="chat-message assistant">
          <div class="message-content">
            <strong>[AÇÃO/RESPOSTA DIRETA — ${p.name}]</strong><br>
            Conversa reiniciada. ${p.greeting} Como posso ajudar com seu código ou arquitetura agora?
          </div>
        </div>
      `;
    });
  }

  // Quick prompts
  document.querySelectorAll('.quick-prompt-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const msg = btn.getAttribute('data-msg');
      if (chatInput && msg) {
        chatInput.value = msg;
        sendMessage();
      }
    });
  });

  function addMessage(text, role, extraHtml = '') {
    const div = document.createElement('div');
    div.className = 'chat-message ' + role;
    const formattedText = text
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\n/g, '<br>');
    div.innerHTML = '<div class="message-content">' + formattedText + extraHtml + '</div>';
    chatHistory.appendChild(div);
    chatHistory.scrollTop = chatHistory.scrollHeight;
  }

  async function sendMessage() {
    const text = chatInput.value.trim();
    if (!text) return;

    addMessage(text, 'user');
    chatInput.value = '';

    const curPersona = personaSelect ? personaSelect.value : 'aurelio_master';
    const p = PERSONA_INFO[curPersona] || PERSONA_INFO.aurelio_master;

    const loader = document.createElement('div');
    loader.className = 'chat-loading';
    loader.textContent = `${p.name} pensando e consultando o Second Brain...`;
    chatHistory.appendChild(loader);
    chatHistory.scrollTop = chatHistory.scrollHeight;

    try {
      const chosenModel = modelSelect ? modelSelect.value : 'qwen2.5-coder:7b';
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          mensagem: text,
          modo: currentAurelioMode,
          modelo: chosenModel,
          persona: curPersona
        })
      });
      const data = await res.json();
      if (chatHistory.contains(loader)) {
        chatHistory.removeChild(loader);
      }

      let responseText = data.resposta || 'Erro ao processar resposta.';
      let extraHtml = '';

      if (data.sugestao_proativa) {
        extraHtml += `
          <div class="proactive-tip" style="margin-top:0.8rem; padding:0.6rem 0.8rem; background:rgba(16,185,129,0.1); border-left:3px solid #10b981; border-radius:4px; font-size:0.82rem; color:#6ee7b7;">
            ⚡ <strong>Sugestão Proativa de Arquitetura:</strong><br>${data.sugestao_proativa}
          </div>
        `;
      }

      if (data.skills_sugeridas && Array.isArray(data.skills_sugeridas) && data.skills_sugeridas.length > 0) {
        const chipsHtml = data.skills_sugeridas.map(s => {
          const recName = s.skill || s.repo || 'Recurso';
          const recReason = s.motivo || '';
          return `<span class="skill-rec-chip" style="display:inline-flex; align-items:center; gap:4px; font-size:0.75rem; background:rgba(56,189,248,0.15); border:1px solid rgba(56,189,248,0.3); color:#38bdf8; padding:3px 8px; border-radius:12px; margin:2px;">🎯 <strong>${recName}</strong>: ${recReason}</span>`;
        }).join('');

        extraHtml += `
          <div class="skills-recommendation-box" style="margin-top:0.8rem; padding:0.7rem; background:rgba(15,23,42,0.6); border:1px solid rgba(56,189,248,0.25); border-radius:8px;">
            <div style="font-size:0.78rem; font-weight:600; color:#38bdf8; margin-bottom:0.4rem;">📚 Recomendações Automáticas para esta Demanda:</div>
            <div style="display:flex; flex-wrap:wrap; gap:4px;">${chipsHtml}</div>
          </div>
        `;
      }

      addMessage(responseText, 'assistant', extraHtml);
    } catch (e) {
      if (chatHistory.contains(loader)) {
        chatHistory.removeChild(loader);
      }
      addMessage('Erro de conexão com o backend Aurélio: ' + e.message, 'assistant');
    }
  }

  chatSend.addEventListener('click', sendMessage);
  chatInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  });
}

document.addEventListener('DOMContentLoaded', initAurelioChat);

