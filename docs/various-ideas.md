# Various ideas

Here we write down all ideas that we've come up with but they weren't classified as *definitely do*
and have some possible value for future.

*Yes, honestly, we just don't want to hold them in backlog :c*

## Table of Contents

- [Various ideas](#various-ideas)
  - [Table of Contents](#table-of-contents)
  - [Automated PR & commit builds](#automated-pr--commit-builds)
  - [Github actions](#github-actions)
  - [Docker image for service](#docker-image-for-service)
  - [Corporative mail service](#corporative-mail-service)
  - [Full fledged REST API for bots](#full-fledged-rest-api-for-bots)
  - [Telegram/VK/Discord bot](#telegramvkdiscord-bot)
  - [AccessKey shortcut for web site](#accesskey-shortcut-for-web-site)
  - [Flasgger](#flasgger)
  - [Grafana Loki](#grafana-loki)
  - [Online tablature recorder/player](#online-tablature-recorderplayer)

## Automated PR & commit builds

Automation is a neat thing, nothing stops humanity from automating everything. Indeed if we'll have
a CI/CD, why do we need auto PR & commit builds - it's a point to think about. Adding to the barrel
raise of computating time and costs this point can become a bit unrealiable and unuseful. Thinking
of it as just testing this as POC looks like a more significant approach.

## Github actions

Explore Github actions possibilities and find something, so much cool things from the whole awesome
world hiding there, hidden gems, sneaking dragons, no reason not to make a research, right?

## Docker image for service

We. Need. Docker. No. Exceptions.
Encapsulate our backend -> Kubernetes or whatever container orchestration -> glorious success, now
we are totally *serious* developers, no kindergarten plays anymore.

## Corporative mail service

Having your own email is at least respectful, sending noreplies is another reason, not a core thing
to do though.

## Full fledged REST API for bots

Expose more information in text, make more specific endpoints to interact with API fully via curl,
separate a new public API layer from internal one's to make it accessable from the whole internet.
100% an odd thing to do unless we'll really decide to make our own bot.

## Telegram/VK/Discord bot

Just one question to break everyones motivation: *who will be using it?*

And another one thought to totally burry it down: *even thinking about this as just training of
making bots, is there any reason to make specially a guitar-app bot which no one will ever use and
not make whatever other bot, for e.g. for our cosy Discord server that will have at least some
audience to use it sometimes? No reason, indeed.*

## AccessKey shortcut for web site

Having a web site in a modern world in 2021 without any accessability features? What are you? Casul?

Fastly get your stuff off the bed and implement that [Access Key](https://en.wikipedia.org/wiki/Access_key)
finally to prove that you're indeed on `anykeys4ek` level at least.

1. Figure out what is the most frequently used input field on each page.
2. Provide some AccessKey association with that field.

## Flasgger

Consider [this thing](https://github.com/flasgger/flasgger), definitely can be helpful, sometimes,
somewhere, maybe... ~~in a long time ago in a galaxy far, far away~~

## Grafana Loki

Loki is an instrument for logs aggregation and *cute* displaying. We MUST have it.

No, seriously, just look at [this thing's demo](https://play.grafana.org)! Don't forget to pick up
your saliva and go implement [it](https://grafana.com/oss/loki/) right ~~nav~~ ahead.

## Online tablature recorder/player

Try it out [here](https://1j01.github.io/guitar/). Possible can help to record some demo input for
our db to avoid copyright strikes in detour of .gp5. Will require some parser, unfortunately.

[Sauce](https://github.com/1j01/guitar).
