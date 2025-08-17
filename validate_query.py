import re

def validate_sql_query(sql: str) -> bool:
    sql_upper = sql.strip().upper()
    allowed = ['SELECT', 'INSERT', 'UPDATE', 'DELETE']
    if not any(sql_upper.startswith(op) for op in allowed):
        return False
    if sql.count(';') > 1 or ';' in sql.rstrip(';'):
        return False

    forbidden = ['DROP', 'TRUNCATE', 'ALTER', 'GRANT', 'REVOKE', 'CREATE']
    if any(f in sql_upper for f in forbidden):
        return False

    return sql
