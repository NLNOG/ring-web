# ring-web

This repository contains the [Hugo](https://gohugo.io/) sourcecode for [ring.nlnog.net](https://ring.nlnog.net/)

## Development hints

To run the site locally, run the following commands:
```
git clone https://github.com/NLNOG/ring-web.git
cd ring-web
cp config.toml.base config.toml # Uncomment baseURL and change to http://127.0.0.1/
mkdir themes
git clone https://github.com/NLNOG/hugo-theme-anubis.git themes/ring-anubis
hugo server --buildDrafts
```
