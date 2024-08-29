from llama_cpp import Llama
import transformers
from transformers import AutoModelForSeq2SeqLM, AutoModelForCausalLM, LlamaForCausalLM, AutoTokenizer, BitsAndBytesConfig, AutoConfig
import torch
from accelerate import init_empty_weights, load_checkpoint_and_dispatch, infer_auto_device_map
from huggingface_hub import login
from parseJson import fetchLLMConfig, fetchPersona
from keyHandler import serve_huggingface
import re
import os


def testNewLLM(prompt):
    ID = serve_huggingface()
    login(token=ID)
    model_name = 'meta-llama/Meta-Llama-3.1-8B-Instruct'
    quantization_config = BitsAndBytesConfig(load_in_8bit_fp32_cpu_offload=True)
    # quantized_model = AutoModelForCausalLM.from_pretrained(model_name,
    quantized_model = LlamaForCausalLM.from_pretrained(model_name,
                                                       device_map="cuda",
                                                       torch_dtype=torch.bfloat16,
                                                       quantization_config=quantization_config)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    input_ids = tokenizer(str(prompt), return_tensors='pt').to('cuda')
    pipeline = transformers.pipeline('text-generation',config=quantization_config, model=quantized_model, tokenizer=tokenizer, max_new_tokens=512)
    output = pipeline(prompt, max_new_tokens=1024)
    print(output[0]['generated_text'][-1])
    response = output[0]['generated_text'][-1]['content']
    print(response)
    return response
