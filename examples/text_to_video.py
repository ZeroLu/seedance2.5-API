from __future__ import annotations

import os
from pprint import pprint

from seedance25_api import Seedance25Client


def main() -> None:
    api_key = os.environ["CYBERBARA_API_KEY"]
    client = Seedance25Client(api_key)

    quote = client.quote_video(
        prompt="A cinematic drone shot over a misty mountain village at sunrise.",
        scene="text-to-video",
        options={"duration": "10", "aspect_ratio": "16:9"},
    )
    pprint({"quote": quote})

    created = client.text_to_video(
        "A cinematic drone shot over a misty mountain village at sunrise.",
        duration="10",
        aspect_ratio="16:9",
    )
    pprint({"created": created})

    task = client.wait_for_task(created["task_id"])
    pprint({"task": task, "videos": task.get("output", {}).get("videos", [])})


if __name__ == "__main__":
    main()
