# Trello workflow

Keeping it quite simple as whatever cool agile methodology doesn't matter a lot in small team and
won't bring a lot of impact and is totally outburst by everyone's motivation. But having some rules
and following basic project managements ideas is always a good thing to maintain the workflow in a
more strict and organized way.

## General points

Basic planning is the key: everyone should know what to do at the moment and doesn't do things on
their own. All tasks and their ordering should be decided on recurring meetups, that replace
grooming, planning and standup sessions, so generally we're more into waterflow model.

For better and more efficient ordering some high level goals should be decided and tasks that move
us toward them should be prioritized over any other.

## Lists' description

We have only one board to track our tasks, we don't need any statistics, nor convenient history, so
here Trello is a perfect simple option. Next four lists are present on the board:

### Propositions

Here goes all new upcoming tasks, any ideas, suggestions, new information, generally speaking -
almost everything except issues. New cards should be processed further on meetup sessions. They
could be converted into tasks, saved in `.md` on Github (if information has some possible value, but
we're unsure if we will definitely do something with it) or archived (if they were declined or don't
require any actions).

### Backlog

This and all the following lists can have only tasks in them, also, must follow two conventions -
task header should start with a verb and the card should have all proper labels in it.

Backlog is a *definitely do* list, so here goes only that tasks that we are mandatory to do at some
moment. Why don't we keep tasks that we're doubtful on or ideas here? Mostly to keep it short and
simple and don't pollute it with a lot of cards that will require some re-reading and will distract
attention.

### Priority Queue

Almost the same as the backlog, but tasks here are prioritized in order. Tasks should be done one by
one descending from the top grouped by assignees.

### Current

Here are tasks that are in progress (not usually means that they're being done right now,
more likely it's the first next task to do). Normally only one task per assignee should go here,
a parallel work on multiple is allowed though. When a task is done, comments (if any) on the
execution should be left, and the card should be merely archived. It is recommended to have a
subscription to this list so notification will be sent for a card on its completion, and in ideal
world nothing will be missed.

## Tracking of issues

It's useful to have historical tracking of issues (more in a meaning of bugs/wrong behavior), but we
don't store them on Trello as its archive is a terrible thing to search. So we use Github issues for
storing: all issue descriptions should be written there - this way they will be kept in the
repository history and will be easy to access later. For tracking of doing particular issues we need
to duplicate them with cards in Trello. Just keep it simple, no links are needed, nor any
description - just label it with `issue` and put header like `!88`, where 88 - is a number of issue
on Github.
