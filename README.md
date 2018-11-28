# Drf定制功能扩展

## BASIC CURD

> 基本的增删改查api开发  

## ViewAttributeUse  

> `filter_backends`,`orderding`,`search_fields` 的使用  

```

filter_backends 
    适用场景：模型数据过滤, 过滤器重用
            比如一些模型数据只过滤出相关用户的
    
orderding 
    适用场景：简单的模型排序, 及前端传值排序
    
search_fields 
    适用场景：模糊搜索框，精确查找等

```

## Serializer

> 根据参数, 序列化器序列不同的字段  

```
    实例化序列化器时, 根据 某某字段 进行序列化指定需要的字段
```

> `source`, 自定义`method`, `null`, `blank`, `default`,

```

```

> 如果drf字段不满足业务需求时, 自定义字段

```
    比如：头像路径，在给前端返回时，是全路径，拼接 `cdn` 域名地址
    
         时间字段, 比如返回 几秒前，几分钟前，几小时前...
```
 
> `to_representation` 方法

```
    比如：多个字段，需要跨表数据且一致
    
         路飞有设置套餐，如果价格有 0 的，就标识为免费, 且要获取价格套餐列表

```

> 序列化嵌套

```
    1、正向一访问一
    2、正向一访问多
    3、反向
        1）设置 `related_name`
        2）不设置 `related_name`
```

## Response

> 全局自定义响应（DRF框架级别）

## 部分源码说明

> `many` 字段  
> 序列化校验, write_only, read_only 区别等  
