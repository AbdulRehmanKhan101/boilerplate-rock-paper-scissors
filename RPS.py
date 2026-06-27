def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    guess = "R"

    if len(opponent_history) > 5:
        pattern_len = 3
        recent = "".join(opponent_history[-pattern_len:])

        move_counts = {"R": 0, "P": 0, "S": 0}

        for i in range(len(opponent_history) - pattern_len):
            window = "".join(opponent_history[i:i+pattern_len])
            if window == recent:
                next_move = opponent_history[i + pattern_len]
                move_counts[next_move] += 1

        predicted = max(move_counts, key=move_counts.get)
        counter = {"R": "P", "P": "S", "S": "R"}
        guess = counter[predicted]

    return guess
