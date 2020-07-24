# Technical Documentation for API

## 1. Motivation

In this section we'll discuss what we actually we want from the ~~backend~~ *reargude*'s API

### 1.1 Common functions

Here we'll describe some general functionality that applies for all available resources, unless it's a some special case.

All basic resources shall implement classic CRUD (**C**reate, **R**ead, **U**pdate, **D**elete) requests with this fairly common set of HTTP methods.

Below the neat table that I snatched directly from restapitutorial.com:

| HTTP Verb | CRUD           | Collection               | Item                        |
|-----------|----------------|--------------------------|-----------------------------|
| POST      | Create         | 201 (Created)            | 405 (Method Not Allowed)    |
| GET       | Read           | 200 (OK)                 | 200 (OK) or 404 (Not Found) |
| PUT       | Update/Replace | 405 (Method Not Allowed) | 200 (OK) or 404 (Not Found) |
| PATCH     | Update/Modify  | 405 (Method Not Allowed) | 200 (OK) or 404 (Not Found) |
| DELETE    | Delete         | 405 (Method Not Allowed) | 200 (OK) or 404 (Not found) |

There are some notes and alterations:

1. POST on collections must return 'Location' header with link to newly created *'/resource/{id}'*
2. We restrict POST query with specific item ID
3. GET on collections employs basic tecniques such as pagination, sorting and filtering. They will be described in the sections below
4. For the time being we can ignore PATCH requests or handle them like PUT with only modified part of the object

#### Pagination

  For pagination we picked the simples kind of it: limit/offset pagination. It needs to parameters:

- *offset* - starting row number. Default value is 0.
- *limit* - sets maximum size of the retrived collection. Default value is 20. Note: we should hardcode some upper limit.
  
#### Sorting

  For sorting we intend to multi-column sorting. It has single parameter *sort_by*:

- *sort_by=\[{field_name}.{desc|asc},\]*

#### Filtering

  Filtering applies before pagination and sorting. Filtering parameters have common template `?filter\[{filter_field}\]__{operator}={value}`. Available operators and their functions varies for diffent type of fields. Multiple filter queries implies logical AND conjuction.

- String fields operators
  - *__in* - filtering by substring
  - *__regex* - filtering by regex query
  - *__exact* - exact value
- Numerical fields operators
  - *__gte* - greter or equal than value
  - *__lte* - less or equal than value
  - *__gt* - greter than value
  - *__lt* - less than value
  - *__exact* - exact value
- Date fields operators
  - *__before* - all dates before value
  - *__after* - all dated after value
  - *__exact* - exact value

#### Date value format

We'll try to stick to (the 5 laws of API dates and times)[http://apiux.com/2013/03/20/5-laws-api-dates-and-times/]

In the nutshell:

- Law #1: Use ISO-8601 for your dates (YYYY-MM-DDTHH:mm:ss.ss±hh:mm, e.g. 1937-01-01T12:00:27.87+00:20)
- Law #2: Accept any timezone
- Law #3: Store it in UTC
- Law #4: Return it in UTC
- Law #5: Don’t use time if you don’t need it

For more discussion look (into this SO page)[https://stackoverflow.com/questions/9581692/recommended-date-format-for-rest-get-api]

#### Including joint resources

Related resources by default represented as single ID or list of them. If we want to include related recources as nested objects we should use `include` parameter For example:

`/songs?include=releses.artists,sheets`

#### Pick only some fields

By default, API returns all available fields. We can specify set of fields we actually want to get using `fields` parameter. For example:

`/releases?fields=id,name,year`

### 1.2 Special cases

Here we'll describe some general functionality that applies for all available resources, unless it's a some special case.

## 2. Documentation