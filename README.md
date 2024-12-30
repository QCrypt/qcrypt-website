# QCrypt 2025+ website

[![Netlify Status](https://api.netlify.com/api/v1/badges/4fa2d41c-275c-4d5a-90ed-14db4a9accb5/deploy-status)](https://app.netlify.com/sites/qcrypt-website/deploys)

Hugo-powered QCrypt website for 2025 edition and later, live at at https://qcrypt.net. QCrypt is the yearly international scientific conference presenting last year’s top results in quantum cryptography. [Hugo](https://gohugo.io/) is a fast static website generator. https://qcrypt.net is generously hosted by [netlify](https://www.netlify.com/) under a [Open Source Plan](https://www.netlify.com/legal/open-source-policy/) :heart:!

Project initiated and maintained by [Christian Schaffner](https://github.com/cschaffner) since 2020.


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
4. In [params], LEAVE the currentYear and date as it is right now. Change this only when the new 2025 site is ready.
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

### create new email addresses
We probably need new email addresses like 2025@qcrypt.net and pcchairs2025@qcrypt.net.

### technical updates
- connect new admins to admins from last year
- Is it time to update the hugo version? check what needs to be updated.

### bump year
Once the new site is ready to be "promoted" to be the current year, make the following changes:
1. In hugo.toml, in [params], change the currentYear and date
2. In [[server.redirects]], change the forward to = "/2025/"
3. In https://github.com/QCrypt/qcrypt-website/blob/main/netlify.toml , adjust the redirect as well


## Later Updates

### call for papers, venue updates, registration
1. adjust the according .md file in content/2025, possibly by switching back "draft: false" and adjusting the content from previous year
2. **all changes to the website should be mentioned in a table with "Website Updates" like on https://qcrypt.net/2023/**, for the convenience of the website visitors
3. The call-to-action buttons on the main site can be adjusted depending on the news.

### tutorial, invited speakers, panelists are known
1. update the .md files in https://github.com/QCrypt/qcrypt-website/tree/main/content/2025/speakers
2. remove previous images from the images subdirectory, upload new ones, and make sure the photoURL field of the speaker is pointing there.
3. Use sensible names for the .md files, like eleni_diamanti.md 
4. Per speaker, create an according session in https://github.com/QCrypt/qcrypt-website/tree/main/content/2025/sessions , using the examples from previous years.

### accepted papers and posters are known
1. Get accepted papers as json export from hotcrp from PC chair
2. run [this python script](https://github.com/QCrypt/qcrypt-website/blob/main/static/python-scripts/sanitize_hotcrp_json.py) to sanitize the output, removing all emails, pc_conflicts etc.
3. put the resulting file as accepted-papers-2025.json into [data](https://github.com/QCrypt/qcrypt-website/tree/main/data)

Proceed accordingly with the list of accepted posters.

### creating a schedule
1. duplicate https://github.com/QCrypt/qcrypt-website/blob/main/data/schedule-2024.yml and call it schedule-2025.yml
2. make sure all sessions exist
3. Adjust the id's of the contributed papers in the sessions with contributed papers


## More detailed explanations of the different content sections

Have a look at the [Hugo Documentation](https://gohugo.io/documentation/), ChatGPT is also quite knowledgable.

Hugo's favorite [Content format](https://gohugo.io/content-management/formats/) is markdown, and that's what we use throughout. For [data sources](https://gohugo.io/content-management/data-sources/) and config files, Hugo understands TOML, YAML, JSON, CSV, XML. We use the first three only.

Every content file contains a [front matter](https://gohugo.io/content-management/front-matter/), specifying metadata for the content, usually in yaml format. Important parameters are title, year, type, draft, menu. They influence how content is displayed.

> [!WARNING]
> In this site, we are deviating from the Hugo-recommended [Organization of content source](https://gohugo.io/content-management/organization/#organization-of-content-source), because our top levels in the `content/<DIRECTORIES>` are years, instead of topics. Therefore, the `.Section` variable is often our `$currentYear`.

The original Hugo template had multilingual support (French / English), but we have dropped this in the meanwhile, some reminders of these times are still around, though.

### file names
> [!IMPORTANT]
> Even though Hugo is quite forgiving, please use sensible and consistent file names for content pages, pictures etc. [This page](https://docs.hugoblox.com/reference/site-structure/) recommends to:
> - Stick to lowercase for all file names, including content files (`about.md`), layouts, and static assets (`images/logo.png`).
> - Use hyphens (`-`) or underscores (`_`) to separate words instead of spaces or capital letters (e.g., `my-article.md` or `my_article.md`).


### Menus in the header
See [Menus](https://gohugo.io/content-management/menus/) in the Hugo documentation. We are using a mix of "In side configuration" and "in front matter" menu definitions.

The basic structure of the top menu is copied from the IACR flagship conference websites (like https://eurocrypt.iacr.org/2024). The basic menu structure is defined in [/hugo.toml](/hugo.toml) under [menu]. We have a menu hierarchy for each year, but these basic entries should basically be the same every year. The items "Technical Program" and "Attend" do not correspond to actual pages, they are used as parent menu items for other pages.

The other items in the menu are defined in the front matter of content pages.

### Footer
The content of the footer is specified in [/data/footer.yml](/data/footer.yml). The "social share" options are currently disabled, the "social follow" options are Twitter and YouTube. 
> [!NOTE]
> Maybe we want to move away from Twitter soon?

The footer rarely needs to be changed. It automatically links to the charter, history and code of conduct of the current year. Just make sure that the content directory of the currentYear also contains these three files:
* `charter.md`
* `history.md`
* `code-of-conduct.md`
  
Copy them over from the previous year and make sure they are up to date!

It is a requirement by the Netlify Open Source plan to link to a code of conduct, so do not remove that part!

### Main page
The main home page per year is the `/content/YEAR/_index.html`, like [/content/2024/_index.html](/content/2024/_index.html). It has `type: home` and `layout: home` in the front matter.

It is the only page without a banner on top, as it starts with a [jumbo element](https://github.com/QCrypt/qcrypt-website/blob/main/themes/devfest-theme-hugo/README.md#jumbo-bloc) which takes as arguments the background image, label and logo. The content of it is the date, and various call to actions using button-links, which in turn take arguments like label, url, icon.

The following elements are:
* home-info: some basic information about QCrypt
* home-keydates: the two most important tables: one with key dates, one with website updates. Again, this is inspired by [the IACR pages](https://eurocrypt.iacr.org/2023/)).
* home-location: image, address, and coordinates of the venue
* partners: list of sponsors, or call for sponsors

### Team
One of the first content pages to update and display. Follow the example of previous years.

All committees get their own subfolder, and there is an image folder for all portrait pictures. Ensure the photoURL front matter item points to the correct picture. When creating and naming new files, follow [reasonable conventions](#file-names).

### Partners / Sponsors
The subdirectory is called `partners` but on the website, we commonly refer to them as "Sponsors". There are subfolders for the different categories. Logos should go into the `logos/` subfolders, and the `logo` front matter entry should refer to that logo file.

### Speakers & Sessions
Very similar to the administration of the [team](#Team).

Make sure to create [sessions](/content/2024/sessions/) for all speakers. In front matter of the session (e.g. [this one](/content/2023/sessions/tutorial_yuen.md)), specify one or more speaker, referring to the `key` entry in the speaker front matter (e.g. `yuen` in [this one](/content/2023/speakers/tutorial/yuen.md)).

The front matter of sessions should specify the `year`, `format` (like `contributed`, `invited`, `industry`, `tutorial` etc.). The `type` has to be `sessions` in order to render the session properly.

For sessions with contributed talks, specify the paper ids once they are known.

There is an [overview of speakers](/content/2025/speakers/_index.html) (e.g. [2024](https://qcrypt.net/2024/speakers/)), and and [overview of sessions](/content/2025/sessions/_index.html) (e.g. [2024](https://qcrypt.net/2024/sessions/), both should be added to the "Technical Program" menu when ready.

### Schedule
Once a schedule is drawn up, insert the session names and start times into [/data/schedule-2025.yml](/data/schedule-2025.yml) like in previous years. A schedule is then automatically generated and can be added to the "Technical Program" submenu by setting `draft: false` in [/content/2025/schedule/_index.html](/content/2025/schedule/_index.html)



