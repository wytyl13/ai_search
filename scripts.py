
import asyncio


from ai_search.tool.google_search import GoogleSearch
from ai_search.utils.yaml_model import YamlModel
from pathlib import Path
from ai_search.llm_api.ollama_llm import OllamLLM
from ai_search.configs.llm_config import LLMConfig

async def test():
    llm = OllamLLM(LLMConfig.from_file(Path("/home/weiyutao/.metagpt/config2.yaml")))
    content = await llm.whoami("我是谁")
    return content

async def main():
    content = await test()  # 使用 await 调用异步函数
    print(content)

if __name__ == '__main__':
    # google_search = GoogleSearch(snippet_flag=1)
    # param = {
    #     "query": "我是谁"
    # }
    # status, result = google_search(**param)
    # print(result)
    
    # print(YamlModel.read(Path('/home/weiyutao/.metagpt/config2.yaml')))
    asyncio.run(main())  # 使用 asyncio.run 来运行主程序