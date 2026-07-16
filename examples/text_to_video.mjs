import { Seedance25Client } from "../index.js";

const client = new Seedance25Client(process.env.CYBERBARA_API_KEY);

const quote = await client.quoteVideo({
  prompt: "A cinematic drone shot over a misty mountain village at sunrise.",
  scene: "text-to-video",
  options: {
    duration: "10",
    aspect_ratio: "16:9"
  }
});

console.log({ quote });

const created = await client.textToVideo(
  "A cinematic drone shot over a misty mountain village at sunrise.",
  {
    duration: "10",
    aspectRatio: "16:9"
  }
);

console.log({ created });

const task = await client.waitForTask(created.task_id);
console.log({ task, videos: task.output?.videos || [] });
