from django.core.signing import TimestampSigner, BadSignature, SignatureExpired
from django.conf import settings

signer = TimestampSigner(salt="password-reset")


def generate_email_confirm_token(user):
    return signer.sign(user.pk)


def verify_email_confirm_token(token):
    try:
        unsigned = signer.unsign(token, max_age=settings.TOKEN_EXPIRY_SECONDS)
        return int(unsigned)
    except (BadSignature, SignatureExpired):
        return None


def generate_temporary_password():
    return signer.sign("temporary")
