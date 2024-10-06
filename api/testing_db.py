# Importing the dbinterface.py functions
from dbinterface import insert_student, insert_organization, clear_tables, create_tables,fetch_organizations,fetch_students

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

print("\n Dummy Pokémon data inserted successfully. \n")


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






