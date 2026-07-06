def aggregate_user_spending(users, transactions):
    # 'users' is a list of dicts: [{'id': 1, 'name': 'Alice'}, ...]
    # 'transactions' is a list of dicts: [{'user_id': 1, 'amount': 50.0}, ...]
    
    # Pre-aggregate transaction totals by user_id to avoid nested O(N*M) loop
    txn_totals = {}
    for txn in transactions:
        u_id = txn['user_id']
        txn_totals[u_id] = txn_totals.get(u_id, 0.0) + txn['amount']
    
    results = []
    for user in users:
        results.append({
            'name': user['name'],
            'total_spent': txn_totals.get(user['id'], 0.0)
        })
    return results
