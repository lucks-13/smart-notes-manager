import json
from datetime import datetime

class Note:
    counter = 1
    def __init__(self,title,content):
        self.id = Note.counter
        Note.counter+=1
        self.title = title
        self.content = content
        self.tags = set()
        self.created = datetime.now()
        self.updated = self.created
        self.dict_to_json()

    def update_title(self,new_title):
        self.title = new_title
        self.updated = datetime.now()
        self.dict_to_json()
    
    def update_content(self,new_content):
        self.content = new_content
        self.updated = datetime.now()
        self.dict_to_json()

    def add_tag(self,tag):
        self.tags.add(tag)
        self.updated = datetime.now()
        self.dict_to_json()

    def remove_tag(self,tag):
        try:
            self.tags.remove(tag)
            self.updated = datetime.now()
            self.dict_to_json()
        except KeyError:
            print(tag," Tag is not created yet so cannot be removed")

    def dict_to_json(self):
        dict = {
            "id" : self.id,
            "title" : self.title,
            "content" : self.content,
            "tags" : list(self.tags),
            "created" : self.created.isoformat(),
            "updated" : self.updated.isoformat()
        }

        with open("session.json","w") as file:
            json.dump(note_dict,file,indent=4)


    
    
note1 = Note("title1","content1")
note2 = Note("title2","content2")

print("\n Before")
print(note1.title)
print(note1.created)
print(note1.updated)

note1.update_title("new title")
print("\n After")
print(note1.title)
print(note1.created)
print(note1.updated)


note1.tags.add("tag")

print(note1.id)
print(note1)
print(note1.title)
print(note1.content)

print(note1.tags)