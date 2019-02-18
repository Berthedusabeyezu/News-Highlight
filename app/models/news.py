class News:
    '''
    NewsSource class to define NewsSource Objects
    '''

    def __init__(self,id,name,description,url,category,language):
        self.id =id
        self.name = name
        self.description = description
        self.url = "https://abcnews.go.com"
        self.category = category
        self.language = language