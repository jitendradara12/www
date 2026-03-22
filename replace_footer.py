import re

with open('static/style.css', 'r') as f:
    css = f.read()

# Find the start of the Footer / Meta Links section
start_idx = css.find('/* Footer / Meta Links */')
if start_idx != -1:
    css = css[:start_idx]

new_footer_css = """/* Footer / Meta Links */
footer.editorial-footer {
  margin-top: var(--spacing-24);
  padding: var(--spacing-16) 0;
  background: var(--surface-container-low);
  /* Boundary defined solely by background color shift */
}

.footer-inner {
  max-width: 800px;
  margin: 0 auto;
  padding: 0 1.5rem;
  display: grid;
  grid-template-columns: 1fr 2.5fr; /* Intentional Asymmetry */
  gap: var(--spacing-10);
}

@media (max-width: 600px) {
  .footer-inner {
    grid-template-columns: 1fr;
  }
}

/* For TAGLIST.HTML */
.taglist {
  text-align: left;
}

.taglist ul {
  list-style: none;
  padding: 0;
  display: flex;
  flex-direction: column; /* Act as an index/appendix */
  gap: 1rem;
}

.taglist a {
  display: inline-flex;
  align-items: center;
  text-decoration: none;
  font-family: var(--font-mono);
  font-size: 0.6875rem;
  text-transform: uppercase;
  color: var(--tertiary);
  letter-spacing: 0.15em;
  transition: color 0.3s ease;
}

.taglist a::before {
  content: '→';
  margin-right: 0.5rem;
  color: var(--outline-variant);
}

.taglist a:hover {
  color: var(--secondary);
}

/* For NEXTPREV.HTML */
.footer-nav {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-10);
}

.footer-nav .nav-item {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.footer-nav .nav-item a.display-md {
  font-family: var(--font-display);
  font-size: 2.5rem;
  line-height: 1.1;
  color: var(--on-background);
  text-decoration: none;
  margin-top: 0.5rem;
  transition: color 0.3s ease;
}

.footer-nav .nav-item a.display-md:hover {
  color: var(--secondary);
}

/* Selection Highlighting */
::selection {
  background: var(--secondary);
  color: var(--on-primary);
}
::-moz-selection {
  background: var(--secondary);
  color: var(--on-primary);
}

/* Article Links */
article a {
  color: var(--on-background);
  text-decoration: underline;
  text-decoration-thickness: 1px;
  text-underline-offset: 4px;
  transition: color 0.3s ease, text-decoration-color 0.3s ease;
}

article a:hover {
  color: var(--secondary);
  text-decoration-color: var(--secondary);
}

/* Content Elements */
article p {
  font-size: 1.125rem;
  margin-bottom: 1.5rem;
}

article ul, article ol {
  font-size: 1.125rem;
  margin-bottom: 1.5rem;
  padding-left: 1.5rem;
}

article li {
  margin-bottom: 0.5rem;
}

blockquote {
  margin: var(--spacing-10) 0;
  padding-left: 2rem;
  border-left: 4px solid var(--primary);
  font-family: var(--font-display);
  font-style: italic;
  font-size: 1.5rem;
  color: var(--primary);
}

/* Inline Code & Mark */
mark {
  background: var(--surface-container-highest);
  color: var(--secondary);
  padding: 0 0.25rem;
}

article code {
  background: var(--surface-container-highest);
  padding: 0.15rem 0.35rem;
  font-size: 0.875rem;
  color: var(--tertiary-fixed-dim);
}
"""

with open('static/style.css', 'w') as f:
    f.write(css + new_footer_css)
