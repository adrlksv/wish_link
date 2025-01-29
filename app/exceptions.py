from fastapi import HTTPException, status


class WishExceptions(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)

class TokenAbsentException(WishExceptions):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "The token is missing"

class UserAlreadyExistsException(WishExceptions):
    status_code = status.HTTP_409_CONFLICT
    detail = "User already exists"

class IncorrectEmailOrPasswordException(WishExceptions):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect email or password"

class TokenExpiredException(WishExceptions):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "The token has expired"

class IncorrectTokenFormatException(WishExceptions):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect token format"

class UserIsNotPresentException(WishExceptions):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = ""

class UserIsNotExistsException(WishExceptions):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "User is not exists"
