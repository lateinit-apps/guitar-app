# Technical Documentation for API

## 1. Overview

In this section we'll highlight what we actually expect from the *Rearguade*'s API.

### 1.1. Common functions

Here we'll describe some general functionality that applies for all available resources, unless
it's some special case.

All basic resources shall implement classic CRUD (**C**reate, **R**ead, **U**pdate, **D**elete)
requests with this fairly common set of HTTP methods. A slightly modified version of the neat table
snatched directly from [REST API Tutorial](restapitutorial.com) locates below:

| HTTP Verb |      CRUD      |   Status codes for collections   |  Status codes for single item   |
|-----------|----------------|----------------------------------|---------------------------------|
| POST      | Create         | `201` (Created)                  | `405` (Method Not Allowed)      |
| GET       | Read           | `200` (OK) or `204` (No Content) | `200` (OK) or `404` (Not Found) |
| PUT       | Update/Replace | `405` (Method Not Allowed)       | `200` (OK) or `404` (Not Found) |
| PATCH     | Update/Modify  | `405` (Method Not Allowed)       | `200` (OK) or `404` (Not Found) |
| DELETE    | Delete         | `405` (Method Not Allowed)       | `200` (OK) or `404` (Not Found) |

There are some notes and alterations:

1. POST on collections must return `Location` header with link to newly created `'/resource/{id}'`
2. We restrict POST query with specific item ID
3. GET on collections employs basic tecniques such as pagination, sorting and filtering. They will
be described in the sections below
4. For the time being we can ignore PATCH requests or handle them like PUT with only modified part
of the object
5. GET returns 204 code if there are no available objects in the collection by given query

---

#### Pagination

We've picked the simplest kind of pagination to implement: limit/offset pagination. It requires
two parameters:

- `offset` - starting row number. Default value is `0`; any number less than zero is invalid
- `limit` - sets maximum size of the retrieved collection. Default value is `20` and cannot be
increased any further, returning HTTP `400 Bad Request` on attempts to specify more than allowed.

---
  
#### Sorting

`?sort_by=<field_name>!<desc|asc>`

Exclamation mark belongs to so-called "safe" URL characters, i.e. it shouldn't be encoded in order
to be passed to the backend. There also can be multiple-column sorting by comma-separated fields
of the resource.

Example:

`/artists?sort_by=year_founded!desc,name!asc`

---

#### Filtering

Filtering allows fetching only specific items from a collection and applies *before* pagination and
sorting. Multiple filter queries implies logical AND conjuction. There are two kinds of filtration
supported in the API: simplified and advanced.

##### Simplified

Provides possibility for exact field value matching. Format: `?<filter_field>=<value>`. Apparently,
valid filter field names are individual for every resource defined in the API. In case some field
name is used in both simplified and advanced interfaces, the latter one takes precedence and
simple filtering is ignored.

Example: 

`/releases?label=volcano&album_kind=studio`

##### Advanced

Advanced filtering parameters have a generic template: `?filter(<filter_field>)<operator>=<value>`.
Available operators and their functions varies for different type of fields.

- String fields operators:
  - `__contains` - filtering by substring
  - `__regex` - filtering by regex query; supports `^` (encoded), `$` (encoded), `.`,
`|` (encoded), `*`, `?` (encoded) symbols;
semantics are similar to [Python's `re` package](https://docs.python.org/3/library/re.html)
  - `__exact` - exact value; case-insensitive

- Numerical fields operators:
  - `__gte` - greater or equal than value
  - `__lte` - less or equal than value
  - `__gt` - greater than value
  - `__lt` - less than value
  - `__exact` - exact value; not applicable to floating point parameters

- Date fields operators:
  - `__before` - all dates before value
  - `__after` - all dated after value
  - `__exact` - exact value

Example:

`/songs?filter(id)__gt=42&filter(name)__contains=ramble`

##### Date value format

We'll try to stick to the
[5 laws of API dates and times](http://apiux.com/2013/03/20/5-laws-api-dates-and-times/).

In the nutshell:

- Law #1: Use [ISO-8601](https://www.iso.org/iso-8601-date-and-time-format.html) for your dates
(`YYYY-MM-DDTHH:mm:ss.sss±hh:mm`, e.g. `1937-01-24T12:00:27.87+00:20`)
- Law #2: Accept any timezone
- Law #3: Store it in UTC
- Law #4: Return it in UTC
- Law #5: Don’t use time if you don’t need it

For more discussion look [into this SO page](https://stackoverflow.com/questions/9581692/recommended-date-format-for-rest-get-api).

---

#### Including joint resources

Related resources by default represented as single ID or list of them. If we want to include related
recources as nested objects we should use `include` parameter. For example:

`/songs?include=releases.artists,sheets`

Note that sorting and filtering can be applied to the nested fields as well. They can be accessed
through their resource name with dot:

`/songs?include=releases.artists&sort_by=releases.artists.name!asc&filter(releases.name)__exact=fear%20of%20the%20dark`

---

#### Picking certain fields

By default, API returns all available fields. We can specify set of fields we actually want to get
using `fields` parameter. 

Example:

`/releases?fields=id,name,year`

### 1.2. Special cases

For now, we don't have resources with some special queries or behavior.

## 2. API Specification

API is subdivided into two modules with separate base paths: `/meta` and `/resources`. The first one
is a collection of helper and transient resources and won't be covered here. Resources are reckoned
as application data, and reflect database entities. Here we go with the definitive list of
available resources along with their fields and neighbor resources (i.e. those that can be reached via "joint resources" notation):

<table>
  <thead>
    <tr>
      <th>Resource</th>
      <th>Adjacent Resources</th>
      <th>Field</th>
      <th>Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="7">Artist</td>
      <td rowspan="7"><ul><li>Genre</li><li>Release</li></ul></td>
      <td>`id`</td>
      <td>Numerical: positive integer</td>
    </tr>
    <tr>
      <td>`about`</td>
      <td>String</td>
    </tr>
    <tr>
      <td>`country`</td>
      <td>String</td>
    </tr>
    <tr>
      <td>`name`</td>
      <td>String</td>
    </tr>
    <tr>
      <td>`year_founded`</td>
      <td>Numerical: positive integer</td>
    </tr>
    <tr>
      <td>`genre_ids`</td>
      <td>List of positive integers</td>
    </tr>
    <tr>
      <td>`release_ids`</td>
      <td>List of positive integers</td>
    </tr>
    <tr>
      <td rowspan="5">Genre</td>
      <td rowspan="5"><ul><li>Artist</li><li>Release</li></ul></td>
      <td>`id`</td>
      <td>Numerical: positive integer</td>
    </tr>
    <tr>
      <td>`highlights`</td>
      <td>String</td>
    </tr>
    <tr>
      <td>`name`</td>
      <td>String</td>
    </tr>
    <tr>
      <td>`artist_ids`</td>
      <td>List of positive integers</td>
    </tr>
    <tr>
      <td>`release_ids`</td>
      <td>List of positive integers</td>
    </tr>
  </tbody>
</table>
