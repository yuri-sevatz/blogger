#!/usr/bin/env python
from cvm.dom import Selector
from cvm.view import Field, View, Page, Group


class Blog(Page):
    def __init__(self):
        self.posts = Group(Post(Selector.CLASS, "post"))
        self.pager = Pager(Selector.ID, "blog-pager")


class Post(View):
    def __init__(self, selector: Selector, value: str):
        super().__init__(selector, value)
        self.blogId = Field(Selector.XPATH, ".//*[contains(concat(' ', normalize-space(@itemprop), ' '), ' blogId ')]")
        self.postId = Field(Selector.XPATH, ".//*[contains(concat(' ', normalize-space(@itemprop), ' '), ' postId ')]")
        self.title = Field(Selector.XPATH, ".//*[contains(concat(' ', normalize-space(@itemprop), ' '), ' name ')]")
        self.url = Field(Selector.XPATH, ".//*[contains(concat(' ', normalize-space(@itemprop), ' '), ' name ')]/a")
        self.body = Body(Selector.XPATH, ".//*[contains(concat(' ', normalize-space(@itemprop), ' '), ' description ')]")
        self.labels = Labels(Selector.CLASS, "post-labels")


class Body(View):
    def __init__(self, selector: Selector, value: str):
        super().__init__(selector, value)
        self.self = Field(Selector.XPATH, ".")
        self.links = Group(Field(Selector.XPATH, ".//a"))
        self.embeds = Group(Field(Selector.XPATH, ".//embed"))


class Labels(View):
    def __init__(self, selector: Selector, value: str):
        super().__init__(selector, value)
        self.tags = Group(Field(Selector.XPATH, ".//a[@rel='tag']"))


class Pager(View):
    def __init__(self, selector: Selector, value: str):
        super().__init__(selector, value)
        self.prev = Field(Selector.XPATH, "id('blog-pager-older-link')/a")
        self.next = Field(Selector.XPATH, "id('blog-pager-newer-link')/a")
