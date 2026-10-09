"""Queries behind the views. Part 2 of the lab happens in this file."""
from blog.models import Post


def posts_for_front_page():
    # `select_related` handles the forward ForeignKey (post -> author) with a
    # single JOIN; `prefetch_related` handles the many-to-many (post <-> tags)
    # with one extra query for all the posts. Two queries total, whatever the
    # number of published posts.
    return (
        Post.objects.filter(published=True)
        .select_related("author")
        .prefetch_related("tags")
        .order_by("-published_at")
    )
