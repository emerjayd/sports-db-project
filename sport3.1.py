import sqlite3
import pandas as pd

def insert_data_from_csv(cursor, csv_file_path):
    # Read the CSV file and specify column names
    column_names = ['FirstName', 'LastName', 'Score', 'Team']
    players_df = pd.read_csv(csv_file_path, names=column_names, header=None)

    # Insert data into PLAYER table
    for _, row in players_df.iterrows():
        cursor.execute('''
        INSERT INTO PLAYER (number, first_name, last_name, score, team)
        VALUES (?, ?, ?, ?, ?)
        ''', (None, row['FirstName'], row['LastName'], row['Score'], row['Team']))

def read_db(cursor):
    cursor.execute('SELECT * FROM PLAYER')
    players = cursor.fetchall()
    for player in players:
        print(player)

def delete_data(cursor):
    cursor.execute('DELETE FROM PLAYER')
    print("All data deleted from PLAYER table.")

def custom_sql(cursor, conn):
    sql = input("Enter your SQL command: ")
    try:
        cursor.execute(sql)
        if sql.strip().lower().startswith("select"):
            results = cursor.fetchall()
            for result in results:
                print(result)
        else:
            conn.commit()
            print("SQL command executed successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def main():
    conn = sqlite3.connect('sports3.1.db')
    cursor = conn.cursor()

    while True:
        print("Options - 1: Read db, 2: Delete data, 3: Populate database, 99: CUSTOM SQL, 0: Exit")
        choice = input("Make a choice: ")

        if choice == '1':
            read_db(cursor)
        elif choice == '2':
            delete_data(cursor)
            conn.commit()
        elif choice == '3':
            csv_file_path = 'players.csv'  # Update with the correct path
            insert_data_from_csv(cursor, csv_file_path)
            conn.commit()
            print("Database populated with data from CSV.")
        elif choice == '99':
            custom_sql(cursor, conn)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()
