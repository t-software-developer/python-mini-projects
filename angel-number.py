import random

angel_codes = {
    "111": "A fresh start is unfolding. Trust your thoughts and take the first step.",
    "222": "Have faith in the process. Balance and harmony are finding their way to you.",
    "333": "You are supported. Express your gifts and let your light shine.",
    "444": "You are protected. Keep building the life you believe in.",
    "555": "Change is arriving. Welcome new opportunities with courage.",
    "666": "Refocus your mind on what truly matters. Peace begins within.",
    "777": "You're on the right path. Keep learning and growing.",
    "888": "Abundance flows where gratitude grows. Stay open to receiving.",
    "999": "One chapter is ending so another can begin. Release what no longer serves you.",
    "1111": "Your intentions are powerful. Dream boldly and act with confidence."
}

number = random.choice(list(angel_codes.keys()))

print(f"🔮 Angel Number: {number}")
print(f'✨ Message: "{angel_codes[number]}"')