from voluptuous import Schema, PREVENT_EXTRA

CREATE_USER_SCHEMA = Schema(
    {
        "name": str,
        "job": str,
        "id": str,
        "createdAt": str
    },
    required=True, #все поля обязательно должны вывестись с ответе
    extra=PREVENT_EXTRA #все перечисленные поля это единственные поля которые должны прийти в ответе, ничего дополнительно быть не может
)

UNKNOWN_LIST_DATA_FIELD = Schema(
    {
        "id": int,
        "name": str,
        "year": int,
        "color": str,
        "pantone_value": str
    }
)

SUPPORT_SCHEMA = Schema(
    {
        "url": str,
        "text": str
    }
)

UNKNOWN_LIST_SCHEMA = Schema(
    {
        "page": int,
        "per_page": int,
        "total": int,
        "total_pages": int,
        "data": [UNKNOWN_LIST_DATA_FIELD],
        "support": SUPPORT_SCHEMA
    }
)
