import jwt


def jwt_get_session_id(token=None):
    """
    session_id
    :param token:
    :return:
    """
    payload = jwt.decode(token, None, False)
    if isinstance(payload, dict):
        return payload.get("session_id", "")
    return getattr(payload, "session_id", "")


def jwt_get_user_secret_key(user):
    """
    JWT secret
    :param user:
    :return:
    """
    return str(user)
