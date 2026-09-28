from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    username: str
    password: str


@dataclass(frozen=True)
class CheckoutDetails:
    first_name: str
    last_name: str
    postal_code: str


STANDARD_USER = User("standard_user", "secret_sauce")
LOCKED_OUT_USER = User("locked_out_user", "secret_sauce")
INVALID_USER = User("usuario_invalido", "senha_invalida")
CHECKOUT_DETAILS = CheckoutDetails("Alessandro", "Teste", "12345")
