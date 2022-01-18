import string
from django.core.exceptions import ValidationError

def validate_symbols(value):
    if ('@' in value) or ('#' in value):
        raise ValidationError("'@'와 '#'은 포함될 수 없습니다", code='symbol-err')
        
#밑은 코드잇에서 준거.
def contains_special_character(value):
    for char in value:
        if char in string.punctuation:
            return True
    return False


def contains_uppercase_letter(value):
    for char in value:
        if char.isupper():
            return True
    return False


def contains_lowercase_letter(value):
    for char in value:
        if char.islower():
            return True
    return False


def contains_number(value):
    for char in value:
        if char.isdigit():
            return True
    return False


def validate_no_special_characters(value):
    if contains_special_character(value):
        raise ValidationError("특수문자를 포함할 수 없습니다.")
        
        
# settings.py에서 AUTH_PASSWORD_VALIDATORS 리스트 안에 내용 다 지우고 바꿨음
class CustomPasswordValidator:
    def validate(self, password, user=None):
        if (
                len(password) < 8 or
                not contains_uppercase_letter(password) or
                not contains_lowercase_letter(password) or
                not contains_number(password) or
                not contains_special_character(password)
        ):
            raise ValidationError("8자 이상의 영문 대/소문자, 숫자, 특수문자 조합이어야 합니다.")

    def get_help_text(self): #admin 페이지에서 비번 바꿀때 나옴
        return "8자 이상의 영문 대/소문자, 숫자, 특수문자 조합을 입력해 주세요."

    
    
    