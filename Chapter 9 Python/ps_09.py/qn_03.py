for i in range(2,21):
    with open(f"ps_09.py/multiplication_tables_of{i}", "w") as f:
        for j in range (1,11):
            f.write(f"{i}X{j}={i*j}\n")