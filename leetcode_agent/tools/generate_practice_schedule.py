"""Tool to generate a structured 7-day LeetCode practice schedule."""


def generate_practice_schedule(topic: str, difficulty: str = "mixed") -> dict:
    """Generate a structured 7-day practice schedule for a DSA topic.

    Creates a progressive schedule that ramps up from fundamentals to
    advanced problems, with built-in review and mock interview days.

    Args:
        topic: The DSA topic to create a schedule for.
        difficulty: Target difficulty level — 'easy', 'medium', 'hard',
                    or 'mixed' (default: 'mixed').

    Returns:
        A dict with 'topic', 'difficulty', and 'schedule' (list of day plans).
    """
    schedule = [
        {
            "day": 1,
            "theme": "Fundamentals & Theory",
            "tasks": [
                f"Study the core concepts of {topic}",
                f"Watch a tutorial or read an article on {topic}",
                "Solve 2 Easy problems to build confidence",
            ],
            "goal": "Understand the underlying patterns",
        },
        {
            "day": 2,
            "theme": "Pattern Recognition",
            "tasks": [
                f"Identify the common patterns in {topic} problems",
                "Solve 2 Easy problems focusing on pattern application",
                "Write notes on when to apply each pattern",
            ],
            "goal": "Recognize problem patterns quickly",
        },
        {
            "day": 3,
            "theme": "Medium Difficulty",
            "tasks": [
                "Solve 2 Medium problems independently",
                "If stuck for 30 min, read hints then retry",
                "Analyze time/space complexity of each solution",
            ],
            "goal": "Apply patterns to harder problems",
        },
        {
            "day": 4,
            "theme": "Deep Dive & Edge Cases",
            "tasks": [
                "Solve 2 Medium problems focusing on edge cases",
                "Practice writing clean, well-commented code",
                f"Study optimized approaches for {topic}",
            ],
            "goal": "Handle tricky edge cases confidently",
        },
        {
            "day": 5,
            "theme": "Hard Problems & Optimization",
            "tasks": [
                "Attempt 1 Hard problem (aim for 45 min)",
                "Study the editorial/discussion for insights",
                "Re-implement the optimal solution from scratch",
            ],
            "goal": "Tackle advanced difficulty and optimize solutions",
        },
        {
            "day": 6,
            "theme": "Review & Revisit",
            "tasks": [
                "Re-solve 2 problems from earlier in the week without looking at solutions",
                "Create a personal cheat sheet for the topic",
                "Identify and work on any weak areas",
            ],
            "goal": "Solidify understanding through repetition",
        },
        {
            "day": 7,
            "theme": "Mock Interview",
            "tasks": [
                f"Simulate a timed interview: solve 2 {topic} problems in 45 min",
                "Practice explaining your thought process aloud",
                "Review performance and plan next steps",
            ],
            "goal": "Build interview-ready confidence",
        },
    ]

    return {
        "topic": topic,
        "difficulty": difficulty,
        "total_days": 7,
        "schedule": schedule,
    }