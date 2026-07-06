def aggregate_user_spending(users, transactions):
    # 'users' is a list of dicts: [{'id': 1, 'name': 'Alice'}, ...]
    # 'transactions' is a list of dicts: [{'user_id': 1, 'amount': 50.0}, ...]
    
    results = []
    for user in users:
        total_spent = 0
        # Inefficient nested loop scan
        for txn in transactions:
            if txn['user_id'] == user['id']:
                total_spent += txn['amount']
        
        results.append({
            'name': user['name'],
            'total_spent': total_spent
        })
    return results
