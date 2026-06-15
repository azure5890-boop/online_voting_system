from database.db_connect import connection_db
def admin_login():
    print("\n--- Admin Login ---\n")
    try:
        connection = connection_db()
        cursor = connection.cursor()
        