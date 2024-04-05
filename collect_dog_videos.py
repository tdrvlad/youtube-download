VIDEOS = {
    'sleeping': [
        "dogs sleeping indoors",
        "puppies sleeping at home",
        "dog napping in dog shelter",
        "pet hotel dogs sleeping",
        "outdoor dog sleeping garden",
        "dogs sleeping in sunlight",
        "nighttime dog sleeping outside",
        "dogs sleeping in different weather conditions",
        "variety of dog breeds sleeping",
        "dogs sleeping in crowded shelters",
        "canine sleeping arrangements at pet hotels",
        "dog sleeping in quiet room",
        "dog napping in noisy environment",
        "dogs sleeping after play",
        "puppies napping with toys",
        "dog sleep patterns in shelters",
        "dog breeds known for snoring sleeping",
        "sleeping dogs in small spaces",
        "large dogs sleeping in spacious areas",
        "dogs sleeping under blankets",
        "dog sleeping positions and what they mean",
        "rescue dogs sleeping in new homes",
        "first day at home puppy sleeping",
        "dogs sleeping with background music",
        "sleeping dogs during thunderstorm"
    ],
    'playing': [
        "dogs playing with toys indoors",
        "dogs playing with toys outdoors",
        "dog shelter dogs playing with toys",
        "pet hotel dogs playing",
        "puppies playing with toys at home",
        "dogs playing fetch outside",
        "canine playing with ball in garden",
        "dogs playing with chew toys in shelter",
        "dog daycare playtime",
        "multi-breed dogs playing with toys",
        "high energy dogs playing with frisbees",
        "dogs playing in snow with toys",
        "beach dogs playing fetch",
        "nighttime dogs playing with light-up toys",
        "dogs playing with toys in water",
        "slow motion videos of dogs playing with toys",
        "first-person view dog playing with toys",
        "dogs playing with toys compilation at shelters",
        "puppy playtime in pet hotels",
        "interactive dog toy play sessions indoors",
        "outdoor dog park playtime with toys",
        "various breeds playing together with toys",
        "dog agility play with toys",
        "shelter dogs' first time playing with toys",
        "dogs playing with automatic toy dispensers"
    ],
    'eating': [
        "dogs eating indoors high quality",  # High-quality videos of dogs eating indoors.
        "dogs eating outdoors daylight",  # Dogs eating outside during daylight to capture different lighting.
        "dogs eating outdoors night",  # Dogs eating outside during nighttime for different lighting conditions.
        "dog shelter feeding time",  # Videos from dog shelters during feeding times.
        "pet hotel dogs eating",  # Dogs eating in pet hotels to capture that specific context.
        "puppies eating together",  # Puppies eating together for videos of younger dogs.
        "senior dogs eating",  # Older dogs eating, covering age variability.
        "dogs eating in different weather conditions",  # Dogs eating in rain, sunshine, snow, etc., to cover weather variations.
        "large breeds dogs eating",  # Focus on larger breeds to ensure breed diversity.
        "small breeds dogs eating",  # Focus on smaller breeds for the same reason.
        "dogs eating with automatic feeders",  # Dogs interacting with technology.
        "dogs eating special diets",  # Dogs eating special or prescribed diets.
        "dogs eating during training sessions",  # Context of eating as part of training.
        "dogs eating slow feeder",  # Dogs using slow feeders to cover eating behavior.
        "rescue dogs first meal at home",  # Capturing emotional and significant moments.
        "dogs eating homemade food",  # Dogs eating non-commercial, homemade meals.
        "dogs eating at dog cafes",  # Dogs eating in social, public places.
        "multi-dog households feeding time"  # Dynamics of feeding in multi-dog households.
    ],
    'active': [
        "dogs playing outside in sunlight",
        "dogs walking around indoors home",
        "active dogs at the beach",
        "dogs moving around in dog parks",
        "puppies being active in the garden",
        "dog shelter daily activities",
        "pet hotel dogs playing",
        "dog daycare playtime",
        "dogs on hiking trails",
        "active dogs in snow",
        "nighttime dog walks",
        "dogs playing in the rain",
        "variety of dog breeds playing outdoors",
        "rescue dogs active in shelters",
        "service dogs in training outside",
        "dogs interacting with outdoor toys",
        "canine agility training outdoors",
        "puppies first time outside",
        "dogs exploring forests",
        "dog walking in urban areas",
        "high energy dogs playing in yards",
        "dog sports competitions outdoors",
        "active dogs at the lake",
        "dogs running in open fields",
        "dog walking on different terrains",
        "puppies playing in pet hotel",
        "dogs socializing in dog cafes",
        "canine rehabilitation exercises indoors",
        "dogs playing in doggy daycare centers",
        "night walks with dogs urban",
    ]
}


""""
Search queries can be generated with ChatGPT with the following prompt:
----
I want to train a machine learning model that can classify videos of dogs with different actions. Now I am interested in: [ACTION].

I want data that shows this in various contexts: indoors, outside or very importantly, at dog shelters or pet hotels. It is important to cover as much variability in my data.

I will use youtube videos as a raw source of data so please list possible search queries that will help me find the best videos to analyze the dogs behaviors. Think of detailed queries so that I filter out irrelevant videos and focus on my target covering as much of the possible variations in scenarios (location, lighting, context, etc) form the query itself.

Give me a list written in python with the search queries strings that I can use directly.
---
"""

from download_videos import download_videos
download_videos(VIDEOS)