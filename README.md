# Seedance 2.5 API

[![GitHub Repo stars](https://img.shields.io/github/stars/ZeroLu/seedance2.5-API?style=for-the-badge)](https://github.com/ZeroLu/seedance2.5-API/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/ZeroLu/seedance2.5-API?style=for-the-badge)](https://github.com/ZeroLu/seedance2.5-API/network/members)
[![MIT License](https://img.shields.io/github/license/ZeroLu/seedance2.5-API?style=for-the-badge)](./LICENSE)

A practical **Seedance 2.5 API** guide for developers who want global access to **text-to-video**, **image-to-video**, and **real human face workflows** without dealing with region locks or fragmented tooling.

CyberBara provides a production-ready API surface for **Seedance 2.5 API** access, with support for reusable uploads, async task polling, and creator workflows that go beyond a thin prompt wrapper.

[Quick Start](#quick-start) | [API Examples](#api-examples) | [Real Face Workflows](#real-face-workflows) | [Related Resources](#related-resources)

---

## Why This Repo Exists

If you are searching for:

- `Seedance 2.5 API`
- `Seedance 2.5 Python SDK`
- `Seedance 2.5 text to video API`
- `Seedance 2.5 image to video API`
- `Seedance 2.5 real face`
- `How to access Seedance 2.5 outside China`

this repository is for you.

Most Seedance discussions online stop at launch news, screenshots, or waitlists. This repo is focused on what developers actually need:

- how to access the API
- how to list models
- how to upload reference assets
- how to create video tasks
- how to poll task status
- how to run real production workflows
- how to connect Seedance to a broader prompt and tooling ecosystem

---

## Why Use CyberBara For Seedance 2.5 API

CyberBara is built for real usage, not just demos.

### Key advantages

- **Global API access**: no need to depend on region-locked consumer apps
- **One API surface**: uploads, generation, task status, model listing, and credit checks
- **Production-friendly**: reusable asset URLs and async task polling
- **Real workflow support**: useful for portrait motion, character-driven content, ads, short drama tests, and creator tooling
- **Broader ecosystem**: works alongside prompt libraries, how-to guides, and agent skills

API docs: [cyberbara.com/api](https://cyberbara.com/api)  
Skill page: [cyberbara.co/skill](https://cyberbara.co/skill)

---

## Quick Start

### Step 1. Get your API key

Create an account and generate an API key from CyberBara.

- API entry: [https://cyberbara.com/api](https://cyberbara.com/api)

### Step 2. Set your base URL

```text
https://cyberbara.com
```

### Step 3. Authenticate

Use either header:

```http
Authorization: Bearer <YOUR_API_KEY>
```

or

```http
x-api-key: <YOUR_API_KEY>
```

---

## API Examples

### 1. List available video models

```bash
curl -X GET 'https://cyberbara.com/api/v1/models?media_type=video' \
  -H 'Authorization: Bearer <YOUR_API_KEY>'
```

Use this first to confirm the currently exposed model names and supported scenes on CyberBara.

---

### 2. Upload a reference image

```bash
curl -X POST 'https://cyberbara.com/api/v1/uploads/images' \
  -H 'Authorization: Bearer <YOUR_API_KEY>' \
  -F 'files=@./reference.png'
```

The response returns a reusable uploaded URL for later generation requests.

---

### 3. Create a text-to-video task

```bash
curl -X POST 'https://cyberbara.com/api/v1/tasks' \
  -H 'Authorization: Bearer <YOUR_API_KEY>' \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "seedance-2.5",
    "scene": "text-to-video",
    "prompt": "A cinematic drone shot over a misty mountain village at sunrise, realistic lighting, smooth camera motion, atmospheric depth.",
    "options": {
      "duration": "10",
      "aspect_ratio": "16:9"
    }
  }'
```

Use this route when you want pure prompt-driven generation.

---

### 4. Create an image-to-video task

```bash
curl -X POST 'https://cyberbara.com/api/v1/tasks' \
  -H 'Authorization: Bearer <YOUR_API_KEY>' \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "seedance-2.5",
    "scene": "image-to-video",
    "prompt": "The woman turns slowly toward camera, soft wind in her hair, natural eye movement, subtle smile, realistic skin texture, cinematic portrait motion.",
    "options": {
      "duration": "10",
      "aspect_ratio": "9:16",
      "image_input": [
        "https://your-uploaded-image-url-here"
      ]
    }
  }'
```

This is the core workflow for portrait animation, character consistency, and creator-facing short video generation.

---

### 5. Check task status

```bash
curl -X GET 'https://cyberbara.com/api/v1/tasks/<TASK_ID>' \
  -H 'Authorization: Bearer <YOUR_API_KEY>'
```

Poll until the task reaches a final state, then read the output URL from the response.

---

### 6. Quote credits before generation

```bash
curl -X POST 'https://cyberbara.com/api/v1/quote' \
  -H 'Authorization: Bearer <YOUR_API_KEY>' \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "seedance-2.5",
    "media_type": "video",
    "scene": "image-to-video",
    "prompt": "Portrait motion test",
    "options": {
      "duration": "10",
      "aspect_ratio": "9:16"
    }
  }'
```

Useful when you want budget visibility before launching larger runs.

---

## Python Example

```python
import requests

API_KEY = "YOUR_API_KEY"
BASE_URL = "https://cyberbara.com"

payload = {
    "model": "seedance-2.5",
    "scene": "text-to-video",
    "prompt": "A high-end perfume commercial, glossy lighting, slow motion liquid splash, premium cinematic style.",
    "options": {
        "duration": "10",
        "aspect_ratio": "16:9"
    }
}

resp = requests.post(
    f"{BASE_URL}/api/v1/tasks",
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    },
    json=payload,
    timeout=60,
)

print(resp.json())
```

---

## Real Face Workflows

One of the biggest reasons creators look for a **Seedance 2.5 API** is not generic video generation. It is reference-driven character work.

Common use cases:

- portrait-to-video
- creator avatar clips
- fashion and beauty content
- UGC-style ads
- short drama character tests
- image-led commercial videos

Real production work needs more than a prompt box. Teams usually need:

- stable reference handling
- asset upload and reuse
- cleaner image-to-video pipelines
- easier handoff between prompt testing and API execution

That is why this repo also points to the broader CyberBara Seedance ecosystem below.

---

## Best Practices

- Use `GET /api/v1/models` first to confirm current model exposure
- Upload reference assets once, then reuse returned URLs
- Keep prompts concrete about camera motion, subject motion, lighting, and shot rhythm
- For portrait workflows, use clean high-resolution references
- Quote credits before large batch runs
- Poll task status asynchronously instead of blocking your app flow

---

## Related Resources

If you want more than just API access, these repositories and pages are part of the same Seedance ecosystem:

- [Awesome Seedance](https://github.com/ZeroLu/awesome-seedance)  
  Curated prompts, example videos, and high-performing Seedance workflows.

- [Seedance How-to](https://github.com/ZeroLu/seedance2.0-how-to)  
  Practical guides on access, usage, and creator workflows.

- [CyberBara Skill](https://cyberbara.co/skill)  
  Use Seedance and other top media models directly inside agent workflows.

- [CyberBara API](https://cyberbara.com/api)  
  Official API entry for generation, uploads, models, task status, and credits.

---

## FAQ

### Is this the official ByteDance repository?

No. This is an independent developer guide for accessing **Seedance 2.5 API** through CyberBara.

### Does this support text-to-video and image-to-video?

Yes. CyberBara exposes a unified API workflow for both.

### Is this only for manual testing?

No. It is designed for real developer usage, including API integration, async polling, asset reuse, and workflow automation.

### Where can I find prompts and workflow inspiration?

Start here:

- [Awesome Seedance](https://github.com/ZeroLu/awesome-seedance)
- [Seedance How-to](https://github.com/ZeroLu/seedance2.0-how-to)

---

## Keywords

Seedance 2.5 API, Seedance 2.5 Python SDK, Seedance 2.5 text to video API, Seedance 2.5 image to video API, Seedance API, CyberBara Seedance API, how to access Seedance 2.5, Seedance 2.5 outside China

---

## Disclaimer

This repository is for educational and developer integration purposes only. Please follow all applicable platform rules, consent requirements, and local laws when working with real-person media.
