# Basic Blog

A minimal, static blog built with Hugo and deployed via GitHub Pages.

## 🚀 Features

- **Static site generation** using [Hugo](https://gohugo.io)
- **Markdown-based** content: easy writing and publishing
- Configurable theme and layout
- Clean structure: posts, pages, assets, config
- GitHub Actions workflow for automatic deployment to GitHub Pages

## 📁 Project Structure

```
basic-blog/
├── archetypes/        # Templates for new posts
├── content/           # Markdown content (posts, pages)
├── layouts/           # Custom templates/layouts
├── static/            # Static assets: images, CSS, JS
├── config.toml        # Hugo configuration file
└── .github/
    └── workflows/
        └── hugo.yml   # Deploy workflow for GitHub Pages
```

## 🛠️ Getting Started

### Prerequisites

- [Hugo](https://gohugo.io/getting-started/installing/) (version 0.XX+)
- Git & a GitHub account

### Setup Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/MehradVol4/basic-blog.git
   cd basic-blog
   ```

2. Run Hugo’s development server:
   ```bash
   hugo server
   ```
   Preview your site locally at `http://localhost:1313/`

### Publishing

- Content updates:
  1. Create a new post:
     ```bash
     hugo new posts/my-new-post.md
     ```
  2. Edit the generated markdown file under `content/posts/`
  3. Commit and push changes to `main` (or `master`)
  
- Deployment:
  - A GitHub Actions workflow automatically builds the site and deploys it to GitHub Pages on each push.

## ✍️ Writing Content

- Use front matter in your markdown files:
  ```yaml
  ---
  title: "My Awesome Post"
  date: 2025-06-10
  tags: ["tag1", "tag2"]
  draft: false
  ---
  ```
- Put posts in `content/posts/` and pages (About, etc.) in `content/`

## ⚙️ Configuration

Open `config.toml` to customize:

```toml
baseURL = "https://yourusername.github.io/basic-blog/"
languageCode = "en-us"
title = "Basic Blog"
theme = "YOUR_THEME_NAME"

[params]
  author = "Your Name"
  description = "A minimal blog powered by Hugo."
```

You can also configure menu items, pagination, taxonomies, etc., based on your theme.

## 🧩 Deployment Workflow

The GitHub Actions workflow (`.github/workflows/hugo.yml`) includes:

- Checks out the repo
- Installs Hugo
- Builds the site
- Deploys the `public/` output to `gh-pages` or the `main` branch's `docs/` folder (depending on setup)

Customize this workflow if you're using a custom domain or alternate deployment strategy.

## 🤝 Contributing

Contributions are welcome! To submit:

1. Fork the project
2. Create a branch: `git checkout -b feature/your-feature`
3. Make your changes and commit: `git commit -m "Add feature"`
4. Push to your fork and open a pull request

For bug reports or feature requests, please create an issue.

## 🔗 Useful Links

- [Hugo documentation](https://gohugo.io/documentation/)
- [GitHub Pages basics](https://docs.github.com/en/pages)

---

## 📄 License

This project is open-source under the [MIT License](./LICENSE), unless otherwise noted.
