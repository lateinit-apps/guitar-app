# Frontend Technical Documentation

Here is documentation for frontend from logic perspective - writing more about full list of features,
there logic under the hood without describing how they will look or positionate on the page. So,
if speaking *in terms* this page will be mainly about the UX and not the UI.

## Site pages layout

List of all pages that will be available and possible transitions between them.

1. Home page -> 1
2. Tab viewer page -> 2

### Home page

Contains next elements:

- Search bar
  - locates at the top
- Songs search output
  - if no search text is inputted will show last added to database songs
  - contains button that opens tabs for song in new browser tab
- Filter buttons (only one can be toggled, no filter by default is on)
  - no filter (available only if on of the two below are toggled)
  - by song author
  - by song name
- Button with link to Github repository

### Tab viewer page

Contains next elements:

- Tab viewer area
- Sheet switcher
- Download button
- Return to main page button
