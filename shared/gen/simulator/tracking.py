"""Código de rastreio de pedido e pagamento (L1b, decisão 12; F0.3).

12 caracteres base32 Crockford dos 60 bits mais altos do SHA-256 de "<sal>:<id>". Determinístico
(a regeração produz o mesmo código) e não deixa adivinhar o vizinho sem o sal, que fica no .env.
"""

from __future__ import annotations

import hashlib

CROCKFORD = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"  # sem I, L, O e U: fácil de ditar
LENGTH = 12
BITS = 5 * LENGTH  # 60 bits


def tracking_code(entity_id: int, salt: str) -> str:
    if entity_id < 1:
        raise ValueError("tracking_code: id precisa ser positivo")
    if not salt:
        raise ValueError("tracking_code: sal vazio (TRACKING_SALT_* no shared/gen/.env)")
    digest = hashlib.sha256(f"{salt}:{entity_id}".encode()).digest()
    value = int.from_bytes(digest[:8], "big") >> (64 - BITS)
    chars = []
    for _ in range(LENGTH):
        value, index = divmod(value, 32)
        chars.append(CROCKFORD[index])
    return "".join(reversed(chars))
