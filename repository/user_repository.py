from db.connection import get_connection
from models.user_model import User

class UserRepository:

    @staticmethod
    def get_all():
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                sql = "SELECT user_id, username, password FROM user"
                cursor.execute(sql)
                rows = cursor.fetchall()
                return [User(**row) for row in rows]
        finally:
            conn.close()

    @staticmethod
    def get_by_id(user_id):
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                sql = "SELECT user_id, username, password FROM user WHERE user_id = %s"
                cursor.execute(sql, (startDate, endDate,))
                row = cursor.fetchone()
                return User(**row) if row else None
        finally:
            conn.close()