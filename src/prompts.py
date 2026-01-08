"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                           YOUR TASK PROMPTS                                   ║
║                                                                               ║
║  CUSTOMIZE THIS FILE to define prompts/instructions for your task.            ║
║  Prompts are selected based on task type and returned to the model.           ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import random


# ══════════════════════════════════════════════════════════════════════════════
#  DEFINE YOUR PROMPTS
# ══════════════════════════════════════════════════════════════════════════════

PROMPTS = {
    "default": [
        "Two circular balls with different colors are positioned at different locations. Animate the balls moving toward each other at the same speed until they completely merge as one. When the balls overlap, the overlapping region should display the additive color mixture of their original colors. The animation should stop after the two balls completely merge into a single ball at the midpoint between their initial positions.",
        "Two colored circular balls start at different positions. They move toward each other at equal speeds until they fully overlap and merge into one. The overlapping region during movement and the final merged ball should show the additive color mixture of the two original ball colors. Stop the animation when the balls have completely merged at the midpoint.",
        "Animate two circular balls with distinct colors moving toward each other at the same velocity. The balls should continue moving until they completely merge as one ball. During overlap and in the final merged state, use additive color mixing to combine the original colors. The animation stops when both balls have fully merged at the midpoint between their starting positions.",
        "Two balls of different colors are placed at separate locations. Show them moving toward each other at identical speeds. When they overlap, the overlapping area should display the additive mixture of their colors. Continue the animation until the balls completely merge into a single ball at the midpoint, then stop.",
    ],
}


def get_prompt(task_type: str = "default", task_data: dict = None) -> str:
    """
    Select a random prompt for the given task type.
    
    Args:
        task_type: Type of task (key in PROMPTS dict)
        task_data: Task data dictionary (not used for color mixing prompts)
        
    Returns:
        Random prompt string from the specified type
    """
    prompts = PROMPTS.get(task_type, PROMPTS["default"])
    return random.choice(prompts)


def get_all_prompts(task_type: str = "default") -> list[str]:
    """Get all prompts for a given task type."""
    return PROMPTS.get(task_type, PROMPTS["default"])


# ══════════════════════════════════════════════════════════════════════════════
#  NOTE: This generator does not use rubrics
# ══════════════════════════════════════════════════════════════════════════════
#
# The TaskPair schema only includes:
#   - task_id, domain, prompt
#   - first_image, final_image  
#   - ground_truth_video (optional)
#
# No rubric field exists in the schema, so only prompts are generated.
# ══════════════════════════════════════════════════════════════════════════════
