import re

with open('d:/dev-portfolio/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace buttons with links
content = re.sub(
    r'<button class="btn-detail" onclick="openProjectModal\(\'([a-zA-Z0-9_-]+)\'\)">(.*?)</button>',
    r'<a class="btn-detail" href="project.html?id=\1" style="display:inline-flex; align-items:center; justify-content:center;">\2</a>',
    content
)

# Remove the modal block
start_marker = "  <!-- Reusable Interactive Project Modal Overlay (80vw x 85vh) -->"
end_marker = "  <!-- AI Chat Assistant Floating Widget -->"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + content[end_idx:]

with open('d:/dev-portfolio/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html")
