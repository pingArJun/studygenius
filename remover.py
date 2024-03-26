import sqlite3

def delete_data(subject_name, data_name, data_type):
    try:
        # Open a connection to the database
        connection = sqlite3.connect("sem6.db")
        cursor = connection.cursor()

        # Delete the data from the specified subject table based on data type
        if data_type.lower() == "assignment":
            cursor.execute(f"DELETE FROM {subject_name} WHERE name_a = ?", (data_name,))
        elif data_type.lower() == "notes":
            cursor.execute(f"DELETE FROM {subject_name} WHERE name = ?", (data_name,))

        # Commit the transaction and close the connection
        connection.commit()
        connection.close()

        print(f"{data_type.capitalize()} deleted successfully.")
    except Exception as e:
        print(f"An error occurred while deleting the {data_type.lower()}: {e}")

if __name__ == "__main__":
    subject_name = input("Enter the subject name (AI/Mobile_Computing/NLP/ANN/Information_Security/Cybersecurity/DBMS): ")
    data_name = input("Enter the name of the data (PDF file name): ")
    data_type = input("Enter the type of data (Assignment/Notes): ")

    # Replace spaces with underscores and convert subject name to uppercase
    subject_name = subject_name.upper().replace(" ", "_")

    delete_data(subject_name, data_name, data_type)
