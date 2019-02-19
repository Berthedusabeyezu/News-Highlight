class Articles:
    '''
    Articles class to define Articles Objects
    '''

    def __init__(self,id,author,title,url,urlToImage,publishedAt,content):
        self.id = id
        self.author = author
        self.title = title
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content