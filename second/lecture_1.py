import pulp

# 创建一个线性规划问题实例，我们要最小化目标函数
prob = pulp.LpProblem("Minimization_Problem", pulp.LpMinimize)

# 定义决策变量，变量的下界是0（非负）
x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)
x3 = pulp.LpVariable("x3", lowBound=0)

# 目标函数：最小化 1*x1 + 2*x2 + 3*x3
prob += 1 * x1 + 2 * x2 + 3 * x3, "Objective Function"

# 不等式约束：-x1 + x2 <= -2 和 -x2 + x3 <= -3
prob += -x1 + x2 <= -2, "Constraint 1"
prob += -x2 + x3 <= -3, "Constraint 2"

# 解决问题
prob.solve()

# 输出结果
print("Status:", pulp.LpStatus[prob.status])
print("Optimal value: ", pulp.value(prob.objective))
print("Optimal variables:", pulp.value(x1), pulp.value(x2), pulp.value(x3))