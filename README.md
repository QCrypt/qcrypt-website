# QCrypt 2023+ website

[![Netlify Status](https://api.netlify.com/api/v1/badges/4fa2d41c-275c-4d5a-90ed-14db4a9accb5/deploy-status)](https://app.netlify.com/sites/qcrypt-website/deploys)

Live site at https://qcrypt.net




## History
Originally based on the Hugo template from https://github.com/GDGToulouse/devfest-theme-hugo
adapted from the fork by the cloudnative-amsterdam people: https://github.com/cloudnative-amsterdam/public-website

Used to run https://2020.qcrypt.net, https://2021.qcrypt.net, https://2022.qcrypt.net

Since 2023, the theme submodule is included directly in this git repository.

In preparation of the 2025 edition, a more permanent solution is envisioned with one main page, where more years can be added, broadly modeled after the IACR flagship websites like https://eurocrypt.iacr.org/2024, https://eurocrypt.iacr.org/2025, https://crypto.iacr.org/2023/, https://asiacrypt.iacr.org/2024/, and the "odd one out" https://crypto.iacr.org/2024/.


## Building this conference site from scratch

1. Install [Hugo](https://gohugo.io)
2. Clone this repo:

```bash
git clone git@github.com:QCrypt/qcrypt-website.git
```

3. It's done. Just start Hugo server to see the site live!

```bash
cd qcrypt-website
hugo server
```

5. Edit the markdown source files with ending .md in the /content/ subdirectories to make changes to the site. You might also have to edit .json and .yml files in the /data/ subdirectory. As long as the hugo server is running, your changes should be visible immediately at http://localhost:1313/.

6. Using a suitable editor like [Visual Studio Code](https://code.visualstudio.com/) allows to easily search across all source files, and will help finding the correct file to edit if you want to make specific changes.

7. When you are happy with the result, commit the changes to the master branch. The site is then automatically deployed to https://qcrypt-website.netlify.com/ and accessible under https://qcrypt.net . If you have the proper rights, you can see the deployment logs on [netlify](https://app.netlify.com/sites/qcrypt-website/deploys).


## Customizing the theme
Is described at [themes/devfest-theme-hugo/README.md ](https://github.com/QCrypt/qcrypt-website/blob/main/themes/devfest-theme-hugo/README.md)


## Setting up the next year 2024 based on year 2023

### design 
1. create a new logo (something with a sheep)


### create new subdirectories


### create new team and add admins
1. on https://github.com/orgs/QCrypt/teams, create a new team ```QCrypt 2024```
2. add admins https://github.com/orgs/QCrypt/teams/qcrypt-2024/members
3. add repositories https://github.com/orgs/QCrypt/teams/qcrypt-2024/repositories

### setting up netfliy & domain name
1. create new site on https://app.netlify.com/teams/qcrypt/overview by "import from existing project"
2. connect to Git provider: GitHub
3. pick correct repository: QCrypt/website-2024
3. rename project to qcrypt2024
4. In [Gandi](https://admin.gandi.net/domain/c9de5b76-af33-11e7-8de2-00163ec31f40/qcrypt.net/records): add a new DNS entry, as suggested in netlify:  ```2024	CNAME	10800	qcrypt2024.netlify.app.```
5. In netlify https://app.netlify.com/teams/qcrypt/members: add new admin as collaborator to 2024 site

### slack integration
1. create a new private channel on QCrypt slack, named website-2024
1. on https://api.slack.com/apps/A01P06YNCCU/incoming-webhooks , create a new Webhook (on the bottom of the page)
1. paste the Webhook URL into netfliy:  https://app.netlify.com/sites/qcrypt2024/settings/deploys (for deploy succeesful and deploy failed)
1. add admins to Slack channel

### general
- connect new admins to admins from last year
- update hugo version? check what needs to be updated.
