# Product Requirements Document

## MVP

ASAP we got the MVP - we go live immediately and start to deploy our platform on official placement.
In concept of game dev this stage is called open beta. After reaching this stage we can show our
platfrom to acquaintances and relatives.

- [x] test database with dummy data for storing all that we will need on this stage
- [x] search by release names and artists names
- [x] sorting by release names and artists names
- [ ] download tabs in .gp5 format
- [ ] tab viewer

*Note: by release here are considered release category from our database, look
[here](db-schema-explanatory.md) for explanation.*

## Release version

The core functionality that stop us from calling our service a solid release candidate. After
reaching this stage at least we are encouraged to share our service via the social channels that we
have.

- Core:
  - [ ] search by year/album name/genre
  - [ ] sorting by album name/release year/genre/release type/album kind
  - [ ] login/password authentication
  - [ ] admin/moderator/user authentication pools
  - [ ] admin/moderator functionality
  - [ ] uploading of tabs in .gp5 format + upload queue (always approved by default)
  - [ ] *somehow* populated database with real life data

- Other:
  - [ ] store custom songs/sheets lists
  - [ ] static rating system statistics (view/download/searched/indexed times)
  - [ ] dark/lite themes
  - [ ] full screen mode
  - [ ] tab editor + editing queue (always approved by default)
  - [ ] tab creator + creation queue (always approved by default)

## Post-release suggestions

The additional functionality that we can consider to implement. After reaching or during this stage
we can consider starting an advertising company to engage a lot of real users to our service.

- Highly likely:
  - [ ] print tabs to PDF
  - [ ] playing of songs + automatic scrolling with various bpm
  - [ ] email authentication
  - [ ] account recovery service
  - [ ] album/author thumbnails
  - [ ] difficulty of song
  - [ ] editing/upload queues verification mechanism
  - [ ] more themes (we definitely need at least another one with anime)
  - [ ] RU localization

- Possible:
  - [ ] SSO authentication
  - [ ] share songs/sheets/tabs via social network
  - [ ] share songs/sheets/tabs or even lists to another account
  - [ ] customizable UI
  - [ ] private storage of self-uploaded content without verifications
  - [ ] timed lyrics for songs
  - [ ] link for youtube video
  - [ ] link for itunes/spotify/soundcloud/deezer/yandex music
  - [ ] download/upload tabs in various Guitar Pro compatible formats (GP, GPX, GP5, GP4 and GP3)

- Arguable:
  - [ ] interactive console aka linux shell just because we can
  - [ ] using sound input to record tabs (we are not an audio recognition service, are we?)
  - [ ] comments section for tab page (we are not a video hosting service, are we?)
  - [ ] forum/messages for discussions (we are not a social network service, are we?)
  - [ ] mobile app (only Artiom will do it)
