import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '/* Grid Layout */\n.tech-grid-filterable {'
end_marker = '/* Filtering States */\n.tech-card.hidden {'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Markers not found")
    exit(1)

replacement = '''/* Horizontal Scrolling Rows Layout */
.tech-category-row {
  margin-bottom: 2rem;
  width: 100%;
}

.tech-row-title {
  color: var(--accent);
  font-size: 0.95rem;
  font-weight: 700;
  letter-spacing: 1.5px;
  margin-bottom: 1rem;
  text-align: left;
}

.tech-scroll-wrapper {
  position: relative;
  width: 100%;
  display: flex;
  align-items: center;
}

.tech-scroll-container {
  display: flex;
  gap: 16px;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  padding: 10px 0;
  width: 100%;
  scrollbar-width: none; /* Firefox */
  -ms-overflow-style: none; /* IE/Edge */
}

.tech-scroll-container::-webkit-scrollbar {
  display: none; /* Chrome/Safari */
}

/* Fade Gradients */
.scroll-fade-gradient {
  position: absolute;
  top: 0;
  bottom: 0;
  width: 60px;
  pointer-events: none;
  z-index: 5;
}

.scroll-fade-gradient.left {
  left: 0;
  background: linear-gradient(to right, var(--bg-primary), transparent);
}

.scroll-fade-gradient.right {
  right: 0;
  background: linear-gradient(to left, var(--bg-primary), transparent);
}

/* Scroll Buttons */
.tech-scroll-btn {
  position: absolute;
  z-index: 10;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: var(--bg-tertiary);
  border: 1px solid rgba(255,255,255,0.1);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  opacity: 0;
  transition: opacity 0.3s ease, background 0.3s ease, transform 0.2s ease;
  box-shadow: 0 4px 10px rgba(0,0,0,0.3);
}

.tech-scroll-wrapper:hover .tech-scroll-btn {
  opacity: 1;
}

.tech-scroll-btn:hover {
  background: var(--accent);
  transform: scale(1.1);
}

.tech-scroll-btn.left {
  left: -16px;
}

.tech-scroll-btn.right {
  right: -16px;
}

@media (max-width: 768px) {
  .tech-scroll-btn {
    display: none; /* Hide hover arrows on mobile */
  }
  .scroll-fade-gradient {
    width: 30px;
  }
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
  
  /* Horizontal scrolling specific styles */
  flex: 0 0 110px;
  scroll-snap-align: start;
}

'''

new_content = content[:start_idx] + replacement + content[end_idx:]

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("CSS Replaced successfully")
