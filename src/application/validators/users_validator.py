from src.domain.entities.user import User


class UsersValidator:
    @staticmethod
    def validate_mailing_time(user: User):
        if not isinstance(user.user_id, int):
            raise ValueError("User ID must be an integer")
        if not isinstance(user.username, str):
            raise ValueError("Username must be a string")

        if not isinstance(user.mailing_time, str):
            raise ValueError("Mailing time must be a string")
        real_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if not (user.mailing_time[0] in real_numbers and
                user.mailing_time[1] in real_numbers and
                user.mailing_time[2] == ':' and
                user.mailing_time[3] in real_numbers and
                user.mailing_time[4] in real_numbers):
            raise ValueError("Invalid mailing time format")

        if not isinstance(user.language, str):
            raise ValueError("Language must be a string")

        # TODO добавить проверку через бд, что такая столовая существует
        if not isinstance(user.canteen_id, int):
            raise ValueError("Canteen ID must be an integer")


