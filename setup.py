import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="ai_hub",                  # 包名称
    version="0.3.5",                                   # 包版本
    author="gaoxiaos",                           # 作者
    license='MIT',                                     # 协议简写
    author_email="ai_hub@qq.com",                 # 作者邮箱
    description="AI_HUB utils package",             # 工具包简单描述
    long_description=long_description,                 # readme 部分
    long_description_content_type="text/markdown",     # readme 文件类型
    install_requires=[                                 # 工具包的依赖包
    'requests>=1.0.0'
    'flask>=1.1.1'
    #'retry>=0.9.2',
    #'urllib3>=1.25.3',
    #'xmltodict>=0.12.0'
    ],
    url="https://github.com/gaoxiaos/AI_HUB",       # 包的开源链接
    packages=setuptools.find_packages(),               # 不用动，会自动发现
    classifiers=[                                      # 给出了指数和点子你的包一些额外的元数据
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
