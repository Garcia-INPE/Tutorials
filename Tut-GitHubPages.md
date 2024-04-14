# Creating GitHub Pages
by [JRM Garcia](https://garcia-inpe.github.io/) / [INPE](https://www.gov.br/inpe/pt-br) / [MCTI](https://www.gov.br/mcti/pt-br), compiled from [ESIIL Data Short Course 2024](https://cu-esiil-edu.github.io/2024-data-short-course/) and [GitHub Docs: Creating a GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)

### Observations (concepts one must keep in mind)

* Sites can contain multiple files: README.md, index.md, images, configurations, html, etc
* These files need a location to be stored in, which in github infra is composed by:
  * a repo (`create a new` or choose an existing)
  * a branch in the repo (create a new or choose an existing, `the “main”`, ex.)
  * a directory inside the branch (`the root “/”` or a new one)
* There are two modes to build the homepage site
  * Automatically from the publishing source or
  * Using GitHub Actions workflow
* `Publishing source` is where the files responsible to build your site are (the location).
* The steps below use the what is highlighted: `<new repo>` : `<main branch>` : `<“/”> (root dir)`
* We will configure GitHub to automatically build the landing page using the files we put inside the dir above

`1. Creating one specific repo for saving the files that will create the site`
* Owner: `<user>` or `<organization>`
* Repo name: `<user>`.github.io or `<organization>`.github.io  
```
if <repo_name> == user_or_organization_name:
   URL = user.github.io
else:
   URL = user.github.io/<repo_name>
```
* Public (must be public for free accounts)
* License: MIT (optional)
* Hit Create Repo button

`2. Create a landing page in Markdown`
* Name it `index.md` and save it inside the root dir “/” of the main branch.

`3. Configuring the landing page to be automatically called when entering the URL`
* Go to the repo / Settings / Pages
* "Source" / `Deploy from a branch`.
* "Branch" / `main / (root)` then `Save`.

`4. Explore [Jekyll themes](https://docs.github.com/pages/setting-up-a-github-pages-site-with-jekyll/adding-a-theme-to-your-github-pages-site-using-jekyll)`

