Last updated on 11:33:05 17-07-2026

# Seedance 2.5 API

[![PyPI version](https://img.shields.io/pypi/v/seedance25-api?style=for-the-badge)](https://pypi.org/project/seedance25-api/)
[![PyPI downloads](https://img.shields.io/pypi/dm/seedance25-api?style=for-the-badge)](https://pypi.org/project/seedance25-api/)
[![GitHub Repo stars](https://img.shields.io/github/stars/ZeroLu/seedance2.5-API?style=for-the-badge)](https://github.com/ZeroLu/seedance2.5-API/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/ZeroLu/seedance2.5-API?style=for-the-badge)](https://github.com/ZeroLu/seedance2.5-API/network/members)
[![MIT License](https://img.shields.io/github/license/ZeroLu/seedance2.5-API?style=for-the-badge)](./LICENSE)

[中文 README](./README.zh-CN.md) | [API Entry](https://cyberbara.com/api) | [Get API Key](https://cyberbara.com/api) | [Awesome Seedance](https://github.com/ZeroLu/awesome-seedance)

![Seedance 2.5 API Cover](./assets/seedance25-api-cover-16x9-cropped.png)

Access the **full-access Seedance 2.5 API** through CyberBara.

This is not the same access path most developers see on BytePlus, Volcengine, or the public Dreamina Seedance 2.5 surface. The version exposed here is positioned around a **full-access enterprise tier** that is typically reserved for customers with very large annual spend, and it includes three benefits developers care about most:

- **Unlimited real human face workflows**
- **More permissive prompt review**
- **VIP priority queue**

If you need real creator workflows instead of a stripped-down demo path, this repo is built for that.

Install from PyPI:

```bash
pip install seedance25-api
```

Install from npm:

```bash
npm install seedance25-api
```

[Quick Start](#quick-start) | [Comparison](#comparison) | [API Examples](#api-examples) | [FAQ](#faq)

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

Most pages only tell you that Seedance 2.5 exists. They do not explain the access gap between:

- public web product access
- standard cloud API access
- full-access enterprise access

This repo focuses on the third one.

---

## Why Use CyberBara For Seedance 2.5 API

CyberBara is built for teams that need the **full-access Seedance 2.5 API**, not a limited public wrapper.

### What "full-access" means here

- **Unlimited real human face support** for production portrait and avatar workflows
- **More permissive moderation** for prompts that often get blocked on stricter public surfaces
- **VIP priority queue** for faster execution during demand spikes
- **Unified developer API** for uploads, generation, status polling, model listing, and credit checks
- **Global access path** without forcing teams into fragmented region-locked flows

API docs: [cyberbara.com/api](https://cyberbara.com/api)  
Skill page: [cyberbara.co/skill](https://cyberbara.co/skill)

---

## Comparison

The biggest confusion around Seedance 2.5 is that people assume every "Seedance 2.5" entry point is the same. It is not.

| Access path | Typical audience | Real human face policy | Prompt review | Queue priority | Notes |
| --- | --- | --- | --- | --- | --- |
| **CyberBara full-access Seedance 2.5 API** | Developers, creators, agencies, growth teams, product teams | **Unlimited real human face workflows** | **More permissive** | **VIP priority queue** | Best fit when you need the full-access enterprise-style capability through an API |
| BytePlus / Volcengine standard API | General cloud customers | Usually more restricted | Usually stricter | Standard queue | Better for standard cloud procurement, not the full-access path highlighted here |
| Dreamina public Seedance 2.5 surface | Consumer and creator UI users | Usually the most limited | Public-product moderation | Shared public queue | Good for testing ideas, not for full API workflow control |
| Direct full-access enterprise deal | Large enterprise buyers | Full-access depending on contract | Full-access depending on contract | Highest priority depending on contract | Commonly associated with very large annual commitments, often at enterprise scale |

### In plain English

If your use case depends on:

- real-person portrait motion
- fewer prompt-review bottlenecks
- better queue priority
- API-first automation

you should not evaluate CyberBara against a consumer UI. You should evaluate it against the **full-access enterprise lane**.

---

## Who It's For

This repo is a strong fit if you are:

- building **real-face video workflows** for ads, UGC, avatar content, or short drama tests
- running a **creator tool, AI video product, or internal media pipeline**
- an **agency or growth team** that needs faster turnaround and fewer moderation bottlenecks
- a **developer team** that wants upload, generation, polling, and asset reuse in one API flow
- comparing Seedance entry points and specifically trying to avoid the limits of public or standard-access surfaces

This repo is probably not your main need if you only want:

- casual web testing
- a consumer playground
- a basic one-off prompt demo without API integration

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

## Python Wrapper

This repository includes a minimal Python wrapper for the CyberBara **Seedance 2.5 API**.

Install from PyPI:

```bash
pip install seedance25-api
```

Or install locally for development:

```bash
pip install -e .
```

Basic usage:

```python
from seedance25_api import Seedance25Client

client = Seedance25Client("YOUR_API_KEY")

created = client.text_to_video(
    "A cinematic drone shot over a misty mountain village at sunrise.",
    duration="10",
    aspect_ratio="16:9",
)

task = client.wait_for_task(created["task_id"])
print(task["output"]["videos"])
```

Image-to-video with uploaded reference:

```python
from seedance25_api import Seedance25Client

client = Seedance25Client("YOUR_API_KEY")
upload = client.upload_images(["./reference.png"])

created = client.image_to_video(
    "The subject turns slowly toward camera, subtle smile, natural skin texture.",
    image_urls=upload["urls"],
    duration="10",
    aspect_ratio="9:16",
)

task = client.wait_for_task(created["task_id"])
print(task["output"]["videos"])
```

Wrapper methods:

- `models()`
- `quote_video()`
- `text_to_video()`
- `image_to_video()`
- `upload_images()`
- `upload_videos()`
- `get_task()`
- `wait_for_task()`

See runnable examples in [examples/text_to_video.py](./examples/text_to_video.py) and [examples/image_to_video.py](./examples/image_to_video.py).

---

## Node.js Wrapper

This repository also includes a zero-dependency Node.js wrapper for the CyberBara **Seedance 2.5 API**.

Install from npm:

```bash
npm install seedance25-api
```

Basic usage:

```js
const { Seedance25Client } = require("seedance25-api");

async function main() {
  const client = new Seedance25Client(process.env.CYBERBARA_API_KEY);

  const created = await client.textToVideo(
    "A cinematic drone shot over a misty mountain village at sunrise.",
    {
      duration: "10",
      aspectRatio: "16:9"
    }
  );

  const task = await client.waitForTask(created.task_id);
  console.log(task.output?.videos || []);
}

main().catch(console.error);
```

Image-to-video with uploaded reference:

```js
const { Seedance25Client } = require("seedance25-api");

async function main() {
  const client = new Seedance25Client(process.env.CYBERBARA_API_KEY);
  const upload = await client.uploadImages(["./reference.png"]);

  const created = await client.imageToVideo(
    "The subject turns slowly toward camera, subtle smile, natural skin texture.",
    {
      imageUrls: upload.urls,
      duration: "10",
      aspectRatio: "9:16"
    }
  );

  const task = await client.waitForTask(created.task_id);
  console.log(task.output?.videos || []);
}

main().catch(console.error);
```

Wrapper methods:

- `models()`
- `quoteVideo()`
- `createVideo()`
- `textToVideo()`
- `imageToVideo()`
- `uploadImages()`
- `uploadVideos()`
- `getTask()`
- `waitForTask()`

See runnable examples in [examples/text_to_video.mjs](./examples/text_to_video.mjs) and [examples/image_to_video.mjs](./examples/image_to_video.mjs).

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
curl -X POST 'https://cyberbara.com/api/v1/videos/generations' \
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
curl -X POST 'https://cyberbara.com/api/v1/videos/generations' \
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
curl -X POST 'https://cyberbara.com/api/v1/credits/quote' \
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

## Real Face Workflows

One of the main reasons teams look for the **full-access Seedance 2.5 API** is real-person media production.

Common use cases:

- portrait-to-video
- creator avatar clips
- fashion and beauty content
- UGC-style ads
- short drama character tests
- image-led commercial videos

The important point is not just "supports image-to-video." It is whether your workflow gets blocked when a real face is involved.

CyberBara is positioned for teams that need:

- **unlimited real human face workflows**
- **fewer moderation bottlenecks**
- **faster queue access**
- **API-first automation**

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

### Is this the same as BytePlus, Volcengine, or Dreamina Seedance 2.5?

No. That is the main point of this repository.

This repo is about accessing a **full-access Seedance 2.5 API lane** through CyberBara, not the standard public path most people see first.

### What makes this "full-access"?

Three things matter most:

- **Unlimited real human face workflows**
- **More permissive prompt review**
- **VIP priority queue**

Those are the differences most teams feel immediately in production.

### Why mention enterprise buyers with very large annual spend?

Because this level of access is commonly associated with enterprise-style procurement, not ordinary self-serve access. For many teams, going through CyberBara is a practical way to reach that capability without needing to negotiate a massive direct annual commitment first.

### Is this useful only for demos or prompt testing?

No. It is designed for real developer usage, including API integration, async polling, asset reuse, and workflow automation.

### Is this the right path if I need real-face creator workflows?

Yes. If real human face support is core to your workflow, this is exactly the point you should evaluate first.

### Where can I find prompts and workflow inspiration?

Start here:

- [Awesome Seedance](https://github.com/ZeroLu/awesome-seedance)
- [Seedance How-to](https://github.com/ZeroLu/seedance2.0-how-to)

---

## Keywords

Seedance 2.5 API, full-access Seedance 2.5 API, Seedance 2.5 Python SDK, Seedance 2.5 text to video API, Seedance 2.5 image to video API, Seedance API, CyberBara Seedance API, how to access Seedance 2.5, Seedance 2.5 outside China, unlimited real face Seedance API

---

## Disclaimer

This repository is for educational and developer integration purposes only. Please follow all applicable platform rules, consent requirements, and local laws when working with real-person media.
