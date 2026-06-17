const projectsData = [
  {
    id: "moneysense",
    title: "MoneySense Mobile",
    categoryLabel: "&#9733; CAPSTONE",
    categoryClass: "",
    filterCategory: "capstone",
    date: "Jan 2026",
    colorBorder: "border-purple",
    colorDot: "dot-purple",
    tech: [
      { class: "tag-flutter", name: "Flutter" },
      { class: "tag-dart", name: "Dart" },
      { class: "tag-yolo", name: "YOLOv8" },
      { class: "tag-resnet", name: "ResNet-18" },
      { class: "tag-ocr", name: "ML Kit OCR" }
    ],
    description: "Accessibility-focused mobile app enabling visually impaired users to identify Philippine banknotes using machine learning.",
    link: "project.html?id=moneysense",
    image: "images/projects/moneysense/cover.jpg"
  },
  {
    id: "mrt3",
    title: "DOTr &mdash; MRT3 Depot Office",
    categoryLabel: "&#128188; INTERNSHIP",
    categoryClass: "badge-intern",
    filterCategory: "internship",
    date: "2026",
    colorBorder: "border-teal",
    colorDot: "dot-teal",
    tech: [
      { class: "tag-it", name: "IT Operations" },
      { class: "tag-records", name: "Records Management" }
    ],
    description: "Applied IT knowledge in a real-world government environment supporting digital operations and data management.",
    link: "",
    image: "images/projects/mrt3/cover.jpg"
  },
  {
    id: "rfid",
    title: "Attendance System with RFID",
    categoryLabel: "&#128187; PERSONAL PROJECT",
    categoryClass: "badge-client",
    filterCategory: "personal",
    date: "2025",
    colorBorder: "border-blue",
    colorDot: "dot-blue",
    tech: [
      { class: "tag-laravel", name: "Laravel" },
      { class: "tag-php", name: "PHP" },
      { class: "tag-xampp", name: "XAMPP" },
      { class: "tag-rfid", name: "RFID" }
    ],
    description: "Web-based attendance monitoring system integrated with RFID for automated and accurate record tracking.",
    link: "project.html?id=rfid",
    image: "images/projects/rfid/cover.jpg"
  },
  {
    id: "inventory",
    title: "Inventory Management System",
    categoryLabel: "&#128187; PERSONAL PROJECT",
    categoryClass: "badge-client",
    filterCategory: "personal",
    date: "2024",
    colorBorder: "border-amber",
    colorDot: "dot-amber",
    tech: [
      { class: "tag-laravel", name: "Laravel" },
      { class: "tag-php", name: "PHP" },
      { class: "tag-xampp", name: "XAMPP" },
      { class: "tag-sql", name: "SQL" }
    ],
    description: "Database-driven system for real-time stock monitoring and inventory control.",
    link: "project.html?id=inventory",
    image: "images/projects/inventory/cover.jpg"
  },
  {
    id: "datavis",
    title: "Data Visualization Dashboards",
    categoryLabel: "&#128202; PERSONAL PROJECT",
    categoryClass: "badge-client",
    filterCategory: "personal",
    date: "2024",
    colorBorder: "border-orange",
    colorDot: "dot-orange",
    tech: [
      { class: "tag-powerbi", name: "Power BI" },
      { class: "tag-excel", name: "Excel" }
    ],
    description: "Interactive dashboards transforming raw data into clear and actionable business insights.",
    link: "project.html?id=datavis",
    image: "images/projects/datavis/cover.jpg"
  },
  {
    id: "ui",
    title: "Prototyping &amp; UI Design",
    categoryLabel: "&#127912; DESIGN",
    categoryClass: "badge-client",
    filterCategory: "design",
    date: "2024",
    colorBorder: "border-pink",
    colorDot: "dot-pink",
    tech: [
      { class: "tag-figma", name: "Figma" },
      { class: "tag-canva", name: "Canva" }
    ],
    description: "UI prototypes, wireframes, and visual materials for web and mobile interfaces.",
    link: "project.html?id=ui",
    image: "images/projects/ui/cover.jpg"
  },
  {
    id: "ecommerce",
    title: "E-Commerce Website",
    categoryLabel: "&#128187; PERSONAL PROJECT",
    categoryClass: "badge-client",
    filterCategory: "personal",
    date: "2023",
    colorBorder: "border-green",
    colorDot: "dot-green",
    tech: [
      { class: "tag-laravel", name: "Laravel" },
      { class: "tag-php", name: "PHP" },
      { class: "tag-xampp", name: "XAMPP" },
      { class: "tag-sql", name: "SQL" }
    ],
    description: "Full-stack e-commerce platform with product listing, shopping cart, and order tracking.",
    link: "project.html?id=ecommerce",
    image: "images/projects/ecommerce/cover.jpg"
  },
  {
    id: "gym",
    title: "Gym Monitoring System",
    categoryLabel: "&#128187; PERSONAL PROJECT",
    categoryClass: "badge-client",
    filterCategory: "personal",
    date: "2023",
    colorBorder: "border-coral",
    colorDot: "dot-coral",
    tech: [
      { class: "tag-laravel", name: "Laravel" },
      { class: "tag-php", name: "PHP" },
      { class: "tag-xampp", name: "XAMPP" },
      { class: "tag-sql", name: "SQL" }
    ],
    description: "Web-based system for gym membership and attendance management.",
    link: "project.html?id=gym",
    image: "images/projects/gym/cover.jpg"
  },
  {
    id: "calc",
    title: "Calculator App",
    categoryLabel: "&#128187; PERSONAL PROJECT",
    categoryClass: "badge-client",
    filterCategory: "personal",
    date: "The Beginning",
    colorBorder: "border-gray",
    colorDot: "dot-gray",
    tech: [
      { class: "tag-html", name: "HTML" },
      { class: "tag-css", name: "CSS" },
      { class: "tag-js", name: "JavaScript" }
    ],
    description: "A simple calculator web app &mdash; the start of the journey.",
    link: "",
    image: "images/projects/calc/cover.jpg"
  },
  {
    id: "guess",
    title: "Number Guessing Game",
    categoryLabel: "&#128187; PERSONAL PROJECT",
    categoryClass: "badge-client",
    filterCategory: "personal",
    date: "The Beginning",
    colorBorder: "border-gray",
    colorDot: "dot-gray",
    tech: [
      { class: "tag-python", name: "Python" }
    ],
    description: "A basic number guessing game built while learning Python fundamentals.",
    link: "",
    image: "images/projects/guess/cover.jpg"
  },
  {
    id: "grade",
    title: "Student Grade Tracker",
    categoryLabel: "&#128187; PERSONAL PROJECT",
    categoryClass: "badge-client",
    filterCategory: "personal",
    date: "The Beginning",
    colorBorder: "border-gray",
    colorDot: "dot-gray",
    tech: [
      { class: "tag-html", name: "HTML" },
      { class: "tag-css", name: "CSS" },
      { class: "tag-js", name: "JavaScript" }
    ],
    description: "A simple grade tracking web app for academic purposes.",
    link: "",
    image: "images/projects/grade/cover.jpg"
  }
];
