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

7. When you are happy with the result, commit the changes to the master branch. The site is then automatically deployed to https://qcrypt-website.netlify.com/ and accessible under https://qcrypt.net. If you have the proper rights, you can see the deployment logs on [netlify](https://app.netlify.com/sites/qcrypt-website/deploys).



## Customizing the theme
Is described at [themes/devfest-theme-hugo/README.md ](https://github.com/QCrypt/qcrypt-website/blob/main/themes/devfest-theme-hugo/README.md)


## Setting up the next year 2025 based on previous years

### design 
1. create a new logo (something with a sheep)
2. choose a background image for the main site, like https://github.com/QCrypt/qcrypt-website/blob/main/static/images/2024/background-2024.jpg 
3. and make a related banner, like https://github.com/QCrypt/qcrypt-website/blob/main/static/images/2024/banner-2024.jpg 
4. pick a related themecolor, like 

### create new subdirectories for content
1. It's probably easiest to copy the entire content folder from a previous year like https://github.com/QCrypt/qcrypt-website/tree/main/content/2024 and start adjusting from there
2. create 2025 subfolder in https://github.com/QCrypt/qcrypt-website/tree/main/static/images
3. put the images (logo, background image, banner) from above to this folder

### add info to main config file https://github.com/QCrypt/qcrypt-website/blob/main/hugo.toml 
4. In [params], change the currentYear and date
5. add a section [params.2025] and supply the required information
6. the timeanddate_cityid can be inferred from https://www.timeanddate.com/worldclock/personal.html by looking at the link after clicking on "Share This Personal World Clock" 
7. Under [menu], create a new [[menu.2025]] structure as for 2023 and 2024.

### adjust content files
1. Go through all .md files in https://github.com/QCrypt/qcrypt-website/tree/main/content/2025 and the _index.md files in the subdirectories, and adjust the front matter. 
2. Adjust the menu: to say 2025 instead of 2024.
3. put "draft: true" in case you want to disable the page for the time being.
4. In general, whenever the year is passed on as parameter, you might have to update it. So, searching under /content/2025 for all occurrences of 2024 and replacing the correct ones with 2025 is probably a good strategy.


### create new team and add admins
1. on https://github.com/orgs/QCrypt/teams, create a new team ```QCrypt 2025```
2. add admins https://github.com/orgs/QCrypt/teams/qcrypt-2025/members
3. add repositories https://github.com/orgs/QCrypt/teams/qcrypt-2025/repositories


### setting up netfliy & domain name
5. In netlify https://app.netlify.com/teams/qcrypt/members: add new admin as collaborator to 2024 site

### slack integration
1. create a new private channel on QCrypt slack, named website-2024
1. on https://api.slack.com/apps/A01P06YNCCU/incoming-webhooks , create a new Webhook (on the bottom of the page)
1. paste the Webhook URL into netfliy:  https://app.netlify.com/sites/qcrypt2024/settings/deploys (for deploy succeesful and deploy failed)
1. add admins to Slack channel

### general
- connect new admins to admins from last year
- update hugo version? check what needs to be updated.
