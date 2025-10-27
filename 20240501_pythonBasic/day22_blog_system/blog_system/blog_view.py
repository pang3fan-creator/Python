class View:
    def display_message(self, message):
        print(message)

    def display_post(self, post):
        print(
            f"文章ID: {post.post_id}, 标题: {post.title}, 作者: {post.author}, 创建时间: {post.created_at}, 更新时间: {post.updated_at}")
        print(f"文章内容:\n{post.content}")
        print("该文章的评论:")
        for comment in post.comments:
            print(f"  评论ID: {comment.comment_id}, 评论作者: {comment.author}, 创建时间: {comment.created_at}")
            print(f"  评论内容: {comment.content}")

    def display_posts(self, posts):
        for post in posts:
            self.display_post(post)

    def get_input(self, prompt):
        return input(prompt)
