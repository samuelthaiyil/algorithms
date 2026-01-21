class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.posts = []
    
    def add_post(content):
        if content != None:
            self.posts.append(content)
    
    def remove_post(index):
        del self.posts[index]
        
class Post:
    def __init__(self, id, created_by, created_at, content, comments):
        self.id = id
        self.created_by = created_by
        self.created_at = created_at
        self.content = content
        self.comments = []
        self.likes = []
    
    def add_comment(comment):
        if typeof(comment) == "Comment":
            self.comments.append(comment)
    
    # would make this toggle like function
    def add_like(user):
        if typeof(user) == "User":
            self.likes.append(user)
    
            
class Comment:
    def __init__(self, id, post_id, created_by, content):
        self.id = id
        self.post_id = post_id
        self.created_by = created_by
        self.content = content


