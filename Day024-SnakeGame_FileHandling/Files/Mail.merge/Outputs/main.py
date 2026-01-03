with open('Day24/Files/Mail.merge/Input/names.txt') as f1:
    contents_f1=f1.read()
    data=contents_f1.split()

with open('Day24/Files/Mail.merge/Input/Birthday_invitation.txt') as f2:
    contents_f2=f2.readlines()
    for name in data:
        with open(f'Day24/Files/Mail.merge/Outputs/{name}.txt','w') as file:
            for contents in contents_f2:
                file.write(contents.replace("name",f"{name}"))
                
