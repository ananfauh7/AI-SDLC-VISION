def recent_transactions_sql(limit:int=10) -> str:
    assert limit > 0
    return (
        "SELECT date, description, amount "
        "FROM transactions WHERE customer_id = :id "
        "ORDER BY date DESC LIMIT :limit"
    )
