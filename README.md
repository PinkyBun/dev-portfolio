# Developer Portfolio Repository

Welcome to my developer portfolio! This structure has been optimized to be clean, modular, and extremely easy to update over time.

## Project Structure

```
/
├── index.html        # Main landing page
├── project.html      # Dynamic project details template (auto-populates)
├── projects.html     # Dedicated page viewing all filtered projects
├── resume.pdf        # Downloadable resume file
│
├── css/
│   ├── style.css     # The entire design system and styling variables
│
├── js/
│   ├── app.js             # Handles Project Rendering, Filtering, and the modal population logic
│   ├── main.js            # Handles Site-Wide Behavior (Navigation, Animations, Terminal Intro, AI Chat)
│   ├── projects-data.js   # The Single Source of Truth database for all your portfolio projects
│
├── images/
│   ├── projects/          # All project screenshots (separated by project ID)
│
└── scripts/               # Maintenance scripts and dev tools
```

## How to Add a New Project (3 Easy Steps)

Thanks to the dynamic architecture, you do **not** need to write any new HTML to add a project. Follow these 3 steps:

### 1. Upload Images
Create a new folder inside `images/projects/` matching your new project's ID (e.g., `images/projects/my-new-app/`).
Add your images using this exact naming convention:
- `cover.jpg` *(The main thumbnail shown on the homepage grid)*
- `screenshot-1.jpg` *(Additional image for the detail slider)*
- `screenshot-2.jpg` *(Additional image for the detail slider)*
*(If you have more screenshots, name them `screenshot-3.jpg`, etc.)*

### 2. Update the Data Source
Open `js/projects-data.js` and add a new project object to the array. Make sure the `id` matches the folder name you just created.
```javascript
{
  id: "my-new-app",
  title: "My Amazing New App",
  categoryLabel: "&#9733; CAPSTONE",
  filterCategory: "capstone",
  date: "2026",
  colorBorder: "border-purple",
  colorDot: "dot-purple",
  tech: [
    { class: "tag-flutter", name: "Flutter" }
  ],
  description: "A short description for the project card.",
  link: "project.html?id=my-new-app",
  image: "images/projects/my-new-app/cover.jpg"
}
```

### 3. Add Detail Data
In `js/app.js`, scroll to the `projectData` repository object and add the detailed breakdown for the project page:
```javascript
  "my-new-app": {
    title: "My Amazing New App",
    tags: ["Flutter", "Dart"],
    category: "Mobile Application",
    year: "2026",
    type: "Capstone Project",
    duration: "4 Months",
    status: "Completed",
    overview: "Detailed overview...",
    challenge: "The challenge...",
    approach: "The approach...",
    results: "The results...",
    github: "https://github.com/...",
    demo: false,
    images: [
      "images/projects/my-new-app/cover.jpg",
      "images/projects/my-new-app/screenshot-1.jpg",
      "images/projects/my-new-app/screenshot-2.jpg"
    ]
  }
```

**That's it!** The project will automatically appear on the homepage grid, instantly work with the `projects.html` filters, and dynamically generate its own `project.html` detail page.
