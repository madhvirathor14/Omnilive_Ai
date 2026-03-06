memory_store = {}


def get_user_memory(user_id: str):
    return memory_store.get(user_id, {
        "history": [],
        "performance": {
            "confidence_trend": [],
            "sentiment_trend": []
        }
    })


def update_user_memory(user_id: str, message: str, response: str):
    user_memory = get_user_memory(user_id)

    user_memory["history"].append({
        "user": message,
        "ai": response
    })

    memory_store[user_id] = user_memory

    return user_memory