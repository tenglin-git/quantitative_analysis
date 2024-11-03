import pulp


def transportation_problem(costs, supply, demand):
    # 行数（供应点数量）和列数（需求点数量）
    row = len(supply)
    col = len(demand)

    # 创建一个线性规划问题实例，我们要最小化目标函数
    prob = pulp.LpProblem('Transportation Problem', pulp.LpMinimize)

    # 定义决策变量，变量的下界是0（非负）
    var = [[pulp.LpVariable(f'x{i + 1}{j + 1}', lowBound=0, cat=pulp.LpInteger) for j in range(col)] for i in
           range(row)]

    # 目标函数：最小化总运输成本
    prob += pulp.lpDot([var[i][j] for i in range(row) for j in range(col)],
                       [costs[i][j] for i in range(row) for j in range(col)])

    # 供应约束：每个供应点的供应量不超过其最大供应量
    for i in range(row):
        prob += pulp.lpSum([var[i][j] for j in range(col)]) <= supply[i]

    # 需求约束：每个需求点的需求量必须满足
    for j in range(col):
        prob += pulp.lpSum([var[i][j] for i in range(row)]) == demand[j]

    # 解决问题
    prob.solve()

    # 输出结果
    print("Status:", pulp.LpStatus[prob.status])
    print("Optimal value (最小总运输成本):", pulp.value(prob.objective))
    for i in range(row):
        for j in range(col):
            if pulp.value(var[i][j]) > 0:
                print(f"从供应点 {i + 1} 到需求点 {j + 1} 的运输量: {pulp.value(var[i][j])}")


# 运输成本矩阵
costs = [
    [902, 1233, 581, 627],
    [615, 846, 901, 1027],
    [1346, 909, 648, 918]
]

# 供应量
supply = [4500, 6800, 3400]

# 需求量
demand = [3200, 5400, 3800, 2300]

# 调用函数解决运输问题
transportation_problem(costs, supply, demand)