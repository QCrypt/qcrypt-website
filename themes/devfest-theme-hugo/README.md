# DevFest Theme Hugo

The theme is located in the `/themes/devfest-theme-hugo/` subdirectory. It used to be an independent theme, as a separate git submodule, but since 2023, it's permanently included in the git repository.

> [!NOTE]
> The original multi-lingual support has been dropped, but reminders of it are still lingering around.

## Getting ready to edit the theme

First, install [yarn](https://yarnpkg.com/lang/en/docs/install/).

Then, use
```
cd themes/devfest-theme-hugo
yarn
```
to install the dependencies.

As you might not have the right version of npm, you might have to install the node version manager [nvm](https://github.com/nvm-sh/nvm). Then, use
```
nvm install 10.0
```

In the same directory, run `npm start` to watch [Sass](https://sass-lang.com/) changes.

When you are happy with the result run `npm run build` to build the minified versions of `theme.js` and `theme.css`. Then commit to these.

### Installing on a new ARM Mac
node-sass is not yet ported to ARM processors, but there is a work-around described here:
https://github.com/sass/node-sass/issues/3033#issuecomment-763180778
TODO: newer software exists now...


## Site parameters

Parameters are mostly set in [hugo.toml](../../hugo.toml)

```toml
#...
baseURL = "https://qcrypt.net"
languageCode = "en"
title = "QCrypt Conference Website"

# Theme
theme = "devfest-theme-hugo"

# Params
enableEmoji = true
enableRobotsTXT = true
enableMissingTranslationPlaceholders = true

GoogleAnalytics = "G-XXXXXXXX-X"

[params]
    title = "QCrypt Conference Website"
    date = "2024-09-02"
    currentYear = 2024
    description = "International Conference on Quantum Cryptography"
    images = ["/images/social-share.jpg"]
    email = "webmaster@qcrypt.net"
    keywords = "event, quantum cryptography, QCrypt"
    copyright = "We :heart: sheep"
    copyright_link = "https://github.com/QCrypt/qcrypt-website"
    # cfpUrl = "/2024/call"
    # subscriptionUrl = ""
    appleTouchIcon = "/apple-touch-icon.png"
    favicon32 = "/favicon-32x32.png"
    favicon16 = "/favicon-16x16.png"
    manifest = "/manifest.json"
    safariPinnedTab = "/safari-pinned-tab.svg"

[params.2023]
  city = "Washington DC, USA"
  timeanddate_cityid = 263
  themeColor = "#ac191c"
  [params.2023.logos]
    jumbo = "/images/2023/QuCrC23_Logo.png"
    header = "/images/2023/QuCrC23_Logo.png"
    banner = "/images/2023/banner-2023.jpeg"

[params.2024]
  city = "Vigo, Spain"
  timeanddate_cityid = 4529
  themeColor = "#0099cc"
  [params.2024.logos]
    jumbo = "/images/2024/QCrypt_2024_logo_final.png"
    header = "/images/2024/QCrypt_24_logo_2.png"
    banner = "/images/2024/banner-2024.jpg"

[params.logos]
    footer = "/images/logos/netlify-color-accent.svg"
    footer_link = "https://www.netlify.com"

[server]
  [[server.redirects]]
      from = "/"
      to = "/2024/"
      status = 302
      force = true 

[menu]
  [[menu.2023]]
    name = "Home"
    weight = 10
    identifier = "home"
    pageRef = '/2023'
  [[menu.2023]]
    name = "Technical Program"
    weight = 20
    identifier = "technical-program"
  [[menu.2023]]
    name = "Attend"
    weight = 30
    identifier = "attend"
  [[menu.2023]]
    name = "Sponsors"
    weight = 40
    identifier = "sponsors"
    pageRef = "/2023/partners"
  [[menu.2023]]
    name = "Committees"
    weight = 50
    identifier = "committees"
    pageRef = "/2023/team"

  [[menu.2024]]
    name = "Home"
    weight = 10
    identifier = "home"
    pageRef = '/2024'
  [[menu.2024]]
    name = "Technical Program"
    weight = 20
    identifier = "technical-program"
  [[menu.2024]]
    name = "Attend"
    weight = 30
    identifier = "attend"
  [[menu.2024]]
    name = "Sponsors"
    weight = 40
    identifier = "sponsors"
    pageRef = "/2024/partners"
  [[menu.2024]]
    name = "Committees"
    weight = 50
    identifier = "committees"
    pageRef = "/2024/team"


[languages]
[languages.en]
    weight = 1
    languageName = "us"

#...
```

### Header

The top navigation bar is build with

* Site title
* Site parameter `logos.header` for the logo, specified per year in [hugo.toml](../../hugo.toml)
* Menu `main`

### Footer

The footer is build with

* Site title
* Site params `email`, `subscriptionUrl`, `logos.footer`, `copyright`
* data from `data/footer.yml`

```yml
share:
  - name: facebook
    url: https://www.facebook.com/sharer.php?u=
  - name: twitter
    url: https://twitter.com/intent/tweet?text=

follow:
  - name: twitter
    url: https://twitter.com/Qcryptc
  - name: youtube
    url: https://www.youtube.com/channel/UClpn9CxuZPHw3nzhdv0m3Hw

content:
  - title: footer_about
    links:
      - nameKey: footer_charter
        name: QCrypt Charter
        url: /charter/
        newTab: false
      - nameKey: footer_history
        name: QCrypt History
        url: /history/
        newTab: false
      - nameKey: footer_coc
        name: QCrypt Code of Conduct
        url: /code-of-conduct/
        newTab: false
```

There are also quite some more options in the original tempalate that we are currently not using.

The `url` in the links of `footer_about` is prepended with the `.Params.currentYear`, so that the footer always point to these documents of the current year.


### Home

The Home page is build with markdown and calling some shortcodes like `jumbo`, `button-link`, `home-info` etc..

#### Jumbo bloc

```hugo
{{% jumbo img="/images/2024/background-2024.jpg" imgLabel="QCrypt 2024 background" logo="/images/2024/QCrypt_2024_logo_final.png" %}}

## 2-6 September 2024

{{< button-link label="Conference Program"
                url="https://umd.box.com/s/0gp344b5j4wupyrv9wbivjdpfw350rvx"
                icon="cfp" >}}
{{< button-link label="Download Photos"
                url="pictures"
                icon="picture" >}}
{{< button-link label="Organize QCrypt 2026"
                url="2025"
                icon="map-marker" >}}
{{% /jumbo %}}
```


#### Info block

With main description and key figures.

```hugo
{{% home-info what="Participants:900,Day:1,Sessions:36,Parallel Tracks:4" class="primary" %}}
## What is QCrypt 2024?

QCrypt 2024 is the 14th edition of the yearly international scientific conference presenting last year's top results in quantum cryptography. See the list of previous conferences <a style="color: yellow" href="/2024/charter/#history-of-qcrypt">here</a>.
{{% /home-info %}}
```

![](images/block-info.png)

#### key dates
Define the two important tables with key dates and website updates.

```hugo
## Key Dates QCrypt 2023
|Date |Event|
|:----|:----|
|<strike> 27 March 2023 </strike> | <!-- <a href="https://hotcrp.science.uva.nl/" target="_blank"> --> <strike> Talk submission open now </strike>|
|<strike> Wed, 12 April 2023, 16:00 CET </strike> | <strike> Talk submission deadline </strike>|
|<strike> Wed, 3 May - Tue, 08 August 2023 </strike>| <strike> Registration open now </strike>|
|<strike> Wed, 21 June 2023</strike>|<strike> Talk acceptance notification </strike>|
|<strike>Thu, 22 June 2023</strike>|<strike> Poster submission opens</strike>|
|<strike>Fri, 30 June 2023, 16:00 CET</strike>|<strike>Poster submission deadline</strike>|
|<strike>Sat, 8 July 2023</strike>| <strike>Poster acceptance notification</strike>|
|<strike>Sat, 15 July 2023</strike>| <strike>Early bird rate deadline</strike>|
|<strike>Tue, 08 August 2023</strike>| <strike>Registration deadline</strike>|
|<strong>Mon, 14 - Fri, 18 August 2023 </strong>| <strong>QCrypt 2023</strong>|


## Website Updates
|Date |Event|
|:----|:----|
|December 12, 2023 |Talks from QCrypt 2023 are now available to <a href="https://www.youtube.com/playlist?list=PLbY0Lk6JsgBEph5CPYTQZs6cOKBPGSnnI">watch on YouTube.</a>|
|August 17, 2023 | QCrypt 2024 Venue Announced <a href="/2023/2024"> here</a>.|
|August 17, 2023 | <strong>Student Paper Awards Announced</strong> <a href="/2023/sessions/business/">here</a>.|
|August 15, 2023 | The group photo from Monday evening is now <a href="https://umd.box.com/s/ro56fac22mf5j8xkjcb06ggw0igil4nv">available to view and download.</a>|
|August 14, 2023 | The <a href="/2023/sessions/rump/">Rump Session</a> theme is: “We love turtles” ❤️🐢❤️|
|August 14, 2023 | Attendees are encouraged to fill out the <a target="_blank" href="https://docs.google.com/forms/d/e/1FAIpQLScFytHnfnz8iix5UXr8YUJgxAiBvdEAtshy3y9twJvQAY8DBA/viewform">exit questionnaire</a> about their conference experience.|
```


#### Feature speakers block (not being used)

Just present your feature speakers

```hugo
{{% home-speakers %}}
## Featured Speakers

{{< button-link label="Submit a presentation"
                url="http://www.conference-hall.io"
                icon="cfp" >}}

{{< button-link label="See all speakers"
                url="./speakers"
                icon="right" >}}

{{% /home-speakers %}}
```

![](images/feature-speakers.png)


#### Subscription block

Call to subscribe

Use the site param `subscriptionUrl`.

```hugo
{{% home-subscribe  class="primary" %}}

## Get notified about the important conference updates

{{% /home-subscribe %}}
```

![](images/subscribe.png)


### Ticket block

Display ticket information.

```hugo
{{% home-tickets %}}
# Tickets

<ul>  
<li>{{< ticket name="Blind Birds"
           starts="2019-04-04"
           ends="2019-11-08"
           price="40 €"
           info="50 first places"
           soldOut="true"
           url="https://www.billetweb.fr/devfest-toulouse-2019" >}}</li>
<li>{{< ticket name="Early Birds"
           starts="2019-04-04"
           ends="2019-11-08"
           price="60 €"
           info="70 first places"
           soldOut="true"
           url="https://www.billetweb.fr/devfest-toulouse-2019" >}}</li>
<li>{{< ticket name="Normal"
           starts="2019-04-04"
           ends="2019-11-08"
           price="80 €"
           info="250 last places"
           soldOut=""
           url="https://www.billetweb.fr/devfest-toulouse-2019" >}}</li>
</ul>

\* Your ticket gives you access to all conferences, coffee breaks, and lunch. Accommodation is NOT included in this price.

{{% /home-tickets %}}
```

![](images/block-ticket.png)

#### Location block

Show conference location.

```hugo
{{% home-location
    image="/images/map.jpg"
    address="11 Espl. Compans Caffarelli, 31000 Toulouse"
    latitude="43.6110956"
    longitude="1.4332799" %}}

## The venue

### Centre de Congrès Pierre Baudis

The Centre de Congrès Pierre Baudis is a modern place of exchange,
located on a privileged location,
in the immediate vicinity of the centre of Toulouse and in a green environment.

{{% /home-location %}}
```

![](images/block-map.png)

### Partners block

Show your partners

```hugo
{{% partners categories="platinium,gold,soutien,media,communautes" %}}
# Partners
{{% /partners %}}
```

![](images/block-partners.png)

#### Album block

```hugo
{{% album images="/images/album/2018/_25A9313.jpg,/images/album/2018/_25A9386.jpg,/images/album/2018/_25A9671.jpg,/images/album/2018/_25A9334.jpg,/images/album/2018/_25A9282.jpg,/images/album/2018/_25A9612.jpg,/images/album/2018/_25A9452.jpg,/images/album/2018/_25A9628.jpg" %}}

### Some pictures of the **DevFest Toulouse 2018** with the 👾 _retro-gaming_ theme.

<a class="btn primary" target="_blank" rel="noopener" href="https://photos.app.goo.gl/nJYFVReFUk9mnXbv9">
    See all photos
    {{% icon "right" %}}
</a>

{{% /album  %}}
```

![](images/block-album.png)


### Partners

A partner should have this params :

```yaml
title: NAME
type: partner
category: soutien
website: 'https://example.com/'
logo: /2024/partners/logos/partner.jpg
socials: []
```

### Speakers

A speaker should have this params :

```yaml
id: jane_doe
name: Mme Jane Doe
company: Super Company
featured: false
photo: /images/speakers/jane_doe.jpg
socials:
  - icon: twitter
    link: 'https://twitter.com/jane_doe'
    name: '@jane_doe'
  - icon: github
    link: 'https://github.com/jane_doe'
    name: jane_doe
shortBio: "Short bio"
companyLogo: /images/speakers/company/company.jpg
country: 'City, Country'
```

The body of the file is used as long bio.

### Sessions

<!> this is not yet stable

A sessions should have this params :

```yaml
id: an_id
title: Super mega title
language: Français
complexity: Beginner
tags:
  - Category
presentation: URL of slides
videoId: Youtub video id
speakers:
  - speaker id
talkType: Keynote
```

The body of the file is used as description.

### Team

A team member should have these params:

```yaml
title: Name
type: core
subtitle: ''
photo: photo.jpg
socials:
  - link: 'https://twitter.com/XXX'
    name: Twitter
  - link: 'https://www.linkedin.com/XXX'
    name: LinkedIn
```

### Blog

A blog should have these params:

```yaml
title: Title
brief: Short brief
image: /images/blog/photo.jpeg
date: 2019-01-20
draft: false
```

And of course, the body is the blog post.

### TODO Schedule

Development scheduled to summer 2019.

### FAQ, Code of Conduct, ...

just classique markdown file, this the `menu.main.weight: 80` to be displayed into the navbar.


### Notes

* We focus on English and French in this theme, so with other language, you should add months into the `layouts/partials/date-short.html`

## License

MIT, see [LICENSE](https://github.com/jweslley/hugo-conference/blob/master/LICENSE).
