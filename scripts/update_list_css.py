import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '/* Horizontal Scrolling Rows Layout */'
end_marker = '/* Light Theme overrides */'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Markers not found")
    exit(1)

replacement = '''/* 3-Column List Grid Layout */
.tech-list-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
  width: 100%;
  transition: max-height 0.8s cubic-bezier(0.16, 1, 0.3, 1);
  position: relative;
}

.tech-list-grid.collapsed {
  max-height: 400px;
  overflow: hidden;
}

.tech-list-grid.collapsed::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 100px;
  background: linear-gradient(to bottom, transparent, var(--bg-primary));
  pointer-events: none;
  z-index: 5;
}

.tech-expand-container {
  display: flex;
  justify-content: center;
  margin-top: 2rem;
}

.tech-list-card {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1.25rem;
  background-color: var(--bg-tertiary);
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.05);
  transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
}

.tech-list-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
  border-color: rgba(255, 255, 255, 0.1);
}

.tech-card-icon {
  flex-shrink: 0;
  width: 50px;
  height: 50px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.8rem;
  background-color: rgba(255, 255, 255, 0.05);
  transition: background-color 0.3s ease;
}

.tech-card-icon img.si-logo {
  width: 26px;
  height: 26px;
  object-fit: contain;
}

.tech-card-content {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.tech-card-title {
  font-size: 1rem;
  font-weight: 700;
  color: var(--text-primary);
  margin: 0;
}

.tech-card-desc {
  font-size: 0.8rem;
  color: var(--text-secondary);
  margin: 0;
  line-height: 1.3;
}

/* Category Backgrounds for Icons */
.bg-frontend { color: #a78bfa; background-color: rgba(167, 139, 250, 0.1); }
.bg-mobile { color: #2dd4bf; background-color: rgba(45, 212, 191, 0.1); }
.bg-backend { color: #60a5fa; background-color: rgba(96, 165, 250, 0.1); }
.bg-database { color: #fbbf24; background-color: rgba(251, 191, 36, 0.1); }
.bg-analytics { color: #f472b6; background-color: rgba(244, 114, 182, 0.1); }
.bg-tools { color: #9ca3af; background-color: rgba(156, 163, 175, 0.1); }
.bg-ai { color: #4ade80; background-color: rgba(74, 222, 128, 0.1); }

/* Hover effect on icons based on card hover */
.tech-list-card:hover .tech-card-icon.bg-frontend { background-color: rgba(167, 139, 250, 0.2); }
.tech-list-card:hover .tech-card-icon.bg-mobile { background-color: rgba(45, 212, 191, 0.2); }
.tech-list-card:hover .tech-card-icon.bg-backend { background-color: rgba(96, 165, 250, 0.2); }
.tech-list-card:hover .tech-card-icon.bg-database { background-color: rgba(251, 191, 36, 0.2); }
.tech-list-card:hover .tech-card-icon.bg-analytics { background-color: rgba(244, 114, 182, 0.2); }
.tech-list-card:hover .tech-card-icon.bg-tools { background-color: rgba(156, 163, 175, 0.2); }
.tech-list-card:hover .tech-card-icon.bg-ai { background-color: rgba(74, 222, 128, 0.2); }

@media (max-width: 992px) {
  .tech-list-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 600px) {
  .tech-list-grid {
    grid-template-columns: 1fr;
  }
}

'''

new_content = content[:start_idx] + replacement + content[end_idx:]

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("CSS Replaced successfully")
