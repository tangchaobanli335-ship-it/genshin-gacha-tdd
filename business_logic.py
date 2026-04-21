def calculate_gacha_probability(pull_num):
    if not isinstance(pull_num, int) or pull_num <= 0:
        raise ValueError("pull_num must be a positive integer")
    
    # 重置为每90抽一轮
    normalized_pull = (pull_num - 1) % 90 + 1
    
    if normalized_pull == 90:
        # 第90抽必定出五星
        return 1.0
    elif normalized_pull < 74:
        # 74抽之前，基础概率0.6%
        return 0.006
    else:
        # 74抽及以后，每抽递增6%
        increase = (normalized_pull - 73) * 0.06
        # 四舍五入到三位小数，避免浮点数精度问题
        return round(0.006 + increase, 3)
