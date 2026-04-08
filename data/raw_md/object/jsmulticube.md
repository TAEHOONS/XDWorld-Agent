---
description: 지도 내 멀티큐브 객체를 생성 및 설정하기 위한 API 입니다.
---

# JSMultiCube

> Module.createMultiCube() API를 생성합니다.

```javascript
var vPosition = new Module.JSVector3D(129.1292403, 35.1721634, 100.0);
var object = Module.createMultiCube("ID", vPosition, false);
```

## Function

### addCube(id, size, count, angle, interval, fillColor, outLine, outLineColor)

> 멀티 큐브 객체를 생성합니다.

{% tabs %}
{% tab title="Information" %}

| Name         | Type                            | Description                                |
| :----------- | :------------------------------ | :----------------------------------------- |
| id           | string                          | 고유 명칭.                                 |
| size         | [JSSize2D](../core/jssize2d.md) | 큐브 크기.                                 |
| count        | number                          | 큐브 각 수(n값 설정 시 n각형의 큐브 생성). |
| angle        | number                          | 큐브 y축 회전 각도.                        |
| interval     | number                          | 큐브 간 간격.                              |
| fillColor    | [JSColor](../core/jscolor.md)   | 채움 색상.                                 |
| outLine      | boolean                         | 외곽선 적용 여부.                          |
| outLineColor | [JSColor](../core/jscolor.md)   | 외곽선 색상.                               |

{% endtab %}

{% tab title="Template" %}

```javascript
var size = new Module.JSSize2D(100.0, 200.0);
var fillColor = new Module.JSColor(255, 255, 255, 255);
var outlineColor = new Module.JSColor(255, 255, 0, 0);
object.addCube("id", size, 6, 30.0, 10.0, fillColor, true, outlineColor);
```

{% endtab %}
{% endtabs %}

### getCubeCount() → number

> 등록된 멀티큐브 객체 총 수를 반환합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   number(0 ~) : 반환 성공.
    -   number(-1) : 반환 실패.

{% endtab %}
{% tab title="Template" %}

```javascript
var cubeCount = object.getCubeCount();
```

{% endtab %}
{% endtabs %}

### getId() → string

> 객체의 고유 명칭을 반환 합니다.

{% tabs %}
{% tab title="Information" %}

-   Return
    -   string: 객체 설명 문자열이 성공적으로 반환.
    -   null: 객체가 null인 경우.

{% endtab %}
{% tab title="Template" %}

```javascript
var strKey = object.getId();
```

{% endtab %}
{% endtabs %}

### setRowSize(size)

> 멀티 큐브 객체 생성 시 열에 해당되는 큐브 수를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description   |
| :--- | :----- | :------------ |
| size | number | 가로 큐브 수. |

{% endtab %}

{% tab title="Template" %}

```javascript
object.setRowSize(3);
```

{% endtab %}
{% endtabs %}

## Getter / Setter

### getDescription(), setDescription(desc) → string

> 객체에 대한 설명을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description  |
| ---- | ------ | ------------ |
| desc | string | 설명 문자열. |

-   Return
    -   string: 객체 설명 문자열이 성공적으로 반환.
    -   null: 객체가 null인 경우.

{% endtab %}
{% tab title="Template" %}

```javascript
var strDesc = object.getDescription();
// ... or ...
object.setDescription("First Object.");
```

{% endtab %}
{% endtabs %}

### getName(), setName(name) → string

> 객체 이름을 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name | Type   | Description |
| ---- | ------ | ----------- |
| name | string | 객체 이름.  |

-   Return
    -   string: 객체 이름을 성공적을 반환
    -   null: 객체가 null인 경우.

{% endtab %}
{% tab title="Template" %}

```javascript
var objName = object.getName();
// ... or ...
object.setName("MyObject");
```

{% endtab %}
{% endtabs %}

### getVisible(), setVisible(visible) → boolean

> 객체의 가시화 유무를 설정합니다.

{% tabs %}
{% tab title="Information" %}

| Name    | Type    | Description                                        |
| ------- | ------- | -------------------------------------------------- |
| visible | boolean | <p>true: 객체 가시화.<br>false: 객체 비가시화.</p> |

-   Return
    -   true: 객체 가시화 상태.
    -   false: 객체 비가시화 상태.

{% endtab %}
{% tab title="Template" %}

```javascript
var objName = object.getName();
// ... or ...
object.setVisible(true);
```

{% endtab %}
{% endtabs %}
