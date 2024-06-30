import os
import random
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# GUI界面
import gradio as gr

# 加载sdk配置
from sparkai.core.messages import ChatMessage
from dwspark.config import Config

# 加载对话模型
from dwspark.models import ChatModel

# 加载讯飞的api
SPARKAI_APP_ID = os.environ["SPARKAI_APP_ID"]
SPARKAI_API_SECRET = os.environ["SPARKAI_API_SECRET"]
SPARKAI_API_KEY = os.environ["SPARKAI_API_KEY"]
config = Config(SPARKAI_APP_ID, SPARKAI_API_KEY, SPARKAI_API_SECRET)

# Test for git push