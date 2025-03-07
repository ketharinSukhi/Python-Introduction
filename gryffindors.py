students = [
            {"name":"Hermione","house":"Gryffindor","patronus":"Otter"},
            {"name":"Harry","house":"Gryffindor","patronus":"Stag"},
            {"name":"Ron","house":"Gryffindor","patronus":"Jack Russel Terrier"},
            {"name":"Draco","house":"Slytherin","patronus":None }
             ]

gryffindors =[
    student["name"] for student in students if student["house"] == "Gryffindor" 
]