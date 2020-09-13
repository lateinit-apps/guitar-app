![database schema pic here](images/crack-schema.png)

`Genre.highlights` &mdash; a short description of main features of the genre, its origin location
and time and brief summary of typical representatives.

`Song.trivia` &mdash; some facts about the song, like the origin of the idea, its recording,
subsequent reproductions at concerts, arrangements from other artists, etc.

`Song.original` &mdash; if the song is a cover of other song by other artist, this field contains
reference to the original song. Otherwise, the field is empty. `Song.covers` acts as a collection
for entities representing covers of the "local" (for relation side) one.

`Release` &mdash; table storing single entity of the artist's discography. The `type` field
contains values like:

- album
- single
- extended_play

Since the **Table-Per-Hierarchy** strategy is employed, field `album_kind` will be empty, unless
the `type` field equals `album`. This feature should be taken into account when working
with ORM models.

`Release.album_kind` &mdash; type of album depending on the place of recording, if it solo or cover
album (check [Wikipedia's page](https://en.wikipedia.org/wiki/Album#Types_of_album) for more info).
Supposed to have the following values:

- concert
- studio
- compilation
- solo
- tribute

`TrackTab.gp5_link` &mdash; link to the Guitar Pro 5 file.

From wikipedia:
> ... can be released for sale to the public in a variety of different formats. In most cases,
> a single is a song that is released separately from an album, although it usually also appears
> on an album.

We agree to not have songs from EPs and singles if they do not contain some major differencies from
their album versions. This means we most likely will not have compilation releases such as box sets
and very few singles and EPs. **There will be multiple versions of the same song only to explicitly
highlight difference of the versions**.
