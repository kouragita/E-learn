def track_progress(user, learning_path):
    # Checks progress for a user on a learning path
    return user.get_progress(learning_path)

def update_progress(user, module):
    if module.is_completed_by(user):
        user.progress[module.id] = True
        return user.progress
    return user.progress
