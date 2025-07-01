# Fine Tuning LLM

Fine-tuning, in the context of machine learning, is the process of adapting a pre-trained model to a specific task or dataset. It involves further training the model on a new, often smaller, dataset, allowing it to learn the nuances and specific characteristics of the new task or data.

## Quantization

Conversion from higer memory format to a lower memory format.

> Changing the datatype from a higher bit value to lower bit value.
>
> float 32 bits --> int 8

FP 32 bit(Full precision) --> FP 16 bit(Half precision)

- Two Types of Quantization
  1. Symmetric Quantization
  2. Asymemetric Quantization

For quantization we need `zero point` and `scale` values.

**Calibration** is the technique to squeze large values within the range of the data type we are quantizing.

### Modes of Qunatization

#### 1. Post training quantization

We already have a pre-trained model, we apply calibration on the model and take the weights to build a quantized model.

In this method there is loss of data, which might reduce the accuracy.

#### 2. Quantization aware training

In this method we have a trained model which is quantized and then added additional training data to fine tune it futher before generating the final quantized model.

---

## LORA

> Low Order Rank Adaption of LLM

Instead of updating weights, it track changes

`Pre-trained Weights` + `LORA Tracked Weights` = `Fine Tuned Weights`


- LORA tacks weights by utilizing 2 matrices using matrix decomposition method.

## QLORA

> Quantized Low Order Rank Adaption of LLM

This method takes care of ordering and quantizing.