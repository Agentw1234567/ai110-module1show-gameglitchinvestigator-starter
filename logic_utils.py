def get_range_for_difficulty(difficulty: str):
    """Return the inclusive range of possible secret numbers for a difficulty.

    Args:
        difficulty: The difficulty level selected by the player, such as
            ``"Easy"``, ``"Normal"``, or ``"Hard"``.

    Returns:
        tuple[int, int]: A ``(low, high)`` pair where both bounds are
        inclusive and ``low <= high``. Unrecognized difficulty values fall
        back to the ``"Normal"`` range.

    Example:
        >>> low, high = get_range_for_difficulty("Normal")
        >>> low <= high
        True
    """
    raise NotImplementedError(
        "Refactor this function from app.py into logic_utils.py"
    )


def parse_guess(raw: str):
    """Parse the player's raw text input into an integer guess.

    Decimal input such as ``"42.7"`` is accepted and truncated toward zero
    to an ``int``. Invalid input never raises; the problem is reported
    through the returned error message instead.

    Args:
        raw: The unprocessed string from the guess input field. May be
            ``None`` or empty if the player has not typed anything.

    Returns:
        tuple[bool, int | None, str | None]: A ``(ok, guess, error)`` triple.

        - On success: ``(True, guess, None)``, where ``guess`` is the parsed
          integer.
        - On failure: ``(False, None, error)``, where ``error`` is a
          human-readable message suitable for display to the player.

    Example:
        >>> parse_guess("42")
        (True, 42, None)
        >>> parse_guess("abc")
        (False, None, 'That is not a number.')
    """
    raise NotImplementedError(
        "Refactor this function from app.py into logic_utils.py"
    )


def check_guess(guess, secret):
    """Compare a guess against the secret number and describe the result.

    Args:
        guess (int): The player's parsed guess.
        secret (int): The secret number the player is trying to find. Both
            values should be integers so that comparisons are numeric.

    Returns:
        tuple[str, str]: An ``(outcome, message)`` pair.

        - ``outcome`` is one of ``"Win"``, ``"Too High"``, or ``"Too Low"``
          and is intended for game logic such as scoring.
        - ``message`` is a player-facing hint pointing toward the secret:
          a guess that is too high should tell the player to go lower, and
          a guess that is too low should tell the player to go higher.

    Example:
        >>> outcome, _ = check_guess(60, 50)
        >>> outcome
        'Too High'
    """
    raise NotImplementedError(
        "Refactor this function from app.py into logic_utils.py"
    )


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Compute the player's new score after a guess.

    A winning guess awards points that decrease the more attempts the
    player needed, with a minimum award so a win is always worth
    something. Incorrect guesses apply a penalty. Unknown outcomes leave
    the score unchanged.

    Args:
        current_score: The player's score before this guess.
        outcome: The result returned by :func:`check_guess`; one of
            ``"Win"``, ``"Too High"``, or ``"Too Low"``.
        attempt_number: The 1-based number of the attempt being scored.

    Returns:
        int: The updated score. The input score is not modified in place.
    """
    raise NotImplementedError(
        "Refactor this function from app.py into logic_utils.py"
    )
