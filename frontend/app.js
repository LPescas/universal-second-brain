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
  { id: 'python_patterns', name: 'Python Patterns', triggers: ['python', 'flask', 'fastapi', 'async', 'typing'], file: 'knowledge/python_patterns.md' },
  { id: 'rpa_architecture', name: 'RPA Architecture', triggers: ['rpa', 'automation', 'selenium', 'driver', 'orchestrator'], file: 'knowledge/rpa_architecture.md' },
  { id: 'frontend_patterns', name: 'Frontend Patterns', triggers: ['html', 'css', 'js', 'react', 'next', 'ui', 'design'], file: 'knowledge/frontend_patterns.md' },
  { id: 'devops_infra', name: 'DevOps & Infra', triggers: ['deploy', 'docker', 'ci', 'server', 'infra'], file: 'knowledge/devops_infra.md' },
  { id: 'governance', name: 'Governance', triggers: ['governance', 'zero-trust', 'compliance', 'audit', 'documentation'], file: 'knowledge/governance.md' },
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

  set('val-interactions', formatNumber(at.total_interactions));
  set('val-tokens', formatNumber(at.avg_tokens_per_session));
  set('val-files', formatNumber(at.avg_files_per_session));
  set('val-duration', (at.avg_duration_per_session || 0) + ' min');
  set('val-efficiency', formatNumber(at.efficiency_tokens_per_minute) + ' /min');

  // Total spent badge
  set('total-spent-badge', formatNumber(at.total_tokens_spent) + ' tokens total');

  // Before vs After (dynamic from backend calculation)
  set('before-tokens', formatNumber(baWithout.avg_tokens || 0));
  set('before-files', formatNumber(baWithout.avg_files || 0));
  set('before-duration', (baWithout.avg_duration || 0) + ' min');
  set('after-tokens', formatNumber(baWith.avg_tokens || 0));
  set('after-files', formatNumber(baWith.avg_files || 0));
  set('after-duration', (baWith.avg_duration || 0) + ' min');

  // Session timeline chart (last 30 sessions, NOT calendar days)
  if (metrics.session_timeline && metrics.session_timeline.length > 0) {
    var sessionData = metrics.session_timeline.map(function(s) {
      return { date: '#' + s.session + ' ' + s.date.slice(5), tokens_saved: s.tokens_spent };
    });
    requestAnimationFrame(function() { drawTimeline('timeline-canvas', sessionData); });
  }

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
    <div class="knowledge-card">
      <div class="knowledge-card-title">${k.name}</div>
      <div class="knowledge-card-triggers">
        ${k.triggers.map(t => `<span class="trigger-tag">${t}</span>`).join('')}
      </div>
      <div class="knowledge-card-meta">Arquivo: <code style="font-family:'JetBrains Mono',monospace; font-size:10px; color:var(--text-code)">${k.file}</code></div>
    </div>
  `).join('');
}

function renderEvolution(metrics, health) {
  const container = document.getElementById('evolution-timeline');
  if (!container) return;

  const events = [];

  // System init
  events.push({
    time: '2026-07-31',
    source: 'INIT | SYSTEM',
    content: 'Second Brain inicializado com arquitetura Hub & Spoke. Projetos RPA e WRPE_Recorder indexados.',
    priority: 'system',
  });

  events.push({
    time: '2026-08-03',
    source: 'EVOLUTION | v2.0',
    content: 'Segunda geracao do Second Brain: Pre-Tool Gate implementado, deduplicacao semantica ativa, frontend visual deployado, metricas de observabilidade habilitadas.',
    priority: 'high',
  });

  // From recent entries
  if (metrics && metrics.recent_entries) {
    metrics.recent_entries.slice(-5).forEach(e => {
      if (e.sb_updates > 0) {
        events.push({
          time: formatDate(e.timestamp),
          source: `${(e.project ? e.project.toUpperCase() : null) || 'AGENT'} | UPDATE`,
          content: `${e.sb_updates} atualizacao(oes) adicionada(s) ao Second Brain. Arquivos evitados: ${e.files_avoided}. Tokens economizados: ${formatNumber(e.tokens_saved_estimate)}.`,
          priority: 'medium',
        });
      }
    });
  }

  // Health events
  if (health && health.issues && health.issues.length > 0) {
    events.push({
      time: formatDate(health.timestamp),
      source: 'HEALTH_CHECK | AUTO',
      content: `${health.issues.length} problema(s) detectado(s): ${health.issues[0]}`,
      priority: 'low',
    });
  }

  events.reverse();

  container.innerHTML = events.map(e => `
    <div class="evolution-entry">
      <div class="evo-dot ${e.priority}"></div>
      <div class="evo-body">
        <div class="evo-header">
          <span class="evo-source">${e.source}</span>
          <span class="evo-time">${e.time}</span>
        </div>
        <div class="evo-content">${e.content}</div>
      </div>
    </div>
  `).join('');
}

// ============================================================
// NAVIGATION
// ============================================================

const SECTION_TITLES = {
  dashboard: 'Dashboard',
  projects: 'Projetos',
  history: 'Historico de Utilizacoes',
  health: 'Saude do Second Brain',
  knowledge: 'Base de Conhecimento',
  evolution: 'Auto-Evolucao',
  repos: 'Hub de 25 Repositórios Especializados',
  graphs: 'Grafo de Conhecimento Visual',
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
    return `
      <div class="repo-card" data-repo="${r.name}">
        <div class="repo-card-top">
          <div class="repo-title">${r.name}</div>
          <span class="${badgeClass}">${r.status}</span>
        </div>
        <div class="repo-category-tag" style="color: ${r.color || '#38bdf8'}">${r.category_label}</div>
        <div class="repo-desc">${r.description}</div>
        <div class="repo-footer">
          <span class="repo-meta">Commit: ${r.last_commit}</span>
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

// ============================================================
// GRAFO DE CONHECIMENTO INTERATIVO (CANVAS 60FPS)
// ============================================================

let isGraphInitialized = false;

async function initKnowledgeGraph() {
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

  let graphData = null;
  try {
    const res = await fetch('graph_data.json');
    if (!res.ok) throw new Error("Falha ao ler graph_data.json");
    graphData = await res.json();
  } catch (e) {
    console.error("Erro no graph_data:", e);
    return;
  }

  const nodes = graphData.nodes;
  const links = graphData.links;
  const centerX = canvas.width / 2;
  const centerY = canvas.height / 2;

  nodes.forEach((n, i) => {
    const angle = (i / nodes.length) * Math.PI * 2;
    const dist = n.type === 'core' ? 0 : n.type === 'category' ? 140 : n.type === 'project' ? 220 : 280;
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

    const typeBadge = node.type.toUpperCase();
    const linksHtml = related.map(r => `
      <div class="inspector-link-item" onclick="inspectByName('${r.label}')" style="cursor:pointer;">
        <span class="legend-dot" style="background:${r.color || '#3b82f6'}"></span>
        <span>${r.label}</span>
      </div>
    `).join('');

    let extraAction = '';
    if (node.type === 'repository') {
      extraAction = `<button class="repo-guide-btn" style="width:100%; margin-top:1rem; padding:0.6rem;" onclick="openAiGuideModal('${node.label}')">Abrir Manual AI_GUIDE.md</button>`;
    }

    detailsCard.innerHTML = `
      <div class="node-inspector-title">${node.label}</div>
      <div class="node-inspector-type" style="color:${node.color || '#38bdf8'}">${typeBadge}</div>
      <div class="node-inspector-desc">${node.desc || 'Nó de relacionamento do ecossistema Second Brain.'}</div>
      <div class="inspector-section-label">Conexões Diretas (${related.length})</div>
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

      isEventsBound = true;
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


// Aurelio Chat Integration
document.addEventListener('DOMContentLoaded', () => {
    const chatInput = document.getElementById('chat-input');
    const chatSend = document.getElementById('chat-send');
    const chatHistory = document.getElementById('chat-history');
    
    if(!chatInput || !chatSend) return;

    function addMessage(text, role) {
        const div = document.createElement('div');
        div.className = `chat-message ${role}`;
        div.innerHTML = `<div class="message-content">${text.replace(/</g, '&lt;')}</div>`;
        chatHistory.appendChild(div);
        chatHistory.scrollTop = chatHistory.scrollHeight;
    }

    async function sendMessage() {
        const text = chatInput.value.trim();
        if(!text) return;
        
        addMessage(text, 'user');
        chatInput.value = '';
        
        const loader = document.createElement('div');
        loader.className = 'chat-loading';
        loader.textContent = 'Aurelio pensando...';
        chatHistory.appendChild(loader);
        chatHistory.scrollTop = chatHistory.scrollHeight;

        try {
            const res = await fetch('/api/chat', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({mensagem: text})
            });
            const data = await res.json();
            chatHistory.removeChild(loader);
            
            let responseText = data.resposta || 'Erro ao processar resposta.';
            if (data.sugestao_proativa) {
                responseText += '\n\n⚡ Sugestão Proativa: ' + data.sugestao_proativa;
            }
            
            addMessage(responseText, 'assistant');
        } catch(e) {
            chatHistory.removeChild(loader);
            addMessage('Erro de conexão com o backend Aurelio: ' + e, 'assistant');
        }
    }

    chatSend.addEventListener('click', sendMessage);
    chatInput.addEventListener('keydown', (e) => {
        if(e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });
});
