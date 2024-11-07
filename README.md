# WhisperHY

The aim of this project is to explore how Whisper can be tuned to perform better for Low-Resource Languages.

To achieve this I will be training and comparing the following models: 
- A model finetuned with Untranscribed Armenian data from the Voxlingua dataset followed by the transcribed Armenian data from the commonvoice dataset.
- A model finetuned with Untranscribed Indo-European Language data from Voxlingua not including Armenian, by the transcribed Armenian data from the commonvoice dataset.
- A model finetuned with Untranscribed Niger-Congo Language data from Voxlingua not including Armenian, by the transcribed Armenian data from the commonvoice dataset.

As a baseline I have finetuned Whisper using the transcribed Armenian data from the commonvoice data following the [Fine-Tune Whisper tutorial](https://huggingface.co/blog/fine-tune-whisper).

