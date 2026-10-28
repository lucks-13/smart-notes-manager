class Note:
    counter = 1
    def __init__(self,title,content,tags):
        self.id = Note.counter
        Note.counter+=1
        self.title = title
        self.content = content
        self.tags = tags
    
note1 = Note("title1","content1")
note2 = Note("title2","content2")

print(note1.id)
print(note1)
print(note1.title)
print(note1.content)