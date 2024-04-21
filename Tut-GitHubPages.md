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
* We will configure GitHub to automatically build the landing page using the files we put inside the dir above located in a new repo

`1. Create a specific repo to store landing page and auxiliary files`

* Go to https://github.com/<user>
* Create a new repo
  * Owner/repo_name: `<user>`/`<user>`.github.io
  * Must be public (for free accounts)
  * Include README.md file
  * License: MIT (optional)  
```
if <repo_name> == user:
   URL will be user.github.io
else:
   URL will be user.github.io/<repo_name>
```
 
`2. Edit README.md Markdown file just created and format it to be the landing page`
* Use ordinary Markdown command or explore` [Jekyll themes](https://docs.github.com/pages/setting-up-a-github-pages-site-with-jekyll/adding-a-theme-to-your-github-pages-site-using-jekyll)
* Commit your work (practically means save with comments)
  
`3. Now, configure GitHub to make README.md to be shown as your landing page`
* Go to the repo just created / Settings / Pages
* "Source" / `Deploy from a branch`.
* "Branch" / `main / (root)` then `Save`.

`4. Checking`
* Every time some thing concerning the landing pages changes, GitHub has to build (render in HTML) he landing page again
* Still in the repo just create click in Actions in the Options bar and check if build is running
* When finishes, goto <user>/github.io and check the result
* And Voilà! 

### To go further

`* Explore` [Google Analytics](https://analytics.google.com/)
  * Create an account
  * Create a property / Put the URL and get the MEASUREMENT_ID or TRACKING_ID
  * Put the entry `google_analytics: [MEASUREMENT_ID] in _config.yml
  * Create the file _includes/head-custom-google-analytics.html with the content shown by the instructions that will appear when creating the property.


