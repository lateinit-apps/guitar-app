# Conventions

This file contains various conventions that we are suposed to be using in our project ~~*or not*~~.

## Project structure

```md
app/
    model/
        *.py
    static/
        *.css, *.js, *.txt, *.etc
    templates/
        *.html          # Jinja2 templates
    __init__.py
    *.py
    taburet.py
docs/
    images/
    *.md
react/
    ???
.env          # in .gitignore
.flaskenv
.gitignore
Pipfile
Pipfile.lock
README.md
run.py
```

## Files/directories naming guidelines

- kebab-case for any files and directories: use all-lowercase, and separate words with hyphens
- snake_case for any python source code: use all-lowercase, and separate words with underscore

## Coding conventions

- [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- 100 characters line length limit
  - supports of opening two files side by side and a console/file explorer tab on 24" monitor
  - having a small part of word over limit is fine

## Database tables naming

Pascal case for ORM-classes, snake case for table names.
