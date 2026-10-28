from note import Note

note1 = Note("title1","content1")
note2 = Note("title2","content2")

note1.update_title("new_title1")
note1.add_tag("1tag1")
note1.add_tag("2tag1")

notes = [note1, note2]
