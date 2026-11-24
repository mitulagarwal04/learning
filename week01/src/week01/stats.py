def mean(values: list[float]) -> float:
    if len(values) == 0:
        raise ValueError("mean of empty list")
    return sum(values) / len(values)
