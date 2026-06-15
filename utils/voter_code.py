import random

def voter_code_generator():
    try:
        var_1 = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=4))
        var_2 = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=4))
        var_3 = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=4))
        voter_code = f"{var_1}-{var_2}-{var_3}"
        return voter_code
    except Exception as e:
        print("An error occurred during voter code generation:", e)
        return None
    