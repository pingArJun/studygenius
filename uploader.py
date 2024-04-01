import sqlite3

def upload_data(file_path, data_name, subject_name, data_type):
    try:
        # Open a connection to the database
        connection = sqlite3.connect("sem6.db")
        cursor = connection.cursor()

        # Read the file data in binary mode
        with open(file_path, "rb") as file:
            data = file.read()

        # Insert the data into the specified subject table based on data type
        if data_type.lower() == "assignment":
            cursor.execute(f"INSERT INTO {subject_name} (name_a, assignment) VALUES (?, ?)",
                           (data_name, data))
        elif data_type.lower() == "notes":
            cursor.execute(f"INSERT INTO {subject_name} (name, docs) VALUES (?, ?)",
                           (data_name, data))

        # Commit the transaction and close the connection
        connection.commit()
        connection.close()

        print(f"{data_type.capitalize()} added successfully.")
    except Exception as e:
        print(f"An error occurred while uploading the {data_type.lower()}: {e}")

if __name__ == "__main__":
    file_path = input("Enter the file path: ").strip('"')  # Remove surrounding double quotes
    data_name = input("Enter the name of the data: ")
    subject_name = input("Enter the subject name (AI/Mobile_Computing/NLP/ANN/Information_Security/Cybersecurity/DBMS): ")
    data_type = input("Enter the type of data (Assignment/Notes): ")
    if not data_name.lower().endswith('.pdf'):
        data_name += '.pdf'


    # Replace spaces with underscores and convert to uppercase
    subject_name = subject_name.upper().replace(" ", "_")

    upload_data(file_path, data_name, subject_name, data_type)




