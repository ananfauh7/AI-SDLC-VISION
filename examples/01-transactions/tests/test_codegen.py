from app.codegen import recent_transactions_sql

def test_sql_contains_core_clauses():
    sql = recent_transactions_sql()
    for token in ["SELECT", "FROM", "ORDER BY", "LIMIT"]:
        assert token in sql
