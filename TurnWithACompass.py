def direction(facing, turn):
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    turns = turn // 45
    
    facing_start = directions.index(facing)
    facing_end = (facing_start + turns) % len(directions)
    
    return directions[facing_end]