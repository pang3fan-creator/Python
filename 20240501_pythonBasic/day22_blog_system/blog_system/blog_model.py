import datetime


class Post:
    def __init__(self, post_id, title, content, author):
        self.post_id = post_id
        self.title = title
        self.content = content
        self.author = author
        self.comments = []
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def add_comment(self, comment):
        self.comments.append(comment)
        self.updated_at = datetime.datetime.now()

    def edit(self, title, content):
        if title:
            self.title = title
        if content:
            self.content = content
        self.updated_at = datetime.datetime.now()


class Comment:
    def __init__(self, comment_id, content, author):
        self.comment_id = comment_id
        self.content = content
        self.author = author
        self.created_at = datetime.datetime.now()


class BlogManager:
    def __init__(self):
        self.posts = {}
        self.next_post_id = 1
        self.next_comment_id = 1

    def create_post(self, title, content, author):
        post_id = self.next_post_id
        self.next_post_id += 1
        post = Post(post_id, title, content, author)
        self.posts[post_id] = post
        return post

    def get_post(self, post_id):
        return self.posts.get(post_id)

    def list_posts(self):
        return list(self.posts.values())

    def delete_post(self, post_id):
        if post_id in self.posts:
            del self.posts[post_id]

    def add_comment_to_post(self, post_id, content, author):
        post = self.get_post(post_id)
        if post:
            comment_id = self.next_comment_id
            self.next_comment_id += 1
            comment = Comment(comment_id, content, author)
            post.add_comment(comment)
            return comment
        return None
