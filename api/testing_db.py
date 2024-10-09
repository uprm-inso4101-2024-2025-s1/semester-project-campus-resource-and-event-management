# Importing the dbinterface.py functions
from dbinterface import *
# Inserting dummy data for students
# insert_student('802123456', 'student1@example.com', 'password123')
# insert_student('802987654', 'student2@example.com', 'password456')

# # Inserting dummy data for organizations
# insert_organization('OrgOne', 'org1@example.com', 'orgpassword1')
# insert_organization('OrgTwo', 'org2@example.com', 'orgpassword2')



# Clear existing tables
clear_tables()

# Recreate tables
create_tables()


pokemon_students = [
    ('001', 'bulbasaur@example.com', 'password001'),
    ('004', 'charmander@example.com', 'password002'),
    ('007', 'squirtle@example.com', 'password003'),
    ('025', 'pikachu@example.com', 'password004'),
    ('039', 'jigglypuff@example.com', 'password005'),
    ('052', 'meowth@example.com', 'password006'),
    ('063', 'abra@example.com', 'password007'),
    ('150', 'mewtwo@example.com', 'password008'),
    ('151', 'mew@example.com', 'password009'),
    ('133', 'eevee@example.com', 'password010')
]

pokemon_organizations = [
    ('Team Rocket', 'rocket@example.com', 'orgpassword1'),
    ('Team Magma', 'magma@example.com', 'orgpassword2'),
    ('Team Aqua', 'aqua@example.com', 'orgpassword3'),
    ('Team Galactic', 'galactic@example.com', 'orgpassword4'),
    ('Team Plasma', 'plasma@example.com', 'orgpassword5'),
    ('Team Flare', 'flare@example.com', 'orgpassword6'),
    ('Team Skull', 'skull@example.com', 'orgpassword7'),
    ('Team Yell', 'yell@example.com', 'orgpassword8'),
    ('Team Star', 'star@example.com', 'orgpassword9'),
    ('Team Cipher', 'cipher@example.com', 'orgpassword10')
]

#Insert the dummy Pokémon data into the database
for student in pokemon_students:
    insert_student(student[0], student[1], student[2])

for organization in pokemon_organizations:
    insert_organization(organization[0], organization[1], organization[2])

print("\n Dummy Students and Organizations data inserted successfully. \n")

# Fetch and display students
students = fetch_students()
print("Students:")
for student in students:
    print(student)

# Fetch and display organizations
organizations = fetch_organizations()
print("\nOrganizations:")
for organization in organizations:
    print(organization)



# Test getting a student
print("\n---Testing getting a student---")
student = get_student_by_id('039')  
print(student)

# Test updating a student's email and password
print("\n---Testing Update for Students---")
update_student('001', 'newbulbasaur@example.com', 'newpassword001')
updated_students = fetch_students()
print("Students after update:")
for student in updated_students:
    print(student)

# Test deleting a student
print("\n---Testing Delete for Students---")
delete_student('025')  # Deleting Pikachu
students_after_delete = fetch_students()
print("Students after deletion:")
for student in students_after_delete:
    print(student)
    

# Test getting a organization
print("\n---Testing getting a organization---")
organization = get_organization_by_name('Team Star')  
print(organization)

# Test updating an organization's email and password
print("\n---Testing Update for Organizations---")
update_organization('Team Rocket', 'newrocket@example.com', 'neworgpassword1')
updated_organizations = fetch_organizations()
print("Organizations after update:")
for organization in updated_organizations:
    print(organization)

# Test deleting an organization
print("\n---Testing Delete for Organizations---")
delete_organization('Team Magma')  # Deleting Team Magma
organizations_after_delete = fetch_organizations()
print("Organizations after deletion:")
for organization in organizations_after_delete:
    print(organization)









