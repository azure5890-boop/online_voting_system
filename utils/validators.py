from database.db_connect import connection_db
from datetime import date

def check_age_eligibility(national_id):
    connection = None
    cursor = None
    try:
        connection = connection_db()
        cursor = connection.cursor()
        query = """
        SELECT dob 
        FROM citizens 
        WHERE national_id = %s
        """
        cursor.execute(query, (national_id,))
        result = cursor.fetchone()
        if result is None:
            return False
        dob = result[0]
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        if age >= 18:
            return True
        else:
            return False
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
    
def check_citizen_exists(national_id):
    connection = None
    cursor = None
    try:
        connection = connection_db()
        cursor = connection.cursor()
        query = """
        SELECT * 
        FROM citizens 
        WHERE national_id = %s 
        """
        cursor.execute(query, (national_id,))
        result = cursor.fetchone()
        if result is None:
            return False
        else:
            return True
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def check_phone_number_exists(phone_number):
    connection = None
    cursor = None
    try:
        connection = connection_db()
        cursor = connection.cursor()
        query = """
        SELECT * 
        FROM citizens 
        WHERE phone_number = %s
        """
        cursor.execute(query, (phone_number,))
        results = cursor.fetchone()
        if results is None:
            return False
        else:
            return True
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def check_national_id_exists(national_id):
    connection = None
    cursor = None
    try:
        connection = connection_db()
        cursor = connection.cursor()
        query = """
            SELECT national_id 
            FROM citizens 
            WHERE national_id = %s
            """
        cursor.execute(query,(national_id,))
        results = cursor.fetchone()
        if results is None:
            return False
        else:
            return True
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def check_voter_exists(national_id):
    connection = None
    cursor = None
    try:
        connection = connection_db()
        cursor = connection.cursor()
        query = """
            SELECT national_id 
            FROM voters 
            WHERE national_id = %s
            """
        cursor.execute(query,(national_id,))
        results = cursor.fetchone()
        if results is None:
            return False
        else:
            return True
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def verify_login(username,password,voter_code):
    connection = None
    cursor = None
    try:
        connection = connection_db()
        cursor = connection.cursor()
        query = """
            SELECT * 
            FROM voters 
            WHERE username = %s AND password = %s AND voter_code = %s
        """
        cursor.execute(query,(username,password,voter_code,))
        results = cursor.fetchone()
        return results
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def check_candidate_exists(national_id):
    connection = None
    cursor = None
    try:
        connection = connection_db()
        cursor = connection.cursor()
        query = """
            SELECT national_id 
            FROM candidates 
            WHERE national_id = %s
            """
        cursor.execute(query,(national_id,))
        results = cursor.fetchone()
        return results is not None
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def verify_admin_login(username,password):
    connection = None
    cursor = None
    try:
        connection = connection_db()
        cursor = connection.cursor()
        query  = """
            SELECT role
            FROM admins
            WHERE username = %s AND password = %s
        """
        cursor.execute(query,(username,password,))
        results = cursor.fetchone()
        return results
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def check_has_voted(voter_id):
    connection = None
    cursor = None
    try:
        connection = connection_db()
        cursor = connection.cursor()
        query = """
            SELECT has_voted 
            FROM voters 
            WHERE voter_id = %s
            """
        cursor.execute(query,(voter_id,))
        result = cursor.fetchone()
        if result is None:
            return
        return result[0]
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def check_candidate_id(candidate_id):
    connection = None
    cursor = None
    try:
        connection = connection_db()
        cursor = connection.cursor()
        query = """
            SELECT * 
            FROM candidates 
            WHERE candidate_id = %s
            """
        cursor.execute(query,(candidate_id,))
        result = cursor.fetchone()
        return result is None
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
