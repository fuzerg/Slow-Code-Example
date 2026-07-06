def aggregate_user_spending(users, transactions):
    # 'users' is a list of dicts: [{'id': 1, 'name': 'Alice'}, ...]
    # 'transactions' is a list of dicts: [{'user_id': 1, 'amount': 50.0}, ...]
    
    # Pre-aggregate transaction amounts by user_id
    spending_by_user = {}
    for txn in transactions:
        user_id = txn['user_id']
        spending_by_user[user_id] = spending_by_user.get(user_id, 0) + txn['amount']
        
    results = []
    for user in users:
        results.append({
            'name': user['name'],
            'total_spent': spending_by_user.get(user['id'], 0)
        })
    return results

