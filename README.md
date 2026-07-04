# Artist Portfolio Website

A minimal, work-first portfolio site designed for GitHub Pages deployment.

## Structure

```
artist-site/
├── index.html          # Landing page / manifesto entrance
├── works.html          # Works gallery and project documentation
├── statement.html      # Artist statement
├── about.html          # Short bio
├── contact.html        # Contact info
├── assets/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── images/
│       ├── work-01.jpg
│       ├── work-02.jpg
│       └── portrait.jpg
└── README.md
```

## Setup

### 1. Create GitHub Repository

1. Go to [github.com](https://github.com) → **New repository**
2. Name it: `your-username.github.io`  
   *(This gives you the URL: `https://your-username.github.io`)*  
   Or any name, e.g. `portfolio` → URL: `https://your-username.github.io/portfolio`
3. Set to **Public**
4. Click **Create repository**

### 2. Upload Files

**Option A — GitHub Web UI (easiest)**
1. Drag and drop all files into the repository
2. Commit with message `Initial commit`

**Option B — Git CLI**
```bash
cd artist-site
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### 3. Enable GitHub Pages

1. Go to repository → **Settings** → **Pages**
2. Source: **Deploy from a branch**
3. Branch: `main` / `(root)`
4. Click **Save**
5. Wait ~1 min → your site is live at the URL shown

---

## Customization Checklist

### Essential
- [ ] Replace `ARTIST NAME` across all HTML files
- [ ] Add work images to `assets/images/` (jpg/webp recommended)
- [ ] Update `src` and `alt` attributes in `index.html` work items
- [ ] Update email in `contact.html`
- [ ] Add portrait photo as `assets/images/portrait.jpg`

### Content
- [ ] Write your artist statement in `about.html`
- [ ] Fill in CV entries (exhibitions, awards, education)
- [ ] Add gallery name / representation if applicable
- [ ] Update Instagram URL

### Optional
- [ ] Add `favicon.ico` to root folder
- [ ] Add `cv.pdf` to `assets/` folder
- [ ] Update `<meta name="description">` in all pages for SEO
- [ ] Add `og:image` meta tag for social sharing previews

---

## Adding More Works

In `index.html`, copy an `<article class="work-item">` block and update:
```html
<article class="work-item" data-index="6">
  <div class="work-thumb">
    <img src="assets/images/work-07.jpg" alt="Description" loading="lazy" />
  </div>
  <div class="work-meta">
    <span class="work-title">Title</span>
    <span class="work-year">2024</span>
  </div>
</article>
```

## Image Optimization Tips

- Export JPGs at quality **75–85%** — sharp enough, fast to load
- Recommended sizes: **1200×900px** for works, **600×800px** for portrait
- For better performance, use **WebP** format (supported in all modern browsers)
- Keep each image under **300KB** ideally

---

## Custom Domain (Optional)

1. Buy a domain (e.g. `artistname.com`)
2. Create a file named `CNAME` in root with your domain:
   ```
   artistname.com
   ```
3. In your domain registrar, add a CNAME record pointing to `your-username.github.io`
4. In GitHub Pages settings, enter your custom domain


