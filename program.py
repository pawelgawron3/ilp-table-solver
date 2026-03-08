from ortools.sat.python import cp_model

model = cp_model.CpModel()

# vars declaration 3x4
x = {}
for r in range(3):
    for c in range(4):
        x[(r,c)] = model.new_int_var(1, 12, f"x_{r}_{c}")

