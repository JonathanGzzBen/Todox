#!/usr/bin/env python3

import sqlite3
import os

database_filename = "todox.db"

def create_database_if_not_exists():
    if os.path.exists(database_filename):
        return
    try:
        sqlite_connection = sqlite3.connect(database_filename)
        sqlite_create_table_todo_query = """
            CREATE TABLE IF NOT EXISTS Todo (
                id INTEGER PRIMARY KEY,
                content TEXT NOT NULL
            );
        """
        cursor = sqlite_connection.cursor()
        cursor.execute(sqlite_create_table_todo_query)
        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Error while creating sqlite table", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

def save_todo(content):
    try:
        create_database_if_not_exists()
        sqlite_connection = sqlite3.connect(database_filename)
        cursor = sqlite_connection.cursor()

        sqlite_insert_todo_query = """
            INSERT INTO Todo (content)
            VALUES (?)
        """
        cursor.execute(sqlite_insert_todo_query, (content,))
        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

def get_todos():
    try:
        create_database_if_not_exists()
        sqlite_connection = sqlite3.connect(database_filename)
        cursor = sqlite_connection.cursor()

        sqlite_select_all_todos = """
            SELECT id, content
            FROM Todo
        """
        cursor.execute(sqlite_select_all_todos)
        todos = cursor.fetchall()
        cursor.close()
        return todos
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

def delete_todo(id):
    try:
        create_database_if_not_exists()
        sqlite_connection = sqlite3.connect(database_filename)
        cursor = sqlite_connection.cursor()

        sqlite_delete_todo_query = """
            DELETE FROM Todo
            WHERE id=?
        """
        cursor.execute(sqlite_delete_todo_query, (id,))
        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to delete todo", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()