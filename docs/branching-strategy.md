# Branching strategy

Strict GitHub Flow is a bit of overkill for us, so to keep things quite simple and flexible, we will
use a cut and modified version of [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/).

**tl; dr version**:

1. Implementing new independent functionality? - Create new branch
2. Working on existing components? - Commit directly to *develop* branch

## Git Flow cut summary

You have two branches that always exist, *master* and *develop*:

- *master* represents the most stable version of your project and you only ever deploy to production
from this branch.

- *develop* contains changes that are in progress and may not necessarily be ready for production.

From the *develop* branch, you create topic branches to work on individual features and fixes. Once
your feature/fix is ready to go, you merge it into *develop*, at which point you can test how it
interacts with other topic branches that your coworkers have merged in. Once develop is in a stable
state, merge it into *master*. It should always be safe to deploy to production from *master*.

## Our own modifications

Anyone is allowed and even encouraged to make commits straight in *develop* branch without using
particular branches. The [original Git Flow idea](https://nvie.com/posts/a-successful-git-branching-model/#feature-branches)
was about creating feature branches on *local* machines:

> Feature branches typically exist in developer repos only, not in origin.

Generally a developer shouldn't create new branches when he is working on existing components, this
will help to avoid merge conflicts and will keep everyones code up-to-date.

And when a developer is going to implement a whole new bunch of functionality that looks to be
independent from the existing ones it'll be a good idea to create a new branch for it, keeping in
mind that it will some day become a PR for code review.

Remember, thinking twice is required before you create a remote tracking branch, or sometimes you'll
get in the Integration Hell:

> I've been working on my classes and think they are perfect. You've been working on yours and I
> suppose you think they're pretty good too. Carl has been working on his, and you know how that
> goes.
>
> Now we have to integrate them to build a new system. Carl's code, as usual, breaks
> everything. It looks to me as if you have a few problems too. My code is solid, I know that
> because I worked hard on it.
>
> What I can't understand is why you think there might be something wrong with my code, and
> Carl, the idiot, is after both of us.
> We're in for a few really unpleasant days. Maybe next time we shouldn't wait so long to
> integrate...
