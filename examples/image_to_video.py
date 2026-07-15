from __future__ import annotations

import os
from pprint import pprint

from seedance25_api import Seedance25Client


def main() -> None:
    api_key = os.environ["CYBERBARA_API_KEY"]
    client = Seedance25Client(api_key)

    upload = client.upload_images(["./reference.png"])
    image_urls = upload["urls"]

    created = client.image_to_video(
        "The subject turns slowly toward camera, subtle smile, natural skin texture.",
        image_urls=image_urls,
        duration="10",
        aspect_ratio="9:16",
    )
    pprint({"created": created})

    task = client.wait_for_task(created["task_id"])
    pprint({"task": task, "videos": task.get("output", {}).get("videos", [])})


if __name__ == "__main__":
    main()
