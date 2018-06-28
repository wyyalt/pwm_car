# 功能说明

树莓派小车调速控制程序（B／S）架构

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
# 路由说明
根据接口不同可能会出现反转，需要自行调试

stop函数并未将redis复位，第二次启动需要手动将redis run 和 init设置为 0

redis 复位可自行实现
```
/ 初始化GPIO
/front/<speed>/ 后退
/back/<speed>/  后退
/left/<speed>/  左转
/right/<speed>/ 右转
/stop/ 停止
```

