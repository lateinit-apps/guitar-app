# Product Requirements Document

## MVP

ASAP we got the MVP - we go live immediately and start to deploy our platform. In concept of game
dev this stage is called open beta. After reaching this stage we can show our platfrom to
acquaintances and relatives.

- test database with dummy data for storing all that we will need on this stage
- search by release names and artists names/albums/year/genre
- download tabs in ASCII .txt (our own format) - *under decision*
- sorting by release names and artists names

*Note: by release here are considered release category from our database, look
[here](db-schema-explanatory.md) for explanation.*

## Release version

The core functionality that stop us from calling our service a solid release candidate. After
reaching this stage at least we are encouraged to share our service via the social channels that we
have.

- sorting by release year/genre name/release type/album kind
- login/password authentication
- admin/moderator/user authentication pools
- admin/moderator page
- store custom songs lists
- store custom sheets/tabs lists
- static rating system statistics (view/download/searched/indexed times)
- full screen mode
- tab editor + editing queue (always approved by default)
- tab creator + creation queue (always approved by default)
- dark/lite themes
- *somehow* populated database

## Post-release suggestions

The additional functionality that we can consider to implement. After reaching or during this stage
we can consider starting an advertising company to engage a lot of real users to our service.

- Most likely:
  - print tabs to PDF
  - playing of songs
  - difficulty of song
  - email authentication
  - account recovery service
  - SSO authentication
  - timed lyrics for songs
  - share songs/sheets/tabs via social network
  - share songs/sheets/tabs or even lists to another account
  - editing/upload queues verification mechanism
  - private storage of self-uploaded content without verifications
  - more themes (we definitely need at least another one with anime)
  - customizable UI
  - download tabs in Guitar Pro compatible formats (GP, GPX, GP5, GP4 and GP3)
  - upload tabs in Guitar Pro compatible formats (GP, GPX, GP5, GP4 and GP3)
  - RU localization
  - album/author thumbnails
  - link for youtube video
  - link for itunes/spotify/soundcloud/deezer/yandex music
  - mobile app

- Arguable:
  - using sound input to record tabs (we are not an audio recognition service, are we?)
  - comments section for tab page (we are not a video hosting service, are we?)
  - forum/messages for discussions (we are not a social network service, are we?)
