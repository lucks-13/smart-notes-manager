from datetime import datetime

class Note:
    counter = 1
    def __init__(self,title,content):
        self.id = Note.counter
        Note.counter+=1
        self.title = title
        self.content = content
        self.tags = []
        self.created = datetime.now()
    
note1 = Note("title1","content1")
note2 = Note("title2","content2")

note1.tags.append("tag")

print(note1.id)
print(note1)
print(note1.title)
print(note1.content)

print(note1.tags)