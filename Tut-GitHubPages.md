# Creating GitHub Pages
by [JRM Garcia](https://garcia-inpe.github.io/) / [INPE](https://www.gov.br/inpe/pt-br) / [MCTI](https://www.gov.br/mcti/pt-br), compiled from [GitHub Docs: Creating a GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)




CREATING GITHUB PAGES 
Personal portfolio

Observations (concepts one must keep in mind)
Sites can contain multiple files: the main index.md, images, configurations, html, etc
These files need a location to be stored in, which in github infra is composed by: 
a repo (create a new or choose an existing)
a branch in the repo (create a new or choose an existing, the “main”, ex.)
a directory inside the branch (the root “/” or a new one)
Two modes to build the homepage site
Automatically from the publishing source or 
Using GitHub Actions workflow 
Publishing source is where the files responsible to build your site are (the location).
The steps below use the what is highlighted in bold: <new repo> : <main branch> : <“/”> (root dir)
We will configure GitHub to automatically build the landing page using the files we put inside the dir above

1) Creating one repo specific for files of the site
Owner: <user> or the <organization>
Repo name: <user>.github.io or <organization>.github.io
Repo name must exactly match user/organization name – CAUTION –
Public (must be public for free accounts)
Add a README file
License: MIT (suggested)
Hit Create Repo button

2) Create a landing page according to markdown format
Name it index.md and save it inside the root dir “/” of the main branch.

3) Creating a landing page
Go to the repo
Configure the publishing source
Settings / Pages
"Build and deployment" / "Source" / Deploy from a branch.
"Build and deployment" 
Choose branch and folder (ex. Main /docs) 

