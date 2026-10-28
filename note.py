class Note:
    def __init__(self,title,content):
        self.title = title
        self.content = content
    
note1 = Note("title1","content1")
note2 = Note("title2","content2")

print(note1)
print(note1.title)
print(note1.content)