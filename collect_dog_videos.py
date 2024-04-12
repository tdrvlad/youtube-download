from dog_tags import DOG_ADJECTIVES, DOG_QUERIES, DOG_BREEDS, ACTIONS, YT_TAGS
from download_videos import merge_search_queries, download_videos

# This results in many search queries
SUBJECTS = merge_search_queries(DOG_ADJECTIVES, DOG_QUERIES + DOG_BREEDS)

# This results in less search queries
SUBJECTS = DOG_QUERIES + DOG_BREEDS

SUBJECTS_ACTIONS = {}
for action, action_queries in ACTIONS.items():
    SUBJECTS_ACTIONS[action] = merge_search_queries(SUBJECTS, action_queries)

download_videos(
    search_queries=SUBJECTS_ACTIONS,
    max_length=300,
    download_limit=3
)