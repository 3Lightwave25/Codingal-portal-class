student_data = { 
    "id1":{"Name": "Sara", "Class": "V", "Subject_Integration": "English, Math, Science"},
    "id2":{"Name": "David", "Class": "V", "Subject_Integration": "English, Math, Science"},
    "id3":{"Name": "Sara", "Class": "V", "Subject_Integration": "English, Math, Science"},
    "id4":{"Name": "Surya", "Class": "V", "Subject_Integration": "English, Math, Science"},
}

result = {}
seen_keys = []

for student_id, details in student_data.items():
    unique_key = (details["Name"], details["Class"], details["Subject_Integration"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details

for k, v in result.items():
    print(k, ":", v)