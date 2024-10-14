# Image Recognition and Object Detection with gpt-4o-mini

## Object Detection

As demonstrated by [the experiment](https://youtu.be/1yXJCsx69_0) I conducted, GPT-4o-mini excels at image recognition and can perform object detection to some extent. However, for accurately identifying the positions of objects, it is better to rely on AI specifically designed for object detection.

## Image Classification

What I have observed:

- gpt-4o-mini is not particularly good at determining a person’s gender, age, or expression and tends to refuse to answer, but it can provide guesses depending on the prompt.
- It answers accurately to questions about what people are doing, which direction they are facing, or how many people are present.
- It also provides accurate descriptions of the environment where people are located.

Therefore, image recognition and classification by GPT-4o-mini can be applied to the generation of dynamic marketing content tailored to visitors.

## Prompts

### Geneder and age 

```
Please guess the gender and age of the person in the attached image. Output only the data in the following JSON format:

{"gender": "male", "age", 25}
```

### Races

```
Please infer the race of the person in the attached image. Output only the data in the following JSON format:

{"race": "white"}
```

### Hair sytle

```
Please guess the hair style of the person in the attached image. Output only the data in the following JSON format:

{"hairstyle": "bob"}
```

### Glasses

```
Is the person in the attached image wearing glasses? Please answer with "Yes" or "No".
```

### Clothing

```
Can you guess the clothing of the person in the attached image? Please output the data in the following JSON format.

{"clothing_style": "suit"}
```


## Image Classification with Infrared Array Sensor

If using a camera poses privacy concerns, let's try using an infrared array sensor.

<img src="./docs/infrared_array_sensor_with_chatgpt.jpg" width=600>
