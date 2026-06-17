import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '/* ==========================================================================\n   BENTO GRID TECH SKILLS STYLING'
end_marker = '/* ==========================================================================\n   TIMELINE V2'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Markers not found")
    exit(1)

replacement = '''/* ==========================================================================
   FILTERABLE TECH SKILLS STYLING
   ========================================================================== */

/* Filter Bar */
.tech-filter-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 12px;
  margin-bottom: 32px;
}

.tech-filter-btn {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: var(--text-secondary);
  padding: 8px 16px;
  border-radius: 20px;
  font-family: var(--font-monospace);
  font-size: 13px;
  cursor: pointer;
  transition: all var(--transition-fast);
}

.tech-filter-btn:hover {
  background: rgba(167, 139, 250, 0.1);
  color: #fff;
  border-color: rgba(167, 139, 250, 0.4);
}

.tech-filter-btn.active {
  background: rgba(167, 139, 250, 0.2);
  color: #a78bfa;
  border-color: #a78bfa;
  box-shadow: 0 0 10px rgba(167, 139, 250, 0.2);
}

/* Grid Layout */
.tech-grid-filterable {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(110px, 1fr));
  gap: 16px;
  width: 100%;
}

.tech-card {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 20px 10px;
  background-color: var(--bg-tertiary);
  border-radius: 12px;
  border: 1px solid rgba(255,255,255,0.05);
  cursor: pointer;
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease, border-color 0.3s ease, opacity 0.4s ease;
}

/* Filtering States */
.tech-card.hidden {
  display: none;
  opacity: 0;
  transform: scale(0.9);
}

.tech-card:hover {
  transform: scale(1.05) translateY(-2px);
  z-index: 10;
}

/* Icons / Labels */
.tech-card .tech-icon {
  width: 48px;
  height: 48px;
  border-radius: var(--border-radius-sm);
  background-color: rgba(255, 255, 255, 0.05);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-secondary);
  font-size: 1.6rem;
  transition: transform var(--transition-fast), color var(--transition-fast);
}

.tech-card .tech-icon img.si-logo {
  width: 24px;
  height: 24px;
  object-fit: contain;
}

.tech-card .tech-label {
  font-size: 0.75rem;
  color: var(--text-secondary);
  font-weight: 600;
  text-align: center;
  transition: color var(--transition-fast);
}

.tech-card:hover .tech-icon {
  color: #fff;
}
.tech-card:hover .tech-label {
  color: #fff;
}

/* Category Color Coding (Borders & Hover Glow) */
.border-frontend { border-top: 3px solid #a78bfa; }
.border-frontend:hover { box-shadow: 0 0 20px rgba(167, 139, 250, 0.2); border-color: rgba(167, 139, 250, 0.4); }

.border-mobile { border-top: 3px solid #2dd4bf; }
.border-mobile:hover { box-shadow: 0 0 20px rgba(45, 212, 191, 0.2); border-color: rgba(45, 212, 191, 0.4); }

.border-backend { border-top: 3px solid #60a5fa; }
.border-backend:hover { box-shadow: 0 0 20px rgba(96, 165, 250, 0.2); border-color: rgba(96, 165, 250, 0.4); }

.border-database { border-top: 3px solid #fbbf24; }
.border-database:hover { box-shadow: 0 0 20px rgba(251, 191, 36, 0.2); border-color: rgba(251, 191, 36, 0.4); }

.border-analytics { border-top: 3px solid #f472b6; }
.border-analytics:hover { box-shadow: 0 0 20px rgba(244, 114, 182, 0.2); border-color: rgba(244, 114, 182, 0.4); }

.border-tools { border-top: 3px solid #9ca3af; }
.border-tools:hover { box-shadow: 0 0 20px rgba(156, 163, 175, 0.2); border-color: rgba(156, 163, 175, 0.4); }

.border-ai { border-top: 3px solid #4ade80; }
.border-ai:hover { box-shadow: 0 0 20px rgba(74, 222, 128, 0.2); border-color: rgba(74, 222, 128, 0.4); }


/* Light Theme overrides */
[data-theme="light"] .tech-filter-btn {
  background: rgba(0, 0, 0, 0.05);
  border-color: rgba(0, 0, 0, 0.1);
  color: var(--text-secondary);
}
[data-theme="light"] .tech-filter-btn:hover {
  background: rgba(124, 58, 237, 0.1);
  color: #1f2937;
  border-color: rgba(124, 58, 237, 0.4);
}
[data-theme="light"] .tech-filter-btn.active {
  background: rgba(124, 58, 237, 0.15);
  color: #7c3aed;
  border-color: #7c3aed;
}

[data-theme="light"] .tech-card {
  background-color: #fff;
  border: 1px solid rgba(0,0,0,0.05);
  box-shadow: 0 4px 6px rgba(0,0,0,0.02);
}
[data-theme="light"] .tech-card .tech-icon {
  background-color: rgba(0,0,0,0.03);
  color: var(--text-secondary);
}
[data-theme="light"] .tech-card:hover .tech-icon {
  color: var(--accent);
}
[data-theme="light"] .tech-card:hover .tech-label {
  color: var(--text-primary);
}

'''

new_content = content[:start_idx] + replacement + '\n' + content[end_idx:]

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("CSS Replaced successfully")
