---
description: 지도 내 2차원 좌표와 관련된 기능을 관리하기 위한 API 입니다.
---

# JSVector2D

> Module.JSVector2D() API를 생성합니다.
>
> JSVector2D 생성 시 기본값 x, y(0, 0) 설정.

```javascript
var position = new Module.JSVector2D(129.128265, 35.171834);
var position = new Module.JSVector2D();
```

## properties

| Name | Type   | Description |
| :--- | :----- | :---------- |
| x    | number | X축 좌표계. |
| y    | number | Y축 좌표계. |

## Function

### set(x, y)

> 좌표 값을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description |
| :--- | :----- | :---------- |
| x    | number | X축 좌표계. |
| y    | number | Y축 좌표계. |

{% endtab %}

{% tab title="Template" %}

```javascript
var position = new Module.JSVector2D().set(120046.02, 345567.55);
```

{% endtab %}
{% endtabs %}
