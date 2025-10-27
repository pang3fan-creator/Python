from blog_model import BlogManager
from blog_view import View


class BlogApp:
    def __init__(self):
        self.manager = BlogManager()
        self.view = View()

    def run(self):
        while True:
            command = self.view.get_input("1创建文章,2查看文章,3编辑文章,4删除文章,5添加评论,6所有信息列表,esc退出:")
            if command == "1":
                self.create_post()
            elif command == "2":
                self.view_post()
            elif command == "3":
                self.edit_post()
            elif command == "4":
                self.delete_post()
            elif command == "5":
                self.add_comment()
            elif command == "6":
                self.list_posts()
            elif command == "esc":
                break
            else:
                self.view.display_message("没有该服务~")

    def create_post(self):
        title = self.view.get_input("文章标题: ")
        content = self.view.get_input("文章内容: ")
        author = self.view.get_input("文章作者: ")
        post = self.manager.create_post(title, content, author)
        self.view.display_message(f"文章添加成功,id为: {post.post_id}")

    def view_post(self):
        post_id = int(self.view.get_input("请输入查看文章的ID: "))
        post = self.manager.get_post(post_id)
        if post:
            self.view.display_post(post)
        else:
            self.view.display_message("未找到该文章")

    def edit_post(self):
        post_id = int(self.view.get_input("请输入编辑文章的ID: "))
        post = self.manager.get_post(post_id)
        if post:
            title = self.view.get_input("新的标题: ")
            content = self.view.get_input("新的内容: ")
            post.edit(title, content)
            self.view.display_message("文章已更新")
        else:
            self.view.display_message("未找到该文章")

    def delete_post(self):
        post_id = int(self.view.get_input("请输入删除文章的ID: "))
        self.manager.delete_post(post_id)
        self.view.display_message("文章已删除")

    def add_comment(self):
        post_id = int(self.view.get_input("请输入评论文章的ID: "))
        content = self.view.get_input("评论内容: ")
        author = self.view.get_input("评论作者: ")
        comment = self.manager.add_comment_to_post(post_id, content, author)
        if comment:
            self.view.display_message(f"评论添加成功id为: {comment.comment_id}")
        else:
            self.view.display_message("未找到该文章")

    def list_posts(self):
        posts = self.manager.list_posts()
        self.view.display_posts(posts)
