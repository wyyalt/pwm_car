# 依赖

redis (用于实现复位和初始化标记)

# redis配置

设置run 参数0用来使小车停止/复位

设置init 参数 运行前设置为 0 第一次访问会执行init（）函数并将些值设置为 1 , 1代表已对GPIO接口进行了初始化 

GPIO口和IP根据实际需要在init函数中设置

# 使用
```
python pwm_car.py
```
