def generate_next_actions(readiness, roles):
    actions = []

    if readiness["status"] != "Ready":
        actions.append("Delay placements and focus on skill improvement")

    if roles:
        actions.append(f"Target roles: {', '.join(roles)}")

    actions.append("Schedule mock interview after 7 days")

    return actions
