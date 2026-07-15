from __future__ import annotations

import json
import mimetypes
import time
import uuid
from pathlib import Path
from typing import Any
from urllib import error, parse, request

from .constants import (
    DEFAULT_BASE_URL,
    DEFAULT_MODEL,
    DEFAULT_POLL_INTERVAL,
    DEFAULT_POLL_TIMEOUT,
    DEFAULT_TIMEOUT,
    DEFAULT_USER_AGENT,
)
from .exceptions import Seedance25APIError


class Seedance25Client:
    """Minimal Python wrapper for CyberBara Seedance 2.5 endpoints."""

    def __init__(
        self,
        api_key: str,
        *,
        base_url: str = DEFAULT_BASE_URL,
        model: str = DEFAULT_MODEL,
        timeout: int = DEFAULT_TIMEOUT,
    ) -> None:
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.timeout = timeout

    @staticmethod
    def _parse_json_bytes(raw: bytes) -> Any:
        if not raw:
            return {}
        text = raw.decode("utf-8", errors="replace")
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return {"_raw": text}

    def _build_url(self, path: str, query: dict[str, Any] | None = None) -> str:
        normalized_path = path if path.startswith("/") else f"/{path}"
        url = f"{self.base_url}{normalized_path}"
        if query:
            clean = {k: v for k, v in query.items() if v is not None and v != ""}
            if clean:
                url = f"{url}?{parse.urlencode(clean)}"
        return url

    def _request(
        self,
        *,
        method: str,
        path: str,
        query: dict[str, Any] | None = None,
        json_body: Any | None = None,
        body: bytes | None = None,
        content_type: str | None = None,
        timeout: int | None = None,
    ) -> Any:
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.api_key}",
            "x-api-key": self.api_key,
            "User-Agent": DEFAULT_USER_AGENT,
        }
        if json_body is not None:
            body = json.dumps(json_body, ensure_ascii=False).encode("utf-8")
            headers["Content-Type"] = "application/json"
        elif content_type:
            headers["Content-Type"] = content_type

        req = request.Request(
            url=self._build_url(path, query),
            data=body,
            headers=headers,
            method=method.upper(),
        )

        try:
            with request.urlopen(req, timeout=timeout or self.timeout) as resp:
                return self._parse_json_bytes(resp.read())
        except error.HTTPError as exc:
            payload = self._parse_json_bytes(exc.read())
            message = self._extract_error_message(payload) or f"HTTP {exc.code}"
            raise Seedance25APIError(message, status_code=exc.code, payload=payload) from exc
        except error.URLError as exc:
            raise Seedance25APIError(f"Request failed: {exc.reason}") from exc

    @staticmethod
    def _extract_error_message(payload: Any) -> str | None:
        if isinstance(payload, dict):
            error_obj = payload.get("error")
            if isinstance(error_obj, dict):
                message = error_obj.get("message")
                if isinstance(message, str) and message:
                    return message
        return None

    @staticmethod
    def _build_multipart_upload(file_paths: list[str]) -> tuple[bytes, str]:
        boundary = f"----Seedance25Boundary{uuid.uuid4().hex}"
        chunks: list[bytes] = []

        for file_path in file_paths:
            path = Path(file_path)
            if not path.is_file():
                raise FileNotFoundError(f"File not found: {path}")

            mime = mimetypes.guess_type(str(path))[0] or "application/octet-stream"
            filename = path.name.replace('"', "")

            chunks.append(f"--{boundary}\r\n".encode("utf-8"))
            chunks.append(
                (
                    "Content-Disposition: form-data; "
                    f'name="files"; filename="{filename}"\r\n'
                ).encode("utf-8")
            )
            chunks.append(f"Content-Type: {mime}\r\n\r\n".encode("utf-8"))
            chunks.append(path.read_bytes())
            chunks.append(b"\r\n")

        chunks.append(f"--{boundary}--\r\n".encode("utf-8"))
        return b"".join(chunks), f"multipart/form-data; boundary={boundary}"

    @staticmethod
    def _unwrap_data(payload: Any) -> Any:
        if isinstance(payload, dict) and "data" in payload:
            return payload["data"]
        return payload

    def models(self, *, media_type: str = "video") -> Any:
        payload = self._request(
            method="GET",
            path="/api/v1/models",
            query={"media_type": media_type},
        )
        return self._unwrap_data(payload)

    def quote_video(
        self,
        *,
        prompt: str,
        scene: str,
        options: dict[str, Any] | None = None,
        model: str | None = None,
    ) -> Any:
        payload = self._request(
            method="POST",
            path="/api/v1/credits/quote",
            json_body={
                "model": model or self.model,
                "media_type": "video",
                "scene": scene,
                "prompt": prompt,
                "options": options or {},
            },
        )
        return self._unwrap_data(payload)

    def create_video(
        self,
        *,
        prompt: str,
        scene: str,
        options: dict[str, Any] | None = None,
        model: str | None = None,
    ) -> Any:
        payload = self._request(
            method="POST",
            path="/api/v1/videos/generations",
            json_body={
                "model": model or self.model,
                "prompt": prompt,
                "scene": scene,
                "options": options or {},
            },
        )
        return self._unwrap_data(payload)

    def text_to_video(
        self,
        prompt: str,
        *,
        duration: str = "10",
        aspect_ratio: str = "16:9",
        resolution: str | None = None,
        model: str | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> Any:
        options: dict[str, Any] = {
            "duration": duration,
            "aspect_ratio": aspect_ratio,
        }
        if resolution:
            options["resolution"] = resolution
        if extra_options:
            options.update(extra_options)
        return self.create_video(
            prompt=prompt,
            scene="text-to-video",
            options=options,
            model=model,
        )

    def image_to_video(
        self,
        prompt: str,
        *,
        image_urls: list[str],
        duration: str = "10",
        aspect_ratio: str = "16:9",
        resolution: str | None = None,
        model: str | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> Any:
        options: dict[str, Any] = {
            "duration": duration,
            "aspect_ratio": aspect_ratio,
            "image_input": image_urls,
        }
        if resolution:
            options["resolution"] = resolution
        if extra_options:
            options.update(extra_options)
        return self.create_video(
            prompt=prompt,
            scene="image-to-video",
            options=options,
            model=model,
        )

    def upload_images(self, file_paths: list[str]) -> Any:
        body, content_type = self._build_multipart_upload(file_paths)
        payload = self._request(
            method="POST",
            path="/api/v1/uploads/images",
            body=body,
            content_type=content_type,
        )
        return self._unwrap_data(payload)

    def upload_videos(self, file_paths: list[str]) -> Any:
        body, content_type = self._build_multipart_upload(file_paths)
        payload = self._request(
            method="POST",
            path="/api/v1/uploads/videos",
            body=body,
            content_type=content_type,
        )
        return self._unwrap_data(payload)

    def get_task(self, task_id: str) -> Any:
        payload = self._request(
            method="GET",
            path=f"/api/v1/tasks/{task_id}",
        )
        data = self._unwrap_data(payload)
        if isinstance(data, dict) and "task" in data:
            return data["task"]
        return data

    def wait_for_task(
        self,
        task_id: str,
        *,
        interval: int = DEFAULT_POLL_INTERVAL,
        timeout: int = DEFAULT_POLL_TIMEOUT,
    ) -> Any:
        deadline = time.time() + timeout
        while True:
            task = self.get_task(task_id)
            status = task.get("status") if isinstance(task, dict) else None
            if status in {"success", "failed", "canceled"}:
                return task
            if time.time() >= deadline:
                raise TimeoutError(f"Task {task_id} did not finish within {timeout}s.")
            time.sleep(interval)
