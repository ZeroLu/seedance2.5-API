export interface Seedance25ClientOptions {
  baseUrl?: string;
  model?: string;
  timeout?: number;
}

export interface ModelsOptions {
  mediaType?: string;
}

export interface QuoteVideoOptions {
  prompt: string;
  scene: string;
  options?: Record<string, unknown>;
  model?: string;
}

export interface CreateVideoOptions {
  prompt: string;
  scene: string;
  options?: Record<string, unknown>;
  model?: string;
}

export interface TextToVideoOptions {
  duration?: string;
  aspectRatio?: string;
  resolution?: string;
  model?: string;
  extraOptions?: Record<string, unknown>;
}

export interface ImageToVideoOptions extends TextToVideoOptions {
  imageUrls: string[];
}

export interface WaitForTaskOptions {
  interval?: number;
  timeout?: number;
}

export class Seedance25APIError extends Error {
  statusCode?: number;
  payload?: unknown;

  constructor(message: string, options?: { statusCode?: number; payload?: unknown });
}

export class Seedance25Client {
  constructor(apiKey: string, options?: Seedance25ClientOptions);

  apiKey: string;
  baseUrl: string;
  model: string;
  timeout: number;

  models(options?: ModelsOptions): Promise<unknown>;
  quoteVideo(options: QuoteVideoOptions): Promise<unknown>;
  createVideo(options: CreateVideoOptions): Promise<unknown>;
  textToVideo(prompt: string, options?: TextToVideoOptions): Promise<unknown>;
  imageToVideo(prompt: string, options: ImageToVideoOptions): Promise<unknown>;
  uploadImages(filePaths: string[]): Promise<unknown>;
  uploadVideos(filePaths: string[]): Promise<unknown>;
  getTask(taskId: string): Promise<unknown>;
  waitForTask(taskId: string, options?: WaitForTaskOptions): Promise<unknown>;
}
