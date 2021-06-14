# Trello workflow

Keeping it quite simple as whatever cool agile methodology doesn't matter a lot in small team and
won't bring a lot of impact and is totally outburst by everyone's motivation. But having some rules
and following basic project managements ideas is always a good thing to maintain the workflow in a
more strict and organized way.

## General points

The key is in a basic planning, everyone should now what to do on in every moment of time and
doesn't do things on their own, all tasks and their ordering should be decided on repeating meetups,
that replace grooming, planning and standup sessions, so generally we're more into waterflow model.

For better and more efficient ordering some high level goals should be decided and things that move
us toward them should be prioritized over any other.

## Lists' description

We have only one board to track our tasks, we don't need any statistics, nor convenient history, so
here Trello is a perfect simple option. Next four lists are present on the board:

### Propositions

Here goes all new upcoming tasks, any ideas, suggestions, new information, generally speaking -
almost everything except issues. On meetup sessions new cards should be processed further. They
could be converted into tasks, saved in .md on github (if information has some possible value, but
we're unsure if we will definitely do something with it) or archived if they were declined or don't
require any actions.

### Backlog

This and all following lists can have only tasks in them, also, should follow next conventions -
task header should start with a verb and the card should have all proper labels in it.

Backlog is a *definitely do* list, so here goes only that tasks that we are mandatory to do at some
moment. Why we don't keep tasks that we're doubtful on or ideas here? Mostly to keep it short and
simple and don't pollute it with a lot of cards that will require some re-reading and will distract
attention.

### Priority Queue

Almost the same as the backlog, but here tasks are prioritized in order. Tasks should be done one by
one descending from the top grouped by assignees.

### Current

Simply here are tasks that are in progress (not usually means that they're being done right now,
more likely it's the first next task to do). Normally only one task per assignee should goes here,
but if by one task multiple things can be closed there can be more than one task.

## Tracking of issues

We don't store issues (more in a meaning of bugs/wrong behavior) on Trello because it's more useful
to have historical tracking of them where Trello's archive is a terrible thing to search. So for
storing issues we use github issues, all issue descriptions should be written there, this way they
will be kept in the repository history and will be easy to access later. For tracking of doing
particular issues we need to duplicate them with cards in Trello. Just keep it simple, no links are
needed, nor any description, just label it with `issue` and put header like `!88`, where 88 - is a
number of issue on github.
