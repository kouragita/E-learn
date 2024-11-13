def award_points(user, points):
    user.points += points
    return user.points

def calculate_xp(user, action_type):
    xp_gain = {
        'complete_module': 100,
        'share_resource': 50,
        'comment': 10
    }
    user.xp += xp_gain.get(action_type, 0)
    return user.xp
