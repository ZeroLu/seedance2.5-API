import { Seedance25Client } from "../index.js";

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

console.log({ created });

const task = await client.waitForTask(created.task_id);
console.log({ task, videos: task.output?.videos || [] });
