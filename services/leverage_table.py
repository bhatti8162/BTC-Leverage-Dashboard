def leverage_table(price):
    lev_data = {
        "100x": 0.01,
        "200x": 0.005
    }

    result = {}

    for lev, move in lev_data.items():
        levels = []

        for level in range(1, 5):
            pct = move * level
            points = price * pct
            long_target = price + points
            short_target = price - points

            levels.append({
                "level": f"{level}x",
                "percent_move": round(pct * 100, 2),
                "points": round(points, 2),
                "long_target": round(long_target),
                "short_target": round(short_target)
            })

        result[lev] = {
            "current_price": round(price),
            "levels": levels
        }

    return result