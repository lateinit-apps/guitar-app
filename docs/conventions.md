# Conventions

- [Conventions](#conventions)
  - [Project structure](#project-structure)
    - [Files/directories naming guidelines](#filesdirectories-naming-guidelines)
  - [Pull requests conventions](#pull-requests-conventions)
  - [Coding conventions](#coding-conventions)
    - [Database tables naming](#database-tables-naming)
  - [Conflict solving](#conflict-solving)
    - [Weapon kits](#weapon-kits)
    - [1 vs 1](#1-vs-1)
    - [2 vs 2](#2-vs-2)

This file contains various conventions that we are suposed to be using in our project ~~*or not*~~.

## Project structure

```txt
docs/
    images/
    *.md
vanguarde/
    public      # definitely should be renamed to a *cool* naming convention
    src/        # definitely should be renamed to a *cool* naming convention
        assets/
        components/
        *.js
    .gitignore
    README.md
    package-lock.json
    package.json
rearguarde/
    data/
       *.txt, *.etc
    model/
        *.py
    Pipfile
    Pipfile.lock
    __init__.py
    *.py
    taburet.py
.env          # in .gitignore
.flaskenv
.gitignore
README.md
```

### Files/directories naming guidelines

- kebab-case for any files and directories: use all-lowercase, and separate words with hyphens
- snake_case for any python source code:    use all-lowercase, and separate words with underscore
- prefer to use rather *cool* names than simple `src`, `app`, etc wherever possible for files and
directories and don't forget to update [glossary](glossary.md)

## Pull requests conventions

- Keep strict to our brand [branching strategy](branching-strategy.md)
- At least two approves are needed to merge a pull request
- All merges are done with a simple merge strategy to preserve all commit history and branches, no
squashes, no rebasing is allowed

## Coding conventions

- [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- 100 characters line length limit
  - supports of opening two files side by side and a console/file explorer tab on 24" monitor
  - having a small part of word over limit is fine

### Database tables naming

Pascal case for ORM-classes, snake case for table names.

## Conflict solving

For any arguable conflicts wherever 1 vs 1 or 2 vs 2 opinions that can't be resolved with a
compromise a PvP match in Minecraft should be held.

### Weapon kits

The player should have the following warrior kit:

- wooden sword (we are in eco-way of solving conflicts, aren't we?)
- leather armor (not so eco as we are trying to strict, nevertherless we can't fight naked :c )
- 5 apples (coz apples are such MVP as macOS (that we can't afford) does, nuff said)

Or the following range dd kit:

- wooden bow (we are in eco-way of solving conflicts, aren't we?)
- 64 arrow (just slap anybody who says it's not enough, at least you can do a nice peasant fist
fight if you are out of ammo)
- leather armor (not so eco as we are trying to strict, nevertherless we can't fight naked :c )
- 5 apples (coz apples are such MVP as macOS (that we can't afford) does, nuff said)

### 1 vs 1

Will be held as a duel, the duelists can choose weapon kit of their choice. The 3 matches should be
held on different biome each. 1 secundans is offered to each duelist. The winner is detecting after
all matchs will be held (blowing off steam is never a bad option).

### 2 vs 2

Rules are the same as for 1 vs 1. 5 matches should be performed, four of 1 vs 1 and one of 2 vs 2.
