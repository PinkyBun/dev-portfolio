import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '/* ==========================================================================\n   ABOUT ME SECTION STYLINGS\n   ========================================================================== */'
end_marker = '/* 3-Column List Grid Layout */'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Markers not found")
    exit(1)

replacement = '''/* ==========================================================================
   ABOUT ME SECTION STYLINGS (Dashboard Grid)
   ========================================================================== */
.about-section {
  padding: 100px 0;
  position: relative;
}

.about-dashboard-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-areas: 
    "exp about"
    "edu about";
  gap: 24px;
  width: 100%;
}

@media (max-width: 992px) {
  .about-dashboard-grid {
    grid-template-columns: 1fr;
    grid-template-areas: 
      "about"
      "exp"
      "edu";
  }
}

.experience-card { grid-area: exp; }
.about-card { grid-area: about; }
.education-card { grid-area: edu; }

.dashboard-card {
  background-color: var(--bg-tertiary);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 16px;
  padding: 30px;
  display: flex;
  flex-direction: column;
  box-shadow: 0 10px 30px rgba(0,0,0,0.2);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.dashboard-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 35px rgba(0,0,0,0.3);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 5px;
}

.header-title-group {
  display: flex;
  align-items: center;
  gap: 12px;
}

.card-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  display: inline-block;
  box-shadow: 0 0 10px currentColor;
}

.bg-accent { color: var(--accent); background-color: var(--accent); }
.bg-secondary { color: #60a5fa; background-color: #60a5fa; }
.bg-primary { color: #f472b6; background-color: #f472b6; }

.card-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--text-primary);
  margin: 0;
}

.card-subtitle {
  font-size: 0.75rem;
  font-family: var(--font-mono);
  letter-spacing: 2px;
  color: var(--text-secondary);
  margin-top: 0;
  margin-bottom: 25px;
  text-transform: uppercase;
}

/* Stat Box in Experience */
.stat-box {
  background: rgba(167, 139, 250, 0.1);
  border: 1px solid rgba(167, 139, 250, 0.2);
  padding: 8px 15px;
  border-radius: 8px;
  text-align: right;
  display: flex;
  flex-direction: column;
}

.stat-number {
  font-size: 1.1rem;
  font-weight: 800;
  color: var(--accent);
  line-height: 1.1;
}

.stat-label {
  font-size: 0.7rem;
  color: var(--text-secondary);
}

/* Vertical Timeline */
.vertical-timeline {
  position: relative;
  padding-left: 20px;
  margin-top: 10px;
}

.vertical-timeline::before {
  content: '';
  position: absolute;
  top: 5px;
  bottom: 5px;
  left: 3px;
  width: 2px;
  background-color: rgba(255, 255, 255, 0.1);
}

.timeline-item {
  position: relative;
  margin-bottom: 25px;
}

.timeline-item:last-child {
  margin-bottom: 0;
}

.timeline-dot {
  position: absolute;
  left: -21px;
  top: 6px;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background-color: var(--accent);
  border: 2px solid var(--bg-tertiary);
  box-sizing: content-box;
}

.timeline-content {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.timeline-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  flex-wrap: wrap;
  gap: 10px;
}

.timeline-title {
  font-size: 1rem;
  font-weight: 700;
  color: var(--text-primary);
  margin: 0;
}

.status-pill {
  font-size: 0.7rem;
  padding: 3px 10px;
  border-radius: 20px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.status-recent {
  background-color: rgba(96, 165, 250, 0.1);
  color: #60a5fa;
  border: 1px solid rgba(96, 165, 250, 0.2);
}

.status-completed {
  background-color: rgba(74, 222, 128, 0.1);
  color: #4ade80;
  border: 1px solid rgba(74, 222, 128, 0.2);
}

.timeline-desc {
  font-size: 0.9rem;
  color: var(--text-secondary);
  margin: 0;
}

/* About Text */
.about-text-content {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.plain-paragraph {
  font-size: 1rem;
  line-height: 1.7;
  color: var(--text-secondary);
  margin: 0;
  text-align: justify;
}

.plain-paragraph strong {
  color: var(--text-primary);
  font-weight: 600;
}

/* Compact Education List */
.compact-edu-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-top: 10px;
}

.edu-item {
  display: flex;
  flex-direction: column;
  gap: 5px;
  padding-bottom: 15px;
  border-bottom: 1px dashed rgba(255, 255, 255, 0.1);
}

.edu-item:last-child {
  padding-bottom: 0;
  border-bottom: none;
}

.edu-row {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.edu-school {
  font-size: 1rem;
  font-weight: 700;
  color: var(--text-primary);
}

.edu-year {
  font-size: 0.85rem;
  color: var(--text-secondary);
  font-family: var(--font-mono);
  background: rgba(255, 255, 255, 0.05);
  padding: 3px 8px;
  border-radius: 4px;
  white-space: nowrap;
}

.edu-details {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
  font-size: 0.9rem;
  color: var(--text-secondary);
}

.edu-divider {
  color: rgba(255, 255, 255, 0.3);
  font-size: 0.8rem;
}

/* ==========================================================================
   SKILLS / TECH STACK SECTION
   ========================================================================== */

'''

new_content = content[:start_idx] + replacement + content[end_idx:]

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("CSS Replaced successfully")
