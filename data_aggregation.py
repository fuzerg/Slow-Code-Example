def aggregate_user_spending(users, transactions):
    # 'users' is a list of dicts: [{'id': 1, 'name': 'Alice'}, ...]
    # 'transactions' is a list of dicts: [{'user_id': 1, 'amount': 50.0}, ...]
    
    from collections import defaultdict
    
    # Pre-aggregate transaction amounts by user_id in O(T) time
    spending = defaultdict(float)
    for txn in transactions:
        spending[txn['user_id']] += txn['amount']
        
    results = []
    # Build the final list in O(U) time
    for user in users:
        results.append({
            'name': user['name'],
            'total_spent': spending[user['id']]
        })
    return results
